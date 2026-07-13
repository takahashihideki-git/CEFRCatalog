# -*- coding: utf-8 -*-
# 第1カタログ 検証範型その2：発語内行為「感情の表出」（表出型の下位分化検証②）
# 検証課題：意見表明範型の点検軸（特に不同意の緩衝）がこの行為に効くか。「作法軸が効かない」疑い。
ACT_TITLE = "感情の表出（Expressing & responding to feelings）"
ACT_TYPE  = "表出的（expressive）── 心的状態そのものを言語化する最も純粋な表出。ただし梯子の中身は対立の管理ではなく叙述の解像度"
ACT_ESSENCE = "自分の感情を名指し、その度合いと出来事にとっての意味を言語化し、相手の感情や知らせに感情で応じる。レベルが上がるとは、感情語彙の解像度（種類→度合い→意味づけ）が上がることである。"

# (mode, level, no, en, jp, exponents, scene, howwell, l1_note, delta)
ROWS = [
 ("口頭","A2",447,
  'Can express how they are feeling, using very basic stock expressions.',
  "ごく基本的な決まり文句を使って、自分の気分を表現できる。",
  ["I'm happy. / I'm tired.", "I'm so excited!", "That's great! / Oh no!"],
  "いまの気分・体調を、決まり文句一つで口にする。",
  "語彙（基本感情語）：I'm + 感情形容詞の骨格と、ごく基本の感嘆定型。",
  "日本語の感情表現は「嬉しい」「疲れた」と主語を立てない形容詞述語だが、英語は I'm + 形容詞で主語の明示が要る。最初の構造的難所は -ed/-ing の別（excited/exciting, bored/boring）── I'm boring.（私は退屈な人間だ）事故はこの段階から始まる。",
  "（起点）感情表出の最小形。決まり文句の貼り付けで、種類はまだ happy/sad/tired 程度の粗さ。"),
 ("口頭","B1",437,
  'Can express and respond to feelings such as surprise, happiness, sadness, interest and indifference.',
  "驚き・喜び・悲しみ・関心・無関心などの感情を表現し、それに応じられる。",
  ["Really? That's amazing!", "I'm so sorry to hear that.", "To be honest, I'm not that interested."],
  "会話の中で自分の感情を種類で言い分け、相手の感情や知らせに感情で応じる。",
  "語彙範囲（感情の種類分化）＋社会言語的適切さ：相手の感情への応答定型を持てるか。",
  "難所は「応じる」側にある。日本語の相槌（へえ、そうなんだ）は感情の名指しを避けて成立するが、英語は That's amazing! / I'm sorry to hear that. と感情語で明示的に反応するのが定石で、この応答定型の在庫が薄いと沈黙が冷淡に響く。また無関心の表明は日本語では回避されがちで、to be honest / not that... の緩衝を添えて言う型ごと学ぶ必要がある。",
  "決まり文句から「種類の分化＋往復」へ。express に respond が加わり、感情表出が対話的になる。"),
 ("口頭","B2",431,
  'Can convey degrees of emotion and highlight the personal significance of events and experiences.',
  "感情の度合いを伝え、出来事や経験の個人的な意味を強調できる。",
  ["I was absolutely devastated.", "It meant a lot to me — more than I expected.", "I can't tell you how relieved I was."],
  "経験を語りながら、感情の強さを段階づけ、その出来事が自分にとって持つ意味を際立たせる。",
  "叙述の正確さ＋語彙使いこなし（強度の段階づけ）：強意副詞と語彙の強度階層、意味づけの言語化。",
  "度合いは強意副詞（absolutely, utterly）と語彙自体の強度階層（sad < upset < devastated）の二層で作るが、日本語話者は very + 基本語（very sad 一本槍）に潰しがち。コロケーション制約（absolutely devastated ○ / very devastated ×）も語彙使いこなしの壁。「個人的な意味の強調」は出来事の事実でなく自分にとっての意味を語るメタ的な一段で、「感動しました」型の総称的評価では代替できない。",
  "種類の分化から「度合いの段階づけ＋意味づけ」へ。口頭系列の到達点で、これ以上（C1）の記述文は無い ── 先は文体の領域。"),
 # ── 書面・オンライン系列 ──
 ("書面","B1",639,
  'Can compose personal letters describing experiences, feelings and events in some detail.',
  "経験・感情・出来事をある程度詳しく描写する個人的な手紙を書ける。",
  ["I've just come back from Kyoto — it was such a special trip.", "I was really nervous at first, but everyone was so friendly."],
  "私的な手紙・メッセージで、経験と出来事に感情を絡めてある程度詳しく書く。",
  "叙述の正確さ：経験・感情・出来事の三点を時間軸の上で絡めて記述できるか。",
  "感情を単独で述べるのでなく、出来事の経過と絡めて書く（at first ... but ...）時間軸上の感情変化の記述が核。日本語の手紙は季節と定型句の層が厚く個人的感情の開示は薄めで、英語の私信に期待される開示量との較差がある ── 何を書けば「詳しく」なのかの感覚ごと調整が要る。",
  "書面系列の起点。感情が経験・出来事との三つ組で叙述される。"),
 ("書面","B1",678,
  'Can make personal online postings about experiences, feelings and events and respond individually to the comments of others in some detail, though lexical limitations sometimes cause repetition and inappropriate formulation.',
  "語彙の制約から時に繰り返しや不適切な表現が生じるものの、経験・感情・出来事についての個人的なオンライン投稿をし、他者のコメントにある程度詳しく個別に応じられる。",
  ["Had an amazing weekend at the beach — feeling so refreshed!", "— Thanks! Yes, the weather was perfect."],
  "SNSに経験と感想を投稿し、ついたコメントに個別に返信する。",
  "語彙範囲（記述文が語彙制約を明示する唯一の行）＋応答の往復。",
  "SNSの感情共有には英語圏固有の言語化慣習（feeling + 形容詞、so + 形容詞の増幅）があるが、日本語SNSでは感情表現が絵文字・スタンプに外注されがちで、言語化された感情共有の在庫が育ちにくい。CEFR自身が「繰り返しと不適切な表現」を明記するとおり、この段階の制約は語彙 ── amazing 一語の使い回しがその典型。",
  "手紙の一方向から、投稿＋コメント返信の往復へ。応答の対話性がオンラインで前面に出る。"),
 ("書面","B1+",636,
  'Can compose letters expressing different opinions and giving detailed accounts of personal feelings and experiences.',
  "異なる意見を表明し、個人的な感情や経験を詳しく述べる手紙を書ける。",
  ["I see it a bit differently — for me, moving away was the right decision.", "Looking back, I realise how anxious I was during those months."],
  "手紙の中で、相手と異なる見解を述べつつ、自分の感情と経験を詳しく振り返る。",
  "叙述の正確さ＋社会言語的適切さ：感情叙述に意見の差異表明が同居する境界的な一行。",
  "ここで初めて意見表明範型の軸（不同意の緩衝：I see it a bit differently）が部分的に接続する。ただし主役はあくまで感情・経験の詳述で、意見の差異はその文脈に置かれる。振り返りの型（Looking back, I realise...）は過去の感情への現在からのメタ視点で、日本語の「今思えば」に対応が良い数少ない箇所。",
  "感情の詳述に「異なる意見の表明」が加わり、意見表明系との境界がここで接する。"),
 ("書面","B1+",676,
  'Can post online accounts of social events, experiences and activities referring to embedded links and media and sharing personal feelings.',
  "埋め込みリンクやメディアに言及し、個人的な感想を共有しながら、社交行事・経験・活動についてオンラインに投稿できる。",
  ["Here are some photos from Saturday's reunion — it was wonderful to see everyone again.", "Can't believe how fast the day went."],
  "行事や活動の報告投稿に、写真・リンクへの言及と自分の感想を織り込む。",
  "話題の展開：メディアへの言及と感情の共有を一つの投稿に構成できるか。",
  "投稿が「感情の一言」から「行事の記録＋感想」の構成体になる段階。日本語のSNS報告文化との機能対応は良いが、感想部分を絵文字で済ませず言語化する慣習の差は678と共通。Can't believe how... のような感嘆の口語定型が構成の中で感情の山を作る。",
  "単発の感情表明から、記録と感想を統合した投稿へ。書面ならではの構成の軸が入る。"),
 ("書面","B2",630,
  'Can compose letters conveying degrees of emotion and highlighting the personal significance of events and experiences and commenting on the correspondent\u2019s news and views.',
  "感情の度合いを伝え、出来事や経験の個人的な意味を強調し、相手の近況や見解にコメントする手紙を書ける。",
  ["I was deeply moved by your letter.", "Your news made my day — you've worked so hard for this.", "That year changed how I see my family."],
  "手紙で、感情の強さと出来事の意味を書き分け、相手の近況・見解にも感情を込めてコメントする。",
  "叙述の正確さ＋社会言語的適切さ：自分の感情の度合いと、相手の知らせへの感情的応答の二方向。",
  "口頭B2の「度合い＋意味づけ」に、相手の近況への感情的コメント（I'm thrilled for you / made my day）が加わる。この応答部分は祝意・気遣いの定型群と接し、B1（437）で入った「応じる」軸の書面到達形。自分語りだけで手紙を埋め、相手の知らせへの応答を落とすのは日本語話者の私信でも起こる偏りで、二方向性そのものを型として意識する必要がある。",
  "書面系列の到達点。度合い・意味づけ・相手への応答の三要素が揃い、口頭B2と対をなす。"),
]

