# -*- coding: utf-8 -*-
# 第1カタログ 範型その4：表出型「意見・見解の表明」（expressive/assertive境界）
ACT_TITLE = "意見・見解の表明（Expressing opinions & views）"
ACT_TYPE  = "表出的（expressive）＋主張的要素 ── 話者の心的態度（賛否・評価）を表明し、根拠で支える"
ACT_ESSENCE = "ある事柄について自分の立場・評価・信念を述べ、レベルが上がるほど根拠と論拠で支え、他者の見解と関係づける。主張の中身より、立場表明の型と、対立を許容する作法が要となる。"

ROWS = [
 ("口頭","A2",479,
  "Can express opinions in a limited way.",
  "意見を限られた形で表明できる。",
  ["I think it's good.", "I like it. / I don't like it.", "For me, it's too expensive."],
  "身近な事柄に、ごく短く賛否や評価を述べる。",
  "文法（I think 節）：I think + 文 の骨格。",
  "I think を付けずに It's good. と言い切ると断定に響く。日本語は「〜と思う」を多用して主観を和らげるが、英語でも I think は立場表明の基本枠。ただし日本語の「思う」ほど義務的ではなく、乱発すると自信なさげにも響く、という温度差がある。",
  "（起点）意見表明の最小形。I think＋評価語のみ。"),
 ("口頭","A2+",473,
  "Can exchange opinions and compare things and people using simple language.",
  "簡単な言葉で意見を交換し、物や人を比較できる。",
  ["I think summer is better than winter.", "This one is nicer, but that one is cheaper.",
   "What do you think? — I agree. / I'm not sure."],
  "二つの選択肢を比べ、意見を交換し合う。",
  "文法（比較級）＋社会言語的適切さ：比較構文と同意/留保の応答。",
  "比較級（better than, nicer）の構造は日本語の「〜より」と語順が逆で作りにくい。また I'm not sure.（やんわり不同意）のような中間的応答の層が薄く、賛成か沈黙かの二択になりがち。",
  "単独の意見から「意見の交換と比較」へ。比較と応答の往復が加わる。"),
 ("口頭","B1",471,
  "Can express beliefs, opinions and agreement and disagreement politely.",
  "信念・意見・賛否を丁寧に表明できる。",
  ["I see your point, but I think...", "I agree with you up to a point.",
   "Actually, I don't really think that's true."],
  "議論の中で、賛成・反対を相手を立てつつ丁寧に表明する。",
  "社会言語的適切さ（不同意の緩衝）：反対を丁寧に包めるか。",
  "ここが表出型最大のL1難所。日本語話者は不同意を避けて曖昧にするか、逆に But that's wrong. と裸で否定して角を立てるかに振れる。英語は I see your point, but... / I'm not sure I agree で、相手をまず受けてから反対する型が定石。この「受けてから返す」二段構えは明示的に教える必要がある。",
  "A2+からの飛躍：単なる評価から「賛否の丁寧な表明」へ。不同意の緩衝が中心課題に。"),
 ("口頭","B1+",464,
  "Can express their thoughts about abstract or cultural topics such as music or films.",
  "音楽や映画などの抽象的・文化的な話題について考えを表現できる。",
  ["What I like about this film is how it handles memory.",
   "It's not really my kind of music, but I can see why people love it.",
   "The story felt a bit slow, but the ending made up for it."],
  "映画・音楽など抽象度の高い対象に、込み入った感想を述べる。",
  "叙述の正確さ＋語彙範囲：抽象的評価の語彙と構造。",
  "抽象的対象の評価は、日本語では「よかった／いまいち」で済ませがちだが、英語では what I like about X is... のような焦点化構文や、譲歩（but I can see why...）を使って立場を立体的に述べる。この構文の層を持たないと、抽象評価が幼く聞こえる。",
  "身近な物から「抽象的・文化的対象」へ。評価語彙と焦点化構文が加わる。"),
 ("口頭","B2",462,
  "Can account for and sustain their opinions in discussion by providing relevant explanations, arguments and comments.",
  "適切な説明・論拠・コメントを提供して、議論の中で自分の意見を述べ、支持できる。",
  ["I'd argue that... for two reasons. First,... Second,...",
   "That's a fair point, but the evidence actually suggests otherwise.",
   "I stand by what I said, because..."],
  "議論で自分の立場を、根拠を挙げて主張し、反論にも耐えて維持する。",
  "話題の展開＋叙述の正確さ：意見を論拠で構造的に支える。",
  "「意見を論拠で支え、維持する」は日本語話者に不慣れ。日本語の議論は結論を曖昧に残す作法もあるが、英語では I'd argue that... because... と立場と根拠を明示し、反論されても I stand by... と保持することが誠実とされる。撤回しすぎると立場が無いと見なされる。",
  "B1+からの飛躍：感想の表明から「論拠で支え維持する主張」へ。表出が論証に接続する。"),
 ("口頭","C1",670,
  "Can evaluate, restate and challenge arguments in professional or academic live online chat and discussion.",
  "専門的・学術的なライブのオンライン議論で、論を評価・言い直し・反論できる。",
  ["If I understand your position correctly, you're saying... — but that assumes...",
   "I'd push back on that slightly. The data you cite doesn't quite support...",
   "Let me reframe: the real question isn't X, it's Y."],
  "専門的議論で、相手の論を正確に捉え直し、的確に反論・再構成する。",
  "叙述の正確さ＋柔軟さ（最大）：論の評価・言い直し・反論の精密制御。",
  "C1では相手の論を restate（言い直して確認）してから challenge する高度な型が要る。日本語話者は相手の論の要約確認を飛ばして直接反論しがちで、議論がかみ合わない。If I understand you correctly...→but... の型は、正確さと礼節を両立させる英語アカデミック議論の作法として明示的に習得を要する。",
  "B2からの到達点：主張の維持から「他者の論の評価・再構成・反論」へ。表出型口頭系列の頂点。"),
 # 書面・オンライン系列
 ("書面","A2",683,
  "Can make brief positive or negative comments online about embedded links and media using a repertoire of basic language, though they will generally have to refer to an online translation tool and other resources.",
  "概してオンライン翻訳ツールその他の資料を参照する必要はあるが、埋め込みリンクやメディアに、基本的な言葉で短い肯定・否定コメントをオンラインでできる。",
  ["Love this! 😍", "Not for me, sorry.", "So true!"],
  "SNSの投稿やリンクに、短い賛否のコメントを付ける。",
  "社会言語的適切さ（オンライン簡略表現）：口語的な短評の型。",
  "英語オンラインの超短評（So true! / Not for me / This!）の語彙が乏しく、硬い I think this is good. で返しがち。日本語の「わかる」「それな」に当たる口語共感表現を、英語の型として別途持つ必要がある。",
  "（書面起点）口頭の意見表明が、オンラインでは超短評として立ち上がる。"),
 ("書面","B1",677,
  "Can post a comprehensible contribution in an online discussion on a familiar topic of interest, provided they can prepare the text beforehand and use online tools to fill gaps in language and check accuracy.",
  "事前に準備でき、言語の穴埋めや正確さの確認にオンラインツールを使えば、関心のある身近な話題のオンライン議論に理解可能な投稿ができる。",
  ["I think the article raises a good point about remote work, but it overlooks the cost side.",
   "In my experience, this approach works better for small teams."],
  "準備の上で、オンライン議論に理由を添えた意見を投稿する。",
  "叙述の正確さ（書面）：準備された、自己完結した意見投稿。",
  "書面の意見投稿では、口頭の往復に頼れず、立場＋理由を一つの投稿で自己完結させる必要がある。日本語話者は結論を最後に置き前置きを長くしがちだが、英語オンライン議論は要点先行（I think X, but Y）が読まれやすい。",
  "超短評から「理由を添えた議論への投稿」へ。準備を挟んだ自己完結した表明。"),
 ("書面","B1+",635,
  "Can compose personal letters giving news and expressing thoughts about abstract or cultural topics such as music or film.",
  "近況を伝え、音楽や映画などの抽象的・文化的話題についての考えを表現する個人的な手紙を書ける。",
  ["I finally watched that film you recommended. I loved the visuals, though the plot lost me a bit.",
   "Lately I've been getting into jazz — there's something about it that really calms me down."],
  "私信で、近況とともに文化的対象への考えを綴る。",
  "叙述の正確さ＋語彙範囲：私信レジスターでの抽象的感想。",
  "私信での考えの表明は、口語的親密さと一定の内容を両立させる。日本語の手紙の様式（時候の挨拶等）を英語に持ち込むと不自然で、英語私信は近況と感想を地続きに書く。この様式差は書面ならではの注意点。",
  "議論投稿から「私信での考えの表明」へ。親密なレジスターでの抽象的感想。書面系列の到達点。"),
]

