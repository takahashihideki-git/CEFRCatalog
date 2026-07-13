# -*- coding: utf-8 -*-
# 第1カタログ 検証範型その1：発語内行為「感謝・詫び・祝意」（表出型の下位分化検証①）
# 検証課題：意見表明範型（表出型代表）の点検軸がこの行為に効くか。儀礼型寄りの疑い。
ACT_TITLE = "感謝・詫び・祝意（Thanking, Apologising & Congratulating）"
ACT_TYPE  = "表出的（expressive）── ただし運用実態は儀礼的（phatic寄り）。心的状態の記述ではなく、型の履行として遂行される"
ACT_ESSENCE = "受けた行為への感謝、自己の過失への詫び、相手の慶事への祝意を、定型表現の適切な選択と授受によって遂行する。誠実さの中身より、型の選択（対象・レジスター・強度）と応答の往復が行為の成否を決める。"

# (mode, level, no, en, jp, exponents, scene, howwell, l1_note, delta)
ROWS = [
 ("口頭","A2",446,
  'Can make and respond to invitations, suggestions and apologies.',
  "招待・提案・詫びをし、それに応じられる。",
  ["I'm sorry I'm late.", "Sorry about that.", "— That's OK. / No problem. / Don't worry about it."],
  "遅刻や小さな不手際について日常の詫びを述べ、相手の詫びを受け入れる。（記述文は招待・提案と束だが、本行為の担当は詫びの授受）",
  "社会言語的適切さ（定型の授受）：詫びと受諾の定型ペアを往復で回せるか。",
  "「すみません」の反射で I'm sorry を乱発すると、英語では過失の正式な承認として重く響く場面がある（軽い接触なら Excuse me / Oops, sorry）。逆に詫びを受ける側の定型（No problem. / It happens.）が日本語の「いえいえ」ほど自動化されておらず、詫びられて沈黙し気まずくなる。",
  "（起点）詫びの最小形。「する」と「受ける」が最初から対で要求される ── 一方向の表明で完結する意見表明との構造差。"),
 ("口頭","A2+",441,
  'Can express how they feel in simple terms, and express thanks.',
  "自分の気持ちを簡単な言葉で表現し、感謝を伝えられる。",
  ["Thank you so much for your help.", "That's very kind of you.", "I really appreciate it."],
  "世話になった相手に、気持ちの言葉を添えて礼を述べる。",
  "社会言語的適切さ（強度の調整）：so much / really で感謝を増幅し、相手の行為を肯定的に評価できるか。",
  "感謝の場面で「すみません」を直訳し I'm sorry と言う転移が典型（荷物を持ってもらって I'm sorry）。日本語の感謝は負債の承認に傾くが、英語は相手の行為への肯定評価（That's very kind of you）で返す。また Thank you への応答（You're welcome. / My pleasure. / No problem.）も型として在庫する必要がある。",
  "詫びの授受に感謝が加わり、気持ちの一言を添えて礼を厚くできる。そして口頭系列はここで打ち止め ── B1以上の記述文は存在しない。"),
 # ── 書面・オンライン系列 ──
 ("書面","A1",685,
  'Can use formulaic expressions and combinations of simple words/signs to post short positive and negative reactions to simple online postings and their embedded links and media, and can respond to further comments with standard expressions of thanks and apology.',
  "定型表現と簡単な語の組み合わせを使って、簡単なオンライン投稿とその埋め込みリンク・メディアに短い肯定的・否定的反応を投稿し、標準的な感謝や詫びの表現でさらなるコメントに応じられる。",
  ["Thanks for sharing!", "Great photo!", "Sorry for the late reply."],
  "SNSの投稿に短い反応を返し、コメントに定型の礼や詫びで応じる。",
  "定型表現の運用（軽装のレジスター）：オンラインの軽い礼・詫びの型をそのまま使えるか。",
  "日本語SNSは「いいね」と絵文字への依存が強く、言語化された反応定型（Thanks for...! / Love this!）の在庫が薄い。またオンラインの軽い詫び（Sorry for the late reply）は手紙の改まった詫びとは別レジスターの別の型であり、混用すると過剰に重くなる。",
  "書面系列の起点。定型をそのまま貼る段階で、感謝・詫びが最初から応答（respond）として要求される。"),
 ("書面","A2",644,
  'Can compose very simple personal letters expressing thanks and apology.',
  "感謝や詫びを伝えるごく簡単な個人的な手紙を書ける。",
  ["Thank you for the lovely present.", "I'm sorry I couldn't come to your party.", "It was really kind of you to invite me."],
  "私的な手紙・メッセージで、対象を明示した礼と詫びを短く述べる。",
  "定型＋対象の明示：for句・that節で感謝や詫びの対象を特定できるか。",
  "日本語の手紙は「お世話になっております」「先日はどうも」のような対象を言わない万能定型で回るが、英語の感謝は Thank you for + 名詞/動名詞 と対象の明示を構造的に要求する。対象を言わない Thank you. だけの礼状は英語では空回りする。詫びも同様に I'm sorry (that) I... と過失内容の言語化が要る。",
  "オンラインの即時反応から、対象を明示した一文の礼状・詫び状へ。for句・that節による対象特定の構造が加わる。"),
 ("書面","A2",646,
  'Can compose a short text in a greetings card (e.g. for someone\u2019s birthday or to wish them a Happy New Year).',
  "グリーティングカードに短い文（誕生日祝いや新年の挨拶など）を書ける。",
  ["Happy birthday! Hope you have a wonderful day.", "Wishing you a very happy New Year.", "Congratulations on your new job!"],
  "カードやメッセージに、祝意の定型句を書く。",
  "祝意の定型選択：Happy X / Wishing you... / Congratulations on... の使い分け。",
  "祝意はほぼ完全な定型の世界で「おめでとう」との機能対応は良い。ただし英語には語彙分業がある ── Congratulations は達成（合格・昇進・結婚）専用で、誕生日や新年には使えない（Happy birthday ○ / Congratulations ×）。「おめでとう」一語の感覚で Congratulations を暦の祝いに使う誤りが典型的な穴。",
  "詫び・感謝と並ぶ第三の要素「祝意」が加わる。完全定型であり、この要素にレベルの梯子は事実上ない。"),
 ("書面","B2",632,
  'Can compose formal e-mails/letters of invitation, thanks or apology using appropriate registers and conventions.',
  "適切な言語使用域と慣習を使って、招待・感謝・詫びの公式なメールや手紙を書ける。",
  ["I would like to express my sincere gratitude for your support.", "Please accept my apologies for the inconvenience caused.", "We would be delighted if you could join us for the reception."],
  "公式なメール・書簡で、儀礼にかなったフォーマル・レジスターの礼状・詫び状・招待状を書く。",
  "社会言語的適切さ（フォーマル・レジスターの慣習体系）：gratitude / apologies の名詞化、would による遠隔化、書簡の型。",
  "日本語のビジネス文書定型（拝啓・時候の挨拶・「平素より格別のご高配を賜り…」）を直訳しようとする転移。英語のフォーマルは冒頭の儀式的定型ではなく、感謝・詫びの名詞化（express my gratitude / accept my apologies）と法助動詞の遠隔化（would / could）で作る。丁寧さの生成原理そのものが違うため、対応表ではなく原理の学習が要る。",
  "A2からB2への跳躍は行為の深化ではなく、レジスターの制度化。口頭系列に存在しないこの一段が、この行為の唯一の「上級」である。"),
]

