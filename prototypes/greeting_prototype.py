# -*- coding: utf-8 -*-
# 第1カタログ 範型その2：発語内行為「挨拶・別れ・安否」（儀礼型 phatic）
ACT_TITLE = "挨拶・別れ・安否（Greeting, Leave-taking & Phatic exchange）"
ACT_TYPE  = "交話的（phatic）── 情報伝達より関係の確立・維持が目的"
ACT_ESSENCE = "出会いと別れの区切りに定型表現を交わし、相手との社会的接触を開き・保ち・閉じる。内容の正しさより、型の適切さとテンポが行為の成否を決める。"

# (mode, level, no, en, jp, exponents, scene, howwell, l1_note, delta)
ROWS = [
 ("口頭","Pre-A1",453,
  'Can understand and use basic, formulaic expressions such as “Yes”, “No”, “Excuse me”, “Please”, “Thank you”, “No thank you”, “Sorry”.',
  "「はい」「いいえ」「すみません」「お願いします」「ありがとう」「けっこうです」「ごめんなさい」などの基本的な決まり文句を理解し、使える。",
  ['Yes. / No.', 'Thank you. / No thank you.', 'Excuse me. / Sorry.', 'Please.'],
  "あらゆる接触の潤滑油となる最小の定型語を、適切な場面で口にする。",
  "社会言語的適切さ（最小単位）：型を型として口に出せるか。",
  "No thank you を「いいえ、結構です」の丁寧な断りとして使えず、単に No と言って冷たく響くことがある。また Sorry と Excuse me の使い分け（謝罪／呼びかけ・断り）が日本語の「すみません」に一括されるため混同しやすい。",
  "（起点）語彙ですらなく「機能語の塊」。関係の潤滑油の最小部品。"),
 ("口頭","Pre-A1",455,
  'Can greet people, state their name and take leave in a simple way.',
  "挨拶し、名前を名乗り、簡単な方法で別れを告げられる。",
  ['Hello. / Hi.', "I'm Kenji.", 'Goodbye. / Bye.', 'See you.'],
  "初対面や店・受付で、挨拶し名乗り、辞去する。会話の開閉の枠。",
  "社会言語的適切さ：出会いと別れの型をペアで押さえられるか。",
  "別れ際の See you. や Bye. を言わずに立ち去る、あるいは Goodbye だけで済ませて素っ気なくなる。日本語の「じゃあ」「どうも」に当たる軽い辞去表現の層が薄い。",
  "定型語から「会話の開閉」へ。挨拶と別れは対で機能する。"),
 ("口頭","A1",451,
  'Can make an introduction and use basic greeting and leave-taking expressions.',
  "紹介をし、基本的な挨拶や別れの表現を使える。",
  ['Good morning. / Good afternoon.', 'This is my friend, Aya.', 'Nice to meet you.', 'Have a nice day!'],
  "他者を紹介し、時間帯に応じた挨拶と、別れ際の一言を添える。",
  "社会言語的適切さ：時間帯・相手による型の選択。",
  "Nice to meet you.（初対面）と Nice to see you.（再会）の別を知らず、再会でも meet を使ってしまう。Have a nice day! のような別れ際の「気遣いの一言」を添える習慣が乏しく、挨拶が短く切れる。",
  "Pre-A1からの差分：時間帯別（morning/afternoon）と紹介（This is...）が加わり、型が場面分化する。"),
 ("口頭","A1",452,
  'Can ask how people are and react to news.',
  "人の調子を尋ね、知らせに反応できる。",
  ['How are you? — Fine, thanks. And you?', "How's it going?", "That's great! / Oh, I'm sorry to hear that."],
  "相手の近況・体調を尋ね、返ってきた知らせに感情で応じる。",
  "社会言語的適切さ＋テンポ：定型的な問い返し（And you?）の即応。",
  "How are you? を「本当に体調を訊く質問」と受け取り、長々と実際の状態を答えてしまう。英語では儀礼的な往復（Fine, thanks. And you?）が基本で、中身より往復のテンポが大事。この phatic な性質が日本語話者に最も伝わりにくい。",
  "一方向の挨拶から「往復」へ。相手の応答に反応する対話性が入る。"),
 ("口頭","A2",444,
  'Can use simple, everyday, polite forms of greeting and address.',
  "簡単な日常の丁寧な挨拶や呼びかけの表現形式を使える。",
  ['Good evening, Mr. Tanaka.', 'Excuse me, sir. / Excuse me, madam.', 'How do you do?（改まった初対面）'],
  "目上や公的な相手に、丁寧なレジスターで挨拶し呼びかける。",
  "社会言語的適切さ（レジスター）：親しさ／改まりで型を選び分けられるか。",
  "英語の呼びかけには sir/madam や Mr./Ms.＋姓があるが、日本語の「〜さん」を万能に使う感覚で first name を使い、目上に馴れ馴れしく響く。逆に過度に Mr. を連発して不自然になることも。相手との距離に応じた呼称選択は明示的な学習を要する。",
  "A1からの差分：中立な挨拶から「丁寧なレジスター」の選択へ。呼びかけ（address）が加わる。"),
 ("口頭","A2+",438,
  'Can establish social contact (e.g. greetings and farewells, introductions, giving thanks).',
  "社交的接触（挨拶と別れ、紹介、感謝など）を確立できる。",
  ["Hi, I don't think we've met — I'm Kenji.", "It was really nice talking to you.", "Thanks so much for having me. / Let's keep in touch."],
  "パーティや職場で、自ら関係を開き、会話を交わし、良い印象で閉じる一連。",
  "社会言語的適切さ＋柔軟さ：開始・維持・終了を状況に合わせて束ねる。",
  "関係を自分から「開く」定型（I don't think we've met）や、良い印象で「閉じる」定型（It was nice talking to you / keep in touch）の層が薄く、挨拶が入口だけで終わりがち。日本語では別れの挨拶が定型的に厚いのに、英語ではその機能表現を別途習得しないと使えない。",
  "個別の挨拶から「社交的接触の確立」へ。開始〜維持〜終了を一続きの営みとして統合する到達点。"),
 # ── 書面・オンライン系列 ──
 ("書面","Pre-A1",686,
  'Can post simple online greetings, using basic formulaic expressions and emoticons.',
  "基本的な決まり文句と絵文字を使って、簡単なオンラインの挨拶を投稿できる。",
  ['Happy birthday! 🎉', 'Good luck! 😊', 'Congrats!'],
  "SNSやチャットで、定型句＋絵文字の短い挨拶を投稿する。",
  "社会言語的適切さ（オンライン・レジスター）：くだけた場の型と絵文字の運用。",
  "日本語のオンライン儀礼（「おめでとう🎊」）の感覚は近いが、英語の Congrats! / Happy belated birthday!（遅れた誕生日祝い）のような口語省略形を知らず、硬い Congratulations に留まる。絵文字の使用も控えめすぎることがある。",
  "（書面起点）口頭の定型語が、オンラインでは絵文字と結んで機能する。"),
 ("書面","A1",648,
  'Can compose a short, simple postcard.',
  "短く簡単なはがきを書ける。",
  ['Dear Aya, Greetings from Kyoto! The temples are beautiful. See you soon, Kenji',
   'Hi Mom, Having a great time here. Weather is lovely. Love, Kenji'],
  "旅先などから、近況の一言を添えた短いはがきを書く。",
  "社会言語的適切さ（書面枠）：Dear... と結び（Love/See you soon）の枠を守れるか。",
  "はがき・手紙の結びの語（Love, / Best, / See you soon,）の層が薄く、日本語の「それでは」を直訳して不自然になる。宛名の Dear は日本語の「親愛なる」より軽く日常的、という温度感も掴みにくい。",
  "オンライン挨拶からの差分：書面の「枠」（宛名・本文・結び）が加わる。"),
 ("書面","A2",682,
  'Can engage in basic social communication online (e.g. a simple message on a virtual card for special occasions, sharing news and making/confirming arrangements to meet).',
  "オンラインで基本的な社交（特別な機会のカードへの一言、近況共有、会う約束の設定・確認など）ができる。",
  ['Congratulations on your new job! So happy for you.',
   'Long time no see! How have you been?',
   "Shall we meet around 7? — Sounds good, see you then!"],
  "オンラインで、祝い・近況・約束の確認まで含む社交的なやりとりをする。",
  "社会言語的適切さ＋テンポ：非同期のやりとりで型と応答を回す。",
  "Long time no see! のような口語定型や、約束確認の Sounds good, see you then! のテンポある応答が出てこず、事務的な確認に終始しがち。日本語のオンライン社交の「クッション」を英語の口語定型に置き換える必要がある。",
  "はがきの一方向から、オンラインの「往復する社交」へ。約束の設定・確認まで機能が広がる書面系列の到達点。"),
]

