#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第2柱（産出・談話構築）第二号範型：Creative writing 24件の全数シート。

CEFRカタログ8。判断(y)の様式（共通器10列＋DISCUSSION 5段落・シート＝スケール・
モード間並行対の二行保持＋相互参照）を踏襲し、糸の切り方は本スレッドの裁定（判断(z)予定）に従う：
- 主タグ6（自己提示2／静的描写5／語り9／感情・評価1／批評3／統合4）の完全分割
- 「創作」は糸でなく副次元（虚構が7行を貫く）
- 技法行3件（333/328/326）は糸を立てず質フラグ＋既存糸に係留（(y)(b)フラグ方式の初適用）
- 感情・評価は1行でも糸として保持（並行対336↔242の糸保存のため）

談話課題タグ（THREADS）・副タグ（SUBTAGS）は作業層 ── シートの正式列にしない
（正準記録ファイルの形式＝保留②は本範型の帰納を材料に確定する）。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Creative writing"
ACT = "創作の文章（第2柱：Creative writing）"

# レベル順→No昇順（表示順の正準）
ORDER = [346, 347, 348,
         342, 343, 344, 345,
         339, 340, 341,
         335, 336, 337, 338,
         333, 334,
         331, 332,
         330,
         327, 328, 329,
         325, 326]

# 談話課題タグ（作業層。主タグ＝完全分割）
THREADS = {
    "自己提示":   [346, 342],
    "静的描写":   [347, 348, 339, 335, 331],
    "語り":       [343, 344, 345, 340, 341, 337, 338, 333, 330],
    "感情・評価": [336],
    "批評":       [334, 332, 329],
    "統合":       [327, 328, 325, 326],
}

# 副タグ（作業層。多対多 ── 主タグと直交）
SUBTAGS = {
    "虚構":       [346, 343, 345, 341, 337, 330, 327],  # Creative の実体＝糸でなく副次元
    "結束条件句": [344, 339, 336, 330],                  # 背骨に埋め込まれた結束の条件句列（333で独立行に昇格）
    "ジャンル":   [343, 344, 334, 332, 329, 330, 325],   # 日記・伝記・詩・レビュー・慣習・genre adopted
    "支援条件":   [345],                                 # 辞書・参照 ── 支え型条件句の書面初例
    "質フラグ":   [333, 328, 326],                       # (y)(b)フラグ方式：課題行でなく技法・資源行
}

# モード間並行対（書面側の実装。相手は Sustained monologue: describing experience。338/247=完全同文・型式標本）
MODE_PAIRS = {342: 254, 339: 249, 340: 250, 335: 240, 336: 242, 338: 247, 331: 237}

