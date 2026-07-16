# -*- coding: utf-8 -*-
# 第1カタログ 範型その3：主張型「事実情報の質問と応答」（assertive）
ACT_TITLE = "事実情報の質問と応答（Asking & answering factual questions）"
ACT_TYPE  = "主張的（assertive）── 世界の事実を尋ね、真偽の判断を伴って答える"
ACT_ESSENCE = "名前・時刻・場所・予定などの事実情報を、質問と応答のペアで往復させる。行為の核は情報の正確な授受であり、緩衝もレジスターも二次的。疑問文の構造そのものが遂行の要となる。"

# (mode, level, no, en, jp, exponents, scene, howwell, l1_note, delta)
ROWS = [
 ("口頭","Pre-A1",579,
  "Can tell people their name and ask other people their names.",
  "自分の名前を名乗り、他の人に名前を尋ねられる。",
  ["What's your name? — My name is Kenji. / I'm Kenji.",
   "And you? What's your name?"],
  "初対面で名前を尋ね合う、最も基本的な情報交換。",
  "文法的正確さ（疑問文の骨格）：What's your name? の語順を作れるか。",
  "日本語は「お名前は？」と述語を略しても成立するが、英語は What is your name? と疑問詞＋be動詞＋主語の語順が必須。主語を落として Name? だけだと幼稚か無礼に響く。疑問文の骨格そのものが最初の壁。",
  "（起点）疑問文の最小形。事実の授受の最小単位。"),
 ("口頭","Pre-A1",585,
  'Can ask very simple questions for information, such as “What is this?” and understand one- or two-word/sign answers.',
  "「これは何?」等の簡単な情報の質問をし、1〜2語の答えを理解できる。",
  ["What is this? — It's a key.",
   "What's that in English?"],
  "物を指して名称を尋ね、短い答えを受け取る。",
  "文法的正確さ＋受容：What疑問文と一語応答の理解。",
  "答えの It's a key. の It's を省いて A key と答えるのは英語でも自然だが、日本語話者は逆に「これはキーです」に引きずられ This is key.（冠詞落ち）としがち。冠詞は日本語に無い範疇なので、事実応答のたびに落ちる。",
  "名前から一般の事物へ。What+be動詞の疑問を汎用化。"),
 ("口頭","Pre-A1",581,
  "Can ask and tell what day, time of day and date it is.",
  "何曜日か、一日のうちのいつか、何日かを尋ね、言える。",
  ["What day is it today? — It's Monday.",
   "What time is it? — It's half past three.",
   "What's the date today? — It's the 5th of July."],
  "曜日・時刻・日付という定型的事実を尋ね合う。",
  "文法的正確さ（非人称の it）：時刻・日付の it is 構文。",
  "時刻・曜日の主語 it（It's Monday）は日本語に対応物が無く、主語を落として Monday. とだけ答えがち。また half past three（3時半）like の英語独特の時刻表現は、日本語の「3時半」から直訳できず、型として覚える必要がある。",
  "事物から「定型的事実（時・日付）」へ。非人称itの構文が加わる。"),
 ("口頭","A1",575,
  "Can ask and answer questions about themselves and other people, where they live, people they know, things they have.",
  "自分や他の人、住んでいる場所、知っている人、持っているものについて質問し、答えられる。",
  ["Where do you live? — I live in Osaka.",
   "Do you have any brothers or sisters? — Yes, I have one sister.",
   "Who's that? — That's my friend Aya."],
  "居住地・家族・所有物など、身辺の事実を双方向に尋ね合う。",
  "文法的正確さ（一般動詞の疑問）：do/does を使った疑問文の構築。",
  "Where do you live? の do は日本語に対応が無く、Where you live? と do を落とす誤りが頻発。日本語の疑問は語尾（〜か）だけで作れるため、英語の「助動詞doを前に立てる」操作が身につきにくい。主張型の中核的な文法的つまずき。",
  "Pre-A1からの飛躍：be動詞疑問から一般動詞疑問（do支持）へ。扱う事実も身辺全般に拡大。"),
 ("口頭","A2",572,
  "Can ask and answer simple questions about an event (e.g. ask where and when it took place, who was there and what it was like).",
  "出来事について簡単な質問をし答えられる（どこで・いつ・誰が・どうだったか）。",
  ["Where was the party? — It was at Kenji's place.",
   "How was it? — It was really fun.",
   "Who was there? — Aya and some people from work."],
  "済んだ出来事について、場所・時・参加者・様子を尋ね合う。",
  "文法的正確さ（過去時制）：was/were と過去疑問の運用。",
  "過去の出来事なので was/were や did が要るが、日本語話者は時制標示を落として Where the party? / How it was?（語順崩れ）としやすい。日本語の過去「〜だった」は英語の時制ほど厳密な一致を求めないため、疑問文中の時制保持が弱い。",
  "現在の事実から「過去の出来事」へ。過去時制の疑問・応答が加わる。"),
 ("口頭","A2",570,
  "Can ask for and give directions referring to a map or plan.",
  "地図や見取り図を参照しながら道順を尋ね、教えられる。",
  ["How do I get to the station? — Go straight and turn left at the bank.",
   "Is it far? — No, about five minutes on foot.",
   "Where are we now? — We're here, near the museum."],
  "地図を見ながら、目的地への行き方を尋ね教え合う。",
  "叙述の正確さ＋文法（命令文の道案内）：方向表現の連鎖。",
  "道案内の応答は命令文（Go straight, Turn left）を使うが、日本語話者は命令形が強く聞こえると感じて避け、遠回しにしがち。英語では道案内の命令文は失礼でなく標準。また前置詞（at the bank, on your right）の選択が日本語の助詞感覚とずれる。",
  "口頭事実交換の応用：静的事実から「空間的手順の授受」へ。命令文応答が加わる。"),
 ("口頭","A2+",563,
  "Can ask and answer questions about habits and routines.",
  "習慣や日課について質問し、答えられる。",
  ["What time do you usually get up? — Around seven.",
   "How often do you exercise? — Twice a week.",
   "Do you always take the train? — Usually, yes."],
  "日常の習慣・頻度について尋ね合う。",
  "文法的正確さ（頻度・習慣の現在形）：頻度副詞と現在形の運用。",
  "頻度副詞（usually, often, twice a week）の位置が日本語と異なり、I usually get up... の語中位置を外して文末や文頭に置きがち。また習慣を表す現在形と進行形の別（I take the train / I'm taking）が、日本語の「〜している」一括感覚で混同される。",
  "単発の出来事から「反復する習慣」へ。頻度表現と習慣の現在形が加わる。"),
 ("口頭","A2+",565,
  "Can ask and answer questions about plans and intentions.",
  "計画や意図について質問し、答えられる。",
  ["What are you doing this weekend? — I'm meeting some friends.",
   "Are you going to travel this summer? — Yes, I'm planning to.",
   "What time will you arrive? — Probably around six."],
  "予定・意図について尋ね合う。",
  "文法的正確さ（未来表現の選択）：will / be going to / 現在進行形の使い分け。",
  "英語の未来表現は三系統（will＝その場の決定・予測、be going to＝既定の意図、現在進行形＝手配済みの予定）あるが、日本語の「〜する／〜するつもり」の二分では捌けず、どれを使うか判断できない。この使い分けは主張型・未来事実の最大の難所。",
  "過去・現在の事実から「未来の予定・意図」へ。未来表現の体系が加わる。主張型口頭系列の到達点。"),
 # 書面系列（Information exchangeは口頭中心。書面はCorrespondence由来の情報交換的記述文を当てる）
 ("書面","A1",643,
  "Can convey personal information of a routine nature, for example in a short e-mail or letter introducing themselves.",
  "日常的な個人情報を伝えられる（自己紹介する短いメールなど）。",
  ["Hi, I'm Kenji. I'm from Osaka and I work at a software company.",
   "I have two cats and I like hiking. What about you?"],
  "自己紹介のメールで、身辺の事実情報を文章で伝える。",
  "文法的正確さ（平叙文の事実記述）：I am / I have / I work の平叙連鎖。",
  "口頭では往復で成立するが、書面では自己完結した平叙文を連ねる必要がある。日本語話者は主語 I の反復を冗長に感じて落としがちだが、英語では各文に主語が要る。話し言葉の省略を書면に持ち込むと非文になる。",
  "（書面起点）口頭の質問応答が、書面では一方向の事実記述として立ち上がる。"),
 ("書面","A2",642,
  "Can exchange information by texting, e-mail or short letter, responding to questions from the other person (e.g. about a new product or activity).",
  "テキスト・メール・短い手紙で情報を交換できる（相手の質問に答えながら）。",
  ["Q: When does the event start? — A: It starts at 2 pm on Saturday.",
   "Q: Where is it? — A: At the community hall, near the station."],
  "メールやテキストで、相手の質問に答えつつ事実情報をやりとりする。",
  "文法的正確さ＋叙述の正確さ：問いに対応した事実の返信。",
  "書面の非同期往復では、相手の質問の時制・焦点に合わせて答える必要があるが、日本語話者は質問を受け止めず自分の言いたい情報を返しがち（質問と応答のかみ合わせのずれ）。英語のQ&Aは問いの構造に応答を対応させる明示性が要る。",
  "自己紹介の一方向から、書面の「往復する情報交換」へ。書面系列の到達点。"),
]

