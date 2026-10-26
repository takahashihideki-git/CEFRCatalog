#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第3柱（受容）量産第五号：Watching TV, film and video 14件の全数シート（CEFRカタログ41、判断(ch)）。

範型（一号＝聴衆として聞く・判断(bs)、二号＝知るために読む・判断(bt)）と量産第一号〜第四号（告知と指示を聞く・判断(by)／他人どうしの会話を聞く・判断(ca)／
録音と放送を聞く・判断(cc)／相手の話を聞く・判断(ce)）と同じ器で立てる。『受容の課題』（判断(br)）が正準。
- シート＝スケール（mode一様＝「見る」）。章名「テレビ・映画・動画を見る」（p3_inventory の章〔仮〕）。第3部で mode「見る」はこのスケールだけ
  （CEFR増補版 p.47 の三分＝口頭受容／視覚受容〔読む・手話〕／視聴覚理解〔尺度は本スケール一つ〕）
- 列10は不変。第3柱での読み替え：
    exponents … 一要素＝二行以上。素材のラベル（Video / Newsreader / Reporter / Advert / Trailer / Film / Presenter / Interviewer / Host / Guest / Play …）に続けて、
                 画面に映るものを角括弧 [picture: …] で置き（「知るために読む」の [picture: …] と同じ形）、聞こえる言葉を続け、最後に You: （分かったしるし＝自分のための理解の丸括弧の行動描写）。
                 この章の素材は映像を伴う ── 画面の中身が理解を担う段では、角括弧の画面が例の証拠になる（下の段）。上の段では画面は場を示すだけで、言葉が理解を担う。
                 「見る」の言葉はしるしの中で英語を出さない（語彙裁定＝判断(s)、照合は入力の英語と角括弧の英語）
    scene     … 「見るもの」＝番組・映画・動画の種類と、その作り（記述文の条件句＝映像の支え・伝え方・言葉の但し書きを含む）
    howwell   … 「分かること」＝求められる層（七層）と、その段でその層を求めることの意味。欄の頭の層名は読者の言葉で置く ── 形→「知っている言葉」（判断(cc)）
    l1        … 「日本語話者の落とし穴」。判定は執筆要綱・規律6-1受容版の五条件＋手順（欄ごとに「Can-Doの一般形→当てる§5の要因→欄」の三行を先に書く＝申し送りに添付）。
                 本シートの欄が拠る§5の箇所：§5.1(b) カタカナ語の音形（95）／
                 §5.4 内容スキーマ＝日本の制度の像の持ち込み〔(e)〕（87）／§5.3 形式スキーマ＝結論の位置（86）／§5.5 控えめに言う型〔(d)、本便で追記〕（85）。
                 空欄10（96・94・92・93・90・91・89・88・83・84）：96＝映像と既有知識が主題を与える段で、言葉の型の持ち込みとして指せるものがない／
                 92・90＝画面が要点と筋を与えている段では、聞き取りの構え（§5.6）がどうであれ画面の分が理解に立つ ── 構えの欄は段の条件（映像が解説を補う・映像と動きが筋を担う）を打ち消す側に回るので立てない（カタログ41 Hideki精読）／
                 94＝ニュースが項目ごとに進む型は日本語の視聴者も慣れている（「録音と放送を聞く」No.73と同じ）／93＝コマーシャルと予告編の型について日本語話者が外す形を§5から指せない（No.75と同じ）／
                 91・89＝身近な話題・個人的関心が条件で§5.4は当たらず、ゆっくり明瞭が§5.6の構えを支える／
                 88＝87と同じ持ち込みしかなく、標準語という条件は言葉の側の支えで内容の持ち込みを打ち消しも足しもしない／83＝俗語・慣用表現は言葉の聞き取りの負荷であって含意の穴ではない（No.69と同じ）／
                 84＝86と同じ型の持ち込みしかなく、細部まで求める段で指せる別の形がない
    delta     … 前の段から。同じ聞く側（告知と指示・聴衆として聞く・他人どうしの会話・録音と放送・相手の話）・語る側（経験を語る・創作の文章）との関係は散文で先に記録（判断(ai)③）
- **四欄（scene・howwell・l1・delta）は書物の本文として書く**（読者語彙。帳簿語は出さない。判断(bs)）。用字＝可能形「〜が取れる」は使わない、態度・気分・視点・関係を目的語にした「取る」は使わない（判断(cc)）、
  「やり取り」は平仮名（判断(cf)）
- 梯子＝条件の解除の一本（CONDITION、完全分割、語彙はスケールごと）：映像の支え → ニュースの型 → ゆっくり → 標準語か馴染みのある方言 → 条件なし → 逆境。
  この章の但し書きの担い手は素材の映像（相手に頼むものでも自分で選ぶものでもなく、画面がくれるもの）。映像の支えは『受容の課題』§4の「絵・写真・図」（層1・2を飛ばして層3へ）の動く形。
  CEFRが鍵概念に立てたのは深さと伝え方の二本で、映像の支えは本書の読み（DISCUSSION 2）。速さの但し書きがB1＋B1+に二段残り、B1+の段（89）は聞く側の全章で最も高い速さの但し書き（6シートをgrepで確認）。
  上端C1は三段が三つの顔に割れる ── 俗語・慣用表現でも（83＝逆境）、難度の高い放送（84＝条件なし）、標準語か馴染みのある方言で（85）
  深さ＝七層（DEPTH、完全分割、正準は『受容の課題』§2・付録A）。一つの項目（命題）と立場の段がない。含意（85）で閉じる。C2なし（原典が「C1を参照」）、Pre-A1あり
- CEFR増補版の企図（規律12、Web裏取り＝p.47・p.52）：視聴覚理解は口頭受容・視覚受容と並ぶ受容の第三の種類で、尺度は一つ、字幕・吹き替え・手話の有無を問わない。
  鍵概念＝話題の切り替わりを追い要点を特定する／細部・ニュアンス・含意（C級）／伝え方（ゆっくり明瞭な標準語から俗語・慣用表現まで）。別立ての理由は原典に書かれていない（2001年版4.4.2.3の定義「聴覚入力と視覚入力を同時に受け取る」を継承）。
  2001年版の母体8件（92・94／90・91・89／87・88／83）に増補版が6件（96・95・93・86・84・85）を足し、下端の三つ（96・95・93）はすべて映像の支えを但し書きに持つ
