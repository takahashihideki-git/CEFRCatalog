# -*- coding: utf-8 -*-
"""第3周-5第三陣：問い合わせ3件の全数シート（管理梯子型）。
実行すると prototypes/catalog_enquiry.json を生成する。"""
import json, os

ACT = '問い合わせ'
TITLE = '問い合わせ（Enquiries）── 全数シート'
SCOPE = '全数（3件。口頭1＋書面2）'
TYPE_ = '指示的（directive）── 持っていない情報・条件を、持っている相手に照会する。下位系＝依頼系、梯子型＝管理梯子型（管理課題＝要求の精密化、A2〜B2。第3周-5第三陣で確定）'
ESSENCE = '持っていない情報・条件を、持っている相手に照会する。梯子は要求の精密化 ── 在庫の有無の二値質問から、広告への開いた照会、複雑なサービスへの要件提示へ。'

ROWS = [
(706, '書面', ["Do you have this in blue?", "Is this size available?"],
 "商品・機能の有無について基本的な質問をする。",
 "有無質問の定型（Do you have ... / Is ... available）。",
 "「〜はありますか」の直訳 Is there ...? でなく、在庫照会は Do you have ...? が標準 ── 存在文と所有文の使い分けの最初の実務。",
 "（起点）問い合わせの最小形＝有無の二値質問。"),
(637, '書面', ["I am writing about the apartment in your advertisement. Could you tell me more about the heating and the monthly costs?", "Is the bike in the photo still for sale?"],
 "広告に文書で返信し、関心のある品目についてさらに情報を求める。",
 "照会の書面定型（I am writing about ... / Could you tell me more about ...）。",
 "何の広告かの明示を冒頭に ── 相手は多数の広告を出している前提で書く。用件の特定が返事の速さを決める。",
 "二値（706）から開いた情報要求へ。書面照会の型が立つ。"),
(528, '口頭', ["We need a two-year rental starting in April. What are the rules if we end it early?", "Does the rent include repairs?"],
 "賃貸契約など、より複雑なサービスについて要件を述べ、詳細な質問をする。",
 "要件提示＋詳細質問の二段構成。",
 "要件を先に述べる（We need ...）ことで質問が絞れる ── 質問だけを重ねる照会は往復が嵩み、相手の提案も的を外す。",
 "情報を求めるだけでなく、自分の要件を差し出して照合する ── 取引の条件交渉（695）の一歩手前（→取引シート相互参照）。"),
]

ORDER = [706, 637, 528]

DISCUSSION = [
"【管理課題の梯子 ── 要求の精密化】 有無の二値（706）→開いた照会（637）→要件の照合（528）。3件と薄いが、求めるものの精密さが単調に上がる軸は明瞭で、cross_axesの管理課題と一致 ── 管理梯子型で確定（仮判定どおり）。",
"【場面 ── 商取引の周縁】 在庫・広告・契約と、いずれも取引の手前の情報収集局面。取引（537「必要な情報をすべて得る」）との分業は、537が対面窓口での完遂、本行為が照会という行為型そのものを受け持つ点にある。",
"【往復・応答の点検 ── 片側往復】 問い合わせる側のみが学習者の役割で、受け手はサービス提供者役割（苦情・取引下段と同じ片側往復）。取引と異なり最上段の役割反転はない ── 照会への応対は取引691（サービス役）の帳簿に吸収される。",
"【口頭1・書面2 ── (o)判定＝非成立（B2未達型）】 Correspondence系列は637（B1+）止まりでB2帯に届かず、判定＝非成立（B2未達型）。口頭の上端528は取引・交渉の語彙圏に接する。",
"【点検総括・語彙裁定】 3件全てが依頼系の「情報の依頼」特化形で、依頼シート（物・行為の依頼）との分業が下位系内で立つ。語彙裁定（判断(s)）：available（706・A2行）＝記述文由来（availability of a product or feature）として保持。heating・advertisement（637行）は収録内で通過。",
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
    json.dump(data, open(os.path.join(here, 'catalog_enquiry.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 3 and len(DISCUSSION) == 5
    print(f"catalog_enquiry.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