R = {  # no -> (exponents, scene, howwell, l1, delta)
346: (
 ["My name is Aki. I live in Osaka. I am a student.",
  "This is Tom. Tom is my cat. He can talk. He likes TV."],
 "自分のこと、そして想像上の人物（しゃべる猫でもよい）について、住まいと活動を簡単な句や文で書く。",
 "単文の正確さ（be動詞・一般動詞）。現実と虚構を同じ構文で書ける。",
 "主語の明示とbe動詞の脱落（×I student）。想像上の人物に特別な言語装置は要らない ── He can talk. の一文で虚構が立つ。書くこと自体の敷居を、現実の自分紹介と同じ高さまで下げる。",
 "書面梯子の起点。自己提示糸に虚構の芽が同居する ── Creative writing の「創作」がA1から副次元として寄生する記述文内証拠。",
),
347: (
 ["My room is small. There is a bed and a desk. The wall is blue. I like my room."],
 "部屋の様子をごく簡単な言葉で書く。",
 "There is/are 構文。基本形容詞（大小・色）。",
 "There is/are の導入（×My room is a bed）。日本語の「〜がある」を主語にしない。冠詞 a/the の初出域。",
 "静的描写糸の起点：空間をひとつ選んで属性を並べる。口頭側の起点（259＝日課）と素材が違う ── 書面は目の前の空間から始まる。",
),
348: (
 ["This is my bag. It is red. It is big.",
  "My cup is small and white. It is old, but I like it."],
 "日常の事物（車の色、大小など）を簡単な語と句で書く。",
 "属性形容詞の述語位置での正確な使用（It is red / big / old）。",
 "まず述語位置（It is red.）で属性を言い切る ── 名詞修飾の語順（a big red bag）は次の段でよい。「古いけど好き」の but が最初の論理接続になる。",
 "静的描写糸：部屋という空間（347）→ 個々の事物の属性へ。描写の最小単位＝属性の言明。",
),
342: (
 ["There are three people in my family: my mother, my father and me. We live in a flat near a big park. I finished junior high school last year. Now I study at a high school in the city."],
 "自己紹介文・プロフィール欄などに、家族・住まい・学歴・現在の仕事や学業を一連の文で書く。",
 "There is/are。過去形と現在形の使い分け（finished / study）。「一連の」文の並び。",
 "家族構成は There are X people in my family が定型（×My family is four people）。「実家」「進学する」など日本語の制度語彙を直訳しない ── 口頭254と同型の注意が書面でも立つ（並行対の内部証拠）。",
 "自己提示糸：自分と想像の人物（346）→ 境遇の描写へ話題領域が拡張。",
),
343: (
 ["Mia Storm is a singer. She was born on a small island. She loved the sea and old songs. At ten, she made her first song. Now she sings all over the world.",
  "Rain, rain on my window, / soft and slow. / The cat sleeps, the tea is hot, / and I don't want to go."],
 "想像上の人物の短い伝記を書く。人についての簡単な詩を書く。",
 "伝記の過去形（was born / loved / made）と現在への切り替え（Now she sings）。詩は語の選択と並置・リフレイン。",
 "伝記の時制は過去に固定し、現在との切り替えを Now で明示。詩に「韻を踏まねば」の負荷を持ち込まない ── simple poems は並置と繰り返しで足りる（Rain, rain）。虚構の人物は現実の伝記と同じ型で書ける。",
 "語り糸に虚構がジャンルとして自立する最初の行（346の芽→伝記・詩）。韻文形式は全24件で本行のみ ── 形式固有の副タグとして記録。",
),
344: (
 ["Saturday. I went to the pool with Emi. The water was cold, but we swam for an hour. After that, we ate ice cream because we were very hungry. It was a good day."],
 "日記に、その日の活動（日課・外出・スポーツ・趣味）・人・場所を書く。",
 "接続詞 and / but / because の使い分け（記述文が名指しする最初の結束装置）。過去形の安定。",
 "「〜て、〜て」を and の連打で写さない ── but（逆接）と because（理由）で文と文の関係を選ぶ。because 節を独立文にしない（×Because we were hungry.）。日付・断片（Saturday.）で始めてよいのは日記というジャンルの慣習。",
 "結束の条件句（and, but, because）がここで初めて背骨に入る ── 339 linked sentences → 336 connected text → 333 明示的シグナルへと昇格していく列の起点。ジャンル＝日記（書面固有の私的記録）。",
),
345: (
 ["One day, a small dog found an old key in the park. He took it home. 'What does it open?' he thought. That night, he heard a sound at the door..."],
 "辞書・参考資料（動詞活用表など）を引きながら、物語の書き出しを書く、または物語の続きを書く。",
 "物語の開始定型（One day）。過去形（不規則動詞は表を引いてよい）。地の文とセリフの書き分け。",
 "支援条件（辞書・活用表）は行の一部 ── 暗記していない不規則過去形は引いてよい、というのが記述文の設計。書き出し定型（One day / Once upon a time）の在庫を持つ。地の文＝過去形・セリフや思考＝現在形の混在を恐れない。",
 "語り糸の書面最下段＝支援つき部分構築（導入だけ・続きだけでよい）。口頭260「事前準備」条件の書面対＝支え型条件句（第1柱・条件句二型の支え型が第2柱書面に初出）。341（支援なしの一話完結）への前段。",
),
339: (
 ["I work in a small bakery near the station. The shop opens at seven, so my day starts early. My boss is strict but kind, and the smell of bread makes every morning better."],
 "人・場所・仕事や学習経験など、身の回りの日常的な事柄を、つながりのある文で書く。",
 "linked sentences ── so / and / but による文間接続。一つの話題の一貫。",
 "一文一情報で切ってから接続語で結ぶ（長い一文に詰め込まない）。so（結果）と because（理由）の向きの混同に注意。makes A + 形容詞（無生物主語）は日本語から出にくい接続の型。",
 "静的描写糸：属性の言明（348）→ 接続された記述へ。背骨：simple connectives（344）→ linked sentences ── 結束条件句の第二段。",
),
340: (
 ["Last Sunday, I climbed a mountain with my club. The weather was perfect. I was tired but happy. I want to go again."],
 "出来事・過去の活動・個人的経験のごく短い記述を書く（SNSの投稿・簡単な報告）。",
 "過去形の安定。時間表現（Last Sunday）。感想一文の締め。",
 "過去形の一貫（climbed / was を途中で現在形に戻さない）。締めの感想でも主語を落とさない（×Was fun.）。tired but happy ── 逆接で気持ちの二面を並べる最小の技術。",
 "語り糸：支援つき虚構（345）→ 実体験の自立した短叙述へ。",
),
341: (
 ["In 2100, people live under the sea. My house is a big glass ball. Fish swim past my window every morning. I go to school by small boat. One day, I want to see the sky."],
 "簡単な物語（休暇の出来事や、遠い未来の生活など）を書く。",
 "設定→日常→展望という物語の枠。設定描写の現在形と、will / want to の展望。",
 "未来生活の叙述は現在形で世界を立てる（×全文を will にしない）── 設定の現在形は英語の語りの規約。「休暇の出来事」（実）と「未来の生活」（虚）が同格の例示 ── 実と虚は同じ課題の素材にすぎない。",
 "語り糸：部分構築（345）→ 一話をひとりで完結。虚構副次元が e.g. の中で実体験と同格に明文化される行。",
),
335: (
 ["I grow vegetables on my balcony. Tomatoes are the easiest: they only need sun, water and a little care every day. This year I am also trying carrots, which grow slowly and quietly under the ground. Watching my small garden change every week gives me something the supermarket can never sell."],
 "関心分野内の身近な主題を、率直で詳細に記述する（ブログ・趣味の紹介文）。",
 "話題の展開（一つの主題を細部で支える）。語彙範囲（趣味領域の具体語）。関係詞による情報の追加。",
 "detailed は「長い」ではなく細部の具体（数・頻度・手順）。「〜が好きです。楽しいです」の感想並置から、細部が好意を証明する組み立てへ。無生物主語の締め（Watching ... gives me ...）は日本語から出にくい。",
 "静的描写糸：接続された記述（339）→ 率直で詳細な記述へ。",
),
336: (
 ["Last spring, I spent two weeks helping on a farm in Nagano. At first, I was nervous, because I had never worked outside before. The mornings were cold and my hands hurt, but slowly I started to enjoy the quiet work. When the family thanked me on the last day, I almost cried. I came home tired, and a little lighter."],
 "経験を、感情と反応を織り込みながら、まとまった簡単な文章で綴る（体験記・ブログ・手紙）。",
 "connected text（時系列＋心情の二重線）。感情語彙の解像度（nervous / enjoy / almost cried）。",
 "感情を「楽しかったです」の総括一語で締めず、場面ごとの反応（At first ... but slowly ...）として分散配置する ── 心情曲線を文章の設計に写す。書面は推敲できるぶん、口頭より開示の敷居が下がる（almost cried と書けるか）── 開示量の較差問題の書面側。",
 "感情・評価糸の書面唯一の行 ── 口頭側の5行梯子（261→253→239→242→238）がここ1行に縮約され、以降は統合（327のpersonal style）へ吸収される。背骨：linked sentences（339）→ connected text。",
),
337: (
 ["Last month, I finally took the night train to the north — a trip I had planned for years. I slept badly, woke up at five, and watched the sea appear in the grey morning light. The old town smelled of apples and rain. I walked all day, ate too much at the market, and decided to miss my last train home."],
 "出来事や最近の旅行（現実でも想像でもよい）の記述を書く（旅行記・紀行文）。",
 "過去形の連なりのリズム（短い動詞句の連続）。五感の細部（smelled of ...）。ダッシュによる補足。",
 "「楽しかった」と書かずに事実の列で語る（slept badly / ate too much / decided to miss）── 事実の選択が感想の代わりに働く、書面叙述の基本技術。real or imagined の明文化＝取材なしで書いてよい（想像の旅行記も同じ can-do）。",
 "語り糸：短叙述（340）→ 一つの出来事を場面の連なりとして構成。虚構副次元が「real or imagined」として記述文本文に昇格。",
),
338: (
 ["The last bus left at eleven, and Kana missed it by one minute. She stood in the empty street, angry at herself, when an old taxi stopped in front of her. 'No money,' she said. The driver smiled. 'Then pay me with a story.' She got in, and by the time they reached her street, she had told him about the day she almost became a singer. The driver did not take her money. 'Good story,' he said. 'Finish it some day.'"],
 "一つの物語を、最初から最後まで書く。",
 "物語の弧（発端→転回→結び）。会話文の組み込み（引用符・伝達動詞 said）。過去完了による時間の畳み込み。",
 "地の文＝過去形・セリフ＝現在形の混在規約。オチは説明しない ── Finish it some day. で閉じ、意味づけは読者へ委ねる（口頭247と同じく、推論委任が正しく働く地点）。",
 "語り糸：出来事の記述（337）→ 物語ることそのものが can-do 化（素材からの自立）。並行対247と完全同文＝型式標本。書面ではこの後、時間順の明示（333）→ ジャンル慣習（330）へと組み立ての社会化が進む。",
),
333: (
 ["At first, nobody noticed the small hotel by the sea. Then, one summer, a travel blog wrote about its breakfast. Within a month, the quiet street was full of visitors. Meanwhile, the owner kept baking bread as before. In the end, it was not the crowds that changed the hotel, but the hotel that changed the street."],
 "物語文の中で、時間の順序を標識（At first / Then / Within a month / Meanwhile / In the end）で明確に示す。",
 "一貫性・結束性 ── 時間標識の選択と運用そのもの（質フラグ行）。",
 "日本語の時間順は文の並びだけで読ませられるが、英語の物語文は標識の明示が読者への設計 ── 「そして」の連発を Then / After that / Meanwhile の選択に置き換える。Meanwhile は同時、In the end は評価の予告、と標識自体が構造情報を運ぶ。",
 "344の条件句（and/but/because）に始まる結束の梯子が、独立の can-do 行に昇格 ── 条件句→独立行の昇格（第1柱にない新形）。質フラグ：課題行でなく技法行（結束性軸の運用が物語文に係留された姿）。主タグは語り糸に係留（in narrative text）。",
),
334: (
 ["'Night Bus' is a small film about a long trip home. The story is simple, but the two main actors are excellent, and the ending stayed with me for days. Some parts are slow. Still, I recommend it — especially if you like quiet films about ordinary people."],
 "映画・本・テレビ番組の簡単なレビューを、限られた言葉の幅で書く（レビューサイト・SNS）。",
 "記述（あらすじ一文）＋評価＋推奨の三部構成。limited range の明記＝語彙の幅は問われない。",
 "あらすじを全部書かない（一文で足りる）── 日本語レビュー慣習の「ネタバレ配慮」はそのまま活きる。評価は主語を立てる（I recommend / the actors are excellent）── 「〜と思われる」の無人称化を避ける。",
 "批評糸の起点 ── 口頭対応物のない書面固有糸（(y)(d)が予告した「宙に浮く糸」の実物）。第1柱・意見表明の書面梯子（677・B1）と同帯だが、課題は「立場の応酬」でなく「作品評という談話の単独構築」── 相互参照。",
),
331: (
 ["What makes second-hand bookshops different is not the price but the order — or the lack of it. A new bookshop tells you what is important now; a second-hand shop tells you what people once refused to throw away. Between a cookbook from the sixties and somebody's old dictionary, you find books that no computer would ever have chosen for you. That accident is the whole point."],
 "関心分野に関わるさまざまな主題を、明快で詳細に記述する（エッセイ・特集記事）。",
 "話題の展開（対比の一貫：新刊書店 vs 古書店）。語彙の使いこなし（refused to throw away の精確さ）。セミコロンによる対句。",
 "variety（主題の幅）と clear（観点の一本化）を両立させる ── 詳細は観点に従属させる（口頭237と同型の注意の書面版）。対比構文（not A but B ／ A tells you X; B tells you Y）が書面の解法。",
 "静的描写糸：詳細（335）→ 明快・詳細＋主題の幅へ。この帯から糸の区別が薄れ、統合（327）へ向かう。",
),
332: (
 ["'The Glass Season' is sold as a love story, but it works better as a portrait of a town that is slowly losing its young people. The direction is patient, sometimes too patient: several scenes explain what the previous scene has already shown. Yet the final image — a school gate opening for nobody — says more about the film's real subject than any of its dialogue. Imperfect, but honest, and worth your two hours."],
 "映画・本・演劇のレビューを書く（媒体寄稿・ブログの書評欄）。",
 "評価の根拠づけ（どの場面が・なぜ）。譲歩の運用（Yet ／ Imperfect, but honest）。",
 "「面白かった・泣けた」という効果の報告から、作品の内的根拠（どの場面が・なぜ）で評価を支える構えへ。批判は譲歩とセットで置く（sometimes too patient → Yet ...）── 第1柱・意見表明の緩衝技術が、ここでは読者に対する公正さとして働く。",
 "批評糸：simple review（334）→ 根拠と譲歩を備えたレビューへ。limited range の条件句が脱落してレベルが刻まれる ── 支え型条件句の脱落（第1柱744→742型）の第2柱書面初再現。",
),
330: (
 ["The invitation arrived on a Tuesday, which was strange in itself: nobody sends paper invitations any more. Stranger still, it was addressed to my grandfather, who had died the year before. I went, of course — partly out of curiosity, partly because the house was one our family had once owned. What I found there explained not only the letter, but also why my grandfather had never spoken about his brother."],
 "現実または想像上の出来事・経験を、アイディア間の関係を明示しながら、ジャンルの慣習（ここではミステリの開き方）に従って記述する。",
 "一貫性・結束性（which ／ not only ... but also ／ partly ... partly による関係の標示）。ジャンル慣習の運用（謎の先行提示）。",
 "「関係の明示」は時間順（333）の上位段 ── 因果・対比・付加を標識で刻む。ジャンル慣習は読者との契約（ミステリなら謎を先に置く）── 日本語の起承転結を英語ジャンルの型にそのまま写さない。",
 "語り糸：物語る（338）→ 関係の明示＋ジャンル慣習の遵守へ ── 組み立ての社会化（読者と共有された型への適合）が始まる。背骨：signal sequence（333）→ marking the relationship between ideas ＋ conventions of the genre。虚構副次元：real or imaginary。",
),
327: (
 ["You asked me what the island is like in winter, so let me be honest with you: it is not beautiful in the way the summer photos promise. The boats run twice a week, when the sea allows it. Most shops close by four, and the only cafe keeps a single table by the stove — mine, by now. And yet I have never worked better. The silence here is not empty; it is attentive, like a room that listens. If you come in February, bring warm boots and low expectations. The island will quietly exceed both."],
 "想定した読者に向けて、自信ある個人的で自然な文体で、よく構成され展開された記述文・創作文を書く（随筆・手紙体エッセイ）。",
 "文体の一貫（personal style）。構成と展開（And yet の転回、対句の締め）。読者への適合（相手の問いから開く）。",
 "「読者にふさわしい文体」は敬体・常体の選択ではなく、情報の順序と開示量の設計（You asked me ... と読者の問いから開く）。assured は強い断定ではなく、判断を留保なしで置けること（it is not beautiful ... と言い切って撤回しない）。",
 "統合糸：糸の区別が消え、記述も創作（imaginative texts）も同じ文体的統御の下に置かれる ── 虚構副次元がここで文体へ結晶する。背骨：genre conventions（330）→ well-structured ＋ style appropriate to the reader。口頭の統合（236＝下位テーマの統合）と対照的に、書面の統合は読者適合が核。",
),
328: (
 ["Our town's yearly marathon is, to put it kindly, a work in progress. Last year the lead runner took a wrong turn and finished the 10-kilometre course — twice. The organisers have promised that this year, the arrows will be bigger than the excuses."],
 "記述文・創作文の中に、慣用表現とユーモアを織り込む。",
 "語彙の使いこなし（イディオムの自然さ：to put it kindly ／ a work in progress）。柔軟さ。── 質フラグ行。",
 "ユーモアの型は言語文化に係留される（自虐・誇張・皮肉の効く場所が日英で違う）── C1でも「必ずしも適切に使えない」とCEFR自身が can-do 内部に明記する稀な記述文。滑ることを許容して試す段。日本語の駄洒落の直訳ユーモアは最初に捨てる。",
 "統合糸のライダー行：327（本体）に付随する資源運用の行。can-do 内部に不完全性の但し書き（though ... not always appropriate）を持つ ── C1→C2 の delta（不安定な取り込み→適切な駆使）が記述文の文言に書かれている。質フラグ：技法・資源行。",
),
329: (
 ["The new production of 'The Cherry Orchard' makes one bold decision and then spends three hours apologising for it. Setting the play in a failing seaside hotel is genuinely illuminating: Chekhov's orchard was always less about trees than about the stories a family tells itself about its own past. Yet having found this insight, the director does not trust it — every metaphor is underlined, every silence is filled with music. The cast deserves better; so, frankly, does Chekhov."],
 "文化的行事（演劇・映画・コンサート）や文学作品の、詳細で批評的なレビューを書く。",
 "叙述の正確さ（解釈の言語化：less about A than about B）。評価と根拠の高密度な接続。",
 "critical は「否定的」ではなく「解釈を立てて測る」── 作品の意図を自分の言葉で再構成してから、その基準で成否を測る二段構え。日本語書評の「〜が惜しい」の婉曲を、根拠つきの明言（does not trust it）へ開く。",
 "批評糸の最上段：レビュー（332）→ 解釈枠を自ら立てる批評へ。第1柱・意見表明C1（670：論点の評価・言い直し・反論）と同じ操作を、応酬でなく一人の談話として遂行する ── 批評糸が第2柱に属する理由がこの行で完結する。",
),
325: (
 ["My father repaired watches, which is another way of saying that he argued with time for a living. Customers brought him their stopped afternoons and broken anniversaries, and he returned them ticking. I grew up believing that everything could be fixed if you found a table quiet enough. It took me thirty years and one unfixable spring to learn what he had always known: the point was never to defeat time, only to keep it company."],
 "採用したジャンル（ここでは回想エッセイ）にふさわしい文体で、明快でよどみなく流れる、読者を引き込む物語・経験の記述を書く。",
 "文体とジャンルの一致。流暢さ・一貫性の完全な統御。読者を引き込む効果（engaging）。",
 "engaging は技巧の露出ではなく像の一貫（時計職人＝時間との交渉、という見立てを最後まで通す ── 口頭234の memorable と同じ原理の書面版）。genre adopted の含意＝ジャンルは与えられるものでなく選ぶもの。選んだら文体でその契約を守る。",
 "統合糸の終点：読者適合（327）→ ジャンル文体の完全な統御＋効果へ。can-do 記述が品質語彙（clear, smoothly flowing, engaging）と一体化 ── 梯子の上端が横串へ溶ける現象が両モードで再現（口頭234と対）。",
),
326: (
 ["He was a careful man. He measured twice and cut once; he read contracts to the very end, including his own marriage's; and when the doctor told him to slow down, he asked for the request in writing. So it surprised everyone that he left his money to the town's only jazz band — a group that had never once finished a song at the speed it started."],
 "慣用表現とユーモアを、テキストの効果を高めるために的確に使う。",
 "語彙の使いこなし・柔軟さの最上段。ユーモアの構造的配置（几帳面な人物造形→遺言の落差）。── 質フラグ行。",
 "328との差＝「使える」から「効果のために配置できる」へ。ユーモアが装飾でなく人物造形の装置になる（笑いの位置が意味を運ぶ）。適切さの判定基準が、場の慣習からテキスト内部の必然へ移る。",
 "統合糸のライダー行：325（本体）に付随。328（取り込み・不安定）→ 326（駆使・効果）── 資源運用の梯子の完結。質フラグ：技法・資源行。",
),
}

