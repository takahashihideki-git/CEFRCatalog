# -*- coding: utf-8 -*-
"""第3周-2：苦情・クレーム（9件）の全数範型。

既存範型（prototypes_4types.json、全数カバー済み）を全数シート様式へ昇格：
jp を作業訳に正準化し、第2周以降の点検軸 ── (n)往復・応答の三点、
(o)書面フォーマル一段（再現の初確認）、判断(t)後の対立管理系内の分業 ──
を適用して DISCUSSION を再構成した。実例・scene・howwell・l1 は既存範型
から継承（旧範型は歴史的サンプルとして凍結、判断(t)付随裁定と同方式）。

単一情報源の設計：en / jp は data から構築時取得。
実行すると prototypes/catalog_complaint.json を生成する。
"""
import json, os

TITLE = "苦情・クレーム（Complaining）── 全数シート"
SCOPE = "全数（9件。口頭5＝Obtaining goods and services／書面4＝Correspondence）"
TYPE_ = "指示的（directive）＋表出的要素 ── 現状が期待に反することを伝え、是正を求める。下位系＝対立管理系（第一分類層）、梯子型＝管理梯子型（管理課題：緩衝の精緻化 A2〜C1）"
ESSENCE = "相手（店・機関・個人）に、現状が期待に反することを伝え、是正を求める。非難と要求の二面を持ち、両者のバランスが行為の成否を決める。レベルが上がるとは、緩衝（mitigation）の技法が精緻化することである。"

