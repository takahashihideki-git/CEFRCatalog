# -*- coding: utf-8 -*-
# 第1カタログ 範型：発語内行為「苦情・クレーム」
# モード×レベルのマトリクス。各セル7項目 + 行為全体のDISCUSSION散文。
# exponent(実例)とL1注意が心臓部。CEFRレベルに語彙・機能・緩衝の度合いを合わせる。

ACT_TITLE = "苦情・クレーム（Complaining）"
ACT_TYPE  = "指示的（directive）＋表出的要素"
ACT_ESSENCE = "相手（店・機関・個人）に、現状が期待に反することを伝え、是正を求める。非難と要求の二面を持ち、両者のバランスが行為の成否を決める。"

# rows: (mode, level, no, en, jp_core, exponents[list], scene, howwell, l1_note, delta)
ROWS = [
 # ── 口頭系列 ──
 ("口頭","A2",544,
  'Can point out when something is wrong (e.g. “The food is cold” or “There is no light in my room”).',
  "何かがおかしいと指摘できる。",
  ['Excuse me, the food is cold.',
   'Sorry, there is no light in my room.',
   'Excuse me, this is not what I ordered.'],
  "レストランやホテルで、出されたもの・状態が違うとき、その事実を一言告げる。",
  "社会言語的適切さ（最小）：Excuse me / Sorry を頭に置けるか。",
  "日本語話者は「事実の指摘」を非難と感じて言い出せない傾向。英語では The food is cold. と現状を述べること自体は失礼でなく、むしろ必要な情報提供。黙って我慢する方が不自然。ただし頭に Excuse me を欠くと唐突。",
  "（起点）行為の最小形。まだ是正要求は含まず、問題の存在を告げるだけ。"),
 ("口頭","B1",533,
  'Can make a complaint.',
  "苦情を言える。",
  ['Excuse me, I ordered the pasta but this is a pizza. Could you change it, please?',
   "I'm sorry, but the room is really noisy. Would it be possible to move to another one?",
   "There seems to be a problem with the bill — I think we've been charged twice."],
  "注文違い・部屋の問題・請求の誤りなど、具体的な不都合について、是正を求めるところまで言う。",
  "社会言語的適切さ＋叙述の正確さ：問題の describe と要求の request を一続きにできるか。",
  "日本語の「すみません、これ頼んでないんですけど……」は語尾を濁して相手に察してもらう構造。英語では Could you change it? まで言い切らないと要求が伝わらず、問題提起だけで終わると「ただ不機嫌な人」になる。緩衝（I'm sorry but / There seems to be）＋明示的要求、の二点セットが鍵。",
  "A2からの飛躍：問題の指摘に「是正の要求」が加わる。行為が完結する最初のレベル。"),
 ("口頭","B1",532,
  'Can cope with less routine situations in shops, post offices, banks, e.g. returning an unsatisfactory purchase.',
  "満足できない買い物の返品など、非日常的な状況に対処できる。",
  ["I bought this shirt yesterday, but there's a hole in the sleeve. I'd like to return it, please.",
   "This isn't working properly — can I get a refund or an exchange?",
   "I'd like to return this. Do you need the receipt?"],
  "店で不良品を返品する、想定外のやりとり（理由の説明・レシートの授受）に対応する。",
  "柔軟さ：相手の反応（レシートは？交換か返金か）に応じて言い足せるか。",
  "返品は日本でも増えたが、英語圏では「正当な権利の行使」であり、過度に低姿勢だと逆に不審。I'd like to return this と平叙で切り出してよい。「返品してもらえますか」を Can I possibly...? と過剰に婉曲化すると、かえって要領を得ない。",
  "同じB1でも、単発の苦情から「一連のやりとりへの対処」へ。相手の応答を捌く柔軟さが問われる。"),
 ("口頭","B2+",526,
  'Can cope linguistically to negotiate a solution to a dispute like an undeserved traffic ticket, financial responsibility for damage in a flat, or blame regarding an accident.',
  "不当な交通違反切符、損害の金銭的責任、事故の責めなど、争いの解決を交渉できる。",
  ["I understand your position, but I don't think I'm liable for this. The damage was already there when I moved in.",
   "I'd like to contest this. Could you tell me exactly which regulation I'm supposed to have broken?",
   "I'm willing to cover part of it, but not the full amount — let me explain why."],
  "責任の所在が争われる場面で、相手の主張を受けつつ自分の立場を通し、着地点を探る。",
  "叙述の正確さ＋柔軟さ＋社会言語的適切さ：反論しつつ関係を壊さない語調の制御。",
  "日本語話者は対立局面で沈黙するか、逆に感情的に強く出るかの両極に振れやすい。英語の交渉苦情は I understand X, but Y（相手の承認→自分の主張）という型が定石で、冷静に but でつなぐ。謝罪の I'm sorry を安易に挟むと責任を認めた含意になり不利。",
  "苦情から「交渉」へ。一方的要求ではなく、相手の立場の承認と自分の譲歩限度の提示が入る。"),
 ("口頭","B2+",527,
  'Can outline a case for compensation, using persuasive language to demand satisfaction and state clearly the limits to any concession they are prepared to make.',
  "説得力ある言葉で補償を求め、譲歩できる限度を明確に述べられる。",
  ["Given the inconvenience caused, I believe a full refund plus compensation for the extra costs is reasonable.",
   "I'm prepared to accept a replacement, but only if it's delivered by Friday — otherwise I'll expect a refund.",
   "This has cost me two days of work. I'd like that reflected in whatever you're offering."],
  "実害が生じた案件で、補償の根拠を筋道立てて示し、受け入れ条件と限度を明言する。",
  "叙述の正確さ（最大）＋話題の展開：根拠→要求→条件を論理的に積む構成力。",
  "「譲歩の限度を明示する」は日本語の交渉文化と最も遠い。日本語では限度をあえて曖昧にして含みで交渉するが、英語では but only if... / otherwise I'll... と条件と帰結を言語化するのが誠実で強い。曖昧なままだと足元を見られる。",
  "交渉に「論理的な根拠づけ」と「条件の明示的言語化」が加わる。口頭系列の到達点。"),
 # ── 書面系列 ──
 ("書面","B1+",638,
  'Can compose basic formal e-mails/letters (e.g. to make a complaint and request action).',
  "基本的な公式メール・手紙（苦情を述べ対応を求める）を書ける。",
  ['Dear Sir or Madam, I am writing to complain about the delayed delivery of my order (#12345). I would like to request a full refund.',
   'I ordered the item on 3 May, but it has still not arrived. Please let me know how you intend to resolve this.'],
  "遅延・不良・誤請求について、公式メールで苦情と対応要求を伝える。",
  "社会言語的適切さ（書面レジスター）：I am writing to... の定型と Dear/Yours の枠を守れるか。",
  "日本語のビジネス苦情メールは長い前置き（お世話になっております＋クッション）から入るが、英語は I am writing to complain about... と冒頭で用件を明示するのが正しい作法。前置きを長くすると要領を得ない印象。",
  "口頭B1と並行して、書面系列が独立に立ち上がる。定型（I am writing to）とレジスターの獲得が核。"),
 ("書面","B2+",629,
  'Can compose a forceful but polite letter of complaint, including supporting details and a statement of the desired outcome.',
  "裏づけの詳細と望む結果を明記した、力強くも丁寧な苦情の手紙を書ける。",
  ['Despite my email of 3 May, the issue remains unresolved. I have now been waiting three weeks for a replacement.',
   'I trust you will appreciate my frustration and arrange a full refund within seven days.'],
  "一度目の苦情が解決されない案件で、経緯を裏づけつつ、丁寧さを保って強く要求する。",
  "話題の展開＋社会言語的適切さ：forceful と polite を両立させる語調設計。",
  "「力強くも丁寧に」の両立が難所。日本語話者は polite に振れすぎて要求が弱まるか、直訳的に強く書いて無礼になるか。英語は I trust you will... / I would appreciate it if... で、丁寧な形式のまま圧をかける定型がある。この「丁寧な強さ」の語彙庫を持つことが鍵。",
  "書面B1+からの飛躍：単発の苦情から、経緯の裏づけ・望む結果の明記・語調の制御へ。"),
 ("書面","B2+",628,
  'Can compose formal correspondence such as letters of enquiry, request, application and complaint using appropriate register, structure and conventions.',
  "適切なレジスター・構成・慣習で、問い合わせ・依頼・応募・苦情の公式通信文を書ける。",
  ['I am writing with reference to invoice #789, which appears to contain an error.',
   'I would be grateful if you could look into this matter and respond at your earliest convenience.'],
  "苦情を含む各種公式通信を、型・レジスター・慣習に則って書き分ける。",
  "社会言語的適切さ（慣習の体系）：with reference to / at your earliest convenience 等の定型群の運用。",
  "英語の公式通信は定型表現の体系（with reference to, I would be grateful if, at your earliest convenience）で動く。日本語の敬語体系とは別物なので、日本語敬語を英語に写そうとせず、英語独自の formal 定型を丸ごと語彙として習得する必要がある。",
  "個別の苦情から「公式通信文一般の型」への一般化。苦情が他の書面行為（依頼・応募）と型を共有すると気づく段。"),
 ("書面","C1",625,
  'Can, with good expression and accuracy, compose formal correspondence such as letters of clarification, application, recommendation, reference, complaint, sympathy and condolence.',
  "うまい表現と正確さで、明確化・応募・推薦・苦情・弔慰などの公式通信文を書ける。",
  ['While I appreciate that delays can occur, a three-week silence following my formal complaint is difficult to justify.',
   'I would ask that you treat this as a matter of urgency and confirm your proposed resolution in writing.'],
  "洗練を要する公式通信で、含意・語調・正確さを制御して苦情を述べる。",
  "叙述の正確さ＋柔軟さ（最大）：含意・皮肉・緩衝を精密に制御する表現力。",
  "C1では While I appreciate that..., ... is difficult to justify のような、譲歩節で相手を立てつつ論理で追い込む高度な緩衝が要る。日本語の高等な苦情（慇懃な圧）に感覚は近いが、英語独自のレトリックなので、日本語の語感からの類推は危険。個別の表現を範例で覚える段階。",
  "B2+からの到達点：正確さに加え「うまい表現（good expression）」＝含意と語調の精密制御。書面系列の頂点。"),
]

