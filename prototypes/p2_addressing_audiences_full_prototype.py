#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第2柱（産出・談話構築）第六号範型：Addressing audiences 18件の全数シート。

CEFRカタログ11・判断(af)(ag)。裁定：
- 並行対3件採用（305↔359／303↔356／299↔354、いずれも同レベル・同文級）── 論証族4対へ
- 305/303/299は論証族・論構造糸（糸保存の不変条件による強制）
- 段差の読み直し：軸はoral/writtenでなく準備・推敲可能性（即応口頭＜準備済み口頭≈推敲書面）
- 303↔277＝口頭×口頭のスケール再掲重複対（第2柱初。mode_pairsに載せず二行保持＋相互参照）
- 講演族は立てない（判断(ag)）：本スケール＝論証族宣言＋固有糸2本（講述・質疑応答）の初の口頭束スケール
- 質疑応答7行は副タグでなく独立の糸（A2〜C2のほぼ全段でプレゼン行と並走＝複数梯子の形式的証拠）
- 質フラグ0件 ── 口頭4スケール目もゼロ
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Addressing audiences"
ACT = "聴衆への講演（第2柱：Addressing audiences）"
FAMILY = ["論証族"]  # 判断(ag)：講演族は立てない。論証族宣言＋固有糸（講述・質疑応答）
SYSTEM = "論証族"

# レベル順→No昇順（表示順の正準）
ORDER = [314, 312, 313, 310, 311, 308, 309, 307, 305, 306, 303, 304, 299, 300, 301, 302, 297, 298]

# 談話課題糸（正準は data/p2_threads.json、本表はbuild()内assertで照合）
THREADS = {
    "講述":     [314, 312, 308, 297],
    "質疑応答": [313, 311, 309, 306, 304, 302, 298],
    "理由づけ": [310],
    "比較考量": [307, 301],
    "論構造":   [305, 303, 299, 300],
}
SUBTAGS = {
    "儀礼定型":   [314],
    "支援条件":   [313],
    "比較考量":   [305],
    "流暢さ明記": [306, 304, 302],
}

# モード間並行対（口頭側の実装。相手は Reports and essays、判断(af)）
MODE_PAIRS = {305: 359, 303: 356, 299: 354}