R = [
# ============ 口頭系列（5行）============
(544, "口頭",
 ["Excuse me, the food is cold.",
  "Sorry, there is no light in my room.",
  "Excuse me, this is not what I ordered."],
 "レストランやホテルで、出されたもの・状態が違うとき、その事実を一言告げる。",
 "社会言語的適切さ（最小）：Excuse me / Sorry を頭に置けるか。",
 "日本語話者は「事実の指摘」を非難と感じて言い出せない傾向。英語では The food is cold. と現状を述べること自体は失礼でなく、むしろ必要な情報提供。黙って我慢する方が不自然。ただし頭に Excuse me を欠くと唐突。",
 "（起点）行為の最小形。まだ是正要求は含まず、問題の存在を告げるだけ。"),
(533, "口頭",
 ["Excuse me, I ordered the pasta but this is a pizza. Could you change it, please?",
  "I'm sorry, but the room is really noisy. Would it be possible to move to another one?",
  "There seems to be a problem with the bill — I think we've been charged twice."],
 "注文違い・部屋の問題・請求の誤りなど、具体的な不都合について、是正を求めるところまで言う。",
 "社会言語的適切さ＋叙述の正確さ：問題の describe と要求の request を一続きにできるか。",
 "日本語の「すみません、これ頼んでないんですけど……」は語尾を濁して相手に察してもらう構造。英語では Could you change it? まで言い切らないと要求が伝わらず、問題提起だけで終わると「ただ不機嫌な人」になる。緩衝（I'm sorry but / There seems to be）＋明示的要求、の二点セットが鍵。",
 "A2からの飛躍：問題の指摘に「是正の要求」が加わる。行為が完結する最初のレベル。"),
(532, "口頭",
 ["I bought this shirt yesterday, but there's a hole in the sleeve. I'd like to return it, please.",
  "This isn't working properly — can I get a refund or an exchange?",
  "I'd like to return this. Do you need the receipt?"],
 "店で不良品を返品する、想定外のやりとり（理由の説明・レシートの授受）に対応する。",
 "柔軟さ：相手の反応（レシートは？交換か返金か）に応じて言い足せるか。",
 "返品は日本でも増えたが、英語圏では「正当な権利の行使」であり、過度に低姿勢だと逆に不審。I'd like to return this と平叙で切り出してよい。「返品してもらえますか」を Can I possibly...? と過剰に婉曲化すると、かえって要領を得ない。",
 "同じB1でも、単発の苦情（533）から「一連のやりとりへの対処」へ。相手の応答を捌く柔軟さが問われる。"),
(526, "口頭",
 ["I understand your position, but I don't think I'm liable for this. The damage was already there when I moved in.",
  "I'd like to contest this. Could you tell me exactly which regulation I'm supposed to have broken?",
  "I'm willing to cover part of it, but not the full amount — let me explain why."],
 "責任の所在が争われる場面で、相手の主張を受けつつ自分の立場を通し、着地点を探る。",
 "叙述の正確さ＋柔軟さ＋社会言語的適切さ：反論しつつ関係を壊さない語調の制御。",
 "日本語話者は対立局面で沈黙するか、逆に感情的に強く出るかの両極に振れやすい。英語の交渉苦情は I understand X, but Y（相手の承認→自分の主張）という型が定石で、冷静に but でつなぐ。謝罪の I'm sorry を安易に挟むと責任を認めた含意になり不利。",
 "苦情から「交渉」へ。一方的要求ではなく、相手の立場の承認と自分の譲歩限度の提示が入る（断る・返す型の苦情版）。"),
(527, "口頭",
 ["Given the inconvenience caused, I believe a full refund plus compensation for the extra costs is reasonable.",
  "I'm prepared to accept a replacement, but only if it's delivered by Friday — otherwise I'll expect a refund.",
  "This has cost me two days of work. I'd like that reflected in whatever you're offering."],
 "実害が生じた案件で、補償の根拠を筋道立てて示し、受け入れ条件と限度を明言する。",
 "叙述の正確さ（最大）＋話題の展開：根拠→要求→条件を論理的に積む構成力。",
 "「譲歩の限度を明示する」は日本語の交渉文化と最も遠い。日本語では限度をあえて曖昧にして含みで交渉するが、英語では but only if... / otherwise I'll... と条件と帰結を言語化するのが誠実で強い。曖昧なままだと足元を見られる。",
 "交渉（526）に「論理的な根拠づけ」と「条件の明示的言語化」が加わる。口頭系列の到達点。"),
# ============ 書面系列（4行）============
(638, "書面",
 ["Dear Sir or Madam, I am writing to complain about the delayed delivery of my order (#12345). I would like to request a full refund.",
  "I ordered the item on 3 May, but it has still not arrived. Please let me know how you intend to resolve this."],
 "【フォーマル】遅延・不良・誤請求について、公式メールで苦情と対応要求を伝える。",
 "社会言語的適切さ（書面レジスター）：I am writing to... の定型と Dear/Yours の枠を守れるか。",
 "日本語のビジネス苦情メールは長い前置き（お世話になっております＋クッション）から入るが、英語は I am writing to complain about... と冒頭で用件を明示するのが正しい作法。前置きを長くすると要領を得ない印象。",
 "口頭B1と並行して、書面系列が独立に立ち上がる。定型（I am writing to）とレジスターの獲得が核。"),
(629, "書面",
 ["Despite my email of 3 May, the issue remains unresolved. I have now been waiting three weeks for a replacement.",
  "I trust you will appreciate my frustration and arrange a full refund within seven days."],
 "【フォーマル】一度目の苦情が解決されない案件で、経緯を裏づけつつ、丁寧さを保って強く要求する。",
 "話題の展開＋社会言語的適切さ：forceful と polite を両立させる語調設計。",
 "「力強くも丁寧に」の両立が難所。日本語話者は polite に振れすぎて要求が弱まるか、直訳的に強く書いて無礼になるか。英語は I trust you will... / I would appreciate it if... で、丁寧な形式のまま圧をかける定型がある。この「丁寧な強さ」の語彙庫を持つことが鍵。",
 "書面B1+からの飛躍：単発の苦情から、経緯の裏づけ・望む結果の明記・語調の制御へ。"),
(628, "書面",
 ["I am writing with reference to invoice #789, which appears to contain an error.",
  "I would be grateful if you could look into this matter and respond at your earliest convenience."],
 "【フォーマル】苦情を含む各種公式通信を、型・レジスター・慣習に則って書き分ける。",
 "社会言語的適切さ（慣習の体系）：with reference to / at your earliest convenience 等の定型群の運用。",
 "英語の公式通信は定型表現の体系（with reference to, I would be grateful if, at your earliest convenience）で動く。日本語の敬語体系とは別物なので、日本語敬語を英語に写そうとせず、英語独自の formal 定型を丸ごと語彙として習得する必要がある。",
 "個別の苦情から「公式通信文一般の型」への一般化。苦情が他の書面行為（依頼・応募）と型を共有する段＝書面フォーマル一段（判断(o)）の苦情版（DISCUSSION④参照）。"),
(625, "書面",
 ["While I appreciate that delays can occur, a three-week silence following my formal complaint is difficult to justify.",
  "I would ask that you treat this as a matter of urgency and confirm your proposed resolution in writing."],
 "【フォーマル】洗練を要する公式通信で、含意・語調・正確さを制御して苦情を述べる。",
 "叙述の正確さ＋柔軟さ（最大）：含意・皮肉・緩衝を精密に制御する表現力。",
 "C1では While I appreciate that..., ... is difficult to justify のような、譲歩節で相手を立てつつ論理で追い込む高度な緩衝が要る。日本語の高等な苦情（慇懃な圧）に感覚は近いが、英語独自のレトリックなので、日本語の語感からの類推は危険。個別の表現を範例で覚える段階。",
 "B2+からの到達点：正確さに加え「うまい表現（good expression）」＝含意と語調の精密制御。書面系列の頂点。"),
]

