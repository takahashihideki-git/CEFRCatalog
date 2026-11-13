#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第4柱（仲介）第一号範型：Processing text in speech or sign 28件の全数シート（CEFRカタログ46、判断(cs)）。

第4部の器（判断(cs)）＝前提文書を立てず、渡す側を英語に固定して立てる（受けるものは同一言語内を標準。判断(cs)②・(cx)、原典p.92・p.250）。
段＝第3部の入力（条件）×第2部の出力（組み立て）×関係（誰に、何を、どんな形で渡すか）。
- シート＝スケール（mode一様＝「口頭」）。章名「テキストをまとめて伝える（口頭）」（p4_inventory の章〔仮〕）
- 列10は不変。第4柱での読み替え：
    exponents … 一要素＝二行以上。入力のラベル（Notice / Leaflet / Radio news / Article / Colleague A / Podcast / Meeting …）に続けて
                 英語の入力（聞く・読むもの）、最後に You (to …): と、渡す相手を括弧に入れて、英語で渡した言葉そのもの。
                 第3部の「You:（分かったしるし）」の丸括弧の行動描写は、第4部では渡した言葉に置き換わる（分かったしるし＝出力）。
                 長い入力（講演・報告書・映画）は「…」で略し、渡した言葉だけを全文で示す。例文は l1 の欄を演じるように作る（欄→例文の順）。
    scene     … 「受けるもの」＝入力のテキストか場と、その条件（記述文の条件句＝入力の側の手加減。何度も聞ける・意味を確かめられる、も含む）
    howwell   … 「渡すもの」＝誰に、どの層の中身（『受容の課題』の七層）を、どんな形で（伝える・要約する・統合する・説明する）渡すか
    l1        … 「日本語話者の落とし穴」＝出力に現れる失敗だけ（入力側で外すことは第3部の対の段が書いている ── 判断(cs)⑤）。
                 判定は執筆要綱・規律6-1の産出版（定型句・語・文法・文章や話の型の四水準で日本語の元の形を添えられ、その形をそのまま英語にした
                 誤形が例文と対照して示せる）。本シートの7欄＝830 名詞の並べ（文にならない）／824 経緯から結論への順序（要点が最後）／
                 826 文ごとの伝聞の印／820 あらすじの過去形／816 両論併記の締め／818「言っている」一語／812 推量の形で留める。
                 空欄21＝出力の側に日本語の形で指せる失敗が立たない段（欄ごと省く）
    delta     … 前の段から。受容の側（第3部）・産出の側（第2部）との対は散文で先に記録（判断(ai)③）。収載は範型二枚のあと一括
- **四欄（scene・howwell・l1・delta）は書物の本文として書く**（読者語彙。帳簿語＝仲介・受容・区分名は出さない。判断(bs)と同じ）
- 梯子＝入力の側の条件の解除の一本（CONDITION、完全分割、語彙はスケールごと、区分は級順）：
  支え（絵・表・簡単な言葉・ゆっくり）→ 身近な主題と明瞭な構成 → 何度も聞ける・意味を確かめられる → 短い素材 → 関心分野 → 条件なし → 専門の内外 → 逆境
- 深さ＝渡す中身の七層（DEPTH、完全分割、語彙は七層で固定＝正準は『受容の課題』§2）：命題2・筋1・要点13・全体8・立場2・含意2（形なし）
- 作業訳の「（A言語）」「（B言語で）」は帳簿では保全し、書物の「できること」への転写で括弧を外す規則は範型章の便で（判断(cs)留保）
- 語彙裁定（判断(s)）：例文は入力の英語と、You 行の英語を照合対象とする。ラベルと括弧の相手は照合外。
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Processing text in speech or sign"
ACT = "テキストをまとめて伝える（口頭）（第4柱：Processing text in speech or sign）"
MODE = "口頭"

SEVEN_LAYERS = ["形", "命題", "筋", "要点", "全体", "含意", "立場"]

# レベル順→No昇順（表示順の正準）
ORDER = [833, 832, 829, 830, 831, 824, 825, 826, 827, 828, 821, 822, 823,
         815, 816, 817, 818, 819, 820, 813, 814, 807, 808, 809, 810, 811, 812, 806]

CONDITION = {
    "支え":                 [833, 832, 829, 830, 831],   # 短くごく簡単な表示／構成のはっきりした短く簡単なテキスト（身振りで補ってよい）／ゆっくり明瞭な簡単なニュース／挿絵や表／簡単で短い情報テキスト
    "身近な主題と明瞭な構成": [824, 825, 826],             # 明確でよく構成された／率直な／人々が明瞭に話せば
    "何度も聞ける・確かめられる": [827, 828, 821],         # 何度か聞ける・見られる／特定の表現の意味を確かめられる
    "短い素材":             [822, 823],                  # 短い物語・記事・講演…／複数の出どころの短い情報
    "関心分野":             [817, 818, 813],             # 自分の関心分野・専門分野に関わる主題
    "条件なし":             [815, 816, 819, 820, 814, 807, 810, 811],
    "専門の内外":           [808, 809, 812],             # 自分の能力の範囲内／専門外（専門概念を確かめてよい）／専門的な話題
    "逆境":                 [806],                       # つながりや含意が明示されていない
}
DEPTH = {
    "形":   [],
    "命題": [833, 830],
    "筋":   [820],
    "要点": [832, 829, 831, 824, 825, 826, 827, 828, 821, 822, 823, 817, 819],
    "全体": [815, 816, 813, 814, 807, 808, 809, 811],
    "含意": [810, 806],
    "立場": [818, 812],
}

