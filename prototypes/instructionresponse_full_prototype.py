# -*- coding: utf-8 -*-
"""第3周-5第三陣：指示への応答1件の全数シート（外部化型＝(n)軸「受け側」の行為化）。
実行すると prototypes/catalog_instructionresponse.json を生成する。"""

ACT = '指示への応答'
OUT = 'catalog_instructionresponse.json'
TITLE = '指示への応答（Responding to instructions）── 全数シート'
SCOPE = '全数（1件。書面1）'
TYPE_ = '応諾的（commissive寄りの応答）── 指示を受け、応じ、確かめる。下位系＝協調調整系、梯子型＝外部化型（外部化先＝明確化・提案・取引のオンライン協働梯子。第3周-5第三陣で確定）'
ESSENCE = '与えられた指示に応じ、受領を伝え、次の一手を確かめる。帳簿はオンライン協働の1件 ── 往復・応答軸（判断(n)）の「受け側」が行為として独立した最小形。'

ROWS = [
(707, '書面', ["OK, I will do the first part.", "Done! What should I do next?"],
 "協力的な相手の助けを得て、簡単な指示に応じ、簡単な質問をして、オンラインで共有課題を達成する。",
 "応答の即時性（受領確認 OK / Done）と次の一手の質問。",
 "指示への無言実行は「受けたのか不明」── OK / Got it の受領確認が協働の潤滑油で、相槌（会話維持）の書面版にあたる。",
 "唯一の行 ── 受け側の行為化の最小形。指示を与える側は517（道案内）・依頼・取引の帳簿に散在する（→各シート相互参照）。"),
]

ORDER = [707]

DISCUSSION = [
"【外部化型 ── 上段はオンライン協働梯子へ】 帳簿はA2の1件のみ。同じGoal-oriented onlineスケールの上段（700取引・697提案・699/702明確化）は3行為に分属しており、指示への応答の深化は「明確化を求めつつ応じる」「提案で返す」として他行為の梯子に吸収される ── スケール一本が行為4つに割れて配架された、篩の分解能を示す配置。",
"【(n)軸の行為化 ── 同意・不同意と同族】 往復・応答軸（判断(n)）の受け側がまるごと行為になったもので、応諾のスタンスを管理する同意・不同意の作業版 ── あちらが立場の応諾、こちらが行動の応諾。",
"【往復・応答の点検 ── 受けの信号が行為核】 受領確認（OK/Done）と次手の質問が核で、確認の省略（伝言）・相槌の欠落（会話維持）と同じ(n)の病理がここでは無言実行として現れる。",
"【書面1行 ── (o)判定＝非成立（Correspondence系列欠如型）】 Correspondence系列を持たず、判定＝非成立（Correspondence系列欠如型）。",
"【点検総括・語彙裁定】 外部化型で確定（仮判定どおり）。支え条件（協力的な相手）つきの起点行為で、脱落後の姿は協働梯子の各行為に引き継がれる。語彙裁定（判断(s)）：フラグなし。",
]

def build(root="."):
    import json, os
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    by_no = {r[0]: r for r in ROWS}
    rows = []
    for no in ORDER:
        _, mode, ex, scene, hw, l1, delta = by_no[no]
        d = desc[str(no)]
        rows.append({"mode": mode, "level": d["level"], "no": no, "en": d["en"], "jp": tr[str(no)],
                     "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta})
    return {ACT: {"title": TITLE, "scope": SCOPE, "type": TYPE_, "essence": ESSENCE,
                  "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    import json, os
    here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
    data = build(root)
    json.dump(data, open(os.path.join(here, OUT), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == len(ROWS) and len(DISCUSSION) == 5
    print(f"{OUT} 生成OK: {len(rows)}行")
