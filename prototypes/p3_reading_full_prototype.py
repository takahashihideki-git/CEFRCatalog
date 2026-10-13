#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第3柱（受容）第二号範型：Reading for information and argument 26件の全数シート（書物の章名「知るために読む」）。

CEFRカタログ34（判断(bt)）。『受容の課題』（判断(br)）と第一号の掛け直し（判断(bs)）に従う。
- シート＝スケール（mode一様＝「読む」）
- 列10は不変。第3柱での読み替え（第一号と同じ）：
    exponents … 一要素＝二行以上。読むもののラベル（Menu / Flyer / News / Text / Letter / Article / Board / Essay / Post …）に続けて読む言葉、
                 最後に You: （分かったしるし＝自分のための理解の丸括弧の行動描写）。例文は l1 の欄を演じるように作る（欄→例文の順）
    scene     … 「読むもの」＝テキストの種類と、その作り（記述文の条件句＝入力の側の手加減を含む）
    howwell   … 「分かること」＝求められる層（七層）と、その段でその層を求めることの意味
    l1        … 「日本語話者の落とし穴」。判定は執筆要綱・規律6-1受容版の五条件（源の領域が指せる／層に見合い条件を打ち消さない／例文を消しても成り立つ／
                 本書の前提なしで読める／**『受容の課題』§5に書かれた要因に拠る**）。§5にない要因が立つと見たときは、欄にせず §5 への追記を先に出す（判断(bt)）。
                 本シートで §5 に追記して欄にしたもの＝§5.2「訳読の転移の第二の形」（161・163・170）、§5.1(c)「住所の書き方」（166）
    delta     … 前の段から。聞く側（聴衆として聞く）との対は層と課題の一致で読み、散文証拠として置く（台帳収載は対の台帳の四柱化で）
- 四欄は書物の本文として書く（読者語彙、帳簿語を出さない、章名は「 」）。範型章は無改変で転写する
- 梯子＝条件の解除の一本（CONDITION、完全分割、語彙はスケールごと）。深さ＝七層（DEPTH、完全分割、語彙は固定）。糸は立てない
- 語彙裁定（判断(s)）：例文は読む言葉と、しるしのうち英語で書いた部分を照合対象とする。日本語で書いたしるしは照合外。
  allowlist 候補は tools/exponent_level_check.py の結果で裁定し、申し送りに記録する
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Reading for information and argument"
ACT = "知るために読む（第3柱：Reading for information and argument）"
MODE = "読む"

SEVEN_LAYERS = ["形", "命題", "筋", "要点", "全体", "含意", "立場"]

# レベル順→No昇順（表示順の正準）
ORDER = [172, 170, 171, 165, 166, 167, 168, 169, 161, 162, 163, 164, 158, 159, 160,
         154, 155, 156, 157, 151, 152, 153, 149, 150, 148, 147]

# 条件（入力の側の手加減。行ごとに一つ、完全分割）
CONDITION = {
    "支え":            [172, 170, 171],                               # 写真・絵・ごく簡単な言葉
    "簡単な言葉と身近": [165, 166, 167, 168, 169, 161, 162, 163, 164],  # 簡単な言葉・身近な主題・予測できる種類・紙面の作り
    "身近と率直":      [158, 159, 160, 154, 155, 156, 157],           # 身近な主題・率直・読み返し・標識
    "条件なし":        [151, 152, 153],
    "分野か辞書":      [149, 150],                                    # 自分の分野／時々辞書
    "逆境":            [148, 147],                                    # 長く複雑／専門外
}
# 深さ＝七層（『受容の課題』§6.1・付録A）
DEPTH = {
    "形":   [],
    "命題": [172, 166, 161, 149],
    "筋":   [170, 162],
    "要点": [167, 163, 164, 158, 160, 156, 157, 153],
    "全体": [171, 165, 168, 169, 159, 154, 150],
    "含意": [148, 147],
    "立場": [155, 151, 152],
}