DISCUSSION = """\
【緩衝（mitigation）が行為の背骨である】
英語の苦情を貫く原理は「非難性の緩衝」である。同じ事実（料理が冷たい）を、A2では Excuse me を頭に置くだけ、B1では There seems to be... で事実を非人称化し、B2+では I understand your position, but... で相手を立て、C1では While I appreciate that... と譲歩節で包む——レベルが上がるとは、緩衝の技法が精緻化することにほかならない。この行為において how well の主軸は一貫して社会言語的適切さであり、文法的正確さではない。文法的に完璧な The food is cold and I want a new one now. は、B1の緩衝された表現より「下手」なのである。

【日本語話者にとっての二重の壁】
第一の壁は「言い出せない」こと。日本語文化では苦情＝関係を損なう行為とされ、我慢が美徳になりやすい。だが英語圏では、正当な苦情は消費者の権利であり情報提供でもあって、黙る方が不自然に映る。第二の壁は、言い出せた場合に「振れすぎる」こと——過度に低姿勢で要求が伝わらないか、直訳的に強く出て無礼になるかの両極。英語の苦情は「丁寧な形式を保ったまま要求を明示する」ことを求めるが、これは日本語の「察してもらう」構造とも「けんか腰」とも異なる第三の様式であり、明示的に学ぶしかない。

【苦情は依頼と背中合わせである】
「部屋が寒い」（苦情）は「暖房を入れてほしい」（依頼）と表裏一体で、多くの苦情は是正の依頼を含意する。25行為インベントリで苦情と依頼を別立てにしたが、実運用では連続する。苦情を教えるとき、是正要求（依頼）まで一続きで示さないと、行為が完結しない——日本語話者が問題提起だけで止まりがちなのは、この連続性が母語で言語化されないためでもある。

【口頭と書面は別の行為に近い】
CEFRが苦情を口頭スケール（Obtaining goods and services）と書面スケール（Correspondence）に分けて記述しているのは示唆的である。口頭の苦情は即時・対面で、緩衝も即興的（Excuse me, sorry）。書面の苦情は経緯の裏づけ・構成・レジスターが前面に出て、定型表現の体系（I am writing to, I would be grateful if）で動く。学習者にとっては習得順序も異なり、口頭A2から始まる系列と、書面B1+から始まる系列は、並行して別々に登らせるのが自然である。

【なぜこの行為が範型に適するか】
苦情は、発語内行為25種の中でも、L1語用論的転移が最も激しく、かつレベル差分が最も明瞭に観察できる。緩衝技法の精緻化としてA2→C1が一直線に読め、how wellの主軸（社会言語的適切さ）が行為全体を貫く。他の24行為を作り込む際、この「緩衝の精緻化」「言い出せない／振れすぎるの二重の壁」「隣接行為との連続」「口頭・書面の分岐」という4つの観察軸が、そのまま点検リストになる。"""
