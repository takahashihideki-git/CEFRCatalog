#!/usr/bin/env python3
"""書物ロードマップの測り直し（セッションのクローズ手順、CLAUDE.md）。

使い方:
    python3 tools/roadmap_measure.py                  # 作業ツリーを測る
    python3 tools/roadmap_measure.py --prev 8c00826   # 前回の根拠コミットも測り、前回値の再現とファイルごとの増減を出す

前回の根拠コミットを --prev に渡すのは、測り方が前回と同じであることを確かめるため。
出力の「前回」の値が、ロードマップに書かれた前回の公表値と一字違わず一致してから、今回の値を文書に写す。

数え方の取り決め（履歴表の各行と揃えるためのもので、変えると過去の値が再現しなくなる）:
  - 字数   deliverables/book/*.md の生の全文を全角換算する。east_asian_width が W/F/A の文字は 1.0、
           それ以外（半角英数・改行・空白）は 0.5。
  - 章     tools/book_style_check.py の SHEET_REGISTRY に載るファイル。段数＝対応シートの rows の長さ。
  - 節     行頭の "## " の数。
  - 外部No 本文の No.(\\d+) のユニーク集合から自章のシート行を引いた数。群引用の後ろの番号
           （「No.165・168」の168）は数えない。
  - 換算   A5判の実効 680字/ページ。巻末部は推計 8,000字。
  - 未執筆 第3部は11章183段、第4部は14章211段（推計）。
  - 層     第3部の章について、見出しに「＊No.」を持つ ### ブロック＝段の層、"## 議論" 節＝議論、残り＝章の層。
           例欄は段ブロック内の **例** から欄ラベル（読むもの・聞くもの・見るもの）の手前まで。
  - 帳簿の名指し  第3部のシートの散文（scene・howwell・l1・delta・discussion）が名指す他行の番号。
           「No.」なしの番号も拾うので偽陽性（「空欄13」など）が混じる。一覧を目で見てから使う。
"""
import argparse
import ast
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

PAGE = 680
APPENDIX = 8000
P3_SEGS, P3_CHAPTERS = 183, 11
P4_SEGS, P4_CHAPTERS = 211, 14
# 三変数式で幅を測る型（第4部の器が決まるまでの仮置き）
TYPES = [("第1部型", 5, 5), ("中位", 6, 10), ("第2部型", 7, 15)]


def width(s):
    return sum(1.0 if unicodedata.east_asian_width(c) in "WFA" else 0.5 for c in s)


def lstsq(X, y):
    """最小二乗（正規方程式、ガウスの消去法）。numpy を要しない。"""
    k = len(X[0])
    A = [[sum(r[i] * r[j] for r in X) for j in range(k)] for i in range(k)]
    b = [sum(r[i] * v for r, v in zip(X, y)) for i in range(k)]
    for c in range(k):
        p = max(range(c, k), key=lambda r: abs(A[r][c]))
        A[c], A[p], b[c], b[p] = A[p], A[c], b[p], b[c]
        for r in range(k):
            if r != c:
                f = A[r][c] / A[c][c]
                A[r] = [x - f * z for x, z in zip(A[r], A[c])]
                b[r] -= f * b[c]
    co = [b[i] / A[i][i] for i in range(k)]
    pred = [sum(c * x for c, x in zip(co, r)) for r in X]
    mean = sum(y) / len(y)
    r2 = 1 - sum((v - p) ** 2 for v, p in zip(y, pred)) / sum((v - mean) ** 2 for v in y)
    return co, r2, [v - p for v, p in zip(y, pred)]


def sheet_rows(root, sheet):
    d = json.load(open(os.path.join(root, "prototypes", sheet), encoding="utf-8"))
    return [r for v in d.values() if isinstance(v, dict) and "rows" in v for r in v["rows"]], d


def layers(text):
    parts = re.split(r"(?m)^(?=#{2,3} )", text)
    seg = ex = dis = 0.0
    nseg = 0
    in_dis = False
    for p in parts:
        head = p.split("\n", 1)[0]
        if head.startswith("## "):
            in_dis = head.startswith("## 議論")
        if head.startswith("### ") and "＊No." in head:
            seg += width(p)
            nseg += 1
            m = re.search(r"\*\*例\*\*.*?(?=\n\*\*(?:読むもの|聞くもの|見るもの))", p, re.S)
            if m:
                ex += width(m.group())
        elif in_dis:
            dis += width(p)
    return nseg, seg, ex, dis