DISCUSSION = """\
【本物の梯子がある ── ただし対立管理ではなく叙述の梯子】
儀礼的表出（感謝・詫び・祝意）でレベル軸が消えたのと対照的に、感情の表出にはA2→B2の実質的な梯子がある。しかしその中身は意見表明の梯子（表明→支持→維持→反論という対立の管理）とは別物で、決まり文句（A2）→種類の分化と応答（B1）→度合いの段階づけと意味づけ（B2）という叙述の解像度の梯子である。C1以上が無いのは欠落ではなく、感情表出のcan doはB2で言語的に完成し、それ以上は文体・修辞（how well）の領域に移るためと読める。同じ表出型の中に、梯子が無い行為（儀礼的表出）・対立管理の梯子（意見表明）・解像度の梯子（感情）の三つの地形が併存する。

【効くhow well軸は叙述の正確さと語彙 ── 適切さの主軸が初めて外れる】
苦情・挨拶・意見表明はいずれも社会言語的適切さが主軸だったが、感情の表出の主軸は叙述の正確さ＋語彙（範囲と使いこなし）である。感情語彙の強度階層（sad < upset < devastated）、-ed/-ing の対立、強意副詞のコロケーション制約（absolutely devastated ○ / very devastated ×）── いずれも「語彙をどれだけ細かく持ち、正しく組み合わせるか」の問題で、対人配慮の問題ではない。No.678がCEFR全記述文でも珍しく語彙の制約（lexical limitations）を明記していることが、この行為の律速段階が語彙であることの内部証拠になっている。この点で感情の表出は、主張型（文法が主軸）とも異なる第三の主軸を持つ。

【L1難所は「作法」ではなく「解像度と開示」】
意見表明のL1中心軸だった不同意の作法（受けてから返す）は、この行為ではほぼ効かない。代わりに立つ難所は四つ。(a) 強度の潰れ：英語側の語彙階層を在庫していないため very + 基本語に一本化される。(b) -ed/-ing 事故：A2から一貫して続く構造的な穴。(c) 開示量の較差：感情の明示的な名指しは日本語では察しと相槌、SNSでは絵文字に外注されがちで、英語圏の言語化された感情共有の慣習との間に「どこまで言葉にするか」の較差がある。(d) 応答定型の欠落：That's amazing! / I'm sorry to hear that. / I'm thrilled for you. のような相手の感情・知らせへの反応の型が無いと、沈黙が冷淡に響く。作法（適切さ）が要るのはこの (d) だけで、しかも不同意ではなく共感の作法である。

【隣接行為との境界 ── 表出型内部の結節点】
この行為は三方向で他行為と接する。第一に、B1（No.437）で入る「応じる」構造は、儀礼的表出の授受構造（詫びを受ける・礼に応える）と同型で、往復性という儀礼型の軸がここにも顔を出す。第二に、書面B1+（No.636)では「異なる意見の表明」が感情叙述と同居し、意見表明系との境界が接する ── CEFR自身が両行為を一つの記述文に束ねている以上、この境界は分類の便宜であって運用では連続する。第三に、書面B2（No.630）の「相手の近況への感情的コメント」は祝意・気遣いの定型群と接する。感情の表出は表出型内部の結節点であり、意見表明系とも儀礼的表出系とも地続きでありながら、主軸（解像度）はどちらとも違う。

【範型検証の記録 ── 表出型は三分割で確定】
意見表明範型の点検軸を当てた結果：①長い梯子 ── 部分的に効く。A2→B2の梯子は実在するが、中身は対立の管理ではなく叙述の精緻化で、C1が無い。②不同意の緩衝 ── 効かない（唯一、境界行のNo.636で微かに接続）。③ I think 枠 ── 効かない。感情は主観標識を要さず I'm devastated. と直に言い切る。④根拠で支える ── 効かない。感情は根拠でなく度合いと意味づけで深まる。儀礼型の軸も主要部は効かない：レベル軸は消えず、定型性はA2のみ、レジスターも主役でない ── ただし「往復・応答」の軸だけは効く。新たに要る軸：感情語彙の強度階層、-ed/-ing、開示量の較差、共感の応答定型。判定：感情の表出は意見表明系（対立管理・適切さ主軸）とも儀礼的表出系（定型履行・レジスター主軸）とも異なる第三の顔＝感情叙述系（解像度・叙述の正確さ＋語彙主軸）を持つ。前回検証と合わせ、表出型は三分割で確定：意見表明系／儀礼的表出系／感情叙述系。残る表出型2行為の帰属は申し送り ── 好悪の表明（A1〜A2のみ4件）は感情叙述系の最下段か意見表明系の起点か、理解状態の表明（Asking for clarification系3件）はそもそも表出型でなく談話運営に近い疑いがあり、それぞれ個別判定を要する。"""