R = {  # no -> (exponents, scene=受けるもの, howwell=渡すもの, l1=落とし穴, delta=前の段から)
833: (
 ["Notice (on the shop door): Closed on Monday.\nYou (to a friend): It's closed on Monday. We can come on Tuesday."],
 "店のドアの掲示、ポスター、催しのプログラムのような、短くごく簡単な表示。書かれていることは簡単で、見当のつくもの（開く時間、休みの日、値段、場所）。",
 "一つの項目 ── 掲示が言っている一つのことを、その場にいる相手に一言で伝える。訳して聞かせるのではなく、相手がすぐ使える形（だから次にどうするか）にして渡す。",
 "",
 "この章の起点。渡す言葉は、やりとりする言葉のA1の段と変わらない短い一文で、違うのは言葉の出どころが自分でなく掲示にあること。「探して読む」の章の最初の段（No.145・141）で自分のために読めるものを、ここでは隣にいる人に向けて声にする。",
),
832: (
 ["Leaflet (from the council): Recycling day is Thursday. Put paper in the blue bag and glass in the green box. Leave them outside by 7 a.m.\nYou (to a new neighbour, pointing at the bags): Thursday — recycling. Paper, blue bag. Glass… this green box. Outside, before seven."],
 "町内のちらしや掲示物のような、短く簡単で、見出しや番号で構成のはっきりしたテキスト。自分の持っている言葉が足りないところは、身振り、絵、指さし、他の言語の語で補ってよい。",
 "要点 ── テキストの言いたいことの中心を相手に渡す。全部を言い直すのではなく、相手が知るべき点だけを、言葉の足りないところは身振りで補いながら。",
 "",
 "一つの項目（No.833）から要点へ。入力は一枚の紙の中に構成を持ち、渡すものは一言から要点へ上がる。言葉の不足を身振りや絵で補ってよいとCan-Do記述文自身が書くのはこの章ではこの段だけで、やりとりする言葉のA2が相手の助けで文を作るのと同じ手加減が、渡す側にも書き込まれている。",
),
829: (
 ["Radio news: A tree fell on the main road early this morning. The road is closed until this evening. Buses are using Park Street.\nYou (to your host family): The main road is closed today — a tree fell on it. The buses are going along Park Street."],
 "出来事・スポーツ・事故を報じる簡単なテレビやラジオのニュース。話題が身近で、ゆっくりはっきり読まれていること。",
 "要点 ── ニュースの要点を、聞いていなかった相手に報告する。何が起きて、いまどうなっているか。誰の意見かは問われず、事実の中心だけでよい。",
 "",
 "入力が紙から放送へ。読み返せない音声の要点をつかんで渡す段で、「テレビ・映画・動画を見る」の章のA2（No.94＝ニュースの話題の切り替わりを追い、主な内容の見当をつける）の一級上に、同じニュースの要点を人に報告する段として立つ。向こうが見当で足りるのに対し、こちらは要点を取って言わなければならない。",
),
830: (
 ["Poster (at the pool): Opening hours — Mon–Fri 7:00–21:00, Sat 9:00–18:00, Sun closed. Adults £4, children £2.\nYou (to a colleague): The pool opens at seven on weekdays and at nine on Saturday. It's closed on Sunday. It's four pounds for adults and two for children."],
 "挿絵や表のついた、短く簡単で構成のはっきりしたテキスト。時間割、料金表、案内図のように、情報が表の形で並んでいる。",
 "一つの項目 ── 表の中の情報を、簡単な文にして渡す。表は読めても文にはなっていないので、項目を主語と動詞のある文に起こすのがこの段の仕事。",
 "表の項目を、日本語では「大人四ポンド」「日曜休み」と名詞を並べるだけで文として通じるため、英語でも名詞を並べて渡してしまい（*Adult four pounds. Sunday close.*）、簡単な文で報告するという段の課題そのものが果たされない。英語では *It's four pounds for adults* / *It's closed on Sunday* と、主語と動詞のある文になる。",
 "要点（No.829）から一つの項目へ戻る。渡す中身は簡単だが、表の項目を文にする仕事が新しい。同じ表を自分のために読む段は「探して読む」の章（No.146・143）にあり、向こうは読めればよく、こちらは文にして言わなければならない。",
),
831: (
 ["School newsletter: Sports Day is on 12 June. Parents are welcome. Please bring water and a hat for your child. The day ends at 3 p.m.\nYou (to another parent): Sports Day is on the twelfth. Parents can come. They need water and a hat, and it finishes at three."],
 "たとえば、学校から来た運動会のお知らせ、職場の回覧、町の広報の一項目。身近な話題で、簡単で短い。身振りや指さしの助けはなく、言葉だけで渡す。",
 "要点 ── テキストを、言葉だけで要約して渡す。短いテキストでも、全部ではなく相手が必要とする点を選んで並べ直す。",
 "",
 "身振りや絵で補いながら伝える（No.832）から、言葉だけで要約するへ。素材は同じように短く簡単な紙でも、渡し手の杖が外れ、要点が全部言葉で立つ。Can-Do記述文の動詞が summarise になる最初の段で、以後C1まで同じ動詞が続く。何を落とすかを渡す側が決める、という仕事がここから始まる。",
),
824: (
 ["Article (company intranet): From next month, staff can work from home two days a week. Managers will agree the days with each team. The office will stay open every day, and meeting rooms must be booked online.\nYou (to a colleague who missed it): The main thing is, from next month we can work from home two days a week. Our manager decides the days with us. The office stays open, and we have to book meeting rooms online."],
 "身近な主題か、個人的な関心のある主題の、明確でよく構成されたテキスト。段落と見出しがあり、何が言いたいかが読み取りやすい。語彙が足りずに言い回しに詰まることはあってよい。",
 "要点 ── テキストを要約して、読んでいない相手に渡す。要点を先に言い、細部はそのあとに。言葉に詰まっても、要点が落ちなければよい。",
 "日本語の説明は「〜で、〜なので、〜になります」と経緯から結論へ流れる順序が自然なので、英語の要約も前置きと経緯から始めて、要点が最後に来る（*Next month the company has a new policy, and the managers talked about it, and…*）。英語の要約では要点（*we can work from home two days a week*）が最初の文に来て、細部はそのあとに続く。",
 "条件が「簡単な言葉」から「明確でよく構成された」へ移る。入力の簡単さが外れ、読み手にとっての読みやすさ（構成）が条件になる。「知るために読む」の章のB1（No.158・159）で自分のために読めるものを、ここでは要約して渡す。",
),
825: (
 ["Travel brochure: Lakeview is a small town two hours from the city. In summer you can swim in the lake, hire a boat or walk in the hills. Hotels are cheap in May and September.\nYou (to a friend planning a trip): Lakeview is two hours away. You can swim and walk, and it's cheaper in May or September."],
 "身近な主題の率直なテキスト ── 旅行パンフレット、雑誌の記事、インタビューの短い記録。",
 "要点 ── 主要な情報の中身を、簡単に要約して渡す。「簡単に」がCan-Do記述文に書かれていて、短い文で、相手の用事に必要となる情報だけで足りる。",
 "",
 "No.824と同じB1に立つ、簡単に要約する段。向こうが語彙の不足を但し書きに持つのに対して、こちらは「簡単に」を渡し方として持つ。同じパンフレットを自分のために読む段は「探して読む」の章（No.131・132）にある。",
),
826: (
 ["Anna (to Ben): So the meeting moves to Thursday?\nBen: Yes, two o'clock. And Sam wants the figures before then.\nAnna: Fine, I'll send them on Wednesday.\nYou (to a colleague who arrived late): They've moved the meeting to Thursday at two. Sam wants the figures first, and Anna is sending them on Wednesday."],
 "個人的または時事的な関心のある主題についての、他の人たちの会話。話し手がはっきり話していること。",
 "要点 ── 会話の要点をまとめて、その場にいなかった相手に渡す。誰が何を言ったかを全部再現するのではなく、何が決まり、何がまだかを。",
 "日本語では人から聞いたことを渡すとき、文ごとに「〜だそうです」「〜って言ってました」と伝聞の形を添えるのが自然なので、英語でも *It seems that the meeting is Thursday. It seems that Sam wants the figures.* と一文ごとに言い切りを弱めてしまう。英語の要約では出どころを一度言えば（*They've moved the meeting*）、あとは言い切りの文が並び、文ごとの伝聞の印は要らない。",
 "入力が書かれたものから、他人どうしの会話へ。「他人どうしの会話を聞く」の章の同じB1（No.25＝議論の要点を追う）と同じ場に立ち、向こうが自分のために要点を追うのに対して、こちらはそれを人に渡す。級が揃うのは、この章の段が受ける側の段に対して置かれる最も普通の形である。",
),
827: (
 ["Podcast (thirty minutes, on the history of the town): …\nYou (to your study group, after listening twice): It's mainly about why the old bridge was built — the river flooded every spring, so the town paid for a stone bridge in 1820. The second half is about who paid, and that's where the argument starts."],
 "関心分野の話題の、口頭で伝えられる長いテキスト（講演の録音、ポッドキャスト、長いインタビュー）。何度か聞き直せること。",
 "要点 ── 長い音声の要点を、聞き直しながら集めて報告する。一度で取れなくてよく、何が主で何が従かを、聞き直しで確かめる。",
 "",
 "入力が長くなり、聞き直しが但し書きとして入る。同じ素材を自分のために聞く段は「録音と放送を聞く」の章のB1（No.73・74）にあるが、向こうの但し書きは速さと明瞭さで、聞き直しは書かれていない。渡す側には聞き直しが与えられる ── 人に渡すことが、もう一度聞く理由を作る。",
),
828: (
 ["Video clip (a cooking show, five minutes): …\nYou (to a friend who asked what it was about): It shows how to make the sauce without cream — you use yoghurt and heat it slowly. The main point is not to let it boil."],
 "テレビ番組や動画クリップ。何度か見直せること。",
 "要点 ── 番組や動画の要点か、出来事の流れを要約して渡す。",
 "",
 "No.827と同じ条件（見直せる）の、映像つきの段。「テレビ・映画・動画を見る」の章のB1（No.91）が同じ番組の要点をつかむ段で、ここでも級が揃う。",
),
821: (
 ["Report (twelve pages, on cycling in the city): …\nYou (to a colleague): The report says cycling doubled in five years, mostly because of the new lanes. The problems are parking and accidents at two junctions. It recommends more bike parking before any more lanes."],
 "関心分野の長いテキスト。分からない表現の意味を確かめられること（辞書で引く、人に聞く）。",
 "要点 ── 長いテキストを要約する。長さが条件から外れる代わりに、表現を確かめる手加減が入る。",
 "",
 "聞き直し（No.827・828）が、読む側では意味の確かめに変わる。「知るために読む」の章のB1+（No.156＝論の主要な結論を見つける）で自分のために読めることを、ここでは要点として渡す。",
),
822: (
 ["Radio interview (eight minutes, with a night nurse): …\nYou (to your class): She's worked nights for ten years. She says the hardest part is sleeping in the daytime, not the work itself.\nClassmate: Does she want to change?\nYou: No — she says she'd miss her team."],
 "たとえば、ラジオで流れた八分のインタビュー、短い物語、雑誌の記事、短い講演や討論、短いドキュメンタリー。長さは一度で頭に入る程度で、渡したあとに相手から細部を聞かれる。",
 "要点 ── 要約して渡したあと、細部についての追加の質問に答える。渡す側が内容を手元に持ち続けていることが、質問への答えで示される。",
 "",
 "要約が一方向でなくなる。相手の問いが返ってきて、細部を答える。「事実情報の授受」の章の答える側が、ここでは自分の知っていることでなく、渡したテキストの細部について立つ。",
),
823: (
 ["Museum website: Open 10–5, closed Mondays.\nFriend's message: The café there is really good.\nBus timetable: Route 14, every 20 minutes.\nYou (to your parents, who are visiting): The museum's open ten to five, but not on Monday. We take the 14 — it runs every twenty minutes — and there's a good café inside."],
 "たとえば、博物館のサイトの開館時間、友だちからのメッセージ、バスの時刻表。複数の情報源に散った短い情報で、一つ一つは簡単だが、相手のためには一つに集めなければならない。",
 "要点 ── ばらばらの情報源から相手が必要とする情報を集め、その相手のために一つにまとめて渡す。情報源が複数になる最初の段。",
 "",
 "情報源が一つから複数へ。集めて要約するという、B2の統合（No.815）の小さな形がここに立つ。他の誰かのために（for somebody else）と、渡す相手がいることも、この段でCan-Do記述文に書かれる。",
),
815: (
 ["Three articles on the same strike: …\nYou (to your manager): All three agree it's about pay, not hours. Two of them say the union will settle by Friday; the third says the vote was closer than reported. So Friday is likely, but not certain."],
 "たとえば、同じストライキを報じた三紙の記事、同じ事故についての会社の発表と組合の声明と地元紙の記事。情報源ごとに事実の選び方と論点の立て方が違い、一致するところと食い違うところがある。",
 "全体 ── 複数の情報源の情報と論点を統合して報告する。並べるのではなく一つの像にする。どこで一致し、どこで食い違うかが、統合の中身。",
 "",
 "集める（No.823）から統合へ。情報源どうしの一致と食い違いを渡す段で、「報告と小論」の章の同じB2（No.360＝複数の情報源からの情報と論点を統合する）とは、「報告する」（*and report*）の二語を除けば同じ文である ── 書く側では統合が小論の組み立てとして、こちらでは人に渡す報告として立ち、違いはその二語に尽きる。",
),
816: (
 ["Two reviews of the same play: …\nYou (to your reading group): Both say the acting carries it. The first thinks the ending is a cop-out; the second reads it as the whole point of the play. I'm with the second — the play is about not getting answers."],
 "たとえば、同じ芝居についての二つの劇評、同じ小説を正反対に読んだ二人の書評、一つの政策をめぐる賛成と反対の論説。事実を扱うテキストも創作を扱うテキストも入り、見解が割れていて、主なテーマが読み取れる。",
 "全体 ── 要約しながら、対立する見解と主なテーマにコメントして論じる。渡すだけでなく、見解の対比を自分の言葉で論じる段。",
 "日本語の報告では、対立する見解を「どちらにも一理ある」「賛否両論ある」と並べて締めるのが礼にかなった形なので、英語でもコメントして論じるという段の課題が *Both have a point.* の一文で終わる。英語ではこの段で、対比を述べたあとに、どちらをなぜ取るかまでが求められる。",
 "要点（No.817・819）から全体へ。要約に自分のコメントが加わる最初の段 ── 人のテキストを渡す営みは自分の意味を表さないのが本来だが、CEFRはB2から、渡す側の評価を添えることを段に書き込む。",
),
817: (
 ["Article (long, on housing policy): …\nYou (to a colleague): The key points: rents have risen faster than wages for eight years; the government's plan is to build on public land; the critics say it's too slow. The author thinks the plan is right but the timetable isn't."],
 "たとえば、住宅政策について数ページにわたる解説記事、自分の関心のある分野（エネルギー、教育、医療）の時事問題を扱う長い特集。一読では追えない長さと、専門の語や抽象の語を含む複雑さがあり、主題は時事。",
 "要点 ── 長く複雑なテキストの重要な点を要約する。複雑さが条件から外れ、関心分野だけが残る。",
 "",
 "長さと複雑さが条件から消え、「関心分野」が残る。「知るために読む」の章のB2（No.151＝特定の立場が取られている記事や報告）で自分のために読めるものを、ここでは重要な点として渡す。",
),
818: (
 ["Opinion column (on homework): …\nYou (to a colleague): It's written for parents, not teachers. The writer's point is that homework should be optional, and she's quite scornful of the schools that refuse — she calls their reasons 'excuses'."],
 "たとえば、宿題の是非を論じる新聞のコラム、ある製品を薦める業界誌の記事、ある政策を批判するブログの投稿。関心のある話題で、読めば誰に向けて書かれたか（保護者か教師か、素人か専門家か）が分かり、著者が何を言いたいのかとどういう態度で言っているのかが読み取れる。",
 "立場 ── 著者が誰に向けて、何のために、どういう態度で書いたかを説明する。内容の要点ではなく、著者の立ち位置を渡す段。",
 "日本語では筆者の態度を「〜と言っている」「〜と書いてある」の一語で受けるのが普通なので、英語でも賛同も非難も皮肉も *The author says…* で渡してしまい、態度を説明するという段の課題が消える。英語では態度ごとに動詞が違い（*argues, admits, dismisses, warns, is scornful of*）、どの動詞を選ぶかがそのまま態度の説明になる。",
 "要点（No.817）から立場へ。同じB2の「聴衆として聞く」の章のNo.40（見解と事実の区別）と「知るために読む」の章のNo.152（事実の提供と説得の区別）が自分のために区別する段で、ここではその区別を著者の態度として人に説明する。",
),
819: (
 ["TV interview (a politician on transport): …\nYou (to a friend): She wants to cut bus fares and says the money will come from parking charges. The interviewer kept asking where the rest comes from, and she didn't really answer."],
 "たとえば、政治家が交通政策を語るテレビのインタビュー、賛否が割れる問題を扱ったニュース特集の一部、専門家が論じるドキュメンタリーの抜粋。事実の報道でなく、誰かの意見と、その根拠と、それへの反論が含まれる。",
 "要点 ── 意見と論拠を含む抜粋を要約する。誰が何を主張し、根拠は何かを、渡す側で分けて渡す。",
 "",
 "入力が事実のニュース（No.829）から、意見と議論を含む放送へ。「テレビ・映画・動画を見る」の章のB2+（No.86＝議論番組から要点を取り出す）の要点の取り方に当たり、こちらが一級下に立つ。",
),
820: (
 ["Film (two hours): …\nYou (to a friend): It's about a nurse who finds a letter in a dead patient's coat. She tracks down the daughter, who doesn't want to know. In the end she reads it to her anyway, and the daughter walks out — but she comes back for the funeral."],
 "たとえば、二時間の映画、一晩の芝居。筋があり、出来事が順に起き、ある出来事が次の出来事を引き起こす。",
 "筋 ── 映画や演劇の筋と出来事の流れを要約する。この章で筋を渡す段はここだけで、中身は出来事の順序と、何が何を引き起こしたか。",
 "日本語ではあらすじを「看護師が手紙を見つけた。娘を探した」と過去の形で語るのが自然なので、英語でも *A nurse found a letter and looked for the daughter* と過去形で語ってしまう。英語の筋の要約は現在形で語るのが普通で（*A nurse finds a letter. She tracks down the daughter*）、過去形で語ると、作品の中の出来事ではなく自分の体験の報告に聞こえる。",
 "要点の段のあいだに一つだけ立つ、筋の段。「経験を語る」の章のB1（No.247＝物語を語れる）が語る側の裏面で、向こうは自分の物語、こちらは他人の作った物語を渡す。筋を自分のために追う段は「テレビ・映画・動画を見る」の章（No.93・90・88）にある。",
),
813: (
 ["Report (forty pages, in your own field): …\nYou (to a visiting colleague, in ten minutes): There are three things in it. First, the problem: our current sensors drift after about six months, and nobody knew why. Second, what they tested: three mounting designs, over a full year, in real conditions. Third, the result: the drift comes from heat, not vibration, so the fix is cheap. That last point is why it matters for us."],
 "たとえば、自分の分野の四十ページの報告書、学会誌の長い論文、業界の白書。主題は関心分野や専門分野に関わる幅広いもので、専門の語と込み入った論の運びを持ち、戻りながらでなければ読めない。",
 "全体 ── 情報と論点を、よく構成された言葉で明快に要約する。渡す側の言葉の構成がCan-Do記述文に書き込まれる最初の段 ── 要約そのものが、一つのまとまった話になる。",
 "",
 "要約の言葉の質（明快さ、構成）が段の条件に入る。「報告と小論」の章のB2+（No.356＝要点の強調と裏づけの詳細）と同じ組み立てが、ここでは他人の論に対して求められる。",
),
814: (
 ["Meeting (one hour, on moving the office): …\nYou (to a colleague who was away): Finance wants to move because of the rent; sales wants to stay because of the clients. The compromise on the table is a smaller office in the same area. Nobody argued for staying as we are — that's the main thing."],
 "たとえば、オフィスの移転をめぐる一時間の会議、三つの部署が別々の理由で別々の案を推す討論。発言者が多く、見解が三つ以上に割れ、互いに部分的に重なる。",
 "全体 ── 複雑な議論の要点を、異なる見解を比較検討しながらまとめる。誰がどちら側かではなく、見解どうしの重さを量って渡す。",
 "",
 "会話の要約（No.826）が、複雑な議論の比較検討になる。「他人どうしの会話を聞く」の章のB2（No.22＝賛否の理由を振り分ける）の一級上に、振り分けた理由を量って人に渡す段として立つ。",
),
807: (
 ["Book chapter (dense, forty pages, on the history of money): …\nYou (to a seminar group): The chapter argues that money did not grow out of barter — that story is a myth. It began as debt: records of who owed what to whom, kept by temples and palaces. Coins came much later, and mainly to pay soldiers. So the author's point is that credit is older than cash, and the book builds on that for the rest of its argument."],
 "たとえば、本の一章、数十ページの研究報告、専門誌の総説。長さは一度に読み切れず何度かに分けて戻りながら読むほどで、難しさは専門の用語、抽象の語、入り組んだ論の運び、暗示に留められた含みから来る。CEFRは長さと難しさを量では定めず、この段ではその二つが但し書きとして負荷の側に立つ。",
 "全体 ── 長く難しいテキストを要約する。手加減の但し書きが一つもなく、長さと難しさという負荷だけが書かれる段。",
 "",
 "手加減の条件が消え、但し書きが負荷の向きに変わる。「知るために読む」の章のC1（No.148＝長く複雑なテキストを細部まで）と「聴衆として聞く」の章のC1（No.35）が自分のために分かる段で、こちらはそれを要約して渡す。",
),
808: (
 ["Panel discussion (in your own field, one hour): …\nYou (to colleagues afterwards): Two of the three speakers want the new standard adopted now; the third wants to wait for the next revision. The case for waiting is actually stronger than it sounded — she pointed out that two of the test methods are about to change. The most important point, though, came from the floor: nobody has costed the transition. That is what we should take back to the team."],
 "たとえば、自分の分野の学会のパネル討論、職場の専門会議での一時間の議論。登壇者が複数いて見解が割れ、自分には内容が分かる事柄で、聞きながら最も重要な点がどれかを見分けられる。",
 "全体 ── 議論を要約しながら、異なる見解を敷衍し、比較検討し、最も重要な点を特定する。言われなかったところを補って広げる（敷衍）が加わる。",
 "",
 "No.814の一級上。比較検討に、敷衍と最重要点の特定が加わる。「他人どうしの会話を聞く」の章のC1（No.18＝複雑な議論を容易に追う）が自分のために追う段。",
),
809: (
 ["Article (economics, in a field that is not yours): …\nYou (to a colleague, after checking two terms): The main point is that the central bank is holding interest rates because it thinks inflation has settled. The critics say the job market is still too tight and that waiting risks a second rise in prices. The author sides with the critics, but admits the data could go either way."],
 "たとえば、経済学の記事を工学の人が、医学の論文を法律の人が読む。自分の専門外の分野の、複雑なテキストで、専門の概念は時折辞書や人に確かめてよい。",
 "全体 ── 専門外の要点を、よく構成された言葉で明快にまとめる。",
 "",
 "専門の内外が、最後の但し書きになる。「知るために読む」の章のC2（No.147＝専門外の複雑な報告の細部と含意）の一級下に、専門外のテキストを明快に渡す段として立つ。",
),
810: (
 ["Two reports on the same figures: …\nYou (to a colleague): The numbers are the same, but the first puts the fall in the headline and treats the recovery as a footnote; the second does the opposite. Neither is wrong — they've chosen what to foreground."],
 "たとえば、同じ売上の数字を載せた二つの報告、同じ事故を伝える二つの記事、同じ調査結果を引く賛成側と反対側の論説。事実も論拠も同じなのに、何を見出しに置き、何を注に回し、何を言い切り何を留保するかが違う。",
 "含意 ── 事実と論拠がどう提示されているかの微妙な区別を説明する。中身ではなく、提示の仕方（何を前に出し、何を控えめにし、何を事実として言うか）を渡す。",
 "",
 "全体から含意へ。No.818（著者の目的と態度）の先に、提示の仕方そのものを説明する段。",
),
811: (
 ["Essay (complex, on urban planning): …\nYou (to the group, in a discussion): The author's strongest point is that cities fail when they separate where people live from where they work — and I think he's right about that. Where I'd part company is his answer: he wants to ban new office districts, but the problem he describes is really about transport, not zoning."],
 "たとえば、都市計画についての長い論考、一つの問題を多面的に論じた評論。情報と論点が複雑に組まれていて、そのまま要約するだけでなく、自分の話題の材料として使える。",
 "全体 ── テキストを素材として話題を論じる。評価のコメントと自分の意見を添える。渡す営みから自分の論へ、最も近づく段。",
 "",
 "No.816の一級上。要約にコメントを添えるところから、テキストを材料に論じるところへ。「論の提示」の章のC1（No.276＝相手の視点を取り込んで論を展開する）と同じ組み立てが、他人のテキストを足場に立つ。",
),
812: (
 ["Article (specialised): …\nYou (to a colleague): She's dismissive of the method — look at the last paragraph, where she calls the results 'suggestive at best'. And she only cites the two studies that failed."],
 "たとえば、ある研究方法を批判する専門誌の論文、業界の技術報告。専門的な話題で、著者の態度や意見が、言い切らずに語の選び方と引用の選び方に表れている。",
 "立場 ── 表明された態度や意見を説明し、自分の推論を、原文の特定の箇所に言及して裏づける。",
 "日本語では筆者の態度を言うとき「〜と考えているようだ」「〜ではないか」と推量の形で留めるのが控えめで適切とされるので、英語でも *The author seems to think maybe…* と、裏づけのない推量に聞こえる言い方になる。英語でこの段に求められるのは、原文の箇所を示したうえでの言い切り（*She's dismissive — see the last paragraph, where…*）で、推量の形では裏づけが立たない。",
 "No.818の一級上。態度の説明に、原文の箇所による裏づけが加わる。",
),
806: (
 ["Letter (from a colleague): 'We were, of course, delighted to hear that the project will be led from head office.'\nYou (to a colleague): That 'of course' is doing a lot of work. He's not delighted — he's saying the decision was made over his head, and he wants us to know he noticed."],
 "つながりや含意が明示されていないテキスト。控えめな表現、皮肉、反語を含む。",
 "含意 ── 明示されていない推意を説明し、表現の形の社会文化的な含み（控えめに言う型、皮肉）を指摘する。",
 "",
 "この章の終点。「聴衆として聞く」の章のC2（No.33）と「知るために読む」の章のC2（No.147）が自分のために含意を取る段で、ここではそれを他人に説明する。級が揃う。",
),
}