def ledger_refs(sheet_json, own):
    txt = []
    for v in sheet_json.values():
        if isinstance(v, dict) and "rows" in v:
            txt += v.get("discussion", [])
            txt += [r.get(k, "") for r in v["rows"] for k in ("scene", "howwell", "l1", "delta")]
    t = " ".join(txt)
    nums = {int(x) for x in re.findall(r"No\.(\d+)", t)}
    nums |= {int(x) for x in re.findall(r"(?<![\d.p])(\d{2,4})(?![\d.]|字|件|行|枚|段|年|分|秒|度|章|本|つ|組)", t)}
    return sorted(n for n in nums - own if 1 <= n <= 1224)


def measure(root):
    src = open(os.path.join(root, "tools/book_style_check.py"), encoding="utf-8").read()
    reg = ast.literal_eval(re.search(r"^SHEET_REGISTRY = (\{.*?^\})", src, re.S | re.M).group(1))
    files = sorted(glob.glob(os.path.join(root, "deliverables/book/*.md")))
    out = {"files": {}, "groups": {}, "chapters": []}
    for f in files:
        name = os.path.basename(f)
        text = open(f, encoding="utf-8").read()
        w = width(text)
        out["files"][name] = w
        if name in reg:
            sheet = reg[name][0]
            rows, sj = sheet_rows(root, sheet)
            own = {int(r["no"]) for r in rows}
            ext = {int(x) for x in re.findall(r"No\.(\d+)", text)} - own
            part = "第3部" if "p3_" in sheet else ("第2部" if "p2_" in sheet else "第1部")
            ch = {"name": name, "part": part, "segs": len(rows), "secs": len(re.findall(r"(?m)^## ", text)),
                  "ext": len(ext), "ext_set": sorted(ext), "chars": w}
            if part == "第3部":
                ch["layers"] = layers(text)
                ch["ledger"] = ledger_refs(sj, own)
            out["chapters"].append(ch)
            g = part + "の章"
        elif "巻頭" in name:
            g = "巻頭"
        elif "聞く人読む人" in name:
            g = "柱の肖像"
        elif "肖像" in name or "幕間" in name:
            g = "級の肖像"
        elif "総括章" in name:
            g = "総括章"
        else:
            g = "?" + name
        n, c = out["groups"].get(g, (0, 0.0))
        out["groups"][g] = (n + 1, c + w)
    total = sum(out["files"].values())
    out["total"] = total
    chs = out["chapters"]
    y = [c["chars"] for c in chs]
    co1, r21, res1 = lstsq([[1, c["segs"]] for c in chs], y)
    co3, r23, res3 = lstsq([[1, c["segs"], c["secs"], c["ext"]] for c in chs], y)
    for c, e1, e3 in zip(chs, res1, res3):
        c["res1"], c["res3"] = e1, e3
    out["one"], out["one_r2"], out["three"], out["three_r2"] = co1, r21, co3, r23
    a, b = co1
    p3 = [c for c in chs if c["part"] == "第3部"]
    rem_segs = P3_SEGS - sum(c["segs"] for c in p3)
    rem_ch = P3_CHAPTERS - len(p3)
    one_p3 = rem_ch * a + b * rem_segs
    one_p4 = P4_CHAPTERS * a + b * P4_SEGS
    out["pages"] = {"now": total / PAGE, "p3done": (total + one_p3) / PAGE,
                    "p4done": (total + one_p3 + one_p4) / PAGE,
                    "final": (total + one_p3 + one_p4 + APPENDIX) / PAGE,
                    "p4_one": one_p4 / PAGE}
    p3cur = sum(c["chars"] for c in p3) + out["groups"].get("柱の肖像", (0, 0.0))[1]
    mean_s = sum(c["secs"] for c in p3) / len(p3)
    mean_e = sum(c["ext"] for c in p3) / len(p3)
    out["p3_mean"] = (mean_s, mean_e)
    types = TYPES + [("第3部の実測型", round(mean_s), round(mean_e))]
    c0, cs, cn, ce = co3
    out["range"] = []
    for label, s, e in types:
        per = c0 + cn * s + ce * e
        f3 = rem_ch * per + cs * rem_segs
        f4 = P4_CHAPTERS * per + cs * P4_SEGS
        out["range"].append((label, s, e, (p3cur + f3) / PAGE, f4 / PAGE, (total + f3 + f4 + APPENDIX) / PAGE))
    return out


