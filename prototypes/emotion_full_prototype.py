# -*- coding: utf-8 -*-
"""第3周-5：感情の表出（8件）の全数シート ── 管理梯子型テンプレートの適用（様式昇格）。

検証範型①（verification_expressive.json）の8行をそのまま継承（全数＝検証範型）。
DISCUSSION は ladder_templates.json 管理梯子型配分で再構成。
第4段落に書面フォーマル一段（判断(o)）の反例を記録：Correspondence が B2（No.630）まで
伸びるのに制度化段が現れない ── 条件の精緻化（業務系列／私的系列の判別）を裁定に付す。
旧検証範型は歴史的サンプルとして凍結。

単一情報源の設計：en / jp は data から構築時取得。継承フィールドは verification_expressive.json から読取。
実行すると prototypes/catalog_emotion.json を生成する。
"""
import json, os

ACT = '感情の表出'
TITLE = '感情の表出（Expressing & responding to feelings）── 全数シート'
SCOPE = '全数（8件。口頭3＋書面5）'
TYPE_ = '表出的（expressive）── 下位系＝感情叙述系、梯子型＝管理梯子型（管理課題＝叙述解像度：決まり文句→種類の分化と応答→度合いと意味づけ）'
ESSENCE = '自分の感情を名指し、その度合いと出来事にとっての意味を言語化し、相手の感情や知らせに感情で応じる。レベルが上がるとは、感情語彙の解像度（種類→度合い→意味づけ）が上がることである。'

ORDER = [447, 437, 639, 678, 636, 676, 431, 630]

DISCUSSION = [
"【管理梯子の背骨 ── 叙述解像度の三段】 管理課題＝叙述解像度。儀礼的表出（感謝・詫び・祝意）でレベル軸が消えたのと対照的に、この行為には A2→B2 の実質的な梯子がある。その中身は苦情の梯子（対立の管理）とも意見表明の梯子（表明→支持→維持→反論）とも別物で、決まり文句（A2・447：I'm + 基本感情語）→ 種類の分化と応答（B1・437／書面 639・678：感情を言い分け、相手の感情に応じる）→ 度合いの段階づけと意味づけ（B2・431／書面 630：強度を刻み、出来事が自分に持つ意味を際立たせる）という解像度の階段である。C1 以上が無いのは欠落ではなく、感情表出の can do は B2 で言語的に完成し、それ以上は文体・修辞（how well）の領域に移るためと読める ── 管理梯子型のうち、梯子が B2 で言語的完成に達する型の代表例。",
"【L1難所 ── 作法ではなく解像度と開示】 意見表明の L1 中心軸だった不同意の作法はこの行為ではほぼ効かず、難所は四つ。(a) 強度の潰れ：英語側の語彙階層（sad < upset < devastated）を在庫していないため、very ＋基本語に一本化される。(b) -ed/-ing 事故：exciting/excited の対立が A2 から一貫して続く構造的な穴。(c) 開示量の較差：感情の明示的な名指しは日本語では察しと相槌、SNS では絵文字に外注されがちで、英語圏の言語化された感情共有の慣習との間に「どこまで言葉にするか」の較差がある。(d) 応答定型の欠落：That's amazing! / I'm sorry to hear that. のような相手の感情・知らせへの反応の型が無いと、沈黙が冷淡に響く。作法（適切さ）が要るのは (d) だけで、しかも不同意ではなく共感の作法である ── how well の主軸も、他行為で主役だった社会言語的適切さではなく、叙述の正確さ＋語彙（範囲と使いこなし）に移る。No.678 が CEFR 全記述文でも珍しく語彙の制約を明記していることが、この行為の律速段階が語彙であることの内部証拠になっている。",
"【隣接行為との境界 ── 表出型内部の結節点】 この行為は三方向で他行為と接する。第一に、B1（437）で入る「応じる」構造は、儀礼的表出の授受構造（詫びを受ける・礼に応える）と同型で、往復性という軸がここにも顔を出す。第二に、書面 B1+（636）では異なる見解の表明が感情叙述と同居し、意見表明系との境界が接する ── CEFR 自身が両行為を一つの記述文に束ねている以上、この境界は分類の便宜であって運用では連続する。第三に、書面 B2（630）の「相手の近況・見解への感情を込めたコメント」は祝意・気遣いの定型群と接する。感情の表出は表出型内部の結節点であり、意見表明系とも儀礼的表出系とも地続きでありながら、主軸（解像度）はどちらとも違う。",
"【口頭書面と書面フォーマル一段 ── 条件への反例、私的系列は制度化しない】 書面系列5件（639・678・636・676・630）は私的な手紙・SNS の系列であり、B1 帯に厚い（経験と感情の絡み・投稿と返信・見解の同居・メディア言及）。ここで判断(o)の適用条件に反例が出る：Correspondence 系列は B2（630）まで伸びるのに、630 の中身は感情の度合い・出来事の意味づけ・相手の近況への感情的コメント ── 叙述解像度の最終段であって、「適切な構造と内容」型のレジスターの制度化ではない。つまり「Correspondence 系列が B2 帯まで伸びる」は制度化段の必要条件であって十分条件ではない。成立3例（632 詫びの制度形・633 業務書簡・628 苦情）はいずれも業務・公式の Correspondence が B2 帯に達する行為であり、私的 Correspondence が B2 に達する本行為では、行為自身の梯子がそのまま B2 を占める。判定は非成立（私的系列型）として記録し、適用条件の精緻化（業務系列／私的系列の判別を条件に加える）を裁定に付す。",
"【点検総括と語彙裁定】 往復・応答（判断(n)）の点検：する側＝感情の名指しと叙述、受ける側＝共感の応答定型（437 で記述文レベルに明文化 ── 往復軸がこの行為では B1 の梯子の段そのものになっている）、断る・返す型＝ネガティブな知らせへの応答（I'm sorry to hear that.）。受け在庫の欠落が冷淡さに化ける往復軸の病理は、L1 難所 (d) と一体である。書面 678 の返信（コメントへの個別応答）は書面側の受け在庫。語彙裁定（判断(s)）：refreshed（678・B1 行、B2 語）── SNS の感想投稿の自然な感情語彙であり、この行為の律速段階が語彙解像度であることを踏まえ、B1 行の実例語として保持を裁定（超過裁定につき本段落に保全、判断(s)-3）。他の実例は検証範型①から変更なし（685 reply の裁定は感謝詫びシートの裁定を継承）。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    inherited = json.load(open(os.path.join(root, "prototypes/verification_expressive.json"), encoding="utf-8"))[ACT]["rows"]
    by_no = {r["no"]: dict(r) for r in inherited}
    rows = []
    for no in ORDER:
        r = by_no[no]
        d = desc[str(no)]
        rows.append({"mode": r["mode"], "level": d["level"], "no": no, "en": d["en"],
                     "jp": tr[str(no)], "exponents": r["exponents"], "scene": r["scene"],
                     "howwell": r["howwell"], "l1": r["l1"], "delta": r["delta"]})
    return {ACT: {"title": TITLE, "scope": SCOPE, "type": TYPE_,
                  "essence": ESSENCE, "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    data = build(root)
    out = os.path.join(here, 'catalog_emotion.json')
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 8, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    print(f"catalog_emotion.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