DISCUSSION = [
 # ¶1 背骨＝構築梯子（書面版）
 "この24件の梯子も、管理課題（第1柱）でなく談話の組み立ての複雑化に宿る ── 構築梯子型（第5型）が第二のスケールでも成立した（この再現を根拠に判断(ab)で本採用）。書面の背骨をCEFR原文語彙に係留すると：simple phrases and sentences（A1）→ a series of（A2・342）→ simple connectives \"and, but, because\"（A2・344）→ linked sentences（A2+・339）→ simple connected text（B1・336）→ clearly signal chronological sequence（B1+・333）→ clear, detailed（B2・331）→ marking the relationship between ideas ＋ conventions of the genre（B2+・330）→ well-structured ＋ style appropriate to the reader（C1・327）→ smoothly flowing, engaging ＋ style appropriate to the genre adopted ＋ exploit ... to enhance the impact（C2・325/326）。口頭の背骨（列挙→線形連鎖→意味づけ→統合→記憶に残る効果）と型は同じだが段の中身が違う：書面梯子は「意味づけ significance」の段を持たず、代わりに結束の明示化→ジャンル慣習→読者適合という社会的次元が入る。目の前の聞き手の記憶を意味づけで稼ぐ口頭に対し、不在の読者への伝達を慣習と構成で保証する書面 ── (y)(d)の「modeの差は解法の差」が、背骨の段名の差として記述文列に刻まれている。もう一つの書面固有の力学は結束条件句の昇格：and/but/because は A2 で条件句として梯子に入り（344）、linked（339）→ connected（336/330）と条件句のまま刻みを進め、B1+ で独立の can-do 行（333）に昇格する ── 条件句→独立行の昇格は第1柱の条件句二型（支え型・負荷型）のどちらでもない第三の形である。",
 # ¶2 糸の構造（主タグ完全分割＋副タグ）
 "糸は主タグ6本の完全分割＋多対多の副タグで切った（本スレッド裁定）：自己提示（346→342。下段専用、第1柱「自己に関する情報提供」と地続き）、静的描写（347/348→339→335→331。属性の言明→接続→詳細→幅と観点）、語り（343/344/345→340/341→337/338→333→330。ジャンルの芽→自立→物語る→順序の明示→慣習）、感情・評価（336のみ）、批評（334→332→329。書面固有）、統合（327/328→325/326）。裁定の含意は三つ。第一に「創作」は糸でなく副次元 ── 虚構は346（imaginary people）→343（伝記・詩）→345→341（未来の生活）→337/330（real or imagined/imaginary）→327（imaginative texts）と7行を貫いて寄生し、独立の梯子を持たない。Creative writing の Creative は課題ではなく、叙述・描写の各糸に A1 から寄生し C1 で文体（personal style）へ結晶する次元である。第二に技法行3件（333/328/326）は糸を立てず質フラグで係留 ──(y)(b)フラグ方式の初適用。第三に感情・評価は1行でも糸として保持 ── 並行対336↔242の糸保存のためで、口頭5行梯子が書面で1行に縮約され統合へ吸収される非対称自体が所見である。そして並行対7組はすべて糸を保存した（342↔254自己提示・339↔249/335↔240/331↔237静的描写・340↔250/338↔247語り・336↔242感情評価）── 糸はモードに先立ち、並行対は糸保存写像である。これは糸の正準化（保留②）の「主タグ完全分割＋副タグ」形式を第二スケールで支持する強い材料になる。",
 # ¶3 mode
 "mode は全行「書面」で一様 ── シート＝スケール裁定どおり。口頭側の対は Sustained monologue: describing experience にあり、並行対7組を本シートの書面側 delta に実装した（型式標本338/247「Can narrate a story.」完全同文）。条件句の書面観察が二つ：345 の支援条件（辞書・動詞活用表）は口頭260「事前準備」の書面対＝支え型条件句の第2柱書面初例で、334→332 の limited range 脱落は支え型条件句の脱落によるレベル刻み（第1柱744→742型）の書面再現 ── 条件句二型の再現域が第2柱まで延びた。批評糸（334→332→329）は口頭対応物を持たない書面固有糸で、(y)(d)が課題別シート再編を退けた根拠「口頭対応物のない糸が宙に浮く」の実物 ── スケール＝シートの器の中でなら、この糸は自然に living space を持つ。第1柱との相互参照は二本：批評糸↔意見・見解の表明の書面梯子（677/670。応酬の対立管理 vs 単独構築の作品評、という分業）、および330/325のジャンル慣習↔社会言語的適切さ（場の慣習でなく読者との契約、という書面版の適切さ）。",
 # ¶4 L1注意の梯子
 "L1注意の三段転換は本シートでも同位置で再現した ── 下段（〜A2）＝統語：be動詞・冠詞・主語の明示に加え、書面固有として接続詞の選択（「〜て、〜て」を and 連打で写さない：344）。中段（A2+〜B1+）＝談話：時制の一貫と切り替え（340/343）、事実の列で語る技術（337：感想語の代わりに事実の選択が働く）、結束標識の選択（333）。上段（B2+〜）＝修辞と開示の再配置：評価の明示とオチの委任の使い分け（338）、開示の書面閾値（336：推敲可能性が開示の敷居を下げる ── 口頭の絵文字外注と対をなす書面側の現象）、ユーモアの文化係留（328）、読者適合としての情報順序の設計（327）。授受（第1柱）→describing experience（第2柱口頭）→本シート（第2柱書面）で三たび同位置（A2+/B1境界とB1+以降）に現れたことで、統語→談話→修辞・開示の三段転換は柱ともモードも超えた日本語話者の一般構造だと言える段階に来た ── 提示レイヤでL1注意を帯で束ねる設計の根拠になる。",
 # ¶5 横串
 "効く how well 軸の主役は一貫性・結束性（背骨の中身がそのまま結束の梯子である）と話題の展開で、第2柱の二スケールで一致した。書面固有の観察は質フラグ3行（333/328/326）の存在：結束性（333）と語彙の使いこなし・柔軟さ（328/326）という横串の軸が、このスケールでは can-do 行として梯子の内部に立っている ── 横串の軸がどこで can-do 化するかは柱・モードごとに違う、という横串埋め込み（判断(d)）の設計への直接の材料である（(y)(b)の軽量点検はフラグ3件：第一号の0件と対照）。正書法（orthographic control）は書面専用の横串だが記述文には一度も現れない ── 完全に横串側で完結している。そして最上段では can-do 記述が品質語彙と一体化し（325：clear, smoothly flowing, engaging）、梯子の上端が横串へ溶ける現象が口頭（234）と書面（325）の両モードで再現した ── 総括系＝束の再記述（(y)(a)）と同じ力学がスケール終端に働くことも二例目となり、C帯の提示は「行為の追加」でなく「質の統御」として設計すべきだという第1柱以来の像が第2柱でも確定した。",
]