def report(m, label):
    print(f"=== {label}")
    print(f"ファイル {len(m['files'])}本  合計 {m['total']:,.1f}字")
    for g, (n, c) in m["groups"].items():
        print(f"  {g:10s} {n:3d}本 {c:12,.1f}字")
    a, b = m["one"]
    print(f"一本式  {a:,.1f} + {b:.1f} × 段数   R² {m['one_r2']:.4f}  n={len(m['chapters'])}")
    c = m["three"]
    print(f"三変数式 {c[0]:,.1f} + {c[1]:.1f}×段 + {c[2]:.1f}×節 + {c[3]:.1f}×外部No   R² {m['three_r2']:.4f}")
    p = m["pages"]
    print(f"いま {p['now']:.2f}p ／ 第3部完結 {p['p3done']:.2f}p ／ 第4部完結 {p['p4done']:.2f}p ／ 全巻 {p['final']:.2f}p"
          f"（{p['now'] / p['final'] * 100:.1f}%、第4部 {p['p4_one']:.1f}p、四六判 全巻 {p['final'] * PAGE / 560:.0f}p・既稿 {m['total'] / 560:.0f}p）")
    ms, me = m["p3_mean"]
    print(f"第3部の章の平均  節 {ms:.2f}  外部No {me:.2f}")
    for lab, s, e, p3, p4, fin in m["range"]:
        print(f"  幅 {lab}（節{s}・外部No{e}）  第3部 {p3:.2f}p  第4部 {p4:.2f}p  全巻 {fin:.2f}p")


def detail(m):
    print("--- 章ごと（段・節・外部No・字数・一本式の残差・三変数式の残差）")
    for c in sorted(m["chapters"], key=lambda c: (c["part"], c["name"])):
        print(f"  {c['part']} {c['name']:32s} 段{c['segs']:3d} 節{c['secs']:3d} 外部{c['ext']:3d} {c['chars']:10,.1f}字"
              f"  {c['res1']:+8.0f} {c['res3']:+8.0f}")
    print("--- 第3部の章の層（1段あたりの段の層・例欄、議論、残り）と帳簿の名指し")
    for c in m["chapters"]:
        if c["part"] != "第3部":
            continue
        n, seg, ex, dis = c["layers"]
        rest = c["chars"] - seg - dis
        led = set(c["ledger"])
        book = set(c["ext_set"])
        print(f"  {c['name']}: 段{seg / n:.0f}字/段 例{ex / n:.0f}字/段 議論{dis:,.1f} 残り{rest:,.1f}  "
              f"書物の外部No {len(book)} ／ 帳簿の名指し {len(led)}")
        print(f"      帳簿にあって書物にない {sorted(led - book)}  書物にあって帳簿にない {sorted(book - led)}")


def snapshot(commit, dest):
    arc = subprocess.run(["git", "archive", commit, "deliverables/book", "tools/book_style_check.py", "prototypes"],
                         check=True, capture_output=True).stdout
    subprocess.run(["tar", "-x", "-C", dest], input=arc, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--prev", help="前回の根拠コミット（前回値の再現とファイルごとの増減を出す）")
    ap.add_argument("--detail", action="store_true", help="章ごとの残差・第3部の層・帳簿の名指しも出す")
    args = ap.parse_args()
    os.chdir(args.root)
    cur = measure(args.root)
    if args.prev:
        with tempfile.TemporaryDirectory() as tmp:
            snapshot(args.prev, tmp)
            prev = measure(tmp)
        report(prev, f"前回（{args.prev}）── ロードマップの前回の公表値と一致することを確かめる")
        print()
    report(cur, "今回（作業ツリー）")
    if args.prev:
        print("--- ファイルごとの増減（前回→今回）")
        for k in sorted(set(prev["files"]) | set(cur["files"])):
            d = cur["files"].get(k, 0) - prev["files"].get(k, 0)
            if d:
                print(f"  {d:+10.1f}  {k}")
        print(f"  合計 {cur['total'] - prev['total']:+,.1f}字")
    if args.detail:
        detail(cur)


if __name__ == "__main__":
    sys.exit(main())