R = {  # no -> (exponents, scene, howwell, l1, delta)
314: (
 ["Good evening, everyone. This is Mr Sato. He is our new teacher. He is from Osaka. Welcome, Mr Sato!",
  "Please stand up and take your glass. Today is a big day for Ken and Aya. To Ken and Aya!"],
 "式や集まりの冒頭で、準備した短い原稿を読み上げる（紹介・乾杯の音頭）。",
 "定型の履行。原稿を用意し、そのまま音読してよい段 ── 即興は求められない。",
 "「僭越ながら」「つたない挨拶ですが」の自己卑下の開頭を訳出しない ── 英語の紹介・乾杯は事実の提示（This is X. He is Y.）から入る。乾杯の発声は To X! の一句で足り、長い前置きを付けない。",
 "講述糸の起点＝ごく短い準備済みテキストの送達。中身は儀礼（紹介・乾杯）で、第1柱・挨拶（儀礼定型）および感謝・詫び・祝意（祝意）と交差する（副タグ・相互参照。行為として遂行するなら第1柱、聴衆の前で原稿として送達するなら本柱）。",
),
312: (
 ["Today I will talk about my town. It is small, but it has a big park and a long river. In summer, we have a festival by the river. Many people come. I like my town very much. Thank you for listening."],
 "授業や集まりで、身近な主題について練習してきた短い発表をする。",
 "基本文の連鎖で足りる。話題は身近な主題に限られ、練習済みであることが行の条件。",
 "一文を短く切る ── 「小さいけれど公園があって夏には祭りがあって」を一文に繋げない。締めの定型（Thank you for listening.）を持つ ── 日本語の「以上です」を直訳しない。",
 "講述糸：儀礼の一句（314）から、身近な主題の短い発表へ。まだ論証はなく、伝える内容の器（開始→本体→締め）が課題のすべて。",
),
313: (
 ["Sorry, could you say that again, please? ... Ah, my favourite place. My favourite place is the park. Yes, the park near my house.",
  "One more time, please. ... The festival? It is in August. Au-gust. Yes."],
 "発表のあとの簡単な質問に、聞き返しと助け船に支えられて答える。",
 "聞き返しの定型（Could you say that again?）と、質問語の復唱による確認。",
 "無言で固まらない ── 分からなければ聞き返し、質問の一部を復唱して確認してから答える。「えっと」の代わりに Ah / Well を置く。単語で答えてよい段だが、Yes だけで終えず一語でも実質を足す。",
 "質疑応答糸の起点。支え型条件句が二重に書かれる（繰り返しを求められること＋回答の言い方への助け）── 論証族口頭の287（相手の忍耐）と同型の、糸の下端の支え。聞き返しの定型そのものは第1柱・明確化（746帯）の帳簿にあり、本行はそれを聴衆の前で運用する側（相互参照）。",
),
310: (
 ["I want to study in Australia next year. I have two reasons. First, I can use English every day. Second, my uncle lives there, so I can ask for help. That is my plan."],
 "自分の計画や意見を短く発表し、理由を添える。",
 "理由の枠（I have two reasons. First ... Second ...）。理由は一文ずつでよい。",
 "理由を because の従属節だけで繋がず、First / Second で立てる ── 「なぜなら〜だし、〜だから」の一文化は係り先が壊れる。数を先に宣言する（two reasons）。",
 "理由づけ糸（論証族）が本スケールに入る最初の行。発表（312）に「理由を短く添える」操作が加わる ── 論証はここでは器でなく添え物で、器になるのはB2（305）から。",
),
311: (
 ["Good question. The trip was three days. ... Yes, we went by train. ... Sorry, one more question only, please."],
 "発表のあとの、少数の率直な質問に答える。",
 "質問への応答定型（Good question. ／ Yes, ... ／ Sorry, ...）と、数の管理（limited number）。",
 "質問を受けたら一拍おいてよいが、沈黙を詫びで埋めない ── Good question. が間を作る定型として機能する。打ち切りは Sorry, one more question only. と明示してよい（無言の会釈で終えない）。",
 "質疑応答糸：助け船つきの一問一答（313）から、少数の質問を自力で受ける段へ。支え型条件句（回答定式化の助け）がここで脱落する ── 744→742型の質疑糸での再現。",
),
308: (
 ["Today I will explain our plan for the school festival. There are three points: the place, the food, and the money. First, the place. We will use Room 12, because it is near the entrance. Second, the food. We will sell curry and rice; one plate will be three hundred yen. Third, the money. We need about twenty thousand yen, and the club will pay half. That is the plan. Thank you."],
 "自分の分野の身近な話題について、要点を立てて過不足なく伝わる発表をする。",
 "要点の先出しと番号立て（There are three points. First ... Second ...）。「たいてい難なく追える」明確さと、要点の reasonable precision。",
 "「いろいろあるんですけど」から入らず、数を先に宣言して番号で刻む。各要点の中で理由を一つだけ添える（because it is near the entrance）── 詳細を足しすぎて要点の輪郭を失わない。",
 "講述糸：短い発表（312）から、要点が立ち聴衆が難なく追える発表へ。followed without difficulty は論証族281（B1+）と完全同句だが本行はB1に立つ ── 受け手基準の最早出現。reasonable precision は教示族268の署名語と同語で、精度の軸がここに顔を出す（主タグは講述に留置）。この行のあと講述糸はC2（297）まで中抜きになる ── 中段の発表の中身が論証族3糸（310→307→305→303→299/300/301）へ外部化されるためで、判断(x)・助言（行為の中抜き型）の糸版。",
),
309: (
 ["Could you speak a little more slowly, please? ... I see. You are asking about the cost. The cost is about fifty thousand yen for one term. That includes the books."],
 "発表のあとの質問を受ける。速い質問は聞き返してよい。",
 "聞き返し（Could you speak more slowly?）と、質問の言い換えによる照準（You are asking about X.）。",
 "聞き返しを恥じない ── 速い質問への繰り返し要求は行の文言に書かれた正当な手続き。答える前に You are asking about X. で照準を宣言すると、取り違えが半減する。",
 "質疑応答糸：数の管理（311）から、内容としては自立した応答へ。ただし速い質問には繰り返しを求めるという但し書きが残る ── 支えの残滓が許容として書かれる段。相手の用語を引用して照準する操作は第1柱・明確化の引用スロット（判断(s)-1拡張）と同じ機構（相互参照）。",
),
307: (
 ["The two phones look similar, and the price is almost the same. The difference is the battery and the camera. Model A works for two days without charging, but the camera is simple. Model B has a very good camera, but you must charge it every night. If you travel a lot, Model A is better; if you take many photos, choose Model B."],
 "製品・国や地域・計画などの類似点と相違点を概説する発表をする。",
 "比較の枠（similar ... The difference is ... A ..., but B ...）と、条件つきの使い分け（If you ..., A is better）。",
 "「AもBもいいんですけど」の並置で終えない ── 差分の軸を名詞で先に言う（The difference is the battery.）。比較は同じ観点で対にする（Aの電池とBのカメラを直接比べない）。",
 "比較考量糸（論証族）の本スケール下段。理由づけ（310）が単発の根拠なら、ここでは二つの対象を同じ軸に載せて往復する ── 第1柱の「比較」五者連関（467/473/511/286/280）に本行が加わり、比較が柱と族をまたぐ蝶番であることが講演の帳簿でも確認される。",
),
305: (
 ["Should our office move to a four-day week? Let me give the arguments on both sides. In favour: people rest better, sick days go down, and good workers stay longer. Against: customers cannot reach us on Fridays, and some projects will move more slowly. Each option has a price. A four-day week costs us speed; a five-day week costs us people. My own view is that people are harder to replace than speed."],
 "一つの論点への賛否の理由と、選択肢の利点・欠点を挙げる、準備済みの明快な発表をする。",
 "賛否の対称な提示（In favour / Against）と、利欠点の言い切り（A costs us X; B costs us Y.）。",
 "賛否の両側を自分で立てる ── 日本語の発表定型「賛否両論あるかと思いますが」で聴衆に委ねない。両論のあとに自分の結論を一文で置く（My own view is ...）── 両論併記で終えると発表として未完に響く。",
 "論構造糸（論証族）が本スケールの器になる最初の行。賛否の理由＋利欠点という中身は理由づけ・比較考量と交差する（副タグ）が、主タグは論構造 ── 書面359（小論のB2・同文級）との並行対が糸保存を強制する（判断(af)）。討論側の280（B2・利欠点の考量）とは、応酬の中の考量／聴衆の前で独力で組み立てる考量、の分業。（モード間並行対：書面 Reports and essays No.359）",
),
306: (
 ["Yes — three questions, one by one. First, the cost: about two million yen in the first year. Second, the schedule: we start in April and finish before the summer. And your third point, about the staff — that is the hardest one. We will need two more people, and I will come back to that in a moment."],
 "一連の追加質問を、自分にも聴衆にも負担のない流暢さで受け続ける。",
 "複数質問の管理（one by one ／ ナンバリングして順に消す）と、保留の宣言（I will come back to that）。no strain ── 受け答えのテンポそのものが基準になる。",
 "複数の質問を受けたら、順番を自分で宣言して一つずつ消す ── 全部を一度に答えようとして混線させない。答えられない点は保留を明示する（I will come back to that.）── 日本語の「後ほど」を無言の省略にしない。",
 "質疑応答糸：単発の応答（309）から、一連の質問の管理へ。fluency and spontaneity という how well 語彙が行の文言に入り（流暢さ明記）、基準は「自分にも聴衆にも負担にならない」── 受け手負担の定型（poses no strain）はPublic announcements 292と共有される。第1柱・授受の情報管理相（複数情報の整理）と機構を共有するが、こちらは聴衆の前の一対多（相互参照）。",
),
303: (
 ["My talk has three parts, and I will give you the main point now, at the start: we should keep the city library open in the evening. Part one shows who actually uses it — the key figure is this: six out of ten visits happen after six o'clock. Remember that number, six out of ten. Part two answers the main objection, the cost. Part three shows what we lose if we close early. Let me start with part one."],
 "重要な点を強調し、関連する詳細で裏づけた、体系的に展開する発表をする。",
 "設計図の先出し（three parts）、主張の冒頭提示、強調の設計（the key figure is this ／ Remember that number）。",
 "強調を声の大きさでなく設計で行う ── 予告（I will give you the main point now）・名指し（the key figure）・復唱（six out of ten）の三点セット。結論を最後まで取っておかない ── 冒頭提示は無作法ではなく体系性の要件。",
 "論構造糸：賛否の提示（305）から、強調と裏づけの体系へ。書面356（小論のB2+・同文級）との並行対。さらに討論側277（B2+）とも同文級（類似度0.786）── 第2柱初の口頭×口頭スケール再掲重複対で、同じ「体系的展開＋強調＋裏づけ」が討論（応酬の中で）と講演（準備の上で）の両帳簿に立つ（二行保持・相互参照、判断(af)）。（モード間並行対：書面 Reports and essays No.356）",
),
304: (
 ["That is a very interesting point — let me leave my slides for a moment. You said your team tried this and it failed after two months. May I ask what happened in the second month? ... Right. So the problem was not the tool, it was the training. That actually connects to my second section — let me pick it up from there, because your case is a better example than mine."],
 "準備した原稿から自発的に離れ、聴衆が出した興味深い論点を追いかける。しばしば目覚ましい流暢さを示す。",
 "原稿からの離脱の宣言（let me leave my slides）、聴衆の発言の取り込み（You said ...）、本筋への接続（That connects to ...）。",
 "原稿への復帰路を先に確保してから離れる（let me leave my slides for a moment）── 離れっぱなしにも、離れることを詫び続けることにもしない。聴衆の事例を自分の例より上位に置く一言（your case is a better example）は、日本語の謙遜と違い、論の資源化として機能する。",
 "質疑応答糸：質問の管理（306）から、質問を素材として論に取り込む段へ。準備済みテキストという講述の器から自発的に離れられることが段の中身で、準備・推敲可能性の軸（判断(af)）の上で言えば、準備済みの側から即応の側へ自力で降りて戻れる能力。remarkable fluency が文言に明記される（流暢さ明記）。",
),
299: (
 ["Why do local shopping streets decline? The easy answer is online stores, and my talk will argue that the easy answer is wrong. My main claim has three supports. First, the timing does not fit: most streets here began losing shops years before online shopping grew. Second, rents: when the owner's family gives up the shop, the rent for the next tenant nearly doubles — I will show the figures for two streets. Third, and this is the subsidiary point people miss: the customers who say they love the old shops buy elsewhere; loyalty in words is not loyalty in money. Each of these supports has its own evidence, and I will take them in turn."],
 "複雑な主題について、補助的な論点・理由・適切な例で見解を長めに裏づける、よく構成された発表をする。",
 "主張と支持の階層（main claim → three supports → subsidiary point → evidence）。長さに耐える構成 ── 各支持が自前の証拠を持つこと。",
 "補助論点を「余談ですが」で導入しない ── subsidiary は脱線ではなく階層の一段（this is the subsidiary point people miss）。長い発表ほど、いま階層のどこにいるかを言語で示す（First / Third / in turn）。",
 "論構造糸：強調の設計（303）から、階層をもつ長い論証へ。書面354（小論のC1・同文級 ── 354の全文が本行から講演の器を外した残り）との並行対。354は討論278（B2）の段差先でもある ── 同一の書面行が、準備済みの講演とは同段で対をなし、即応の討論とは段差を作る。準備・推敲可能性の軸（判断(af)）が一つの行の両側に見える帳簿上の実例。（モード間並行対：書面 Reports and essays No.354）",
),
300: (
 ["Before I begin, let me give you the map of this talk, because it is a long one. Part one describes the problem and why it matters. Part two clears the ground: I will take the two most common answers and show why each fails. Part three builds my own proposal on what remains. If you keep one sentence from each part, the whole argument will stand by itself at the end — and I will return to this map twice, so you always know where we are."],
 "聞き手がアイディアの流れを追い、全体の論証を理解できるように、長めの発表を適切に構成する。",
 "メタ談話（the map of this talk ／ where we are）と、部分と全体の関係の明示（what remains ／ stand by itself）。",
 "地図は冒頭に一度で終えず、戻ってくることを予告して実際に戻る（I will return to this map twice）── 日本語の「話は変わりますが」で区切りを済ませない。各部の役割を動詞で言う（describes / clears / builds）。",
 "論構造糸：階層の構築（299）と同段に立つ、構成そのものの運用面 ── 299が論の中身の階層なら、本行は聴衆の追跡を保証するメタ談話。二行がC1に並ぶことは、論構造糸がこの帯で中身と運用に分化することの帳簿上の形（糸内の同段二行＝厳密単調の唯一の例外）。書面の背骨の外枠（読者適合）に対応する口頭側の実装で、係留語は help the audience follow。",
),
301: (
 ["What happens if we do nothing? Suppose rents keep rising at the current rate: within ten years, only chain stores can pay, and the street loses the very character that draws people. Now suppose instead we cap the rents. The first effect is good — the old shops stay — but the second is not: owners stop repairing the buildings, and the street decays in a different way. So let me put a third option on the table and weigh it against both: the city buys the worst three buildings and rents them below market. It is the most expensive path today, and, if my projection is right, the cheapest one in twenty years."],
 "複雑な主題の提示の中で、推測や仮説を立て、代替案や論を比較・評価する。",
 "仮定の枠（Suppose ... Now suppose instead ...）と、複数案の秤（weigh it against both）。仮説と事実の区別（if my projection is right）。",
 "仮定は Suppose / What if で明示して立てる ── 「〜だったりすると」の曖昧な仮定のまま論を進めない。自分の推測には印を付ける（if my projection is right）── 断定と仮説の混線は論全体の信用を落とす。",
 "比較考量糸の上端：実物の比較（307）から、仮想の選択肢を立てて秤にかける段へ。討論側の考量（280・B2）よりさらに上で、比較の対象そのものを仮説として生成する。第1柱・提案の比較帯（467）と機構を共有するが、こちらは相談でなく独話の中の思考実験（相互参照）。",
),
302: (
 ["(A voice from the floor: 'That is not what the report says!') — Fair point, and thank you for reading it. The report does say that, on page ten. Read one page further, though, and it also gives the numbers for last year — and those numbers are exactly where my argument starts. So we agree on the source; we differ on which page matters. Let me show you why page eleven wins."],
 "不規則な発言（interjection）を、ほとんど苦もなく自発的に処理する。",
 "割り込みの受け止め（Fair point）、部分的承認からの切り返し（The report does say that ... though ...）、対立の再定義（we agree on X; we differ on Y）。",
 "割り込みを詫びで受けない ── Fair point. は承認であって謝罪ではない。反論は相手の正しい部分を先に確定してから（does say that）行う ── 全否定から入ると対立が論点から人格へ移る。",
 "質疑応答糸：予定された質問の外から来る発言への即応。effortlessly が文言に明記される（流暢さ明記）── 準備の外で流暢さが試される点で、本糸の上端二行の入口。割り込みの処理は第1柱・会話維持（発言権の運用）と機構を共有するが、こちらは一対多の聴衆の前で論の側に引き戻す操作（相互参照）。",
),
297: (
 ["You are all here because your electricity bill went up, not because you care about grid engineering — so let me start from the bill, and I promise the engineering will explain itself on the way. ... I can see that this diagram is one step too many; let me put it differently. Think of the grid as a road system at rush hour ... Good — I see that landed. Now, you remember the bill we started from? Here is the same story told in yen: the traffic jam is what you are paying for."],
 "その話題に馴染みのない聴衆に、複雑な話題を、聴衆の必要に合わせて柔軟に構成・調整しながら自信をもって提示する。",
 "聴衆の現在地からの設計（start from the bill）、その場での再構成（let me put it differently）、着地の確認と回収（you remember the bill we started from?）。",
 "聴衆が追えていない徴候を検知したら、話を戻すのでなく別の道で言い直す（let me put it differently ── 「先ほども申し上げたとおり」で同じ説明を繰り返さない）。専門語は聴衆の生活語に着地させてから導入する。",
 "講述糸の上端＝C2での再浮上。B1（308）以降、発表の中身は論証族3糸へ外部化されていたが、ここで戻ってくる課題は論の質ではなく送達の質 ── 馴染みのない聴衆という条件が、構成・調整という講述固有の課題を最上段で復活させる（判断(x)・助言の中抜き型と同じ再浮上の力学）。係留語は adapting the talk flexibly to meet the audience's needs ── 書面背骨の最終段（読者適合）の口頭版が、独立の行として立つ唯一の場所。",
),
298: (
 ["('Is it true that you were paid by the developer to say this?') — I will answer the question, and then the question behind it. Yes, the developer funds this study; the funding is on the first slide, and the data is public, so you can check every number without trusting me. The question behind yours is whether the money chose my conclusion. It did not — and you do not have to take my word for it: the same result appears in the city's own survey, run by people who oppose this project. If it is wrong, it is wrong twice, independently."],
 "難しい質問や、敵対的な質問さえも処理する。",
 "敵意の分解（the question behind it）、検証可能性への転換（you can check every number without trusting me）、独立の裏づけ（wrong twice, independently）。",
 "敵対的な質問に謝罪から入らない ── 日本語の「誤解を招いたとすれば」型の緩衝は、ここでは過失の承認として読まれる。攻撃を人格から命題へ移し替える（the question behind yours is whether ...）── 応じるのは攻撃でなく、その中の検証可能な問い。",
 "質疑応答糸の上端＝敵意の処理。第1柱の対立管理（意見表明487のchallenge・苦情の対立）と接するが、あちらが応酬の往復であるのに対し、こちらは一対多の聴衆の前で、一撃を論の資源に変える独話側の技術（相互参照）。質疑糸はA2の支え（313）からC2の敵意（298）まで七段 ── 第1柱の往復・応答(n)が第2柱に糸として帳簿化される唯一の場所であり、(n)を柱横断の軸に戻す必要はない（軸でなく糸で書ける ── 判断(ab)の第1柱降格は不変、判断(ag)）。",
),
}