- 語彙裁定（判断(s)）：例文は入力（素材の言葉）と角括弧の画面の英語を照合対象とする。日本語で書いたしるし（行動）は照合外。allowlist＝quid・telly（C1行83の俗語を演じる語。人名 Tom・Ken は裁定済み）
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Watching TV, film and video"
ACT = "テレビ・映画・動画を見る（第3柱：Watching TV, film and video）"
MODE = "見る"

SEVEN_LAYERS = ["形", "命題", "筋", "要点", "全体", "含意", "立場"]

# レベル順→No昇順（表示順の正準）
ORDER = [96, 95, 94, 92, 93, 90, 91, 89, 87, 88, 86, 83, 84, 85]

# 条件（素材の側の但し書き。行ごとに一つ、完全分割）
CONDITION = {
    "映像の支え":                 [96, 95, 92, 93, 90],  # 視覚情報と既有知識（96）・視覚情報と一般知識（95）・映像が解説を補う（92）・映像が理解を大いに助け明瞭で比較的ゆっくり（93）・映像と動きが筋を担い平明な言葉で明瞭に（90）── 画面が理解を担う
    "ニュースの型":               [94],                  # 事実を伝えるテレビニュース ── 映像にも速さにも但し書きがなく、項目ごとに進むニュースの型が支え（『受容の課題』§4「予測できる状況・型」＝層3。付録Aの層も筋）
    "ゆっくり":                   [91, 89],              # 比較的ゆっくり明瞭に（身近な話題のテレビ番組・個人的関心のある話題の番組）── 速さの但し書きがB1・B1+に残る。B1+（89）は聞く側の全章で最も高い
    "標準語か馴染みのある方言":   [88, 85],              # 標準語または馴染みのある地域の方言やアクセントであれば（88＝ドキュメンタリー・生インタビュー・トークショー・演劇・大半の映画、85＝ニュアンスと含意）
    "条件なし":                   [87, 86, 84],          # テレビのニュースと時事番組の大半（87）・議論から要点を抽出（86）・難度の高い放送の論を詳細に（84）── 入力の難しさが行の主語になる
    "逆境":                       [83],                  # かなりの俗語や慣用表現を使う映画でも ── 但し書きが「〜であっても」へ裏返る
}
# 深さ＝七層（『受容の課題』付録A の写像）
DEPTH = {
    "形":   [95],
    "命題": [],
    "筋":   [96, 94, 93, 90],
    "要点": [92, 91, 86],
    "全体": [89, 87, 88, 83, 84],
    "含意": [85],
    "立場": [],
}