DISCUSSION = [
"【緩衝（mitigation）の精緻化がA2→C1を貫く ── 管理梯子型の背骨】 英語の苦情を貫く原理は「非難性の緩衝」である。同じ事実（料理が冷たい）を、A2では Excuse me を頭に置くだけ、B1では There seems to be... で事実を非人称化し、B2+では I understand your position, but... で相手を立て、C1では While I appreciate that... と譲歩節で包む ── レベルが上がるとは、緩衝の技法が精緻化することにほかならない（cross_axes の管理課題「緩衝の精緻化」と一致）。この行為において how well の主軸は一貫して社会言語的適切さであり、文法的正確さではない。文法的に完璧な The food is cold and I want a new one now. は、B1の緩衝された表現より「下手」なのである。",
"【日本語話者にとっての二重の壁】 第一の壁は「言い出せない」こと。日本語文化では苦情＝関係を損なう行為とされ、我慢が美徳になりやすい。だが英語圏では、正当な苦情は消費者の権利であり情報提供でもあって、黙る方が不自然に映る。第二の壁は、言い出せた場合に「振れすぎる」こと ── 過度に低姿勢で要求が伝わらないか、直訳的に強く出て無礼になるかの両極。英語の苦情は「丁寧な形式を保ったまま要求を明示する」ことを求めるが、これは日本語の「察してもらう」構造とも「けんか腰」とも異なる第三の様式であり、明示的に学ぶしかない。",
"【隣接行為との連続と、対立管理系内の文脈分業】 「部屋が寒い」（苦情）は「暖房を入れてほしい」（依頼）と表裏一体で、多くの苦情は是正の依頼を含意する。22行為インベントリで苦情と依頼は別行為（第1周④の統合否定・相互参照）だが、実運用では連続する ── 苦情を教えるとき、是正要求（依頼）まで一続きで示さないと行為が完結しない。日本語話者が問題提起だけで止まりがちなのは、この連続性が母語で言語化されないためでもある。さらに全数シートで確認された分業：苦情の梯子はC1（625）で止まり**C2を持たない**。対立管理系のC2（論戦の対等・敵対的応酬の保持）は意見・見解の表明のフォーマル討議側（482/484）にのみ立つ。すなわち対立管理系の内部は、苦情＝取引・サービス文脈の対立管理（A2〜C1）、意見表明＝討議文脈の対立管理（A1〜C2）という**文脈分業**であり、484のdelta「苦情・クレームの最上段と稜線を接する」の逆側からの確認である。",
"【口頭と書面は別の行為に近い ── 書面フォーマル一段（判断(o)）の再現を初確認】 CEFRが苦情を口頭スケール（Obtaining goods and services）と書面スケール（Correspondence）に分けて記述しているのは示唆的である。口頭の苦情は即時・対面で、緩衝も即興的（Excuse me, sorry）。書面の苦情は経緯の裏づけ・構成・レジスターが前面に出て、定型表現の体系（I am writing to, I would be grateful if）で動く。学習者にとっては習得順序も異なり、口頭A2から始まる系列と書面B1+から始まる系列は、並行して別々に登らせるのが自然である。そして No.628「個別の苦情から公式通信文一般の型への一般化」は、No.632（感謝詫び）・No.633（授受）と同一現象の**3例目**であり、判断(o)「書面フォーマル一段」が苦情で**再現**した。意見表明での非再現（Correspondence系列がB1+止まり）と対をなし、精緻化条件「Correspondence系列がB2帯まで伸びる行為でのみ現れる」の**成立側を初確認**（現れる段はB2+の628で、B2帯という帯指定と整合）。",
"【往復・応答の点検：苦情は「片側往復」の行為である ── 語彙裁定の記録】 テンプレート要件（判断(n)）の点検結果：9件すべてが「する側」で、**「受ける側」の記述文はゼロ**。苦情の受け手はサービス提供者・機関の役割であり、CEFRの学習者can-doには現れない ── 往復軸が行為の性質上「片側往復」になる初のケースである。(n)の病理（応答の不在が行為の不履行になる）は、苦情では「受け」でなく**「言い切り」**に現れる：要求（Could you change it?）まで言い切らないと行為が不履行になる（533のL1注意）。断る・返す型は526（相手の主張を受けつつ通す）・527（譲歩限度の明示）に内在する。語彙裁定（判断(s)の枠内、CEFRカタログ4）：liable（526）・inconvenience（527）・unresolved（629）・urgency（625）＝B2+〜C1行の交渉・公式通信の実態語彙として保持／madam（638・B1+）＝書面定型 Dear Sir or Madam の不可分の一部として保持／invoice（628・B2+）＝公式通信の実務語彙として保持。全件保持＝苦情の上位帯は語彙面でもB2+〜C1の実態と整合し、下位帯（544/533/532）にはフラグが無い ── 緩衝の梯子が語彙レベルの梯子とも並走している。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    rows = []
    for no, mode, ex, scene, hw, l1, delta in R:
        d = desc[str(no)]
        rows.append({"mode": mode, "level": d["level"], "no": no, "en": d["en"],
                     "jp": tr[str(no)], "exponents": ex, "scene": scene,
                     "howwell": hw, "l1": l1, "delta": delta})
    return {"苦情・クレーム": {"title": TITLE, "scope": SCOPE, "type": TYPE_,
                            "essence": ESSENCE, "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    data = build(root)
    out = os.path.join(here, "catalog_complaint.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data["苦情・クレーム"]["rows"]
    assert len(rows) == 9, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    print(f"catalog_complaint.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