DISCUSSION = [
 # ¶1 背骨
 "この18件は、第2柱で初めての口頭の束スケールである ── 判断(y)(d)「口頭＝課題純粋／書面＝課題の束」はここで初の反例を得るが、帳簿は壊れない：束は書面の専売でなく、聴衆が実在する場（講演）の性質から生じる、と読み替えればよく、判断(ad)「族は糸の属性でありスケールは複数族を宣言できる」がそのまま口頭側でも働く。背骨は三重に走る。第一に講述の器：練習済みの一句 rehearsed statement（314）→ 基本的な発表 basic presentation（312）→ 難なく追える発表 followed without difficulty / reasonable precision（308）→（中抜き）→ 聴衆の必要への柔軟な適合 adapting to the audience's needs（297）。第二にその中身として入る論証：理由 reasons（310）→ 類似と相違 similarities and differences（307）→ 賛否と利欠点 in support of or against / advantages and disadvantages（305）→ 体系と強調 systematically / highlighting（303）→ 階層と裏づけ subsidiary points, reasons and relevant examples（299）・全体論証の追跡保証 overall argumentation（300）・仮説の考量 speculate or hypothesise（301）。第三に質疑：助けを借りた応答（313）から敵対的質問の処理 hostile questioning（298）まで。受け手基準は本スケールで最も早く現れる ── followed without difficulty は論証族281ではB1+だが、ここではB1（308）の行に立ち、C2（297）では audience's needs が構成の判定基準そのものになる。聴衆の実在が、受け手基準を梯子の全域に浸透させる。",
 # ¶2 糸
 "糸は5本、完全分割（正準：data/p2_threads.json）：講述（314→312→308→297）／質疑応答（313→311→309→306→304→302→298）／理由づけ（310）／比較考量（307→301）／論構造（305→303→299→300）。論証族3糸を宣言し、講述・質疑応答は固有糸 ── 講演族は立てない（判断(ag)：残余と告知の梯子は文言を共有せず、族の存在理由＝モード間接続の器を持たないため）。質疑応答は副タグでは収まらない ── A2からC2まで、ほぼ全段でプレゼン行と並走しており（A2: 312/313、A2+: 310/311、B1: 308/309、B2: 305/306、B2+: 303/304、C1: 299-301/302、C2: 297/298）、判断(ae)の形式基準「二糸が並ぶ＝複数梯子の証拠」がスケール全域で成立する。putting a case の対話者副タグ（両端2行＝条件と資源）とは別種で、ここでは対話者の処理そのものが各行の課題である。講述糸はB1→C2の中抜き ── 中段の発表の中身が論証族3糸へ外部化され、C2で送達の質という固有課題が再浮上する。行為の中抜き型（判断(x)・助言）の糸版であり、可視性がレベルに対して単調でないことは糸のレベルでも起きる。論構造のC1二行（299＝中身の階層／300＝追跡保証のメタ談話）は糸内の同段分化で、厳密単調の唯一の例外。副タグ4種：儀礼定型（314＝第1柱・挨拶／祝意との交差）、支援条件（313の二重の支え）、比較考量（305の交差）、流暢さ明記（306/304/302）。",
 # ¶3 mode
 "modeは全行「口頭」で一様。並行対は3件 ── 305↔359（B2）・303↔356（B2+）・299↔354（C1）、いずれも同文級で、論証族は4対になる（判断(af)。カタログ10申し送りのpendingはここで解消）。書面側はいずれもReports and essaysの論構造糸で、糸保存の不変条件が305/303/299の論構造帰属を強制した。356は277（討論）と303（講演）の二つの口頭行を受け、354は299と同段の対をなしつつ278（討論B2）の段差先でもある ── 一つの書面行が二役を務めるこの形が、段差の読み直し（判断(af)）の核心である：非対称の軸はoral/writtenでなく準備・推敲可能性であり、即応の討論だけが下に置かれ、準備済みの講演は推敲可能な小論と同段で対をなす（即応口頭＜準備済み口頭≈推敲書面。「書面は待ってくれる媒体」は「準備・推敲が待ってくれる」へ一般化）。303↔277（類似度0.786・ともにB2+）は第2柱初の口頭×口頭スケール再掲重複対 ── 第1柱466/512型の第2柱版で、mode_pairsには載せず二行保持＋相互参照で処理する。第1柱境界は行の移動なしに四箇所：313/309↔明確化（聞き返しの定型と引用スロット）、298↔意見表明487・苦情（応酬の対立管理 vs 独話側の敵意処理）、302↔会話維持（発言権 vs 一対多の割り込み処理）、314↔挨拶・感謝詫び祝意（儀礼の遂行 vs 原稿としての送達）。",
 # ¶4 L1
 "L1注意の三段転換は七例目 ── ただし本スケールでは、日本語の発表文化そのものが転移源になる。下段（〜B1）＝定型・統語：自己卑下の開頭（「僭越ながら」「つたない発表ですが」）を訳出しない・締めの定型を持つ・一文一情報で切る・数の事前宣言。質疑側では、無言で固まらず聞き返しの定型で時間を作る。中段（B1+〜B2+）＝談話：要点と結論の先出し（両論併記で終えない）・差分の軸の名詞化・複数質問のナンバリング管理・保留の明示。上段（C1〜C2）＝修辞・開示の再配置：強調を声量でなく設計で行う（予告・名指し・復唱）・仮説と断定の区別に印を付ける・割り込みと敵意を謝罪で受けない ── 「誤解を招いたとすれば」型の緩衝は過失の承認として読まれ、攻撃は人格から命題へ移し替えて処理する。論証族（強調の設計）と共有する転換に、聴衆対応固有の転換（謝罪先行の禁止・承認と謝罪の峻別 ── Fair point. は謝罪ではない）が重なる点が本スケールの署名で、第1柱・感謝詫びの「すみません問題」（負債承認の一原理）が、講演の場では敵意への応答戦略の水準で再来する。",
 # ¶5 横串
 "効く how well 軸は帯で交代する：講述・論構造帯の主軸は一貫性・結束性（設計図・地図・階層のメタ談話）、質疑糸では流暢さが主軸に立つ ── fluency / spontaneity / effortlessly が行の文言に直接入る（306/304/302、副タグ・流暢さ明記）。教示族が全行で流暢さを明示しなかった（言い直しが許される営み）のと正反対の配置で、質疑は言い直しの時間がない一対多の即応の場だから、と読みが対になる。社会言語的適切さは質疑上段（302/298）で、対立管理の作法として効く。質フラグは0件 ── 306/304/302のhow well語彙はいずれも課題持ちの本体行の基準記述であり、課題を持たない技法行（333型）は本スケールに存在しない。これで口頭4スケールすべて0件（Public announcementsを合わせ5スケール）となり、「質フラグは全て書面側」の規則性は第2柱の全スケールで確定する（判断(ac)(x)の反証テスト完了）。最後に、本スケールはC2まで届くが上端は横串に溶けない ── 297も298も課題（聴衆適合・敵意処理）を保持したままC2に立つ。溶解の三例（234/325/351）がいずれもC2到達スケールで起きたことから「C2到達＝溶解」と読みたくなるが、本スケールが反例となり、C2到達は溶解の必要条件であって十分条件ではない ── 判断(o)（B2到達は必要条件であって十分条件ではない）と同じ精緻化が、横串溶解にも要ることが分かる。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 18
    tagged = [n for v in THREADS.values() for n in v]
    assert sorted(tagged) == sorted(ORDER), "主タグが完全分割でない"
    assert all(n in set(ORDER) for v in SUBTAGS.values() for n in v), "副タグに帳簿外のNo"
    th = json.load(open(os.path.join(ROOT, "data", "p2_threads.json"), encoding="utf-8"))["scales"][SCALE]
    assert th["族"] == FAMILY, "FAMILYがp2_threads.jsonの族宣言と不一致"
    assert {k: sorted(v) for k, v in THREADS.items()} == {k: sorted(v) for k, v in th["主タグ"].items()}, "THREADSがp2_threads.jsonと不一致"
    assert {k: sorted(v) for k, v in SUBTAGS.items()} == {k: sorted(v) for k, v in th["副タグ"].items()}, "SUBTAGSがp2_threads.jsonと不一致"
    mp = json.load(open(os.path.join(ROOT, "data", "mode_pairs.json"), encoding="utf-8"))
    sys_rec = next(s for s in mp["systems"] if s["族"] == SYSTEM)
    canon = {p["oral"]: p["written"] for p in sys_rec["pairs"] if p["oral"] in set(ORDER)}
    assert MODE_PAIRS == canon, "並行対がmode_pairs.json（論証族・本スケール分）と不一致"
    # 糸の単調性：論構造（C1同段二行＝299/300）のみ弱単調、他は厳密単調（判断(af)(ag)）
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    for t, ns in THREADS.items():
        lv = [order_lv.index(desc[str(n)]["level"]) for n in ns]
        if t == "論構造":
            assert all(lv[i] <= lv[i + 1] for i in range(len(lv) - 1)), f"糸が単調でない: {t}"
        else:
            assert all(lv[i] < lv[i + 1] for i in range(len(lv) - 1)), f"糸が厳密単調でない: {t}"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        rows.append({
            "mode": "口頭", "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "聴衆への講演（Addressing audiences）── 第2柱第六号範型・全数シート",
        "scope": "全数（18件。口頭18 ── mode一様、(d)裁定1）",
        "type": "第2柱（産出・談話構築）。梯子型＝構築梯子型（第5型・判断(ab)）。初の口頭束スケール：論証族宣言（理由づけ／比較考量／論構造）＋固有糸2本（講述・質疑応答）── 講演族は立てない（判断(ag)）",
        "essence": "聴衆の前で、準備の上に立って話す。器（講述）はB1で中抜きし中身は論証族へ外部化されてC2の聴衆適合で再浮上、質疑応答はA2の支えからC2の敵意処理まで七段の固有糸として並走する。並行対3件（305/359・303/356・299/354）が論証族を4対にし、段差の軸を準備・推敲可能性へ読み直させた（判断(af)）。質フラグ0件 ── 口頭側の反証テスト最終回を通過。",
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p2_addressing_audiences.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