R = {  # no -> (exponents, scene=読むもの, howwell=分かること, l1=落とし穴, delta=前の段から)
172: (
 ["Menu: [photo] Cheeseburger $4.50 ／ [photo] Chicken Burger $5.00 ／ [photo] Salad $2.20 ／ Orange Juice $1.80\nYou: （写真でチキンバーガーを選び、値段は五ドルだと読み取って、レジで代金を用意する。）"],
 "写真つきのファストフード店のメニューや、ごく簡単な日常語で書かれた絵物語。品物や場面は写真と絵が与え、言葉は品名・値段・一言の文に限られる。",
 "命題 ── 一つの項目が何を言っているか。この品がいくらか、この絵の人が何をしているか。項目どうしをつなぐことは求められない。",
 "",
 "読む側の梯子の起点。写真と絵が場面を与え、言葉はそこに添えられた一項目ずつの札である。聞く側の起点（「聴衆として聞く」の章のNo.49）が間と速さの手加減で支えられるのに対し、読む側は視覚が言葉の代わりをする。",
),
170: (
 ["Flyer: [picture: a band on a stage, food and games] Summer Festival ── Saturday, 2 July, 4 p.m. – 9 p.m. ／ Music, food and games ／ Free for children ／ City Park, near the station\nYou: （何の催しで、いつ、どこで、子どもは無料、とおおよその中身をつかみ、行くかどうかを決める。）"],
 "簡単な案内資料（ちらし・掲示）や、短く簡単な説明。写真や図が添えられていることが多い。",
 "筋 ── 全部は読めなくても、何についての資料で、何が書かれているかのおおよそ。項目の並びから中身の見当をつける。",
 "英文は頭から終わりまで全部訳すものだという読み方のため、絵と分かる語から全体の見当をつける読み方に切り替えられず、分からない語が一つあると資料全体が分からないものとして扱ってしまう。",
 "項目を一つずつ読む（No.172）から、資料全体の見当をつける段へ。言葉はまだ簡単で視覚の支えもあるが、求められるのは一項目の意味ではなく、資料が何かという像になる。",
),
171: (
 ["News: [photo: a singer on stage] Big concert in Tokyo! ── Pop star Mia Lee sang in Tokyo on Sunday. Many fans came. She sang twelve songs. She sings in Osaka in May.\nYou: （誰が、どこで、何曲、次はどこでいつ、と短い記事の中身を全部受け取り、大阪の日程を調べる。）"],
 "自分の関心のある主題 ── スポーツ・音楽・旅行の速報や物語 ── の短いテキスト。ごく簡単な言葉で書かれ、挿絵や写真が添えられている。",
 "全体 ── 短いテキストに書かれたことの大半を、一つの像として持つ。関心のある主題なので、知っていることが言葉を支える。",
 "ごく簡単な言葉で書かれていても、知っている語をカタカナの音形で覚えているため、綴りを見ても同じ語だと気づかず、読めるはずの短いテキストを辞書を引きながら読む。",
 "見当をつける（No.170）から、短いテキストの全体を取る段へ。言葉と視覚の支えは同じまま、関心のある主題という内容の支えが加わって、全部読める。",
),
165: (
 ["Text: In Spain, people eat lunch late, at two or three o’clock. Dinner is at nine or ten at night. Shops close in the afternoon and open again at five.\nYou: （昼食は二時か三時、夕食は九時か十時、店は午後に閉まる、と書かれた暮らしの違いをそのまま受け取る。）"],
 "人・場所・日常生活・文化を描いたテキスト。言葉は簡単で、挿絵の支えはもうない。",
 "全体 ── 描かれた人や暮らしの様子を、書かれたとおりに一つの像として持つ。",
 "日常生活の記述を、日本の生活の像（学校は四月に始まる、夕食は七時）で補って読んでしまい、書かれている違いを違いとして受け取れず、読み終えた像が自分の暮らしに寄る。",
 "A2で初めて、視覚の支えなしに文章だけで全体を取る段が立つ。簡単な言葉だけで、記述の全体を取る。No.171の「関心のある主題」が、ここでは「人・場所・暮らし」という身近な主題に広がる。",
),
166: (
 ["Brochure: [map] 1 Old Castle ── 10 Castle Street, open 9–17 ／ 2 City Museum ── 25 King’s Road, closed Monday ／ 3 Fish Market ── Saturday morning\nYou: （城は九時から五時まで、博物館は月曜休み、市場は土曜の朝、と地図の番号と項目を結びつけて予定を組む。）"],
 "絵入りの観光パンフレットや地図。見どころごとに、名前・場所・開いている時間が項目で並ぶ。",
 "命題 ── 項目ごとの情報。どこに何があり、いつ開いているか。地図の印と項目を結びつける。",
 "所在地を「大きい区分から小さい区分へ」の順で待つため、番地・通り・地区の順で書かれた住所を読み違え、地図の上で見どころの位置を取り違える。",
 "層は命題に戻る（No.172と同じ）。視覚は写真でなく地図と絵になり、項目は品名と値段から名前・場所・時間へ増える。",
),
167: (
 ["News: Star player leaves City ── City’s best player, Dan Oko, will play for United next year. He said goodbye to fans on Sunday. City paid him a lot of money, but United paid more.\nYou: （移籍した、相手はユナイテッド、理由はお金、と要点を取る。）"],
 "スポーツや有名人など、自分の関心のある主題の短いニュース。見出しと短い本文からなる。",
 "要点 ── 誰が、何を、どうした。細部（日付・金額の正確さ）ではなく、ニュースの核。",
 "",
 "層が全体（No.165）から要点へ。読むものはニュースになり、見出しと本文の二層から核を拾う。",
),
168: (
 ["Report: Sales in March ── We sold 120 bikes in March. That is 20 more than in February. Most people bought the city bike. The new shop in Leeds opened on 15 March.\nYou: （三月は百二十台、二月より二十台多い、売れ筋はシティバイク、新店は十五日開店、と報告の全部を受け取る。）"],
 "自分の分野（仕事や学習）の短い事実的な記述や報告。簡単な言葉で書かれ、予測できない細部は出てこない。",
 "全体 ── 報告に書かれた事実の大半を一つの像として持つ。分野の知識が、言葉の簡単さと並んで支えになる。",
 "",
 "全体を取る段が、暮らしの記述（No.165）から仕事の報告へ移る。「予測できない細部を含まない」が条件に加わり、分野の知識が支えになる。",
),
169: (
 ["Post: Hi, I’m Ken, 24, from Osaka. I love hiking and old films. I’m looking for friends who like the mountains. Please don’t message me about football ── I don’t watch it.\nYou: （山好きの友だちを探している、サッカーの話は要らない、と書かれたとおりに受け取り、返事をするか決める。）"],
 "個人広告や掲示板・SNSの投稿。書き手が自分のこと（年齢・住まい・好きなもの）と、相手に求めることを述べる。",
 "全体 ── 書き手が自分についてどう言い、相手に何を求めているか。その大半を像にする。",
 "",
 "全体を取る段の三つめ（No.165・168・169）。読むものが人の自己紹介になり、書き手の好みと求めが中身になる。A2の「全体」は、暮らし・仕事・人の三つの場面で揃う。",
),
161: (
 ["Letter: Dear Ms Tanaka, Thank you for your order. Your books will arrive on Thursday 12 May. If you are not at home, the driver will leave them with a neighbour. Best wishes, Green Books\nYou: （いつ届くか、だけを知りたくて手紙を見、十二日の木曜、不在なら隣人に預ける、の二点を拾う。）"],
 "手紙・パンフレット・出来事を報じる短いニュース記事など、簡単な資料。全部を読む必要はなく、自分が要る情報がどこかにある。",
 "命題 ── 要る情報の一項目。日付、場所、条件。資料のなかから、その項目だけを見つけて読み取る。",
 "文章は頭から順に読むものだという読み方のため、要る情報が一項目だけのときも最初の文から全部を日本語に置き換えて読み進め、探している項目だけを見つけて取り出す読み方ができない。",
 "層は命題（No.166）に戻るが、視覚の支えはなく、資料は地図からまとまった文章（手紙・記事）に変わる。文章のなかから一項目を取り出す、という読み方がここで初めて要る。",
),
162: (
 ["News: Heavy snow closed roads in the north of the country on Monday. Trains stopped for six hours. Schools were closed on Tuesday. The weather office says the snow will end on Wednesday.\nYou: （大雪で道路と列車が止まり、学校が休みになり、水曜には終わる、と出来事の流れを追う。）"],
 "身近な種類の出来事（大雪・事故・祭り）についてのニュース報道。内容は身近で、何が書かれるかおよそ予測できる。",
 "筋 ── 何が起きて、どうなったか。出来事の流れを追う。予測できる種類の出来事なので、次に何が書かれるかの見当が読みを支える。",
 "出来事の種類が分かっていても、一文ごとに日本語の語順に組み替えて読む読み方のため、一文を読み終えるごとに前の文が薄れ、短い報道でも終わりまで読んだときに流れが一つにつながらない。",
 "一項目を取る（No.161）から、出来事の流れを追う段へ。「身近な種類の出来事」が条件で、型の知識が支えになる。",
),
163: (
 ["News: **Bridge to close for six months** ── [photo: the bridge] The Old Bridge will close from 1 June for repairs. The work will cost £2 million. The city said the bridge is “safe but tired”. Buses will use the New Bridge.\nYou: （六か月の閉鎖、六月一日から、二百万ポンド、バスは新橋へ、と見出しと数字から要点を拾う。）"],
 "短いニュースや簡単な記事。見出し・数字・名前・図が目立つ作りで、それらが本文の意味を支える。",
 "要点 ── 主要な情報。見出しが何の話かを言い、数字と名前が核を与える。本文は全部読まなくてよい。",
 "見出しや数字を本文の添え物として扱い、頭から全部訳す読み方で本文の文章へ入るため、見出しと数字だけで取れたはずの要点に、本文を読み終えてから戻る。",
 "筋（No.162）から要点へ。テキストの作り（見出し・数字・図）が支えになる最初の段で、言葉の簡単さでなく紙面の形が条件になる。",
),
164: (
 ["Text: More and more people in the city are cycling to work. The city has built new bike lanes, and bikes are cheaper than trains. But some drivers say the lanes make the roads too small for cars.\nYou: （自転車通勤が増えている、理由は専用レーンと安さ、反対の声もある、と要点を取る。）"],
 "生活様式・趣味・スポーツ・天気など、日常の話題を扱う短いテキスト。見出しや数字の支えは条件に入っていない。",
 "要点 ── 何が言われているかの核。短いテキストのなかで、主な点と添えられた点を分ける。",
 "結論を最後に置く文章の型で待つため、第一文に置かれた言いたいことを導入として読み流し、理由や例の文のなかに要点を探す。",
 "No.163と同級で、紙面の支え（見出し・数字）が外れ、話題の身近さだけが条件になる。要点を文章そのものから取る最初の段。",
),
158: (
 ["Article: The city council voted on Tuesday to raise bus fares by 10 per cent from April. The council says the money will pay for new buses. Passenger groups called the rise “unfair”, and 5,000 people have already signed a letter against it.\nYou: （値上げが決まった、四月から一割、新車両のため、反対の手紙に五千人が署名した、と重要な点を拾う。）"],
 "身近な主題（交通・学校・町の出来事）の率直な新聞記事。短いテキストではなく記事の長さで、言葉は簡単とは限らない。",
 "要点 ── 記事のなかの重要な点。決まったこと、理由、反応。細部の数字や引用は添え物として扱える。",
 "結論を最後に置く文章の型で待つため、新聞記事が第一文に詰め込んだ核（誰が・何を・いつ・どうしたか）を読み流して次へ進み、重要な点をあとの段落から拾い直す。",
 "要点を取る段が、短いテキスト（No.164）から新聞記事へ。長さが増え、言葉の簡単さの条件が落ちる。「身近な主題」と「率直な」が残る条件。",
),
159: (
 ["Text: How to apply for a library card ── You can apply online or at any branch. Bring one proof of address, such as a bill or a bank letter. Cards are free if you live in the city; people from outside pay £15 a year. Children under 12 need a parent’s signature.\nYou: （オンラインか窓口、住所の証明が一つ、市内に住む人は無料で市外の人は年十五ポンド、十二歳未満は親の署名、と読み返しながら全部を取る。）"],
 "関心のある身近な主題（手続き・施設・趣味）について、暮らしのなかで出会う事実情報。読み返す時間が十分にある。",
 "全体 ── 書かれた事実情報の大半。要点ではなく、条件や例外を含めた全部を、読み返しながら組み立てる。",
 "",
 "要点（No.158）から全体へ。「読み返す時間が十分あれば」という、読む側だけが持つ手加減が初めて条件に書かれる。聞く側にこの支えはない。",
),
160: (
 ["Board: Roman Glass Bowl, about AD 100 ── Found in 1932 near the river. Bowls like this were made in Italy and sold across the Empire. The blue colour comes from a metal in the glass. Only three complete bowls of this type are known.\nYou: （二千年前のローマの器、イタリア製、青は金属の色、完全な形は三つだけ、と説明板の要点を取る。）"],
 "博物館の展示解説や展覧会の説明板。目の前の品物についての、短い記述メモ。",
 "要点 ── この品物が何で、なぜここにあるか。展示の解説は目の前の品物についての短い記述で、全部を読まずに核が取れる。",
 "",
 "No.158と同級で、読むものが新聞記事から展示の説明板へ。実物が目の前にあるという支えが、記事の「身近な主題」の代わりをする。",
),
154: (
 ["Text: Honey bees live in groups of up to 60,000. Each group has one queen, a few hundred males, and thousands of female workers. Workers live for about six weeks in summer, but the queen can live for several years. In winter the group gets smaller, and the bees keep the queen warm by forming a tight ball around her.\nYou: （群れの大きさ、三種の蜂、寿命の差、冬の過ごし方、と書かれていることの大半を一つの像にする。）"],
 "自分の関心や学習に関わる主題の、率直な事実的テキスト。短いという条件はなく、言葉の簡単さも条件に入っていない。",
 "全体 ── 書かれた事実の大半を一つの像として持つ。主題への関心と知識が、言葉の支えの代わりになる。",
 "",
 "全体を取る段（No.159）から、読み返しの条件が外れる。残る支えは主題への関心だけで、テキストの長さと言葉の難しさの但し書きがなくなる。",
),
155: (
 ["Letter to the editor: I was disappointed to read that the council plans to close the Park Road library. Libraries are not just about books. For many older people in this area, it is the one place they go every week. If the council needs to save money, it should look elsewhere first.\nYou: （図書館の閉鎖に反対している、理由は高齢者の居場所、代案は他で節約、と書き手の立場と筋を取る。）"],
 "身近または時事的な主題について、人々が見解を述べる短いテキスト。オンラインフォーラムへの批評的な投稿や、新聞の読者投書。",
 "立場 ── 書き手が何に賛成し、何に反対し、なぜそう考えるか。事実の記述ではなく、一人の見解として読む。",
 "",
 "層が全体（No.154）から立場へ出る。読むものが事実のテキストから見解のテキストに変わり、書き手が誰で何を主張しているかを読む最初の段。",
),
156: (
 ["Essay: Should schools start later in the morning? First, teenagers’ sleep patterns differ from adults’. Second, studies show that students come to school more often when it starts later. However, later starts create problems for working parents. On balance, the evidence favours a later start, but schools should offer early care for families who need it.\nYou: （結論は「遅らせるべき、ただし早朝の受け入れを添えて」と、順序と結びの標識から見分ける。）"],
 "論の構成が明示された論説文。「第一に・第二に・しかし・結論として」のような標識が、論の組み立てを示す。",
 "要点 ── 主な結論がどれか。標識を頼りに論の骨組みをたどり、結論を他の部分から見分ける。",
 "逆接の標識のあとに主張の転換が来ると待つため、別の側面を一つ添えるだけの逆接を主張の転換と読み過ぎ、譲歩として置かれた反対意見を結論と取り違える。",
 "立場（No.155）の隣に、論の構造を読む段が立つ。読むものは論説文になり、標識が支えになる。聞く側では「聴衆として聞く」の章のNo.42（主要なアイディアと補助的詳細の区別）が同じB1+で同じ要点の層に立つ。",
),
157: (
 ["Article: Cities are getting warmer. Some blame the changing climate alone, but the bigger local cause is the buildings and roads themselves: they take in heat by day and give it out at night. Planting trees helps, yet trees take years to grow. White roofs work faster and cost less, which is why several cities now require them on new buildings.\nYou: （原因は建物と道路、木は遅い、だから白い屋根、と論がどう進むかを追う。細かい数字は要らない。）"],
 "一つの問題を扱った記事や論説。論がどう進むか（問題→原因→対策の比較→結論）が読む対象で、詳細までは求められない。",
 "要点 ── 論の筋道。何が問題で、どの原因が選ばれ、どの対策が推されるか。細部を落としても骨組みがたどれればよい。",
 "",
 "No.156と同級で、標識の支えが外れる。論の構成が明示されていなくても、問題の扱いの筋道が追える段。",
),
151: (
 ["Article: Rent controls are back on the agenda, and once again the usual warnings are being recycled. Yes, controls can reduce the supply of rental housing ── if they are badly designed. But the experience of several European cities shows that well-designed controls protect neighbourhoods without freezing the market. The real question is not whether to regulate, but how.\nYou: （書き手は家賃規制に賛成の側、反対論を「使い古された警告」と退けている、と立場を取って読む。）"],
 "現代の問題（住宅・移民・環境・労働）について、書き手が特定の立場を取っている記事や報告。",
 "立場 ── 書き手がどの側に立ち、反対側をどう扱っているか。問題そのものについての知識と、立場を表す言葉の読みが要る。",
 "英語圏で論じられている問題を、日本の制度や社会の像で補って読んでしまい、書き手が何に反対しているのかの前提が合わず、取られている立場の輪郭を取り損ねる。",
 "立場の層が、身近な主題の短い投書（No.155）から現代の問題を扱う記事へ。主題の身近さが外れ、問題についての知識が支えの代わりになる。聞く側では「聴衆として聞く」の章のNo.37（時事の話題について表明された見解）が同じ立場の層に立つ。",
),
152: (
 ["Text A: The new tram line opened on 3 March. It runs every eight minutes between the station and the hospital, and a single ticket costs £2.\nText B: At last the city has a tram line worthy of the name ── frequent, clean, and affordable. Anyone who still doubts the value of public transport should take the eight-minute ride to the hospital.\nYou: （Aは事実の提供、Bは同じ路線を使って読者を説得しようとしている、と二つの書き方を見分ける。）"],
 "事実情報を提供するテキストと、読者を説得しようとするテキスト。同じ主題でも書き方が違う。",
 "立場 ── テキストが何をしようとしているか。情報を伝えているのか、読者を動かそうとしているのか。中身ではなく、書き手の資格と狙いを見る。",
 "日本語の広告や案内が「〜と言われています」「〜が人気です」と事実の形で読者を動かす型に慣れているため、英語の説得文が評価を言い切り読者に直接呼びかけていても、それを事実の報告として読み、説得されていることに気づかない。",
 "立場の層の三段目。No.151が一つの記事の立場を読むのに対し、ここでは事実と説得という書き方の違いそのものを見分ける。聞く側では「聴衆として聞く」の章のNo.40（表明された見解を報告される事実と区別する）が同じB2に立ち、同じ区別を音声で行う。",
),
153: (
 ["Text: Two approaches to recycling compete in the city. The first relies on households sorting waste into five bins; the second collects everything together and sorts it at a plant. The first produces cleaner material but depends on people’s cooperation; the second is easier for residents but costs more. Most cities have ended up combining the two.\nYou: （二つの方式の対比として組まれている、と構造を認識し、それぞれの長所と短所を対で読む。）"],
 "論述テキスト。対比、問題と解決、原因と結果のどれかの構造で組まれている。",
 "要点 ── テキストがどの構造で組まれているか。対比なら二つの側、問題-解決なら問題と解決、因果なら原因と結果を、構造として見分ける。",
 "",
 "要点の層の最上段。No.156の論説文の結論、No.157の論の筋道に続いて、ここでは論述の型そのものを認識する。",
),
149: (
 ["Journal abstract: We report a randomised trial of a five-day antibiotic course versus ten days in pneumonia. Non-inferiority was demonstrated for the primary outcome; adverse events were fewer in the five-day arm. We argue that current guidelines should be revised.\nYou: （五日投与でも劣らない、副作用は少ない、著者はガイドライン改定を主張、と自分の仕事に要る三点を取り出す。）"],
 "自分の分野の高度に専門的な情報源 ── 専門誌、技術報告、業界の文書。言葉は専門的で、分野の知識が前提になる。",
 "命題 ── 要る情報・アイディア・意見を取り出す。全体を読み通すことではなく、専門の知識を頼りに、情報源から必要なものを得る。",
 "",
 "層は命題（No.161）に戻るが、読むものが簡単な資料から高度に専門的な情報源へ。分野の知識が言葉の専門性を支え、要るものを取り出す読み方は同じ。",
),
150: (
 ["Article (economics): The central bank’s decision to hold rates reflects a view that inflation is now anchored. Critics argue that the labour market remains tight and that waiting risks a second wave of price rises.\nYou: （「anchored」と「tight」を辞書で確かめ、据え置きの理由と批判の中身を全体として受け取る。）"],
 "自分の専門外の専門的な記事。用語の解釈を時々辞書で確かめることができる。",
 "全体 ── 専門外でも、記事の大半を一つの像として持つ。辞書は用語の確認に限って使い、文章の組み立ては自分で追う。",
 "",
 "自分の分野（No.149）から専門外へ。分野の知識が外れた代わりに、辞書という読む側の手加減が条件に書かれる。読み返し（No.159）に続く、読む側だけが持つ二つめの支え。",
),
148: (
 ["Review: The report is thorough, and its authors have clearly worked hard. It is also, at nearly three hundred pages, considerably longer than it needs to be, and the recommendations in the final chapter will surprise no one who has followed the debate.\nYou: （「よく働いた」「長すぎる」「驚かない」から、評者は報告を評価していない、と暗示された意見を取る。）"],
 "社会・職業・学術の生活で出会う、長く複雑なテキスト。態度や意見が明示されるとは限らない。",
 "含意 ── 細かな点まで理解した上で、書かれていない意見と態度を補う。言われたことの全体が組み上がった先で、言外に出る。",
 "肯定の言葉に軽い但し書きを添えるだけで批判を含ませる言い方を、但し書きつきの褒め言葉として読んでしまい、含まれた批判を取り損ねる。",
 "全体（No.150）から含意へ。専門外の条件も辞書の支えも外れ、長く複雑なテキストで、言われていないことまで読む。",
),
147: (
 ["Report (engineering): The bridge remains within its design limits. Inspection intervals have been cut from five years to two, and the operator has been asked to provide a replacement plan by the end of the year.\nYou: （許容範囲内と言いながら点検を倍に増やし、建て替えの計画を求めている ── 書かれていない懸念を読む。）"],
 "専門外の、複雑な報告や記事。辞書の但し書きはなく、専門外であることが条件でなく逆向きの但し書きとして付く。",
 "含意 ── 専門外でも、細部と含意を取る。知識の支えなしに、報告が言わずに示していることを読む。",
 "",
 "読む側の梯子の終点。No.148の含意が、専門外という逆向きの但し書きの下でも求められる。聞く側では「聴衆として聞く」の章のNo.33（つながりや含意が明示されない場合の推論）が同じC2で同じ含意の課題に立ち、聞く側の終点（No.34、冗談の意図）と同じく、梯子は「分かる」の形のまま尽きる。",
),
}

