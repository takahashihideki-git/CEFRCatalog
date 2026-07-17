# -*- coding: utf-8 -*-
"""第3周-5第三陣：道案内の依頼と提供3件の全数シート（外部化型）。全行口頭。
実行すると prototypes/catalog_directions.json を生成する。"""
import json, os

ACT = '道案内の依頼と提供'
TITLE = '道案内の依頼と提供（Asking for & giving directions）── 全数シート'
SCOPE = '全数（3件。口頭3）'
TYPE_ = '指示的（directive）── 行き方・手順を求め、与え、従う。下位系＝依頼系、梯子型＝外部化型（消失点B1。外部化先＝事実情報の授受・提案・指示への応答。第3周-5第三陣で確定）'
ESSENCE = '場所への行き方・作業の手順を求め、与え、従う。A2+〜B1で出尽くす外部化型 ── 詳細化はB1で閉じ、空間情報のやりとりは授受へ、協働の手順は提案・指示への応答へ流れる。'

ROWS = [
(566, '口頭', ["How do I get to the library? — Go straight and turn left at the corner.", "— Go straight, turn left. OK, thank you!"],
 "簡単な道順・指示を与え、それに従う（どこかへの行き方の説明など）。",
 "空間定型（go straight / turn left / next to）の授受と、聞いた道順の復唱。",
 "「与え、従う」の後半が盲点 ── 従う技能の核心は聞いた道順の復唱（確認）で、うなずきだけでは道順は運べない。",
 "（起点）与える・従うが対で書かれる。570（授受A2の日常情報）と対をなす場面（→授受シート相互参照）。"),
(517, '口頭', ["First, you cut the vegetables. — OK. What next?", "You do the salad, and I'll set the table. Sound good?"],
 "協働作業で次にすべきことを話し合い、提案し応じ、指示を求め与える。",
 "手順の授受と提案の混成運用。",
 "協働の指示（You do X）は命令でなく分担の提案 ── and I'll ... の対提示が命令文を和らげる。",
 "道順（空間）から手順（作業）へ ── directions の両義が一つの記述文に同居し、提案・指示への応答と交差する（→各シート相互参照）。"),
(558, '口頭', ["Could you tell me exactly how to get there from the station?", "Take the No.4 bus, get off at the third stop, and it's across the street. — The third stop, across the street. Got it."],
 "詳細な道順を尋ね、それに従う。",
 "複数ステップの系列保持（尋ねる側の精密化と復唱）。",
 "三手以上の道順は記憶でなく手続きで運ぶ ── 聞きながらの復唱・メモ（657＝伝言の要点管理と同じ技能）。",
 "到達点＝詳細化。この先の深化（効率的な説明・複雑な経路）はhow well（叙述の正確さ）と授受の情報管理へ外部化され、行為の梯子はここで閉じる。"),
]

ORDER = [566, 517, 558]

DISCUSSION = [
"【消失点B1 ── 場面固定行為の早期完成】 A2+〜B1の3件で梯子が閉じる外部化型（仮判定どおり確定）。B1以上の空間・手順のやりとりは、事実情報の授受（539の交通場面・情報管理相の詳細度調整）とhow well軸（叙述の正確さ）へ外部化される ── 道案内は「場面」としては一生続くが、「行為の梯子」としてはB1で完成する。",
"【directionsの両義 ── 空間と手順】 566/558は空間の道順、517は作業の手順で、英語のdirectionsが両者を貫く。517は提案（making and responding to suggestions）と指示の授受を一つの記述文に持つ混成で、篩が本行為に割り当てたのは「指示を求め与える」核ゆえ ── 提案シート475・指示への応答707との三面相互参照。",
"【往復・応答の点検 ──「従う」が明記される珍しい行為】 give and follow が対で書かれ、受け側の技能（従う＝復唱・確認・実行）が記述文に明文化される ── (n)軸の受け側が行為定義に入る点で指示への応答・同意不同意と同族だが、本行為は与える側も同居する対称往復。",
"【全行口頭 ── (o)判定＝書面系列なし】 書面の道案内（案内文・地図の説明）はCorrespondence・オンライン帳簿に独立の記述文を持たず、判定＝書面系列なし。",
"【点検総括・語彙裁定】 外部化型で確定。539（取引）にも ask and give directions が含まれ、道案内が取引・移動場面の部品としても現れることを帳簿が示す ── 行為としての独立（本シート）と部品としての埋め込み（539）の二重性。語彙裁定（判断(s)）：フラグなし。",
]

def build(root="."):
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
    here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
    data = build(root)
    json.dump(data, open(os.path.join(here, 'catalog_directions.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 3 and len(DISCUSSION) == 5
    print(f"catalog_directions.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}）")