R = {  # no -> (exponents, scene=見るもの, howwell=分かること, l1=落とし穴, delta=前の段から)
96: (
 ["Video: [picture: a kitchen; a woman; tomatoes; eggs; the words Easy Pizza] Hello! … Today … pizza. … Very easy! … Look.\nYou: （料理の動画で、ピザの作り方だと分かる。）",
  "Video: [picture: a football field; two teams; the numbers 2–1] … City! … And … goal! … City two, Town one.\nYou: （サッカーの試合の映像で、シティが勝った試合のまとめだと分かる。）"],
 "短い動画。料理、スポーツ、乗り物、動物のような、何についてかが画面を見れば分かる素材で、題名や画面の文字、映っているものが、言葉より先に主題を与える。言葉は聞き取れなくてよい。",
 "筋 ── この動画が何についてのものか。文を一つも聞き取れなくても、画面に映るものと、自分が知っていること（料理番組はこういう画面、試合のまとめはこういう画面）から、主題の見当がつけばよい。",
 "",
 "この章の梯子の起点。聞く側の章の起点のうち、「告知と指示を聞く」の章（No.67）が身振りつきの一語の指示から、「相手の話を聞く」の章（No.422）が自分への簡単な質問から、「録音と放送を聞く」の章（No.81）が顔の見えない声の中の知っている語から始まるのに対して、この章は言葉より先に画面から始まる ── 聞き取れた語を数えるのではなく、映っているものから何の動画かを見当づける。聞く・読む言葉の章の中で、言葉を一つも要らない段から立つのは、この章だけである。",
),
95: (
 ["Newsreader: [picture: the word NEWS; a photo of rain and a river] … Rain … tomorrow. … [picture: a photo of a football player] … Football: City wins. … [picture: a photo of a school] … Schools open on Monday.\nYou: （雨、サッカー、学校、と見出しの話題が一つずつ分かる。）",
  "Advert: [picture: a bottle of cold water; a beach; the sun] … Cool Water. … Cold. … Good. … Cool Water — in shops now.\nYou: （水の広告で、商品の名前が分かる。）"],
 "ニュースの見出しのまとめと、テレビの広告。見出しは写真と一語二語の文字を伴って一つずつ出され、広告は商品を映しながら名前を繰り返す。画面の文字と写真、そして自分の一般知識が、聞こえる語を支える。",
 "知っている言葉 ── 見出しに知っている語が出た、広告に知っている商品が出た、と気づくこと。見出しが何を報じているかの中身ではなく、雨・サッカー・学校という話題の語が拾え、商品の多くが何か分かればよい。",
 "外国の商品名や土地の名前はカタカナで知っている語が多く、その音形で待っているため、強勢の位置や母音の違う英語の音形で言われると、知っているはずの名前がそれだと結びつかず、画面に文字で出た商品しか拾えない。",
 "画面が与える主題（No.96）から、聞こえる語へ。何についての映像かを画面で見当づける段から、見出しや広告の中に知っている語を一つずつ拾う段へ上がる。画面の支えは同じで、文字と写真が語を予告する。「録音と放送を聞く」の章の起点（No.81）が録音の中の知っている語で立つのと同じ層に、この章は画面の支えつきでA1に立つ ── 向こうは音だけ、こちらは文字と写真が音を支える。",
),
94: (
 ["Newsreader: [picture: a new school building; children at the door] A new school opened today in the city. … Three hundred children started classes this morning. … [picture: a road; a lot of cars] And on the roads: the road to the airport is closed this weekend. … Please use the train.\nYou: （学校の開校の話から道路の話に移ったと分かり、新しい学校が開き、空港への道が週末に閉まる、と見当がつく。）",
  "Newsreader: [picture: a market; boxes of apples] Prices at the market went up again this month. … Apples cost more than last year. … [picture: a river; a boat] Now to the river: the new boat starts on Saturday. … It goes every hour.\nYou: （物価の話から川の船の話に変わったと分かり、リンゴが値上がりし、船の便が土曜に始まる、と見当がつく。）"],
 "事実を伝えるテレビニュース。開校、道路の閉鎖、物価、新しい便のような出来事を、項目ごとに短く伝える。映像にも速さにも但し書きはなく、ニュースが一項目ずつ進み、画面が変わると話題も変わる、という型が支えになる。",
 "筋 ── 話題がいつ変わったかと、各項目のおおよその中身。細部ではなく、学校の話が終わって道路の話になった、新しい学校が開いた、道が閉まる、という見当がつけばよい。",
 "",
 "画面の文字と写真に知っている語を拾う段（No.95）から、項目の移り変わりを追う段へ。層は知っている言葉から筋へ上がり、映像の支えは条件から消えて、ニュースの型だけが残る ── 項目ごとに進み、画面が変わると話題が変わるという作りが、次に来るものを予告する。「録音と放送を聞く」の章のB1（No.73）がニュースの各項目の要点をつかむ段であるのに対し、こちらはA2で、話題の移りと中身の見当にとどまる。",
),
92: (
 ["Reporter: [picture: a river over a road; people in small boats; a house with water at the door] Heavy rain last night. … The river came up two metres. … Fifty families left their homes. … Nobody was hurt.\nYou: （大雨で川があふれ、五十家族が家を離れたがけが人はいない、と要点が分かる。）",
  "Reporter: [picture: a bus on its side; police cars; a closed road] A bus hit a car on the road to the city this morning. … Twelve people went to hospital. … The road was closed for three hours. … It is open again now.\nYou: （バスの事故で十二人が病院へ運ばれ、道路は三時間閉鎖されたが今は開いている、と要点が分かる。）"],
 "事件や事故を報じるテレビニュース。洪水、交通事故、火事のような出来事を、現場の映像とともに伝える。映像が解説を補っていること ── 川があふれた画面、横倒しのバスの画面が、言葉より先に何が起きたかを見せること ── が条件である。",
 "要点 ── その出来事の要点。何が起きて、どれだけの人が関わり、どうなったか。解説の全部ではなく、映像が見せているものと言葉が伝える数とを合わせて、項目の核がつかめればよい。",
 "",
 "項目の見当（No.94）から要点へ。層は筋から要点へ上がり、映像の支えが条件に戻る ── ニュースの型だけでなく、現場の映像が解説を補うことが、要点をつかむ支えになる。「録音と放送を聞く」の章のA2（No.78）が短い放送の重要情報を拾う段で、向こうは型と短さが支え、こちらは画面が支える。「告知と指示を聞く」の章の同じA2+（No.60）が、その場で流れる率直なアナウンスをゆっくり明瞭にという但し書きつきで聞く段で、向こうは速さが支え、こちらは画面が支える。",
),
93: (
 ["Advert: [picture: a family in a car; the sea; a small white house by the beach] This summer … go to Cornwall. … Sun, … sea, … and a house by the beach. … From two hundred a week. … Book now at Sunny Homes.\nYou: （コーンウォールでの休暇の広告で、海辺の家を貸す話だと分かる。）",
  "Trailer: [picture: a dark street; a man runs; a woman with a phone] He has one night. … [picture: a train at night] One train. … [picture: the man and the woman together] And one chance. … Last Train — in cinemas this Friday.\nYou: （一晩で何かを果たす話の映画の予告編で、金曜から公開だと分かる。）"],
 "テレビのコマーシャル、映画の予告編、映画の一場面。売る側や宣伝の側が、映像を主に、言葉を短く作った素材で、映像が理解を大いに助け、言葉は明瞭で比較的ゆっくり伝えられること、の二つが条件である。",
 "筋 ── 何についてのコマーシャルか、何の話の映画か。売り文句や台詞の全部ではなく、休暇の家の広告だ、一晩の逃走の映画だ、という話題が追えればよい。",
 "",
 "同じA2+に立つ、もう一つの段。ニュースの要点（No.92）とは層が違い、宣伝と予告編の話題を追う ── 層は筋で、映像の支えに加えて、明瞭さと速さの但し書きがこの章で初めて付く。「録音と放送を聞く」の章の同じA2+（No.75）が短いコマーシャルの最重要情報を拾う段で、向こうは音だけで何がいくらかを拾い、こちらは画面が何の広告かを先に見せる。この章の作り物の線（コマーシャル・予告編→映画→演劇と映画→俗語の映画→映画・演劇・番組の言葉の含み）はここで立つ。",
),
90: (
 ["Film: [picture: rain; a boy finds a small wet dog in the park and carries it home] Mum: Where did you get that? … Boy: He was in the park. He was cold. … Mum: We can’t keep him. … [picture: the boy puts up posters: LOST DOG; days pass; nobody comes] … Mum: Well. … I think he can stay.\nYou: （拾った犬を飼えないと言われ、飼い主を探しても現れず、最後に飼ってよいと言われる、と筋が追える。）",
  "Film: [picture: an old man alone in a big house; he looks at old photos] Woman: You should sell it, Dad. … It’s too big for you. … Old man: I was born in this house. … [picture: a young family looks at the house; the old man watches from the window; later, he opens the door to them] … Old man: Come in. … It’s a good house for children.\nYou: （家を売れと言われて断った老人が、見に来た家族を迎え入れる、と映像と短い台詞から筋が追える。）"],
 "映像と動きが筋の大部分を担う映画。拾った犬の話、家を手放す話のような、出来事が画面に映り、台詞が短くて平明な言葉で明瞭に話される作品。筋は画面が運び、台詞はそれを確かめる。",
 "筋 ── 映画の筋。何が起きて、誰がどうして、どう終わるか。台詞の一つ一つではなく、映像の運びと短い台詞とを合わせて、話のはじめから終わりまでが追えればよい。",
 "",
 "作り物の線の二段目。予告編の話題（No.93）から、一本の映画の筋へ。層は筋のまま、見るものが数分の宣伝から一本の作品へ長くなる。条件は映像と動きが筋を担うこと、言葉が平明で明瞭なことの二つで、「比較的ゆっくり」は外れる。「録音と放送を聞く」の章のA2（No.79）が短い物語の録音の筋を追う段で、向こうは語り手の声だけで筋を追い、こちらは画面が筋を運ぶ。語る・書き上げる言葉の「経験を語る」の章の同じB1（No.244）が、本や映画の筋を語る側から立てている。",
),
91: (
 ["Presenter: [picture: a kitchen; a bowl of flour] Today we’re making bread at home. … You need flour, water, salt and a little yeast. … [picture: hands mix the dough] Mix it well, … then leave it for an hour. … [picture: an oven; a loaf] Bake it for thirty minutes. … And that’s it.\nYou: （材料四つ、混ぜて一時間おいて三十分焼く、と番組の要点がつかめる。）",
  "Presenter: [picture: a small town by a lake; a boat; a market] This week we’re in a small town by the lake. … In the morning there’s a market by the water. … [picture: a path up a hill] And in the afternoon you can walk up the hill. … The view from the top is wonderful.\nYou: （湖畔の町で、朝は市場、午後は丘に登る、と番組の要点がつかめる。）"],
 "身近な話題のテレビ番組。料理、旅、暮らしのような、自分の知っている話題を扱う番組で、比較的ゆっくり明瞭に話されること ── 学習者を含む視聴者に向けて速さを抑えて作られていること ── が条件である。",
 "要点 ── 番組の要点。材料と手順、朝と午後の行き先のような、番組が伝えたい核。画面が見せるものと言葉とを合わせて、要点がつかめればよい。",
 "",
 "映画の筋（No.90）と同じB1に立つ、番組の線の段。層は要点で、条件が映像の支えから速さの但し書きへ変わる ── 画面が理解を担うのではなく、話し方が抑えられていることが支えになる。この章で速さの但し書きが付くのはB1（91）とB1+（89）の二段で、聞く側のどの章よりも高い級に残る。「録音と放送を聞く」の章の同じB1（No.73）がニュースの要点を比較的ゆっくりの但し書きつきでつかむ段で、向こうは音だけ、こちらは画面つきである。",
),
89: (
 ["Interviewer: [picture: a studio; a woman in running clothes] You ran your first big race at fifty. Why? … Runner: My doctor told me to walk more. … So I walked, … then I ran a bit, … and then I couldn’t stop. … The first year was hard — my knees, my feet, everything. … But I had a group, and that made all the difference.\nYou: （五十歳で走り始めた理由、最初の一年の苦労、仲間の支え、と話の大部分が分かる。）",
  "Lecturer: [picture: a lecture hall; a picture of a bee; a flower] Bees visit about a thousand flowers a day. … [picture: a map of a town] In a town, they find more flowers than in the fields outside, … because gardens have flowers all year. … So a city can be a good home for bees — if we leave some space for them.\nYou: （蜂は一日に千の花を訪れ、庭のある町では野原より花が多く、街は蜂の住処になりうる、と講演の大部分が分かる。）"],
 "インタビュー、短い講演、ニュースの報道のような、個人的関心のある話題のテレビ番組。比較的ゆっくり明瞭に話されることと、自分の関心のある話題であることの二つが支えになる。",
 "全体 ── 番組の大部分。要点だけでなく、なぜ走り始めたか、最初の一年はどうだったか、何が支えになったか、という話の大半が一つの像として入る。",
 "",
 "要点（No.91）から大部分へ。層は要点から全体へ上がり、条件は「比較的ゆっくり明瞭」のまま、身近な話題が個人的関心のある話題へ広がる。速さの但し書きがこの級まで残るのは、聞く側の章では「聴衆として聞く」の章（No.45）も「録音と放送を聞く」の章（No.73・74）もB1までで、B1+に残るのはこの章だけである。「録音と放送を聞く」の章の同じB1+（No.72）が関心のある話題の録音の大部分を聞く段で、向こうは「明瞭な標準語で」が条件、こちらは速さが条件である。",
),
87: (
 ["Newsreader: [picture: a parliament building; then a hospital corridor] The government’s new health bill passed its second vote tonight, by a narrow margin. … Opponents say the money falls short of what hospitals need, … while ministers insist the changes will cut waiting times within two years. … [picture: a reporter outside the hospital] Reporter: Staff here are cautious. One nurse told me the money is welcome, but the plan says nothing about finding new staff.\nYou: （法案が僅差で通り、野党は予算不足を言い、政府は待ち時間の短縮を約束し、現場は人手の手当てがないことを心配している、と番組の大半が分かる。）",
  "Presenter: [picture: a studio; a chart of house prices going up] House prices rose again last month, for ten months in a row. … [picture: a street of small houses; a young couple] For first-time buyers, the gap between wages and prices is now the widest on record. … The bank is expected to raise interest rates again next week, … which will make it harder still.\nYou: （住宅価格が十か月続けて上がり、初めて買う人には賃金との差が過去最大で、来週の利上げでさらに厳しくなる、と分かる。）"],
 "テレビのニュースと時事番組。政治、経済、社会の出来事を、スタジオと現場の映像を切り替えながら伝える。速さにも映像にも言葉にも但し書きはなく、番組の大半が分かることが求められる。",
 "全体 ── ニュースと時事番組の大半。項目ごとの要点ではなく、何が決まり、誰が何を言い、現場がどう受け止めたか、という報道の全体が一つの像として入る。",
 "番組が扱う議会、保険、年金、住宅のような制度を、日本の同じ名前の制度の像で見てしまうため、語は聞き取れているのに、何が争点で、なぜ野党が反対し、なぜ現場が心配しているのかが組み上がらない。",
 "速さの但し書きが消える段。B1・B1+（No.91・89）で残っていた「比較的ゆっくり明瞭」がここで外れ、「個人的関心のある話題」も消えて、ニュースと時事番組の大半を但し書きなしで見る。層は全体のまま、見るものが関心のある番組から時事の全般へ広がる。「録音と放送を聞く」の章の同じB2（No.71）がドキュメンタリーの大半を標準語の但し書きつきで聞く段で、向こうには言葉の但し書きが残り、こちらにはない。",
),
88: (
 ["Host: [picture: a talk show; a sofa; an actor] So the new film — you play a man who loses everything. … Actor: Everything but his dog, yes. … Host: And you shot it in winter, in Scotland. … Actor: In January. Honestly, the dog was the only one of us who enjoyed it.\nYou: （新作で何もかも失う男を演じ、スコットランドの一月の撮影で犬だけが楽しんでいた、とトークショーのやりとりが分かる。）",
  "Narrator: [picture: a river; a small town; an old mill] For two hundred years, the mill was the town. … Everyone worked here, or for someone who did. … [picture: an old man by the water] Old man: My father ran the big wheel. … When it stopped, in 1979, the whole street went quiet. … You could hear the river for the first time.\nYou: （製粉所が町そのもので、止まった年に通りが静まり返った、とドキュメンタリーの全体が分かる。）"],
 "ドキュメンタリー、生のインタビュー、トークショー、演劇、そして大半の映画。制作された番組と作品で、標準語または馴染みのある地域の方言やアクセントで伝えられていれば、という言葉の但し書きだけが残る。",
 "全体 ── 番組と作品の全体。話の大半を、誰が何を語り、どう受け答えしたかまで一つの像として受け取る。トークショーの軽口も、ドキュメンタリーの証言も、同じ層で求められる。",
 "",
 "同じB2に立つ、もう一つの段。報道（No.87）と並んで、作り物と語りの番組を見る ── 作り物の線は映画の筋（No.90）からここで演劇と大半の映画へ広がり、番組の線はB1+のインタビューと講演（No.89）からトークショーとドキュメンタリーへ広がる。条件は言葉の側の但し書き（標準語か馴染みのある方言）で、この章で初めて付く。同じ形の但し書きは聞く側のB2に五つ並ぶ ── 「聴衆として聞く」の章（No.39）、「告知と指示を聞く」の章（No.54）、「他人どうしの会話を聞く」の章（No.22）、「相手の話を聞く」の章（No.415）とこの段。「録音と放送を聞く」の章の同じB2（No.71）だけは標準語のみで、馴染みのある方言を但し書きに持たない。",
),
86: (
 ["Host: [picture: a studio; two guests] Should the city ban cars from the centre? … Guest 1: Yes, and soon. The air quality figures speak for themselves, and every city that has done it has seen its shops do better, not worse. … Guest 2: I’d be careful. Those figures come from cities with good public transport. Ours isn’t there yet — ban cars now and you simply move the traffic one street out.\nYou: （賛成の論拠は空気の質と商店の売上、慎重論の論拠は公共交通の不足と渋滞の移動、と双方の要点が抜き出せる。）",
  "Reporter: [picture: a school; a teacher; a parent at the gate] Teacher: Longer school days would give children who have no quiet place at home somewhere to work. … Parent: Or it would take away the one part of the day that’s theirs. The children who need help aren’t the ones who’d stay.\nYou: （延長に賛成の論拠は家で勉強できない子の居場所、反対の論拠は子どもの時間と対象のずれ、と要点が抜き出せる。）"],
 "ニュースと時事番組の中の議論。司会が問いを立て、立場の違う出演者や当事者が論を述べる。但し書きはなく、議論の言葉から要点を取り出すことが求められる。",
 "要点 ── 議論の要点。それぞれが何を主張し、何を論拠にしているか。発言の全部ではなく、賛成の論拠と慎重論の論拠が抜き出せればよい。番組の大半が分かる段（No.87）の先で、分かったものから論の骨を取り出す段。",
 "討論の出演者が立場を先に言って論拠を続けるのに、結論は最後に来るものと待って、論拠の列挙から立場を組み立て直そうとしているうちに次の出演者に移ってしまい、誰が何を主張したかの要点を取り損ねる。",
 "全体（No.87・88）の上に、要点の段がもう一度立つ。層は全体から要点へ戻るが、求めるものは違う ── 番組の大半が分かる段の先で、議論の言葉から論の骨を抜き出す。条件なしは同じ。「他人どうしの会話を聞く」の章のB2（No.22）が、議論の賛否の主な論拠を傍らで聞き分ける段で、向こうには明瞭な標準語か馴染みのある方言という但し書きが残り、こちらにはない。「聴衆として聞く」の章のB2+（No.37）が、講演で表明された視点を理解する段である。",
),
83: (
 ["Film: [picture: a pub; two friends at a table; a phone on the table] Tom: You’re having a laugh, mate. Fifty quid for that? … Ken: It’s a steal, that is. Go on — you’d be daft not to. … Tom: Daft, is it. … Well, don’t come crying to me when it packs in after a week.\nYou: （五十ポンドは高いと渋る友人を、もう一人が買い得だと押し、買ってもすぐ壊れると言い返す、と俗語混じりの台詞から筋が追える。）",
  "Film: [picture: a small flat; a mother and a teenage son; the television is on] Mother: Turn that telly off and give us a hand, will you? … Son: In a minute. … Mother: It’s always in a minute with you. … Son: All right, all right, keep your hair on.\nYou: （テレビを消して手伝えと言う母と、すぐ、と先延ばしにする息子の、慣用表現混じりのやりとりが分かる。）"],
 "かなりの俗語や慣用表現を使う映画。パブの会話、家庭の口喧嘩のような、日常のくだけた言葉で台詞が作られた作品で、標準語という但し書きは外れ、俗語や慣用表現が混じっていても、という逆向きの条件になる。",
 "全体 ── 映画の全体。くだけた台詞の一語一語が辞書どおりでなくても、誰が何を言い、何が起きているかを、作品の全体として追う。",
 "",
 "言葉の但し書きが裏返る段。B2の「標準語か馴染みのある方言であれば」（No.88）が、C1で「俗語や慣用表現を使っていても」へ形を変える。層は全体のまま、作り物の線が大半の映画から、くだけた言葉の映画へ進む。「録音と放送を聞く」の章の最上段（No.69）が一部に非標準的な語法を含む放送を聞く段で、同じ裏返りの形をしている。この一文は、質のものさしの側（社会言語的適切さ、No.1230）にも同じ文で載っている。",
),
84: (
 ["Interviewer: [picture: a studio; an economist; a chart of interest rates] You’ve argued the rate rise was a mistake. … Economist: Not the rise itself — the timing. Inflation was already turning; the figures come two months late, so the bank was tightening into a slowing economy it couldn’t yet see. … Interviewer: Its critics would say it had no choice. … Economist: It had a choice: wait one quarter. The cost of waiting was small; the cost of being wrong the other way, as we now see, was not.\nYou: （誤りは利上げそのものでなく時期であり、指標の遅れのために減速の中で引き締めた、待つ費用は小さく逆の誤りの費用は大きかった、と論の細部まで分かる。）",
  "Host: [picture: a discussion programme; three guests] Guest 1: The problem with the housing target is that it counts homes, not where they are. Build them where there are no jobs and you’ve met the target and solved nothing. … Guest 2: Then you’re arguing for building in the cities, where the land is dearest and the objections loudest. … Guest 1: I’m arguing for counting the right thing. Count homes within reach of work, and the target changes where you build.\nYou: （目標は戸数でなく場所を数えるべきだという主張と、それは都市での建設を意味するという切り返し、数え方を変えれば場所が変わるという再反論、と論の運びが細部まで分かる。）"],
 "時事番組、インタビュー、討論番組、トーク番組のような、難度の高いテレビ放送。専門家や論客が、抽象的で込み入った論を、切り返しと再反論を交えて展開する。但し書きはない。",
 "全体 ── 放送で提示される論の細部。要点の骨だけでなく、どこを区別し、何を認めて何を認めないか、という論の運びの細かな点まで一つの像として受け取る。",
 "",
 "議論の要点（No.86）から、論の細部へ。層は要点から全体へ上がり、見るものが時事の議論から難度の高い放送へ。条件なしは同じで、上端のC1三段のうち、但し書きをどちらの向きにも持たないのはこの段である。「聴衆として聞く」の章のC1（No.35）が、大半の講演や討論を比較的たやすく追う段で、向こうは聴衆の席から、こちらは番組の中の応酬を画面越しに追う。",
),
85: (
 ["Play: [picture: a kitchen; a mother and her grown-up son, who has just said he is moving abroad] Mother: Well. … That’s a long way. … Son: It’s a good job, Mum. … Mother: I’m sure it is. … [picture: she goes back to washing the plates] … You’ll want to take the good coat.\nYou: （「遠いのね」「いいお仕事でしょうとも」の短さと、皿洗いに戻る間とコートの一言に、賛成も反対も言わないまま寂しさが込められている、と分かる。）",
  "Host: [picture: a chat show; a sofa; a guest] So, the hotel. How was it? … Guest: Oh, it had character. … Host: That bad? … Guest: The shower was … an experience. … Host: And the breakfast? … Guest: We went out for breakfast.\nYou: （「個性があった」「経験になった」「外で食べた」という控えめな言い方が、ひどかったという強い評価を言っている、と分かる。）"],
 "大半の映画、演劇、テレビ番組。台詞やトークの受け答えの中に、言われていないことが込められている素材で、標準語または馴染みのある地域の方言やアクセントで伝えられていれば、という言葉の但し書きが残る。",
 "含意 ── ニュアンスと含み。言葉に出された意味の先で、短い返事の間や、控えめな言い回しに込められた気持ちや評価を読み取る。この章の最上段で、梯子はここで言外へ出て終わる。",
 "評価を控えめに言う型 ── 弱い肯定で強い賛辞を、軽い言い回しで強い不満を言う型 ── を知らずに、言葉どおりの弱い評価として聞いてしまい、台詞に込められた含みを取り損ねる。",
 "条件の列の終わり。同じC1に、俗語の映画（No.83）、難度の高い放送（No.84）と並んで、標準語か馴染みのある方言という但し書きつきで、言外へ出る段が立つ ── 上端の三段は、但し書きの向きで三つに割れる。層は全体から含意へ。作り物の線（93→90→88→83）はここで言外に合流する。この尺度にC2の段はない。「録音と放送を聞く」の章の最上段（No.69）が言われていないことまで含む細かな点で、「他人どうしの会話を聞く」の章の最上段（No.17）が言葉づかいの社会文化的な含意で閉じるのに対し、こちらは映画・演劇・テレビ番組の言葉に込められた含みで閉じる。",
),
}

