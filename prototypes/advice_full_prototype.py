# -*- coding: utf-8 -*-
"""第3周-5第三陣：助言3件の全数シート。
判断(x)：帯の飛び（B1→C2）を「中段外部化・上端再浮上（中抜き型）」と判定し、
外部化型で確定（信頼度低フラグ解消）。全行口頭。
実行すると prototypes/catalog_advice.json を生成する。"""
import json, os

ACT = '助言'
TITLE = '助言（Advising）── 全数シート'
SCOPE = '全数（3件。口頭3）'
TYPE_ = '指示的（directive）── 相手の状況に行動の指針を差し出す。下位系＝協調調整系、梯子型＝外部化型（中抜き型：中段B1+〜C1は意見表明・提案へ外部化、C2で再浮上。判断(x)・第3周-5第三陣で確定）'
ESSENCE = '相手の状況に対して、経験・知識から行動の指針を差し出す。B1の「経験分野内の簡単な助言」の後、帯はC2まで飛ぶ ── 中段の助言実務は意見表明・提案へ外部化され、デリケートな案件の扱いとして上端に再浮上する。'

ROWS = [
(560, '口頭', ["If I were you, I'd take the earlier train.", "You should try the small shop first — it's faster."],
 "自分の経験分野内の簡単な事柄について助言を申し出る。",
 "助言定型（you should / if I were you）と押しつけの回避。",
 "should の直截さを恐れて助言自体を控えがちだが、経験分野内の should は世話であって越権ではない ── maybe/perhaps の緩衝で強さを調整する。",
 "（起点にして中段の消失点）この先B1+〜C1に助言の記述文はない ── 理由つきの勧めは意見表明（677帯）へ、行動の相談は提案（467）へ吸収される。"),
(456, '口頭', ["Have you thought about how you'll tell your family? That part can be difficult.", "I hear you — and honestly, I'd wait a year. Here's why."],
 "デリケートな問題について気まずさなく助言・議論し、口語的な言及を理解し、意見の相違・批判に外交的に対処する。",
 "気まずさの管理 ── 踏み込みと退路の同時設計。",
 "デリケートな案件の助言は「求められてから・仮定形で・退路つき」── 察しの作法が例外的に資産になる領域だが、英語ではその察しを言語化する必要がある。",
 "再浮上の第一 ── 助言が再びcan-doになるのは、内容がデリケートになったとき。インフォーマル側。"),
(483, '口頭', ["Given the legal side, I'd recommend a step-by-step approach — I can walk you through the risks.", "This issue divides people, so let me lay out both options and their costs."],
 "必要な専門知識があれば、会議で複雑・デリケート・論争的な問題について助言・対処する。",
 "専門的助言の構造化（選択肢の陳列＋推奨＋根拠）。",
 "専門助言は断定でなく選択肢＋推奨 ──「先生の言うとおりに」を期待する助言観から、判断材料を渡す助言観への転換。",
 "456のフォーマル対（判断(r)で成立したInformal/Formal対）── 二行保持・相互参照。専門知識という条件が助言をC2で支える。"),
]

ORDER = [560, 456, 483]

DISCUSSION = [
"【帯の飛びの判定（判断(x)）── 中抜き型の外部化型で確定】 B1（560）の後、B1+〜C1に助言の記述文はなく、C2（456/483）で再浮上する。この中抜きは欠測でなく外部化 ── 中段の助言実務（理由つきの勧め・選択肢の提示）は意見表明の根拠支持帯（677〜）と提案の比較帯（467）が担っており、助言が独立のcan-doとして再び立つのは「デリケートさの管理」という質的に別の課題が加わるC2のみ。従来の外部化型（上段消失：依頼・道案内）と異なる「中段外部化・上端再浮上」の新形態で、これをもって信頼度低フラグを解消する。",
"【場面 ── 経験分野から、友人のデリケート案件と会議の専門案件へ】 560は生活の中の世話（経験分野内という限定が越権を防ぐ）、456は友人間のデリケートな相談、483は会議での専門的助言。456/483は判断(r)で成立したInformal/Formal対で、C2の助言が私的・公的の両面で同時に立つ ── 対の存在自体が「デリケートさの管理」がレジスター横断の課題であることを示す。",
"【往復・応答の点検 ── 助言する側の片側行為】 3件とも助言を与える側で、求める側は問題・事情の説明（593「助言を求め」）に埋め込まれている ── 説明シートとの間で「求める→与える」が行為をまたいで完結する分業。456の「相違・批判への外交的対処」は同意・不同意488と同じ作法の助言文脈版。",
"【全行口頭 ── (o)判定＝書面系列なし】 書面の助言（推薦文・アドバイス記事）はやり取りの帳簿に独立の記述文を持たず、判定＝書面系列なし。",
"【点検総括・語彙裁定】 外部化型（中抜き型）で確定。中抜きの帳簿的意味は「行為の可視性はレベルに対して単調でない」── 行為は一度他の帳簿に潜り、条件が変わると再浮上する。この知見は仮判定行為の型判定一般に効く（帯の飛び＝即・低信頼ではない）。語彙裁定（判断(s)）：フラグなし。",
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
    json.dump(data, open(os.path.join(here, 'catalog_advice.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 3 and len(DISCUSSION) == 5
    print(f"catalog_advice.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}）")
