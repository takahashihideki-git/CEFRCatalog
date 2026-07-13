# -*- coding: utf-8 -*-
"""全1,224記述文の区分分割（四本柱＋横串＋方略・複言語）を生成・検証する。
出力: data/block_partition_1224.json  {No(str) -> {"block": 区分, "sub": やり取りのみ}}

判定手続き（企画書v1.1 §2、引き継ぎ書 設計判断(i)）:
 1. 篩判定済み244件は判定に従い「やり取り」へ（採用/除外のサブ状態）
    ── 篩はAsking for clarification（スキーム=方略）から12件を採用済みのため、
       スキーム機械切りは第0層の確定判断と衝突する。篩優先はそのための例外規則。
 2. 残りをスキーム優先で: 能力→how well ／ 方略 ／ 複言語
 3. 活動はモードで: 受容 ／ 仲介 ／ 産出・談話構築
    やり取りの残余62件は「篩対象外」として第1柱の帳簿に留置（帰属精査は第2周）。
"""
import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")

EXPECTED = {"やり取り": 306, "仲介": 251, "受容": 197, "how well": 182,
            "産出・談話構築": 132, "方略": 104, "複言語": 52}
EXPECTED_SUB = {"篩採用": 170, "篩除外": 74, "篩対象外": 62}

def build():
    D = lambda f: json.load(open(os.path.join(ROOT, "data", f), encoding="utf-8"))
    desc, verd, inv = D("descriptors_en_1224.json"), D("sieve_verdicts_244.json"), D("inventory_170to25.json")
    part = {}
    for no, d in desc.items():
        sch, mo = d["scheme"].lower(), d["mode"]
        if no in verd:
            part[no] = {"block": "やり取り",
                        "sub": "篩採用" if verd[no]["verdict"] == "ADOPT" else "篩除外"}
        elif "competences" in sch:
            part[no] = {"block": "how well"}
        elif "plurilingual" in sch:
            part[no] = {"block": "複言語"}
        elif "strategies" in sch:
            part[no] = {"block": "方略"}
        elif mo == "Reception":
            part[no] = {"block": "受容"}
        elif mo == "Mediation":
            part[no] = {"block": "仲介"}
        elif mo == "Production":
            part[no] = {"block": "産出・談話構築"}
        elif mo == "Interaction":
            part[no] = {"block": "やり取り", "sub": "篩対象外"}
        else:
            raise AssertionError(f"未割当 No.{no}")
    verify(part, desc, inv)
    return part

def verify(part, desc, inv):
    from collections import Counter
    assert len(part) == 1224 and set(part) == set(desc), "完全被覆の失敗"
    cnt = Counter(p["block"] for p in part.values())
    assert dict(cnt) == EXPECTED, f"区分件数の不一致: {dict(cnt)}"
    sub = Counter(p.get("sub") for p in part.values() if p["block"] == "やり取り")
    assert dict(sub) == EXPECTED_SUB, f"やり取り内訳の不一致: {dict(sub)}"
    adopted = {n for n, p in part.items() if p.get("sub") == "篩採用"}
    assert adopted == set(inv), "篩採用170とインベントリの不一致"

if __name__ == "__main__":
    part = build()
    out = os.path.join(ROOT, "data", "block_partition_1224.json")
    json.dump(part, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("生成・検証OK:", {b: c for b, c in EXPECTED.items()}, "→", out)
