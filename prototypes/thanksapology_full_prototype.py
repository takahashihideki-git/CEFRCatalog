# -*- coding: utf-8 -*-
"""第3周-3：感謝・詫び・祝意（6件）の全数範型（様式昇格）。

既存検証範型の著述フィールドを継承し、全数シート様式へ昇格：jp を作業訳に正準化
（構築時取得）、第2周以降の点検軸（(n)往復・応答／(o)書面フォーマル一段／
判断(s)語彙裁定）を DISCUSSION に適用。旧範型は歴史的サンプルとして凍結。

単一情報源の設計：en / jp は data から構築時取得。
実行すると prototypes/catalog_thanksapology.json を生成する。
"""
import json, os

TITLE = '感謝・詫び・祝意（Thanking, Apologising & Congratulating）── 全数シート'
SCOPE = '全数（6件。口頭2＋書面4）'
TYPE_ = '表出的（expressive）だが運用上は定型の履行 ── 下位系＝儀礼的表出系（第一分類層）、出自類型＝表出、梯子型＝定型履行型（難所は横＝レジスターと授受の対へ）'
ESSENCE = '受けた行為への感謝、自己の過失への詫び、相手の慶事への祝意を、定型表現の適切な選択と授受によって遂行する。誠実さの中身より、型の選択（対象・レジスター・強度）と応答の往復が行為の成否を決める。'

R = [
(446,
 '口頭',
 ["I'm sorry I'm late.", "Sorry about that.", "— That's OK. / No problem. / Don't worry about it."],
 "遅刻や小さな不手際について日常の詫びを述べ、相手の詫びを受け入れる。（記述文は招待・提案と束だが、本行為の担当は詫びの授受）",
 "社会言語的適切さ（定型の授受）：詫びと受諾の定型ペアを往復で回せるか。",
 "「すみません」の反射で I'm sorry を乱発すると、英語では過失の正式な承認として重く響く場面がある（軽い接触なら Excuse me / Oops, sorry）。逆に詫びを受ける側の定型（No problem. / It happens.）が日本語の「いえいえ」ほど自動化されておらず、詫びられて沈黙し気まずくなる。",
 "（起点）詫びの最小形。「する」と「受ける」が最初から対で要求される ── 一方向の表明で完結する意見表明との構造差。"),
(441,
 '口頭',
 ["Thank you so much for your help.", "That's very kind of you.", "I really appreciate it."],
 "世話になった相手に、気持ちの言葉を添えて礼を述べる。",
 "社会言語的適切さ（強度の調整）：so much / really で感謝を増幅し、相手の行為を肯定的に評価できるか。",
 "感謝の場面で「すみません」を直訳し I'm sorry と言う転移が典型（荷物を持ってもらって I'm sorry）。日本語の感謝は負債の承認に傾くが、英語は相手の行為への肯定評価（That's very kind of you）で返す。また Thank you への応答（You're welcome. / My pleasure. / No problem.）も型として在庫する必要がある。",
 "詫びの授受に感謝が加わり、気持ちの一言を添えて礼を厚くできる。そして口頭系列はここで打ち止め ── B1以上の記述文は存在しない。"),
(685,
 '書面',
 ["Thanks for sharing!", "Great photo!", "Sorry for the late reply."],
 "SNSの投稿に短い反応を返し、コメントに定型の礼や詫びで応じる。",
 "定型表現の運用（軽装のレジスター）：オンラインの軽い礼・詫びの型をそのまま使えるか。",
 "日本語SNSは「いいね」と絵文字への依存が強く、言語化された反応定型（Thanks for...! / Love this!）の在庫が薄い。またオンラインの軽い詫び（Sorry for the late reply）は手紙の改まった詫びとは別レジスターの別の型であり、混用すると過剰に重くなる。",
 "書面系列の起点。定型をそのまま貼る段階で、感謝・詫びが最初から応答（respond）として要求される。"),
(644,
 '書面',
 ["Thank you for the lovely present.", "I'm sorry I couldn't come to your party.", "It was really kind of you to invite me."],
 "私的な手紙・メッセージで、対象を明示した礼と詫びを短く述べる。",
 "定型＋対象の明示：for句・that節で感謝や詫びの対象を特定できるか。",
 "日本語の手紙は「お世話になっております」「先日はどうも」のような対象を言わない万能定型で回るが、英語の感謝は Thank you for + 名詞/動名詞 と対象の明示を構造的に要求する。対象を言わない Thank you. だけの礼状は英語では空回りする。詫びも同様に I'm sorry (that) I... と過失内容の言語化が要る。",
 "オンラインの即時反応から、対象を明示した一文の礼状・詫び状へ。for句・that節による対象特定の構造が加わる。"),
(646,
 '書面',
 ["Happy birthday! Hope you have a wonderful day.", "Wishing you a very happy New Year.", "Congratulations on your new job!"],
 "カードやメッセージに、祝意の定型句を書く。",
 "祝意の定型選択：Happy X / Wishing you... / Congratulations on... の使い分け。",
 "祝意はほぼ完全な定型の世界で「おめでとう」との機能対応は良い。ただし英語には語彙分業がある ── Congratulations は達成（合格・昇進・結婚）専用で、誕生日や新年には使えない（Happy birthday ○ / Congratulations ×）。「おめでとう」一語の感覚で Congratulations を暦の祝いに使う誤りが典型的な穴。",
 "詫び・感謝と並ぶ第三の要素「祝意」が加わる。完全定型であり、この要素にレベルの梯子は事実上ない。"),
(632,
 '書面',
 ["I would like to express my sincere gratitude for your support.", "Please accept my apologies for the inconvenience caused.", "We would be delighted if you could join us for the reception."],
 "【フォーマル】公式なメール・書簡で、儀礼にかなったフォーマル・レジスターの礼状・詫び状・招待状を書く。",
 "社会言語的適切さ（フォーマル・レジスターの慣習体系）：gratitude / apologies の名詞化、would による遠隔化、書簡の型。",
 "日本語のビジネス文書定型（拝啓・時候の挨拶・「平素より格別のご高配を賜り…」）を直訳しようとする転移。英語のフォーマルは冒頭の儀式的定型ではなく、感謝・詫びの名詞化（express my gratitude / accept my apologies）と法助動詞の遠隔化（would / could）で作る。丁寧さの生成原理そのものが違うため、対応表ではなく原理の学習が要る。",
 "A2からB2への跳躍は行為の深化ではなく、レジスターの制度化。口頭系列に存在しないこの一段が、この行為の唯一の「上級」である。"),
]

