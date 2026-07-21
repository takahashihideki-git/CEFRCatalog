# -*- coding: utf-8 -*-
"""生成ソース↔成果物の同期点検（restore.py の範囲外を埋める）。

restore.py は「成果物JSONの中身が原典と合っているか」を見る。
このスクリプトは「その成果物を生む .py ソースが成果物と一致しているか」を見る ──
二重管理が静かにずれる経路（partition.py・verdicts.py で実際に起きた）を塞ぐ。

  A. 全数シート  各 prototypes/<act>_full_prototype.py の build() ↔ catalog_<act>.json
                 （メモリ上で照合するのでコミット前でも使える。git diff 方式の代替）
  B. 旧範型      prototypes/*_prototype.py（4範型＋検証範型）↔ 統合JSON の全10列
  C. 篩帳簿      analysis/verdicts.py の V ↔ data/sieve_verdicts_*.json
  D. 作業訳      analysis/ja_tr1〜9.py の JA1〜JA9 合成 ↔ data/working_translations_1224.json

ファイル名は glob で拾う（採用数・篩件数の確定で改名されるため、数字を直書きしない）。

    python3 tools/source_sync_check.py
"""
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = ["mode", "level", "no", "en", "jp", "exponents", "scene", "howwell", "l1", "delta"]

# 旧範型 .py → (統合JSON, 行為キー)。第0層の4範型と第1周の検証範型5枚。
# 手書き正準・生成器なし、かつJSON側のキーは .py の ACT_TITLE と表記が違う（例：苦情クレーム↔苦情・クレーム）
# ため、推測せず対応表で持つ。
LEGACY = [
    ("complaint_prototype", "prototypes_4types.json", "苦情クレーム"),
    ("greeting_prototype", "prototypes_4types.json", "挨拶別れ安否"),
    ("factqa_prototype", "prototypes_4types.json", "事実質問応答"),
    ("opinion_prototype", "prototypes_4types.json", "意見表明"),
    ("thanksapology_prototype", "verification_expressive.json", "感謝詫び祝意"),
    ("emotion_prototype", "verification_expressive.json", "感情の表出"),
    ("infoexchange_prototype", "verification_assertive.json", "事実情報の授受"),
    ("request_prototype", "verification_directive.json", "依頼・要求"),
    ("conversation_prototype", "verification_phatic.json", "会話の開始・維持"),
]

ng = []
warn = []


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def J(rel):
    return json.load(open(os.path.join(ROOT, rel), encoding="utf-8"))


def only(pattern):
    """glob で一意に定まるファイルを返す（改名追随のため名前を直書きしない）。"""
    hits = sorted(glob.glob(os.path.join(ROOT, pattern)))
    if len(hits) != 1:
        ng.append(f"ファイル特定不能: {pattern} -> {[os.path.basename(h) for h in hits]}")
        return None
    return hits[0]


# ---------- A. 全数シート：build() ↔ catalog_*.json ----------
print("=== A. 全数シート（build() ↔ catalog_*.json）===")
sheets = 0
for src in sorted(glob.glob(os.path.join(ROOT, "prototypes", "*_full_prototype.py"))):
    act = os.path.basename(src)[: -len("_full_prototype.py")]
    out = os.path.join(ROOT, "prototypes", f"catalog_{act}.json")
    if not os.path.exists(out):
        ng.append(f"A:{act} 成果物 catalog_{act}.json が無い")
        continue
    mod = load(src, f"full_{act}")
    built = mod.build(ROOT)
    saved = json.load(open(out, encoding="utf-8"))
    if built != saved:
        # どこがずれたかを具体的に出す
        bk, sk = set(built), set(saved)
        if bk != sk:
            ng.append(f"A:{act} 行為キー不一致 py={sorted(bk)} json={sorted(sk)}")
        for k in bk & sk:
            for field in set(built[k]) | set(saved[k]):
                if built[k].get(field) != saved[k].get(field):
                    if field == "rows":
                        br, sr = built[k]["rows"], saved[k]["rows"]
                        if len(br) != len(sr):
                            ng.append(f"A:{act} 行数 py={len(br)} json={len(sr)}")
                        for i, (b, s) in enumerate(zip(br, sr)):
                            for c in COLS:
                                if b.get(c) != s.get(c):
                                    ng.append(f"A:{act} 行{i}(No.{b.get('no')}) 列{c} が不一致")
                    else:
                        ng.append(f"A:{act} {field} が不一致")
    if len(getattr(mod, "DISCUSSION", [])) != 5:
        ng.append(f"A:{act} DISCUSSION段落数={len(getattr(mod, 'DISCUSSION', []))}（期待5）")
    sheets += 1
print(f"  全数シート {sheets}枚を照合")