DISCUSSION = """\
【主張型の核は疑問文の構造そのものである】
苦情（指示型）の核が緩衝、挨拶（儀礼型）の核がレジスターとテンポだったのに対し、事実情報の質問と応答（主張型）の核は、疑問文と応答の文法構造そのものにある。この行為で一貫して効く how well 軸は社会言語的適切さではなく文法的正確さである。What's your name? / Where do you live? / What are you doing this weekend? ── レベルが上がるとは、扱える疑問の時制と法が広がること（be動詞疑問→do支持疑問→過去疑問→未来表現の三系統）にほかならない。緩衝もレジスターも、この行為ではほぼ問われない。

【日本語話者のつまずきは「疑問文の作り方」に集中する】
指示型・儀礼型のL1問題が語用論（言い出せない、phaticの誤解）だったのに対し、主張型のL1問題は純粋に文法・統語に寄る。第一に do 支持 ── 日本語は語尾「〜か」だけで疑問を作れるため、Where do you live? の do を立てる操作が身につかず Where you live? が頻発する。第二に時制の保持 ── 疑問文中で was/did を落とす。第三に冠詞と主語 ── This is key. / 主語Iの脱落。これらは語用論的配慮ではなく、日本語に存在しない文法範疇（助動詞do、厳密な時制一致、冠詞）が事実の授受のたびに露出する現象である。したがってこの行為のL1注意は「文化」ではなく「構造」を突くものになる。

【未来表現の三系統が唯一の高度な難所】
主張型はおおむね平明だが、一点だけ質的な難所がある ── 未来の予定・意図（A2+）を表す will / be going to / 現在進行形の使い分けである。日本語の「〜する／〜するつもり」の二分では英語の三系統に対応できない。ここだけは文法項目の暗記では足りず、話者の心的態度（その場の決定か、既定の意図か、手配済みか）と結びつけて教える必要がある。カタログではこの一点を厚く扱う。

【口頭は往復、書面は自己完結】
情報交換はCEFRでは圧倒的に口頭（Information exchange スケール）に記述が集中し、書面はCorrespondence由来の情報記述が少数あるのみ。この非対称は本質的で、事実の授受は本来リアルタイムの往復（Q — A）に最も自然に宿る。書面に移ると、口頭の省略（主語や述語の脱落）が使えず、自己完結した平叙文を連ねる必要が生じる ── 話し言葉の省略を書面に持ち込むと非文になる、という書面固有の壁が現れる。

【範型としての検証 ── 主張型の点検軸】
主張型に効く点検軸は、指示型・儀礼型と異なる。(1) レベル軸は「疑問の時制・法の拡大」として明快に立つ（初級で出尽くすが、内部に文法的段階がある）。(2) L1注意は語用論ではなく統語（do支持・時制・冠詞・主語）を突く。(3) how well の主軸は文法的正確さ。(4) 唯一の高度な難所は未来表現の三系統。(5) 口頭往復と書面自己完結の差。この5点が、同じ主張型の他行為（自己に関する情報提供、経験・出来事の叙述、問題・事情の説明など）を作る際の点検リストになる。ただし主張型内でも「経験・出来事の叙述」は疑問応答ではなく一方向の語りなので、疑問文構造の軸が効かない可能性がある ── これは汎用性検証で確かめるべき論点である。"""