DISCUSSION = [
    # 1 梯子
    "読む側の梯子も、入力の側の手加減が外れていく列に宿る。本スケール26行の条件句を並べると、支え（写真・絵・ごく簡単な言葉：No.172/170/171）→ 簡単な言葉と身近な主題（165/166/167/168/169/161/162/163/164）→ 身近な主題と率直さ（158/159/160/154/155/156/157）→ 条件なし（151/152/153）→ 自分の分野か辞書（149/150）→ 専門外（148/147）の六区分になる。深さは七層で引く ── 命題（172/166/161/149の4段）・筋（170/162）・要点（167/163/164/158/160/156/157/153の8段）・全体（171/165/168/169/159/154/150の7段）・含意（148/147）・立場（155/151/152）。聞く側と同じく層は級に対して単調でなく、命題はPre-A1からB2+まで四段にわたり、全体はA1に既にある。読む側の特徴は要点の層が厚いこと（8段。聞く側は4段）と、命題の層が上の級まで残ること ── 文字は動かないので、要るところだけを取る読み方が、簡単な資料（161）から専門誌（149）まで、独立した段として数えられる。",
    # 2 読む側だけが持つ手加減
    "条件の列のなかに、聞く側にはない手加減が二つ現れる。読み返す時間（No.159、B1）と辞書（No.150、B2+）である。どちらも読み手が自分で取る手加減で、話し手の側がしてくれる「ゆっくり・繰り返し」とは向きが逆 ── 聞く側では繰り返しの支えがA2（「聴衆として聞く」の章のNo.47）で消え、以後は聞き手が求める側に回るのに対し、読む側の手加減はB1からB2+まで残り、C1・C2で外れる。もう一つ、紙面の作り（見出し・数字・名前・図：No.163）が意味を支える段は読む側だけにある。文字のテキストは、言葉以外の層（配置・太字・数字）で読み手を助けることができる。",
    # 3 聞く側との対
    "聞く側と同じ級で同じ層に立つ段は、読む側に十段ある（170↔49・162↔46・158/160↔45・156/157↔42・153↔39・151/152↔40・147↔33/34）。そのうち課題まで一致する ── 同じ区別、同じ推論を、文字と音声で行う ── 三組を対として読む：156↔42（B1+・要点：論説文の主な結論／講義の主要なアイディアと補助的詳細）、152↔40（B2・立場：事実の提供と説得の見分け／見解と事実の区別）、147↔33（C2・含意：複雑な報告の含意／明示されない含意の推論）。文言はほとんど共有されず、級と層と課題の一致で読む。条件の列の形は違う ── 聞く側は音形の支え（ゆっくり・明瞭・標準語）が最後まで残り、読む側は言葉の簡単さの支えがB1で外れて、主題の身近さと紙面の作りだけが残る。読む側は文字が逃げないので、下の層の支えを早く外せる。",
    # 4 落とし穴
    "日本語話者の落とし穴は、この章では三つの源に分かれる。一つは訳読で身についた読み方 ── 頭から終わりまで全部を日本語に置き換える読み方は、文が長くなると前の文が薄れ（No.162）、要る一項目を探す読み（161）、見出しと数字から要点を取る読み（163）、絵と分かる語から見当をつける読み（170）に切り替わらない。読む目的に応じて読み方を変えることが、この章の下半分の段の多くで求められているのに、全部を順に読む一つの読み方しか持たないことが穴になる。もう一つは文章の型と文脈 ── 結論を最後に置く型で待って第一文の要点を読み流す（164/158）、逆接の標識を主張の転換と読み過ぎる（156）、日本の暮らしの像で補って書かれた違いを違いとして受け取れない（165）、日本の制度や社会の像で補って立場の前提を外す（151）、事実の形で読者を動かす広告や案内に慣れて説得を事実の報告と読む（152）、軽い但し書きで批判を含ませる言い方を褒め言葉と読む（148）。三つめは文字の形 ── カタカナの音形と綴り（171）、住所の書き方（166）で、下の段にだけある。穴のない段が13段あり、聞く側（8段）より多い ── 専門の知識や辞書が条件の段（149/150）、紙面の型や語彙の段階が難しさの源である段（167/154/157/160/153）、段の条件がすでに支えを与えている段（写真と絵が語を経ずに場面を与える172、分野の知識が前提の168、読み返す時間が与えられる159）、そして日本語話者に固有の持ち込みの形が見当たらない段（自己紹介の投稿169、直接に立場を書く投書155、専門外という逆向きの但し書きに固有の穴がなく含意の穴は148と同じ147）である。",
    # 5 何がこの梯子を測るか
    "聞く側と同じく、この梯子を測るものさしは条件と層の二つで、読み手は何も産出しない。読む側で足すべきことは一つ ── 条件のなかに読み手が自分で取る手加減（読み返し・辞書）があるので、「どんなテキストなら」の問いに「どれだけ戻ってよいなら」が加わる。ある段が自分にできるかどうかは、どんな文章を、どこまで（命題か・筋か・要点か・全体か・含意か・立場か）、戻らずに読めるか、で確かめる。上端が「含意」で閉じるのは聞く側と同じだが、読む側の最上段（No.147）は「専門外であっても」という逆向きの但し書きで、聞く側の最上段（冗談の意図）のように話し手の癖ではなく、読み手の知識の外側に置かれる。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 26
    for name, m in (("CONDITION", CONDITION), ("DEPTH", DEPTH)):
        tagged = [n for v in m.values() for n in v]
        assert sorted(tagged) == sorted(ORDER), f"{name}が完全分割でない"
    assert list(DEPTH.keys()) == SEVEN_LAYERS, "DEPTHの語彙が七層でない"
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    arc = ["支え", "簡単な言葉と身近", "身近と率直", "条件なし", "分野か辞書", "逆境"]
    prev_min = -1
    for c in arc:
        lv = sorted(order_lv.index(desc[str(n)]["level"]) for n in CONDITION[c])
        assert lv[0] >= prev_min, f"条件の列が級順でない: {c}"
        prev_min = lv[0]
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        rows.append({
            "mode": MODE, "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "知るために読む（Reading for information and argument）── 第3柱第二号範型・全数シート",
        "scope": "全数（26件。読む26 ── mode一様）",
        "type": "第3柱（受容）。梯子＝条件の解除の一本（支え→簡単な言葉と身近→身近と率直→条件なし→分野か辞書→逆境）、深さ＝七層は段の属性。糸は立てない。四欄（scene＝読むもの・howwell＝分かること・l1・delta）は書物の本文そのもの（判断(bs)）。落とし穴は『受容の課題』§5に拠るものだけ（判断(bt)）。",
        "essence": "読み手は最後まで「分かる」の形で書かれ、段を区切るのは入力の側の手加減である。写真から専門外までの条件の列が背骨、命題から含意までの層が段の中身。読む側だけの手加減（読み返し・辞書・紙面の作り）が条件に現れ、要点の層が厚く、命題の層が上の級まで残る。聞く側（聴衆として聞く）とは筋・要点・立場・含意の段で同級に並び、課題まで一致する三組（156↔42・152↔40・147↔33）を対として読む。",
        "axes": {"条件": CONDITION, "深さ": DEPTH},
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p3_reading.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
    print("落とし穴欄:", sum(1 for r in sheet["rows"] if r["l1"]), "/ 空欄:", [r["no"] for r in sheet["rows"] if not r["l1"]])