# ---------- B. 旧範型 .py ↔ 統合JSON ----------
print("=== B. 旧範型（.py ↔ 統合JSON、全10列）===")
covered = {}
for name, js, key in LEGACY:
    mod = load(os.path.join(ROOT, "prototypes", name + ".py"), name)
    data = J("prototypes/" + js)
    covered.setdefault(js, set()).add(key)
    if key not in data:
        ng.append(f"B:{name} 行為キー {key!r} が {js} に無い（keys={list(data)}）")
        continue
    blk = data[key]
    if mod.ACT_TYPE != blk.get("type"):
        ng.append(f"B:{name} type不一致")
    if mod.ACT_ESSENCE != blk.get("essence"):
        ng.append(f"B:{name} essence不一致")
    if mod.DISCUSSION != blk.get("discussion"):
        ng.append(f"B:{name} discussion不一致")
    paras = [p for p in re.split(r"\n\s*\n", mod.DISCUSSION.strip()) if p.strip()]
    if len(paras) != 5 or mod.DISCUSSION.count("【") != 5:
        ng.append(f"B:{name} DISCUSSION段落={len(paras)}／【見出し={mod.DISCUSSION.count('【')}（期待5・5）")
    rows = blk["rows"]
    if len(rows) != len(mod.ROWS):
        ng.append(f"B:{name} 行数 py={len(mod.ROWS)} json={len(rows)}")
    for i, (tup, row) in enumerate(zip(mod.ROWS, rows)):
        for col, val in zip(COLS, tup):
            jval = row[col]
            if col == "exponents":
                val, jval = list(val), list(jval)
            if val != jval:
                ng.append(f"B:{name} 行{i}(No.{row.get('no')}) 列{col} が不一致")
    print(f"  OK {name:26s} -> {js} [{key}] {len(rows)}行")

# 統合JSON側に .py の無い行為が残っていないか（範型追加時の登録漏れ検出）
for js, keys in covered.items():
    orphan = set(J("prototypes/" + js)) - keys
    if orphan:
        ng.append(f"B: {js} に対応する .py の無い行為 {sorted(orphan)} ── LEGACY登録漏れの疑い")

# ---------- C. verdicts.py ↔ sieve_verdicts_*.json ----------
print("=== C. 篩帳簿（verdicts.py ↔ sieve_verdicts_*.json）===")
sieve_path = only("data/sieve_verdicts_*.json")
if sieve_path:
    v = load(os.path.join(ROOT, "analysis", "verdicts.py"), "verdicts")
    py = {str(k): t for k, t in v.V.items()}
    js = json.load(open(sieve_path, encoding="utf-8"))
    if set(py) != set(js):
        ng.append(
            f"C: No集合不一致 py={len(py)} json={len(js)} "
            f"py側のみ={sorted(set(py) - set(js), key=int)} json側のみ={sorted(set(js) - set(py), key=int)}"
        )
    for no in sorted(set(py) & set(js), key=int):
        jv = js[no]
        jver = jv.get("verdict") if isinstance(jv, dict) else jv
        if py[no][0] != jver:
            ng.append(f"C:No.{no} verdict py={py[no][0]} json={jver}")
        if isinstance(jv, dict) and py[no][1] != jv.get("reason", ""):
            ng.append(f"C:No.{no} reason py={py[no][1]!r} json={jv.get('reason')!r}")
    adopt_py = sum(1 for t in py.values() if t[0] == "ADOPT")
    adopt_js = sum(1 for x in js.values() if (x.get("verdict") if isinstance(x, dict) else x) == "ADOPT")
    if adopt_py != adopt_js:
        ng.append(f"C: ADOPT数 py={adopt_py} json={adopt_js}")
    print(f"  {os.path.basename(sieve_path)}: py {len(py)}件／json {len(js)}件、ADOPT py {adopt_py}／json {adopt_js}")

# ---------- D. ja_tr1〜9.py ↔ working_translations ----------
print("=== D. 作業訳（ja_tr1〜9.py 合成 ↔ working_translations_1224.json）===")
merged, origin = {}, {}
for i in range(1, 10):
    mod = load(os.path.join(ROOT, "analysis", f"ja_tr{i}.py"), f"ja_tr{i}")
    for k, val in getattr(mod, f"JA{i}").items():
        k = str(k)
        if k in merged:
            if merged[k] == val:
                warn.append(f"D: No.{k} が ja_tr{origin[k]} と ja_tr{i} に重複（値は同一）")
            else:
                ng.append(f"D: No.{k} が ja_tr{origin[k]} と ja_tr{i} で相違 ── 合成順に結果が依存する")
        merged[k], origin[k] = val, i
wt = J("data/working_translations_1224.json")
if set(merged) != set(wt):
    ng.append(f"D: No集合不一致 py={len(merged)} json={len(wt)}")
bad = [n for n in set(merged) & set(wt) if merged[n] != wt[n]]
if bad:
    ng.append(f"D: 訳文不一致 {len(bad)}件 例={sorted(bad, key=int)[:5]}")
print(f"  py合成 {len(merged)}件／json {len(wt)}件、本文不一致 {len(bad)}件")

# ---------- 総括 ----------
print()
for w in warn:
    print("警告:", w)
if ng:
    print(f"\n同期NG {len(ng)}件:")
    for x in ng:
        print("  -", x)
    sys.exit(1)
print("\n生成ソース同期OK: 全数シート／旧範型／篩帳簿／作業訳")