DISCUSSION = """\
【表出型の皮を被った儀礼型 ── レベル軸の消失】
サールの分類では感謝・詫び・祝意は話者の心的状態を表出する行為（表出型）だが、CEFRの記述文分布は儀礼型の地形を示す。口頭系列はA2/A2+で出尽くし、B1以上の記述文が一つも無い ── 挨拶と同じ消失パターンである。理由も同じで、Thank you は感謝の記述ではなく感謝の遂行（performative）であり、誠実条件の中身を精緻に述べる必要がない。型を適切に履行すれば行為は成立する。C2話者も Thank you so much. と言う。したがってこの行為のカタログも挨拶と同様、「レベルを上る」構造ではなく「型を場に合わせて選ぶ」水平の広がりを持つ。

【すみません問題 ── L1で感謝と詫びが一語に融合している】
この行為に固有の最大のL1難所は、日本語の「すみません」が負債の承認という一つの原理で感謝と詫びを兼ねることにある。英語は Thank you（相手の行為への肯定評価）と I'm sorry（自己の過失の承認）を峻別し、混用は単なる不自然ではなく機能の取り違えになる ── 荷物を持ってもらって I'm sorry と言えば、相手は何を詫びられたのか分からない。加えて日本語の詫び反復（「何度もすみません」「恐縮です」）を写すと英語では過剰で自罰的に響く。さらに授受の非対称：日本語話者は礼と詫びを「言う」側の定型は学ぶが、「受ける」側の定型（You're welcome. / No worries. / It happens.）の在庫が薄く、応答の沈黙が儀礼の不履行になる。挨拶範型の「テンポ」軸がここでも効いている。

【口頭は登らないが、書面は登る ── 挨拶範型との差分】
挨拶は書面系列もA2で消えたが、この行為は書面にB2（フォーマル・レジスター）が一段だけ立つ。ただしその中身は行為の深化ではない ── 詫びる内容が高度になるのではなく、gratitude / apologies の名詞化や would の遠隔化といったレジスターの慣習体系が制度化されるだけである。つまり唯一の「上級」はhow well軸（社会言語的適切さ）が書面で制度化された姿であり、can doの梯子ではない。この発見は儀礼型の内部にも差分があることを示す：儀礼型は「書面フォーマルの一段を持つ行為（感謝・詫び）」と「持たない行為（挨拶）」に分かれ、前者では書面レジスターを独立の到達点として教える必要がある。

【祝意の語彙分業 ── 完全定型の世界】
祝意は三要素の中で最も定型性が高く、「おめでとう」との機能対応も良いため転移は少ないが、一点だけ構造的な穴がある。英語の祝意には語彙分業があり、Congratulations は努力による達成（合格・昇進・結婚）専用、暦や記念日は Happy X / Wishing you... が担当する。「おめでとう」一語の感覚で誕生日に Congratulations と書く誤りは、この分業が母語に存在しないために起こる。逆に言えば、祝意はこの分業表一枚でほぼ教え尽くせる ── レベルの梯子も、緩衝の精緻化も要らない。

【範型検証の記録 ── 意見表明範型は効かなかった】
表出型の範型「意見・見解の表明」の点検軸をこの行為に当てた結果：①A2→C1の長い梯子（表明→支持→維持→反論の深化）── 効かない。口頭はA2+で消失。②不同意の緩衝（受けてから返す）── 全く効かない。この行為に対立の契機が構造的に存在しない。③ I think 枠と主観標識の温度差 ── 効かない。④根拠で支える叙述 ── 効かない。効いたのはすべて儀礼型（挨拶範型）の点検軸である：レベル軸の消失、定型性、レジスター選択、型の往復とテンポ、そして機能概念（phatic性／遂行性）の明示的説明の必要。新たに要る軸は「L1での機能融合（すみません問題）」と「書面フォーマル一段の有無」の二つ。判定：感謝・詫び・祝意は類型タグ上「表出」だが、運用上は儀礼型として振る舞う。表出型は単一ではなく、少なくとも意見表明系と儀礼的表出系に割れる ── 次の検証（感情の表出）で、感情叙述系を加えた三分割になるかを確定する。"""
