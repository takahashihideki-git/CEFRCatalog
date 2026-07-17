# -*- coding: utf-8 -*-
"""第3周-5第三陣：経験・出来事の叙述1件の全数シート（外部化型の純粋形＝第2柱への窓口）。
実行すると prototypes/catalog_experience.json を生成する。"""

ACT = '経験・出来事の叙述'
OUT = 'catalog_experience.json'
TITLE = '経験・出来事の叙述（Describing experience in interaction）── 全数シート'
SCOPE = '全数（1件。書面1）'
TYPE_ = '主張的（assertive）── 起きたこと・したことを語る。下位系＝叙述系、梯子型＝外部化型（外部化先＝第2柱・産出-談話構築のSustained monologue帯。設計判断(i)。第3周-5第三陣で確定）'
ESSENCE = '起きたこと・したことを相手に語る。やり取りの帳簿にはオンライン投稿の1件のみが立ち、叙述の本体（28件）は第2柱・産出-談話構築にある ── この行為はその窓口。'

ROWS = [
(680, '書面', ["Went hiking with friends today — beautiful weather, great views!", "Tried a new ramen place. Loved the noodles."],
 "日常の事柄・社交活動・気持ちについて、簡単な重要事項を添えた短い記述的なオンライン投稿をする。",
 "短い叙述の粒（出来事＋一言の評価・気持ち）。",
 "SNSの電報体は主語省略が正用 ── 完全文の強迫を外す。気持ちの表現は絵文字への外注（→感情シート678）と地続き。",
 "やり取り帳簿における叙述の唯一の行 ── 叙述の実体は第2柱（Sustained monologue: describing experience 28件）で展開し、本行為はやり取りへの接続点。"),
]

ORDER = [680]

DISCUSSION = [
"【外部化型の純粋形 ── 帳簿一行の窓口行為】 やり取り側の記述文は680のみで、消失点は起点と同時（A2+）。叙述の梯子（過去の語り・経験の構造化・物語）はまるごと第2柱・産出-談話構築のSustained monologue帯（28件）へ外部化されており、本行為は「やり取りの中で叙述が顔を出す最小の窓」── 設計判断(i)（産出との境界）の帳簿上の証拠。",
"【場面 ── オンライン投稿という半対話】 独話（叙述）でありながら読み手の反応を予定する投稿という場面が、産出とやり取りの境界に立つ ── 680がやり取り側に篩われたのは、投稿が返信・リアクションの連鎖（Online conversationスケール）に埋め込まれているため。",
"【往復・応答の点検 ── 反応は他行為の帳簿へ】 投稿への返信・共感は会話の開始・維持（オンライン相）と感情の表出（678）の帳簿が受け持ち、本行為は発信側のみ ── 窓口行為ゆえの片側性。",
"【書面1行 ── (o)判定＝非成立（Correspondence系列欠如型）】 Correspondence系列の叙述（手紙で近況を語る）は独立の記述文を持たず、判定＝非成立（Correspondence系列欠如型）。",
"【点検総括・語彙裁定】 外部化型で確定（仮判定どおり）。第2柱の範型設計時に、この窓口行為との接続（投稿→独話叙述の梯子）を最初の横断線として使える。語彙裁定（判断(s)）：ramen・noodles（680・A2+行）＝食物対象スロット（(s)-1）として保持（hiking は収録内で通過）。",
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
