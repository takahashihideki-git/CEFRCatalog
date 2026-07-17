# -*- coding: utf-8 -*-
"""第3周-5第三陣：応募・出願1件の全数シート（外部化型＝書面フォーマル一段の行為化）。
実行すると prototypes/catalog_application.json を生成する。"""

ACT = '応募・出願'
OUT = 'catalog_application.json'
TITLE = '応募・出願（Applying in writing）── 全数シート'
SCOPE = '全数（1件。書面1）'
TYPE_ = '指示的（directive）── 地位・機会を求めて制度に自分を差し出す。下位系＝依頼系、梯子型＝外部化型（外部化先＝面接と事実情報の授受・書面制度化段。第3周-5第三陣で確定）'
ESSENCE = '求人・入学などの機会を求めて、制度の型に従い自分を差し出す。帳簿は基本の応募書簡1件 ── 判断(o)が捉えた「書面フォーマルの制度化」が、独立の行為として立った姿。'

ROWS = [
(641, '書面', ["Dear Sir or Madam, I am writing to apply for the part-time job on your website. I have two years of experience in a cafe. I am available at weekends. Yours faithfully, Ken Sato", "Please find my CV attached."],
 "限られた裏づけ情報を添えて、基本的な応募の手紙を書く。",
 "応募書簡の制度定型（頭語・用件宣言・裏づけ・結語の対応規則）。",
 "Dear Sir or Madam ↔ Yours faithfully の対応など、内容より先に制度の型が評価される ── 型の誤りは内容以前に応募者の信頼を削る。",
 "唯一の行 ── 書面フォーマルの制度化（判断(o)の現象）が行為核そのものになった行為。裏づけの厚い応募・志望動機の展開は面接（595以降）と業務書簡（授受640）へ。"),
]

ORDER = [641]

DISCUSSION = [
"【外部化型 ── 一段で完成する制度行為】 帳簿はB1の1件のみ。応募の深化（志望動機の展開・条件交渉）は面接シート（口頭）と授受の書面制度化段（640・632/633）へ外部化され、行為としての応募は「型の履行」で完成する。",
"【(o)との関係 ── 制度化段の行為化】 判断(o)の制度化段（632/633/628）は諸行為の書面上端にB2で現れるが、応募はB1で立つ ── 制度化段が「運用の成熟」（how well軸）であるのに対し、応募は制度型の再生産そのものが行為核であり、型を写せば行為が成立するため一段早い。(o)現象と行為の関係を測る基準点として全数シート群に置く。",
"【往復・応答の点検 ── 片側行為】 応募する側のみで、受け側（審査・返答）は取引691（サービス役）の領分。",
"【書面1行 ── (o)判定＝非成立（B2未達型）】 Correspondence系列はB1の本行のみでB2帯に届かず、形式上は非成立（B2未達型）。ただし②のとおり、本行為は(o)現象そのものの行為化であり、「B2未達」は制度化の不在でなく早期完成を意味する ── 判定区分の但し書きとして記録。",
"【点検総括・語彙裁定】 外部化型で確定（仮判定どおり）。横串は社会言語（書簡の制度的丁寧さ）。語彙裁定（判断(s)）：madam（641・B1行）＝応募書簡の制度定型（Dear Sir or Madam）の構成語として保持 ── 苦情638と同裁定。CV は収録内で通過。",
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