DISCUSSION = """\
【この行為に「上級」は無い ── 儀礼型の本質】
苦情がA2からC1まで長い梯子を持つのに対し、挨拶・別れ・安否はPre-A1からA2+に完全に収まり、B1以上に記述文が一つも無い。これは欠落ではなく、交話的（phatic）行為の本質である。挨拶に高度な熟達は存在しない ── C2話者も "Hi, how are you?" と言う。CEFRがこの行為を初級だけで記述し尽くしているのは、関係の潤滑という機能が、初級の定型表現でほぼ充足されるからである。したがってこの行為のカタログは「レベルを上る」構造ではなく、「初級の型を、いかに場に合わせて選ぶか」という水平の広がりを持つ。

【難しさは「レベル」ではなく「レジスターとテンポ」にある】
では日本語話者にとって易しいかというと逆で、難所がレベル軸と直交する二つの次元に潜む。第一はレジスター（親しさ・改まりの選択）。sir/madam、Mr.＋姓、first name、ニックネームの使い分けは、日本語の「〜さん」一括感覚では捌けず、相手との距離を英語の呼称体系で測り直す必要がある。第二はテンポ。How are you? — Fine, thanks. And you? の往復は、中身ではなく「間髪入れず型を返す」ことに意味がある。この二つは文法でも語彙でもなく、how well の軸でいえば社会言語的適切さに全面的に属する。

【How are you? は質問ではない ── phatic の核心的誤解】
日本語話者が最もつまずくのは、儀礼的な問いを情報要求と受け取ることである。How are you? に実際の体調を長々答える、How's it going? に詰まる ── これは英語力ではなく、phatic communion（意味の交換ではなく接触の確認そのものが目的の発話）という概念が母語で意識されないために起こる。この行為を教えるとき、「中身より往復」「型は型として回す」という phatic の性質そのものを明示的に伝えることが、どの実例よりも効く。

【開始は言えるが、維持と終了が言えない】
日本語話者の挨拶は入口（Hello, Nice to meet you）に偏り、関係を「閉じる」定型（It was nice talking to you / Let's keep in touch / Have a nice day）の層が決定的に薄い。日本語では別れの挨拶がむしろ厚い（「それでは失礼します」「お世話になりました」）のに英語で出てこないのは、機能が同じでも表現が一対一で写らず、英語側の閉じる定型を別個の語彙として持っていないためである。カタログでは開始・維持・終了を必ず三点セットで示し、とりわけ終了の定型を厚くする。

【範型としての検証 ── 苦情型との対比で見えたこと】
苦情（指示型）では「緩衝の精緻化」がレベル軸を貫いたが、挨拶（儀礼型）ではレベル軸がほぼ消え、代わりに「レジスター選択」「テンポ」「phaticの理解」という水平の難しさが前面に出た。これは範型が行為の類型ごとに異なる顔を持つことを示す。指示型の点検軸（緩衝・二重の壁・隣接行為・口頭書面）はそのままでは効かず、儀礼型には「レベルの梯子が短い／無い」「難所がレジスターとテンポに移る」「phatic性の明示的説明が要る」という別の点検軸が要る。25行為を作り込む際は、まず各行為が指示型・儀礼型・主張型・表出型のどれに属するかを見極め、類型ごとの点検軸を当てるのが正しい ── 単一のテンプレートを全行為に機械適用してはならない。"""