DISCUSSION = [
"【表出型の皮を被った定型履行型 ── レベル軸の消失】 サールの分類では感謝・詫び・祝意は話者の心的状態を表出する行為（出自類型＝表出）だが、CEFRの記述文分布は定型履行型の地形を示す。口頭系列はA2/A2+で出尽くし、B1以上の記述文が一つも無い ── 挨拶と同じ消失パターンである。理由も同じで、Thank you は感謝の記述ではなく感謝の遂行（performative）であり、誠実条件の中身を精緻に述べる必要がない。型を適切に履行すれば行為は成立する。C2話者も Thank you so much. と言う。第2周-4でこの行為が下位系＝儀礼的表出系として第一分類層に立ち、出自類型（表出）は理論タグに退いたのは、この運用実態の追認である。",
"【すみません問題 ── L1で感謝と詫びが一語に融合している】 この行為に固有の最大のL1難所は、日本語の「すみません」が負債の承認という一つの原理で感謝と詫びを兼ねることにある。英語は Thank you（相手の行為への肯定評価）と I'm sorry（自己の過失の承認）を峻別し、混用は単なる不自然ではなく機能の取り違えになる ── 荷物を持ってもらって I'm sorry と言えば、相手は何を詫びられたのか分からない。加えて日本語の詫び反復（「何度もすみません」「恐縮です」）を写すと英語では過剰で自罰的に響く。さらに授受の非対称：日本語話者は礼と詫びを「言う」側の定型は学ぶが、「受ける」側の定型（You're welcome. / No worries. / It happens.）の在庫が薄く、応答の沈黙が儀礼の不履行になる ── 往復・応答軸（判断(n)）の病理の典型例で、No.446は受諾（That's OK. / No problem.）まで記述文が明記する。",
"【口頭は登らないが、書面は一段登る ── 書面フォーマル一段（判断(o)）の原点】 挨拶は書面系列もA2で消えたが、この行為は書面にB2（No.632、フォーマル・レジスター）が一段だけ立つ。中身は行為の深化ではない ── 詫びる内容が高度になるのではなく、gratitude / apologies の名詞化や would の遠隔化といったレジスターの慣習体系が制度化されるだけである。つまり唯一の「上級」はhow well軸（社会言語的適切さ）が書面で制度化された姿であり、can doの梯子ではない。この観察（第1周①）が判断(o)「書面フォーマル一段」の原点であり、第3周までに授受No.633・苦情No.628で再現して3例となった。精緻化条件「Correspondence系列がB2帯まで伸びる行為でのみ現れる」の成立例の初出として、この行為は軸の型式標本である。",
"【祝意の語彙分業 ── 完全定型の世界】 祝意は三要素の中で最も定型性が高く、「おめでとう」との機能対応も良いため転移は少ないが、一点だけ構造的な穴がある。英語の祝意には語彙分業があり、Congratulations は努力による達成（合格・昇進・結婚）専用、暦や記念日は Happy X / Wishing you... が担当する。「おめでとう」一語の感覚で誕生日に Congratulations と書く誤りは、この分業が母語に存在しないために起こる。逆に言えば、祝意はこの分業表一枚でほぼ教え尽くせる ── レベルの梯子も、緩衝の精緻化も要らない。",
"【点検総括と語彙裁定】 往復・応答（判断(n)）の三点：する側＝全6件、受ける側＝446の受諾定型が記述文に明記（往復の双方向が記述文レベルで立つ、挨拶と並ぶ教科書例）、断る・返す型＝詫びの受諾（That's OK.）がその機能を担う。書面フォーマル一段（判断(o)）＝成立の原点（第3段落）。語彙裁定（判断(s)の枠内、CEFRカタログ4）：reply（685・A1行）＝オンライン定型 Sorry for the late reply. の不可分の一部として保持／inconvenience（632・B2行）＝公式詫び定型 apologies for the inconvenience caused の実態語彙として保持（苦情527と同語・同裁定）。congratulations/congrats は allowlist 裁定済み（判断(s)-2）。",
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
    return {'感謝・詫び・祝意': {"title": TITLE, "scope": SCOPE, "type": TYPE_,
                      "essence": ESSENCE, "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    data = build(root)
    out = os.path.join(here, 'catalog_thanksapology.json')
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data['感謝・詫び・祝意']["rows"]
    assert len(rows) == 6, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    print(f"catalog_thanksapology.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