DISCUSSION = """\
【表出型の核は「不同意を許容する作法」である】
苦情（指示型）の核が緩衝、挨拶（儀礼型）がレジスターとテンポ、事実Q&A（主張型）が疑問文構造だったのに対し、意見・見解の表明（表出型）の核は、立場の表明と、とりわけ対立を許容し丁寧に扱う作法にある。レベルが上がるとは、意見を「述べる」だけから、根拠で「支え」、他者の論と「関係づけ」、最終的に「評価・再構成・反論する」へと、社会的な議論の営みへ深化することである。効く how well 軸は、低位では文法（I think節・比較級）だが、B1以降は社会言語的適切さと叙述の正確さ（論拠の構造）へ移る。

【最大のL1難所は「受けてから返す」不同意の型】
日本語話者にとって表出型の中心的困難は、不同意の扱いにある。日本語文化では公然の不同意が回避されやすく、その結果、英語でも二つの失敗形に振れる ── 曖昧にして立場を消すか、But that's wrong. と裸で否定して角を立てるか。英語の作法は第三の道で、I see your point, but... / That's a fair point, but... と、まず相手を受けてから反対する二段構えである。この「受けてから返す」型は、B1で登場しC1まで一貫して深化する（C1では相手の論を restate してから challenge する）。表出型カタログの背骨は、この不同意の作法の段階的精緻化として引くべきである。

【意見は「維持」まで含めて一つの行為である】
主張型の事実Q&Aが単発の授受で完結するのに対し、意見表明はB2で「維持する（sustain）」が加わる点が質的に異なる。I stand by what I said, because... ── 反論されても根拠とともに立場を保つことが、英語では誠実さとされる。日本語話者は対立を避けて安易に撤回しがちだが、それは英語の議論では「立場が無い」と受け取られる。表明・支持・維持を一続きの行為として示すことが、この行為のカタログの要点である。

【抽象的対象には専用の構文がある】
B1+以降、評価対象が身近な物から抽象的・文化的対象（音楽・映画・思想）へ移ると、what I like about X is... の焦点化構文や、I can see why..., though... の譲歩構文が要る。日本語の「よかった／いまいち」の二元では抽象評価が幼く響く。この構文層は語彙ではなく「立場を立体的に述べる型」であり、表出型に固有の習得課題である。

【範型としての検証 ── 表出型の点検軸】
表出型に効く点検軸：(1) レベル軸は「表明→支持→維持→評価・反論」という議論の深化として長く立つ（苦情型に似て梯子が長い）。(2) L1注意の中心は不同意の作法（受けてから返す）。(3) how well の主軸は低位で文法、B1以降は社会言語的適切さ＋叙述の正確さへ移動する。(4) 意見の「維持」が行為の一部。(5) 抽象的対象用の焦点化・譲歩構文。この5点が、同じ表出型の他行為（感情の表出、好悪の表明、感謝・詫び・祝意など）を作る際の点検リストになる。ただし表出型内でも「感謝・詫び」は定型性が高く儀礼型に近い顔を持つ可能性があり、「感情の表出」は不同意の作法が効かない ── 表出型は内部の振れ幅が大きく、汎用性検証で下位分化を確かめる必要がある。"""