DISCUSSION = [
    # 1 梯子
    "この尺度14行の条件句を並べると一本の列になる ── 映像の支え（視覚情報と既有知識・視覚情報と一般知識・映像が解説を補う・映像が理解を大いに助ける・映像と動きが筋を担う：No.96/95/92/93/90）→ ニュースの型（事実を伝えるテレビニュース：No.94）→ ゆっくり（比較的ゆっくり明瞭に：No.91/89）→ 標準語か馴染みのある方言（No.88/85）→ 条件なし（No.87/86/84）→ 逆境（かなりの俗語や慣用表現を使っていても：No.83）。他の聞く側の章と違うのは但し書きの担い手で、最初の五段では画面が理解を担う ── 相手に頼むものでも（「相手の話を聞く」の章）、自分で選ぶものでもなく（「録音と放送を聞く」の章）、素材が映しているものである。No.94に映像の但し書きがないのは、事実を伝えるニュースが項目ごとに進み画面が変わると話題が変わる型を持つからで、その型が次に来るものを予告する。速さの但し書きはB1（91）とB1+（89）の二段に残り、B1+に残るのは聞く側の全章でこの章だけである（「聴衆として聞く」の章のNo.45、「録音と放送を聞く」の章のNo.73・74はB1まで）。上端のC1は三段が三つの顔に割れる ── 俗語でも（83）、難度の高い放送（84＝但し書きなし）、標準語か馴染みのある方言で（85）。深さは七層で引く ── 知っている言葉（95）・筋（96/94/93/90）・要点（92/91/86）・全体（89/87/88/83/84）・含意（85）。一つの項目の段と立場の段がない。層は二つの線をなす。番組の線（ニュースと時事番組から、身近な話題の番組、インタビューと講演、討論まで）は、見出しの語（95）から項目の移り（94）、要点（92・91）、大部分（89・87）を経て、議論の要点（86）と論の細部（84）へ。作り物の線は、コマーシャルと予告編の話題（93）から映画の筋（90）、演劇と大半の映画（88）、俗語の映画（83）を経て、含み（85）へ出る。ドキュメンタリー・生インタビュー・トークショーと演劇・映画を一段に持つ88は二つの線にまたがる。B2+の要点（86）がB2の全体（87・88）の上に立つのは層の戻りではなく、分かったものから論の骨を取り出すという別の求めである。この尺度にC2の段はなく、Pre-A1の段がある。",
    # 2 CEFRの企図
    "CEFR増補版は、受容を三つの種類に分けている ── 口頭受容（生か録音かを問わず他者が産出した入力を受け取る）、視覚受容（書かれたテクストと手話のテクストを読む）、そして視聴覚理解。視聴覚理解の尺度はこの一つで、テレビ・動画・映画を見てマルチメディアを使う営みとされ、字幕・吹き替え・手話の有無を問わない（第3章 p.47）。なぜ聞く側や読む側と別に立てるかは増補版に書かれていない ── 2001年版の「聴覚入力と視覚入力を同時に受け取る活動」（読み上げを目で追う・字幕つきの視聴・マルチメディア）という定義を継いだままである。尺度の鍵概念は三つで、話題の切り替わりを追い要点を特定すること、細部・ニュアンス・含意を特定すること（C級）、伝え方（ゆっくり明瞭な標準語から、俗語と慣用表現を扱えるまで）である（p.52）。つまりCEFRが自分で立てた軸は深さと伝え方の二本で、映像が理解を担う度合いは鍵概念に入っていない。にもかかわらず、2001年版の母体8件（92・94／90・91・89／87・88／83）に増補版が足した6件（96・95・93・86・84・85）のうち、下端の三つ（96・95・93）はすべて映像の支えを但し書きに持つ ── CEFRは伝え方の但し書きで尺度を組み、映像の支えは下端を伸ばすために足した。本書が最初の五段を映像の支えの段として読むのは本書の読みで、『受容の課題』§4の「絵・写真・図」が層1・2を飛ばして層3を与える手加減の、動く形である。「録音と放送を聞く」の章との境は、CEFRが明言している ── 映像を伴わない放送と録音が向こう、映像を伴うものがこちら。鍵概念の違いは上端に出る ── 向こうは話し手の気分・態度・視点、こちらはニュアンスと含意である。",
    # 3 他の章との関係
    "聞く側のほかの章とは、同じ級に裏面を持ちながら、文言を共有しない。「録音と放送を聞く」の章とは素材が重なる ── ニュース（73↔87）、コマーシャル（75↔93）、ドキュメンタリー（71↔88）、物語（79↔90）── が、向こうは音だけで、こちらは画面が理解を担う。B1の要点の段はどちらも「比較的ゆっくり明瞭」の但し書きつきで、向こうはニュース（73）、こちらは身近な話題の番組（91）である。最上段の裏返りも同じ形で、向こうは非標準的な語法を含む放送（69）、こちらは俗語の映画（83）。言葉の但し書き（標準語か馴染みのある方言）は聞く側のB2に五つ並ぶ ── 「聴衆として聞く」の章（39）、「告知と指示を聞く」の章（54）、「他人どうしの会話を聞く」の章（22）、「相手の話を聞く」の章（415）、この章（88）。「録音と放送を聞く」の章のB2（71）だけは標準語のみである。再スキャン（母集団36枚411行）で閾値内の対は0件で、最近傍は85/54（0.67、「告知と指示を聞く」の章のB2＝標準語か馴染みのある方言の但し書きの共有）と91/73（0.58）で、いずれも対でない。読む側に対はなく（映像のある素材は文字にない）、語る側では「経験を語る」の章のB1（No.244＝本や映画の筋を語る）と「創作の文章」の章のB1+・B2・C1（No.334・332・329＝映画やテレビ番組の批評を書く）が、この章で見た作品を語り書く側に当たるが、見ることと語ることは別の課題で、対としては採らない。橋渡しの側では、テレビ番組や動画の要点を別の言語で伝える段（No.828・829）が第4部にある。対の台帳のうち、聞く↔読むの器（系「受容」）はこの章に席がなく、受容内の再掲対にもこの章の行は入らない。質のものさしの側では、社会言語的適切さの軸（No.1230）がNo.83と同じ一文を載せている ── 行為の段とものさしの一文の全文一致10組の一つで、帳簿への収載は導出ビルドの時に裁定する。",
    # 4 落とし穴
    "日本語話者の落とし穴は四つの段に立つ。知っている言葉の段（95）では、商品名や土地の名前をカタカナの音形で待つこと。時事番組の大半（87）では、議会や保険や住宅のような制度を日本の同じ名前の制度の像で見ること。議論の要点（86）では、結論は最後に来るものと待って、立場を先に言う発言の論拠から立場を組み立て直そうとするうちに次の発言者に移ること。含み（85）では、評価を控えめに言う型を知らず、言葉どおりの弱い評価として聞くこと。穴のない段は十 ── 画面から主題を見当づける段（96）には言葉の型の持ち込みがない。事件・事故のニュースの要点（92）と映像と動きが筋を担う映画（90）では、画面が要点と筋を与えていて、聞き取りの構えがどうであれ画面の分は理解に立つ ── 音だけの録音で一項目を待ち構えられない形（「録音と放送を聞く」の章のNo.80）は、画面のある段では起きない。ニュースが項目ごとに進む型（94）は日本語の視聴者も慣れている。コマーシャルと予告編の型（93）について日本語話者が外す形は指せない。身近な話題と個人的関心（91・89）は条件が内容の知識を与え、速さの但し書きが構えを支える。演劇と大半の映画（88）には87と同じ持ち込み以外の要因がなく、標準語の但し書きは言葉の側の支えで内容の持ち込みを変えない。俗語と慣用表現（83）は言葉の聞き取りの負荷であって含みの穴ではない。論の細部（84）には86と同じ型の持ち込み以外に指せる形がない。",
    # 5 何がこの梯子を測るか
    "この梯子を測るものさしは、ほかの聞く側の章と同じく、但し書きの数と向き、そして層である。ただしこの章では、但し書きの担い手が画面にある。「相手の話を聞く」の章の但し書きは相手に頼むもので、「録音と放送を聞く」の章の但し書きは自分で選ぶものだった。この章の最初の五段の但し書きは、素材が映しているもの ── 川があふれた画面、横倒しのバス、犬を拾う少年 ── で、言葉が聞き取れなくても場面が立つ。だからこの尺度には、言葉を一つも要らない起点（96）がある ── 聞く側の章の起点はどれも、聞こえた言葉を聞き取るところから立つ。画面の支えが外れると（B1の91から）、残る但し書きは聞く側の章と同じ三つ ── 速さ、言葉、そして条件なしと裏返り ── だが、速さがB1+まで残るのはこの章だけで、テレビが視聴者に向けて速さを抑えて作られる素材を持つからである。上端は含み（85）で閉じる ── 「聴衆として聞く」の章が一人の話し手の含みと冗談で、「他人どうしの会話を聞く」の章が言葉づかいの含意で、「録音と放送を聞く」の章が放送を通した社会の言葉と人の関係で閉じるのに対して、この章は映画・演劇・テレビ番組の言葉に込められた含みで閉じる。CEFRがこの尺度の鍵概念に立てた「細部・ニュアンス・含意」は、本書の読みでは二つの線の上端に分かれて現れる ── 細部は番組の線の上端（84）に、ニュアンスと含意は作り物の線の上端（85）に。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 14
    for name, m in (("CONDITION", CONDITION), ("DEPTH", DEPTH)):
        tagged = [n for v in m.values() for n in v]
        assert sorted(tagged) == sorted(ORDER), f"{name}が完全分割でない"
    assert list(DEPTH.keys()) == SEVEN_LAYERS, "DEPTHの語彙が七層でない"
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    arc = ["映像の支え", "ニュースの型", "ゆっくり", "標準語か馴染みのある方言", "条件なし", "逆境"]
    assert list(CONDITION.keys()) == arc
    prev_min = -1
    for c in arc:
        lv = sorted(order_lv.index(desc[str(n)]["level"]) for n in CONDITION[c])
        assert lv[0] >= prev_min, f"条件の列が級順でない: {c}"
        prev_min = lv[0]
    assert "C2" not in {desc[str(n)]["level"] for n in ORDER}, "このスケールにC2はない"
    assert "Pre-A1" in {desc[str(n)]["level"] for n in ORDER}, "このスケールにPre-A1がある"
    for no, (ex, scene, hw, l1, delta) in R.items():
        assert not hw.startswith("形 ──") and not hw.startswith("命題 ──"), f"分かることの頭に裸の層名 No.{no}"
        for f in (scene, hw, l1, delta):
            assert "が取れる" not in f and not re.search(r"(態度|気分|視点|関係|好悪|立場|含意)を取", f), f"退役語形「〜が取れる」「態度などを取る」 No.{no}"
            assert "やり取り" not in f, f"四欄に「やり取り」（平仮名へ、判断(cf)） No.{no}"
        for e in ex:
            assert "[picture:" in e or no not in CONDITION["映像の支え"], f"映像の支えの段の例に画面がない No.{no}"
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
        "title": "テレビ・映画・動画を見る（Watching TV, film and video）── 第3柱量産第五号・全数シート",
        "scope": "全数（14件。見る14 ── mode一様。C2なし、Pre-A1あり）",
        "type": "第3柱（受容）。梯子＝条件の解除の一本（映像の支え→ニュースの型→ゆっくり→標準語か馴染みのある方言→条件なし→逆境）、深さ＝七層（『受容の課題』§2）は段の属性。糸は立てない。四欄（scene＝見るもの・howwell＝分かること・l1・delta）は書物の本文そのもの（判断(bs)）。",
        "essence": "テレビ・映画・動画を見る段は、但し書きの担い手が画面にある ── 相手に頼むのでも自分で選ぶのでもなく、素材が映しているものが理解を担い、言葉を一つも要らない起点から梯子が立つ。画面の支えが外れたあとは聞く側と同じ三つの但し書き（速さ・言葉・条件なしと裏返り）だが、速さがB1+まで残り、上端のC1は三段が三つの顔（俗語でも・但し書きなし・標準語で）に割れる。層は番組の線（知っている言葉→項目の移り→要点→全体→議論の要点→論の細部）と作り物の線（話題→筋→全体→俗語の映画→含み）の二線で、含みで閉じる。",
        "axes": {"条件": CONDITION, "深さ": DEPTH},
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p3_tv.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
    print("落とし穴欄:", sum(1 for r in sheet["rows"] if r["l1"]), "/ 空欄:", [r["no"] for r in sheet["rows"] if not r["l1"]])