DISCUSSION = [
    # 1 梯子
    "この章の梯子は、二つのものでできている。一つは入力の側の条件で、第3部の章と同じく条件の解除の一本の列になる ── 支え（短くごく簡単な表示・構成のはっきりした短いテキスト・ゆっくり明瞭な簡単なニュース・挿絵と表：No.833/832/829/830/831）→ 身近な主題と明瞭な構成（824/825/826）→ 何度も聞ける・意味を確かめられる（827/828/821）→ 短い素材（822/823）→ 関心分野（817/818/813）→ 条件なし（815/816/819/820/814/807/810/811）→ 専門の内外（808/809/812）→ 逆境＝つながりや含意が明示されていない（806）。条件なしの段がB2で始まり、そのあとに専門の但し書きが戻り、上端に逆境が来るという形は「知るために読む」の章と同じである（向こうは条件なしのNo.151〜153〔B2〕のあとに分野か辞書の但し書き〔No.149・150、B2+〕が戻り、逆境のNo.148・147〔C1・C2〕で閉じる。戻る級が一つ違う ── 向こうはB2+、こちらはC1）。渡す側の条件は受ける側の条件を引き継いでいる。もう一つは渡す中身の深さで、『受容の課題』の七層がそのまま並ぶ ── 一つの項目（833・830）・筋（820）・要点（832から819まで13段）・全体（815・816・813・814・807・808・809・811）・立場（818・812）・含意（810・806）。知っている言葉の層だけがない：語を一つ渡すことは仲介の段にならない。要点がB1からB2まで十三段を占め、全体がB2から、立場と含意がB2・C1から立つ。層は級に対して単調でない（要点の段がB2に三つ残り、一つの項目がA2+に戻る）── 段を決めるのは条件と、渡し方（伝える→要約する→統合する→コメントして論じる→説明する）で、深さはその中身である。",
    # 2 CEFRの企図
    "増補版第4章のこの尺度は、聞いたか読んだかしたテキストを、たいていはもっと凝縮した形で、場面に合う仕方で別のテキストへ移すこと、として定められている。「特定の情報を伝える」の尺度が相手の知りたい一点を原文から探して渡すのに対して、この尺度では原文の要点を全部理解していなければならず、したがって「知るために読む」（注意深く読む）と結びつき、目的に応じて相手に別の順序で提示してもよい、と原典は書く。鍵概念は、原文の要点をまとめること、複数の情報源からの情報と論点を集めること、ほか。CEFRが立てた軸は、要約という渡し方の背骨と、入力の側の条件の二本で、渡す相手は for somebody else（823）・specific audience（書面の838）として段に現れる。本書の読みはこれに「渡す中身の深さ」を重ねる ── 要約の動詞は一つでも、渡しているものが要点か、全体か、著者の立場か、言われていない含みかで、段の中身は違う。Language A と Language B は原典が受けるものと渡すものに置いた置き札で、別の言語でも同じ言語でも等しく当てはまり、較正は関わる言語に依らない（増補版 p.92・p.250）。本書は渡す側を英語に固定し、受けるものは英語を標準として段を立てる。この前提は柱の肖像「橋渡しする人」が述べる（判断(cs)②・(cx)）。",
    # 3 境目と対
    "受ける側との対は、段の欄が名指している受ける側のCan-Do記述文ごとに数えると二十八あり、同級18・一級上3・一級下3・二級以上の差4。同級＝833↔141（A1）・824↔158・159（B1）・825↔132（B1）・826↔25（B1）・827↔73・74（B1）・828↔91（B1）・821↔156（B1+）・817↔151（B2）・818↔40／152（B2）・820↔88（B2）・807↔148／35（C1）・808↔18（C1）・806↔33／147（C2）。一級上＝833↔145（A1／Pre-A1）・829↔94（A2+／A2）・814↔22（B2+／B2）。一級下＝825↔131（B1／B1+）・819↔86（B2／B2+）・809↔147（C1／C2）。二級以上＝830↔143・146（A2+／A1・Pre-A1）・820↔93・90（B2／A2+・B1）。人に渡すことが分かることより一段重い、という規則はこの分布からは立たない ── 原典は受ける尺度と渡す尺度を、同じ素材について同じ級に書くのが常である。一級の差は、対のどちらかが持つ但し書きの差で説明がつく（94＝見当で足りる／829＝要点を取る、22＝標準語か馴染みのある方言で／814＝複雑な議論に但し書きなし、145＝Pre-A1の標識／833＝掲示に加えてポスターとプログラム、131＝使えるかどうかを見分ける／825＝簡単に要約するという渡し方の手加減、86＝番組全体から要点を取り出す／819＝抜粋、147＝専門外でも含意まで／809＝専門概念を確かめてよい）。二級以上の差は、渡す段のdeltaが受ける側の梯子を下から辿って指した参照（830＝表から場所と時間と値段を拾う最初の段146・143、820＝映像で筋を追う列93・90、その上の88が同級の対）で、同じ条件の段どうしの対ではない。語る・書き上げる側との対は、要約の言葉の質が段に入るところから立つ ── 813↔356（よく構成された要約／要点の強調と裏づけ、B2+）・811↔276（他人の論を足場に論じる／相手の視点を取り込んで論を展開する、C1）・815↔360（複数の情報源の情報と論点を統合する、B2＝「報告する」の二語を除けば同じ文。正準の正規化では0.75で閾値内、Language の括弧も落とせば0.92）。書面の同じ尺度（テキストをまとめて伝える（書面）17行）とは、口頭↔書面の対が同級で並ぶ（824↔844・813↔839・807↔837・806↔835 ほか）。収載は第4部の範型二枚のあと一括（判断(cs)⑦）。全1,224件を Language の括弧を落として正規化し逐語で引くと、本シートの28行に同じ文は一件もない。815と360が最も近く（0.92）、二語の差で分かれる。",
    # 4 落とし穴
    "日本語話者の落とし穴は、この章では渡した言葉の側にだけ立つ。受け取る側で外すこと（要点がつかめない、含意を拾わない）は第3部の対の段が書いているので、ここには書かない。欄は七段。表の項目を名詞を並べただけで渡し、文にならない（830）。経緯から結論へ流れる説明の順序のまま、要点が最後に来る（824）。聞いたことを渡すときに文ごとに伝聞の印を添え、言い切りが弱まる（826）。あらすじを過去の形で語る（820）。対立する見解を「どちらにも一理ある」で締める（816）。著者の態度を「言っている」の一語で受けて、態度が消える（818）。態度の説明を推量の形で留めて、裏づけが立たない（812）。七つのうち四つが、著者の態度と見解の扱い（816・818・812）と伝聞の印（826）── 人の言ったことを自分の言葉で言い切ることへのためらいが、日本語の形（伝聞・推量・両論併記）として出る。穴のない二十一段は、渡す仕事の難しさが入力の長さと複雑さの側にあり、出力の側に日本語の形で指せる失敗が立たない段である。",
    # 5 何がこの梯子を測るか
    "この梯子を測るものさしは三つある。一つは入力の側の条件 ── 第3部と同じく、どれだけの手加減の下で、という但し書きの数と向き。もう一つは渡す中身の深さ ── 要点か、全体か、立場か、含意か。三つめが第4部で加わるもので、渡し方 ── 伝える、要約する、統合する、コメントして論じる、説明する ── と、誰のために渡すか。段を上がるとは、入力の手加減が減りながら、渡す中身が深くなり、渡し方が凝縮から組み立てへ移ることである。だから同じ「要約できる」の動詞がB1からC1まで続いても、段は違う。この章が第3部と第2部の両方に接続するのは、ものさしの一つめが第3部の、三つめが第2部のものだからで、仲介の段は受ける段と語る段の合成として測られる。上端が含意（806）で閉じるのは「聴衆として聞く」「知るために読む」と同じで、言われていないことを人に説明するには、言われたことの全体が組み上がっていなければならない。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 28
    for name, m in (("CONDITION", CONDITION), ("DEPTH", DEPTH)):
        tagged = [n for v in m.values() for n in v]
        assert sorted(tagged) == sorted(ORDER), f"{name}が完全分割でない"
    assert list(DEPTH.keys()) == SEVEN_LAYERS, "DEPTHの語彙が七層でない"
    assert not DEPTH["形"], "知っている言葉の層に段がある（語を一つ渡すことは仲介の段にならない）"
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    prev_min = -1
    for c, nos in CONDITION.items():
        lv = sorted(order_lv.index(desc[str(n)]["level"]) for n in nos)
        assert lv[0] >= prev_min, f"条件の列が級順でない: {c}"
        prev_min = lv[0]
    # 表示順＝級順→No昇順
    assert ORDER == sorted(ORDER, key=lambda n: (order_lv.index(desc[str(n)]["level"]), n)), "ORDERが級順→No昇順でない"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        for e in ex:
            assert "\nYou (to " in e or "\nYou: " in e, f"例に You (to …): の行がない No.{no}"
        rows.append({
            "mode": MODE, "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "テキストをまとめて伝える（口頭）（Processing text in speech or sign）── 第4柱第一号範型・全数シート",
        "scope": "全数（28件。口頭28 ── mode一様）",
        "type": "第4柱（仲介）。梯子＝入力の側の条件の解除の一本（支え→身近な主題と明瞭な構成→何度も聞ける・確かめられる→短い素材→関心分野→条件なし→専門の内外→逆境）、深さ＝渡す中身の七層（『受容の課題』§2）は段の属性。四欄（scene＝受けるもの・howwell＝渡すもの・l1・delta）は書物の本文そのもの（判断(cs)、判断(bs)と同じ）。Language A＝B＝英語（判断(cs)②）。",
        "essence": "聞いたか読んだかしたテキストを、別の相手に英語で渡す。段を区切るのは入力の側の条件と渡し方（伝える→要約する→統合する→コメントして論じる→説明する）で、渡す中身の深さ（一つの項目から含意まで）がその中身。受ける側（第3部）の段と同じ級に並ぶのが常で（一級の差は但し書きの差、二級以上は受ける側の梯子を下から辿った参照）、要約の言葉の質が問われる段から語る側（第2部）と並ぶ。",
        "axes": {"条件": CONDITION, "深さ": DEPTH},
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p4_processing_speech.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
    print("落とし穴欄:", sum(1 for r in sheet["rows"] if r["l1"]), "/ 空欄:", [r["no"] for r in sheet["rows"] if not r["l1"]])