def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    # 全数性：スケール所属集合＝ORDER集合（第2柱インベントリ未整備のためスケール所属で代替 ── (c)設計3）
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 24
    # 糸タグの完全分割（作業層の自己検証）＋副タグの実在
    tagged = [n for v in THREADS.values() for n in v]
    assert sorted(tagged) == sorted(ORDER), "主タグが完全分割でない"
    assert all(n in set(ORDER) for v in SUBTAGS.values() for n in v), "副タグに帳簿外のNo"
    # 糸の正準照合（判断(aa)：jsonが正準、pyはassertで追随 ── mode_pairs方式）
    th = json.load(open(os.path.join(ROOT, "data", "p2_threads.json"), encoding="utf-8"))["scales"][SCALE]
    assert {k: sorted(v) for k, v in THREADS.items()} == {k: sorted(v) for k, v in th["主タグ"].items()}, "THREADSがp2_threads.jsonと不一致"
    assert {k: sorted(v) for k, v in SUBTAGS.items()} == {k: sorted(v) for k, v in th["副タグ"].items()}, "SUBTAGSがp2_threads.jsonと不一致"
    # 並行対：書面側キーは本シート所属、相手は口頭スケール（正準は data/mode_pairs.json。
    # 判断(ac)で系構造化 ── 本シートは叙述系のpairsと照合する）
    mp = json.load(open(os.path.join(ROOT, "data", "mode_pairs.json"), encoding="utf-8"))
    sys_rec = next(s for s in mp["systems"] if s["name"] == "叙述系")
    canon = {p["written"]: p["oral"] for p in sys_rec["pairs"]}
    assert MODE_PAIRS == canon, "並行対がmode_pairs.json（叙述系）と不一致"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        if no in MODE_PAIRS:
            delta += f"（モード間並行対：口頭 describing experience No.{MODE_PAIRS[no]}）"
        rows.append({
            "mode": "書面", "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "創作の文章（Creative writing）── 第2柱第二号範型・全数シート",
        "scope": "全数（24件。書面24 ── mode一様、(d)裁定1）",
        "type": "第2柱（産出・談話構築）。梯子型＝構築梯子型（第5型。本採用＝判断(ab)・CEFRカタログ8）。談話課題糸＝自己提示／静的描写／語り／感情・評価／批評／統合（作業層）＋副タグ（虚構・結束条件句・ジャンル・支援条件・質フラグ）",
        "essence": "一人で、不在の読者に向けて、記述・物語・レビューを書き上げる。梯子は組み立ての複雑化（接続→結束の明示→ジャンル慣習→読者適合→効果）に宿り、「創作」は糸でなく全糸を貫く副次元である。並行対の口頭側は describing experience（型式標本338/247）。",
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}

if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p2_creative_writing.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
