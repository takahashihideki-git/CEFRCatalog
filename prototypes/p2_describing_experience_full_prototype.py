#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第2柱（産出・談話構築）第一号範型：Sustained monologue: describing experience 28件の全数シート。

CEFRカタログ7。設計判断は引き継ぎ書§2に追記予定の(y)系（4論点(a)〜(d)の裁定）に基づく：
- (a) 総括系17件は留置＝範型母集団115件
- (b) 篩なし／ジャンル×談話課題の二層／構築梯子型（仮・第5梯子型）
- (c) 第一号＝本スケール。共通器10列＋DISCUSSION 5段落を維持、
      exponents＝最小充足テクスト、delta＝組み立ての複雑化の読み
- (d) シート＝スケール（mode一様）、モード間並行対（型式標本247/338）は二行保持＋相互参照

談話課題タグ（THREADS）は作業層 ── シートの正式列にしない（正準記録ファイルの形式は範型完成後に判定）。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Sustained monologue: describing experience"
ACT = "叙述・経験の語り（第2柱：Sustained monologue: describing experience）"

# レベル順→No昇順（表示順の正準）
ORDER = [260, 261, 258, 259, 254, 255, 256, 257,
         248, 249, 250, 251, 252, 253,
         240, 241, 242, 243, 244, 245, 246, 247,
         239, 237, 238, 235, 236, 234]

# 談話課題タグ（作業層・正準化前。二層設計(b)の実地検証用）
THREADS = {
    "自己提示":   [260, 258, 254, 256],
    "静的描写":   [259, 255, 249, 252, 240, 237, 235],
    "語り":       [257, 248, 250, 251, 241, 243, 244, 245, 246, 247],
    "感情・評価": [261, 253, 239, 242, 238],
    "統合":       [236, 234],
}

# 副タグ（作業層。¶2の交差記録を判断(aa)で機械可読へ遡及昇格 ── 正準は data/p2_threads.json）
SUBTAGS = {
    "語り":       [242],  # 感情・評価糸の242は語りと交差
    "感情・評価": [252],  # 静的描写糸の252は評価の芽と交差
}

# モード間並行対（(d)裁定2。相手は Creative writing。247/338=完全同文・型式標本）
MODE_PAIRS = {254: 342, 249: 339, 250: 340, 240: 335, 242: 336, 247: 338, 237: 331}

R = {  # no -> (exponents, scene, howwell, l1, delta)
260: (
 ["My name is Ken. I am ten years old. This is my father and my mother.",
  "I am from Japan. I like dogs."],
 "事前に準備した上で、簡単な語と定型表現で自分のこと（名前・年齢・家族・国籍）を述べる。",
 "定型表現の正確な再生。語彙範囲は最小。",
 "主語の明示（日本語の無主語文の直訳で動詞から始めない）。be動詞の脱落（×I ten years old）。「準備できること」が条件 ── 暗記した定型句の束でよい。",
 "構築梯子の起点：準備した定型句・孤立句。自己提示糸の最下段（第1柱「自己に関する情報提供」の帳簿と地続き）。",
),
261: (
 ["I am happy!", "I am tired."],
 "身体言語（表情・身ぶり）を添えて、happy / tired のような簡単な形容詞で今の気持ちを表す。",
 "基本感情形容詞の正確な使用。伝達の大半は身体言語が担う。",
 "感情の言語化を身体言語に外注しすぎない ── 語彙が1語でも「言う」こと自体が課題。-ed/-ing の区別はまだ射程外（第1柱・感情の表出の下段と同域）。",
 "感情・評価糸の起点。定型句一つ＋非言語 ── 談話の組み立て以前の粒。",
),
258: (
 ["I am Ken. I am a student. I live in a small town. I play tennis after school."],
 "自分のこと・していること・住んでいる所を述べる。",
 "単文の正確さ（語順・be動詞・一般動詞の現在形）。",
 "単文を並べる勇気 ── 複文を作ろうとして止まるより、短い文を積む。三単現・冠詞（a student）の脱落に注意。",
 "Pre-A1（準備した定型句）→ 準備なしで言える単文へ。まだ孤立文の並置で、接続はない。",
),
259: (
 ["I get up at seven. I eat breakfast with my family. I go to school by bus. In the evening, I watch TV and do my homework."],
 "事前に準備した上で、簡単な語と基本句を使い、日常生活の簡単な様相を一連の単文で描写する。",
 "単文の連なり（series of simple sentences）。時間表現（at seven / in the evening）。",
 "習慣の現在形を過去形と混ぜない。日本語の「〜て、〜て」連鎖を and で全部つながず、文を切る。前置詞（by bus / at seven）の選択。",
 "孤立文（258）→「一連の」単文へ ── 連なりの最初の一段。接続詞はまだ and 程度。静的描写糸（日常の様相）の起点。",
),
254: (
 ["There are four people in my family: my father, my mother, my sister and me. We live in a small flat near the station. I finished school two years ago, and now I work at a hotel."],
 "家族・住環境・学歴・現在または直近の仕事を描写する。",
 "There is/are 構文。過去形と現在形の使い分け（finished / work）。",
 "家族構成は There are X people in my family が定型（×My family is four people）。「実家」「就職する」など日本語の制度語彙を直訳しない（work at 〜で足りる）。",
 "自己提示糸：名前・年齢（260/258）→ 境遇の描写へ話題領域が拡張。モード間並行対：Creative writing No.342（書面）とほぼ同文言 ── 同一課題の口頭・書面並行の証拠。",
),
255: (
 ["My friend Sato is tall and very kind. He always helps me.",
  "Our town is quiet. It has a big park and an old bridge. I like walking there."],
 "人・場所・持ち物を簡単な言葉で描写する。",
 "形容詞の選択と位置。has / there is の使い分け。",
 "冠詞と単複が描写で一斉に顕在化する（a big park / an old bridge）。日本語の「静かな町」の感覚で the をつけ忘れる・つけすぎる。人物描写は外見＋性格＋一言の行動でよい。",
 "静的描写糸：日常の様相（259）→ 対象別の描写（人・場所・物）へ。まだ simple terms ── 解像度でなく対象の幅が広がる段。",
),
256: (
 ["I am good at cooking. I make dinner every day, and my curry is famous in my family. But I am not good at sports — I can't run fast."],
 "得意なこと・不得意なこと（スポーツ・ゲーム・技能・科目など）を述べる。",
 "be good at + 動名詞。can / can't による能力の言い換え。",
 "「〜が苦手」を weak で直訳しない（not good at が自然）。謙遜の定型（「大したことないですが」）を前置きしない ── 英語の自己提示は直叙が基本。",
 "自己提示糸：境遇（254）→ 能力の自己評価へ。評価の芽（good at）が入るが、対象は自分に限られる ── 好悪の説明（253）への前段。",
),
257: (
 ["This weekend I am going to visit my grandmother. On Saturday we are going to make lunch together. On Sunday I am going to watch a movie with my friends."],
 "週末や休暇に何をする予定かを短く描写する。",
 "be going to による予定の表現。曜日・時の副詞句の前置。",
 "予定は be going to / 現在進行形 ── will の乱発（その場の決定の含み）と区別。日本語の「〜するつもり」を毎文 think で訳さない。",
 "語り糸の起点（未来方向）：時間軸に沿って出来事を並べる最初の形。過去の語り（248〜）と対をなす。",
),
248: (
 ["Last Sunday we went to the sea. First, we swam for an hour. Then we had lunch on the beach. After that, we played volleyball. Finally, we watched the sun go down. It was a great day."],
 "物語を語る、または何かを簡単な列挙（list of points）で描写する。",
 "列挙の談話標識（First / Then / After that / Finally）。過去形の一貫。",
 "「〜て、〜て、〜て」の連鎖を談話標識に置き換える ── 列挙は接続詞でなく標識で刻む。過去の語りに現在形（歴史的現在）を混ぜない。締めの一文（It was a great day）で閉じる習慣。",
 "構築梯子の要の一段：単文の連なり（A2）→ **列挙（list of points）**へ。出来事が順序を持ち、標識で構造化される。語り糸が過去方向に立つ。",
),
249: (
 ["I work in a small office near my house. The people there are friendly, and we often eat lunch together. Next to our building there is a park. When it is sunny, I read there after lunch."],
 "身の回りの環境の日常的な様相（人・場所・仕事や学業の経験など）を描写する。",
 "空間表現（near / next to）。when 節による条件・習慣の接続。",
 "場所の描写は「近くに〜がある」＝ there is 構文へ。日本語の「職場の人」を coworker と訳そうとして止まらない（the people there で足りる）。",
 "静的描写糸：対象別の描写（255）→ 環境のまとまった描写へ。文どうしが場所・習慣で緩やかにつながり始める。モード間並行対：Creative writing No.339（書面・linked sentences）。",
),
250: (
 ["We had a festival at our school last week. Many families came. We sang songs, played games and sold food. Everyone had a good time."],
 "出来事や活動について、短い基本的な描写をする。",
 "過去形の並列。and による動詞句の列挙。",
 "出来事の報告は「いつ・どこで」を先に置く（last week / at our school）。動詞の過去形（sang / sold）の不規則変化がまとめて顕在化する帯。",
 "語り糸：列挙の型（248）を、自分の体験でない出来事（行事）にも適用 ── 語る対象の一般化。モード間並行対：Creative writing No.340。",
),
251: (
 ["I usually run in the morning before work — it wakes me up. Last year I ran in a small race for the first time. Next spring I want to try a longer one, so I am training three times a week."],
 "計画・取り決め・習慣・日課・過去の活動・個人的経験を描写する。",
 "習慣（現在形）・過去・予定の三時制の混在管理。頻度表現。",
 "一つの談話の中で時制を切り替える最初の課題 ── 習慣は現在形、済んだことは過去形、これからは want to / be going to。日本語は時制標識が薄いため、切り替えの合図（usually / last year / next spring）を言語側で明示する。",
 "語り糸：単一の出来事（248/250）→ 習慣・過去・計画をまたぐ時間の幅へ。三時制の管理が「組み立て」の課題として初めて立つ。",
),
252: (
 ["My new phone is bigger than my old one, and it is much faster. But the old one was easier to use, and the battery was better. I still keep it in my desk."],
 "簡単な描写の言葉で、物や持ち物について短く述べ、比較する。",
 "比較級（bigger than / easier）。one による名詞の言い換え。",
 "比較は「AよりB」の語順転倒（B is 比較級 than A）を体で覚える。than の後の省略（my old one）。「〜のほうが」を more で全部作らない（一音節は -er）。",
 "静的描写糸に**比較**が加わる ── 第1柱で「比較の三つ巴蝶番」（提案467・意見473・問題説明511）をなした課題の、第2柱側の最下段。描写が評価の入口になる。",
),
253: (
 ["I like this cafe because the coffee is good and the music is quiet. I can read here for hours. But I don't like the chairs — they are hard, and my back hurts after an hour."],
 "何かについて、どこが好きか・嫌いかを説明する。",
 "because による理由接続。好悪＋根拠の対。",
 "like の目的語落ち（×I like.）に注意。理由を「なんとなく」で止めず一つ言い切る ── because 節一つで足りる。好悪の直言は失礼ではない（対象が物・場所なら緩衝は不要）。",
 "感情・評価糸：気持ちの表出（261）→ **好悪の説明**へ。第1柱「意見・見解の表明」評価相（No.480/448、A1〜A2）と同域の課題が、産出側では理由つきの短い談話として現れる ── 柱間の相互参照点。",
),
240: (
 ["I have played the guitar for five years. I practice at night, after everyone goes to bed, so I play quietly. My guitar was cheap, but it has a warm, soft sound. For me, playing is not about being good — it is the easiest way to forget a busy day."],
 "関心分野のさまざまな身近な主題について、率直な描写をする。",
 "現在完了（継続）。理由・対比の接続（so / but）。話題の展開。",
 "「5年やっています」＝現在完了 for が最初の山。趣味の説明で「下手ですが」と謙遜から入らない ── 事実＋自分にとっての意味の順で組む。",
 "静的描写糸：simple terms（A2帯）→ 率直だが**まとまった**描写へ。文が理由・対比で有機的につながり、最後に一言の意味づけが芽生える（238への遠い前段）。モード間並行対：Creative writing No.335。",
),
241: (
 ["Let me tell you about my trip last autumn. First, we took an early train to the mountains. Then we walked for about three hours to a small lake. We had lunch there, and the water was so clear that we could see the fish. On the way back, it started to rain, so we ran to a little shop and drank hot tea. Finally, we caught the last bus home, wet but happy."],
 "関心分野の主題について、論点を直線的に並べる形（linear sequence of points)で、かなり流暢に率直な叙述・描写を続ける。",
 "流暢さ（本スケールで唯一 fluently が明記される行）。線形連鎖の維持。so 〜 that 構文。",
 "止まらずに続けることが課題 ── 完璧な文より流れ。冒頭の予告（Let me tell you about 〜）で聞き手に枠を渡す。日本語の相槌待ちの語り（聞き手と共同構築する語り）から、一人で運ぶ monologue への転換点。",
 "構築梯子の要の一段：列挙（list, 248）→ **線形連鎖（linear sequence）**へ。点の並びが線になり、流暢さの要件が加わる。口頭固有の課題（時間拘束の中で結束を保つ）が最も裸で現れる行。",
),
242: (
 ["Last month I gave my first presentation at work. Before it, I was really nervous — my hands were shaking, and I could not remember my first line. But when people started to nod, I felt calmer. In the end, my boss said it was clear and well prepared. I felt proud, and most of all, I felt glad that I did not run away from it."],
 "経験について詳しく語り、気持ちや反応を描写する。",
 "叙述の正確さ（感情の解像度）。出来事と内面の交互織り。",
 "出来事だけ語って感情を落とさない ── 日本語の語りは評価・感情を聞き手の推論に委ねがちだが、英語の語りは evaluation（どう感じたか）を明示する節を要求する。感情語彙を very+基本語に潰さない（nervous / calm / proud / glad の使い分け ── 第1柱・感情の表出B1帯と同じ課題）。",
 "語り糸：出来事の連鎖（241）→ **出来事＋感情・反応の二重線**へ。detailed の中身は情報量でなく内面の解像度。モード間並行対：Creative writing No.336。第1柱・感情の表出（叙述解像度の梯子）との柱間接続点。",
),
243: (
 ["Something strange happened on my way home yesterday. The bus stopped very suddenly, and some bags fell from the seats. A car had turned into our street without looking. Nobody was hurt, but we had to wait for the police for almost an hour. I finally got home at nine, two hours late."],
 "予期しない出来事（例：事故）の詳細を語る。",
 "過去完了（had turned）による因果の遡り。出来事の順序再構成。",
 "起きた順でなく「気づいた順」で語るときの時制管理（過去完了で一歩戻る）。「大変でした」で総括して詳細を省かない ── 何がどの順で起きたかを言い切る。",
 "語り糸：準備できる話題（旅行・行事）→ **準備できない出来事**へ。台本のない語りで線形連鎖（241）を保てるかが試される段。",
),
244: (
 ["The film is about an old man who travels across the country to find his brother. On the way, he meets people who slowly change him — a young driver, a singer, a boy with a dog. I expected a sad ending, but the last scene is full of hope. I almost cried, and I thought about the film for days."],
 "本や映画の筋を語り、自分の反応を描写する。",
 "プロット再話の現在形規約。関係詞による人物の圧縮描写。",
 "筋の再話は**現在形**が規約（The film is about 〜 / he meets 〜）── 日本語話者は「見た」記憶に引かれて過去形にしがち。あらすじと自分の反応（過去形）の時制の切り替えが山。ネタバレの管理（結末は印象だけ言う）。",
 "語り糸：自分の経験 → **他者（作品）の物語の再話**へ。語る素材が受容（第3柱：読む・観る）から供給される ── 柱間接続の新形（受容→産出の変換点）。反応の描写は感情・評価糸と交差。",
),
245: (
 ["My dream is to open a small bakery in my hometown. I want to get up early, bake bread, and talk with my customers every morning. It will not be easy — I need money and experience. But I am saving now, and I hope I can start in five years."],
 "夢・希望・野心を描写する。",
 "to 不定詞による願望の対象化。現実の障害との対比構成。",
 "夢を語るのは自慢ではない ── 「いつか〜できたら」の仮定形に逃げず、want to / My dream is to で言い切る。障害（It will not be easy）を添えると現実味が出る、という談話の型。",
 "語り糸：過去（243）・現在の習慣（251）に続き、**未来・非現実方向**の語りが立つ。257（予定）の一般化＝時間軸が人生スケールへ伸びる。",
),
246: (
 ["Imagine one morning nobody in your city can speak. People write notes and draw pictures. The trains still run, the shops still open, but everything is slow and quiet. At first it feels strange, even a little scary. Then something interesting happens: people start to look at each other — really look — for the first time."],
 "現実の、または想像上の出来事を描写する。",
 "聞き手の巻き込み（Imagine 〜）。現在形による仮構の提示。",
 "想像の話は Imagine / Let's say で枠を宣言してから入る ── 枠なしで仮構を始めると聞き手が事実と取り違える。日本語の「〜としたら」を毎文 if で訳さず、枠宣言の後は直叙でよい。",
 "語り糸：real or imagined ── 現実の語り（243）と想像の語り（245の先）が**同じ組み立て**で扱える段。虚構への通路＝Creative writing（創作固有糸）への窓口。",
),
247: (
 ["Once there was a young fisherman who lived by the sea. Every day he caught just enough fish for his family. One evening he found a gold bottle in his net, and a voice inside said, 'You have one wish.' The fisherman thought for a long time. Then he smiled and said, 'I wish for tomorrow to be like today.'"],
 "物語を語る。",
 "物語の定型（Once there was 〜）。直接話法の導入。結末の効き。",
 "Once there was / One evening という物語の開始定型を持つ ── 日本語の「昔々」に相当する在庫。会話文（direct speech）の導入で語りに声が入る。オチを説明しない（結末の意味は聞き手に渡す ── ここでは推論委任が正しい側に働く）。",
 "語り糸の自立点：素材（経験・作品・想像）から独立に**「物語る」という行為そのもの**が can-do になる。モード間並行対の型式標本：Creative writing No.338と**完全同文** ── 語りが mode を選ばないことの帳簿上の証拠。",
),
239: (
 ["Finishing the race made me really happy — but not because of my time. In the middle of it, I almost stopped. My legs hurt, and I could not see the end. When I finally crossed the line, I understood something: I am stronger than I thought. That is why this race means so much to me."],
 "経験したことについての気持ちをはっきり表現し、その気持ちの理由を説明する。",
 "感情＋理由の明示的接続（That is why 〜）。not because A but B の焦点化。",
 "「感動しました」で止めない ── 何が・なぜそう感じさせたかを because / That is why で言語化する。理由の言語化は日本語では野暮になりうるが、英語の語りでは誠実さとして働く（推論委任の逆転が起きる帯）。",
 "感情・評価糸：気持ちの描写（242）→ **気持ちの理由の説明**へ。evaluation が語りの付属物から主役になる ── 238（意味づけ）への直接の前段。",
),
237: (
 ["Photography is my hobby, and what interests me most is how light changes a city. In the early morning, the streets look soft and almost private, and long shadows give ordinary buildings real character. By noon, the same corner can look flat and crowded. That is why I keep returning to one place: the subject never changes, but the picture never repeats itself."],
 "関心分野に関わる幅広い主題について、明快で詳細な描写をする。",
 "話題の展開（一つの観点で談話を貫く）。語彙範囲（描写の解像度）。",
 "detailed は「長い」ではなく「観点が通っている」── 一つの主張（光が街を変える）に細部を従える組み立て。形容詞の解像度（soft / flat / crowded）を上げ、good / nice への潰れを避ける。",
 "静的描写糸：率直な描写（240）→ **明快で詳細な描写**へ。wide range（主題の幅）と観点の一貫が同時に要求される。モード間並行対：Creative writing No.331。この帯から糸の区別が薄れ始める（描写と語りが観点の下で合流）。",
),
238: (
 ["Moving abroad at twenty-five changed the direction of my life. At the time, it simply felt like an adventure. Looking back, it was the year I learned to live with uncertainty. Small daily battles — opening a bank account, making my first phone call in English — taught me more about myself than any success has. That year did not just give me memories; it gave me a way of facing the unknown."],
 "出来事や経験の個人的な意味を詳しく描写する。",
 "叙述の正確さ（意味づけの言語化）。時間の二視点（At the time / Looking back）。",
 "経験を教訓へ言語化する型（It taught me 〜 / It gave me 〜）を持つ ── 日本語の「いい経験になりました」という総括定型のままでは意味の中身が空く。当時の視点と現在の視点を往復させる時制管理。",
 "感情・評価糸の最上段：理由の説明（239）→ **人生の中での意味づけ（personal significance）**へ。構築梯子の「意味づけ」段の型式標本。語りの素材が同じでも、この段だけが経験を再解釈する。",
),
235: (
 ["The slow decline of local shopping streets is usually blamed on online stores, but the reality is more complicated. Rents rise while the population ages; the owners' children move away and choose other careers; and the customers who say they love the old shops quietly buy elsewhere. Any one of these pressures might be survivable. Together, they form a silent weight that empties one shop after another."],
 "複雑な主題について、明快で詳細な描写をする。",
 "複数要因の並列と統合。セミコロンによる列挙の高密度化（口頭では休止・列挙イントネーション）。",
 "複雑さを「難しい語彙」で出さない ── 要因を並べ、最後に一段抽象して束ねる（Together, they form 〜）という組み立てで出す。通説の提示→反転（usually blamed on 〜, but）という開き方の型。",
 "静的描写糸の最上段：主題が身近（240）→幅広（237）→**複雑**へ。描写対象が具体物から構造（複数要因の絡み）になり、統合（236）の一歩手前に立つ。",
),
236: (
 ["Let me describe how our town changed after the factory closed — in three stages. First, the economic stage: jobs disappeared, and young families moved away. Second, the social stage: the summer festival lost its volunteers, and the school lost a whole class. But there is a third stage, which visitors rarely notice: empty buildings slowly turned into studios and cafes, and newcomers arrived with unfamiliar ideas. So the closing of the factory was an ending — but it was also, unexpectedly, a beginning."],
 "下位テーマを組み込み、特定の点を展開し、適切な結論で締めくくる、入念な叙述・描写をする。",
 "構造の予告（in three stages）。下位テーマの明示的分節。結論の締め（So 〜）。",
 "構造を**先に宣言**する（in three stages / First... Second...）── 日本語の「聞けば分かる」構成から、予告で聞き手の地図を先に渡す構成へ。結論は要約でなく再解釈（ending でもあり beginning でもある）で締める。",
 "統合糸：糸ごとの梯子がここで合流し、**下位テーマの統合＋結論の締め**という組み立てそのものが can-do になる。総括系No.227（C1）と同文言域 ── (a)裁定の「束の再記述」の束ねられる側。",
),
234: (
 ["My grandmother's kitchen was a small country with its own laws. Time moved differently there: it was measured not in minutes but in the colour of onions in the pan. She never opened a recipe book; she read the food the way sailors read the sky. And when the lid finally came off, the steam carried the whole history of our family into the room."],
 "明快でよどみなく流れる、入念で、しばしば記憶に残る描写をする。",
 "文体（比喩・リズム）。流暢さと構成の完全な自動化。聞き手への効果。",
 "memorable は装飾でなく**像の一貫**（台所＝国、料理＝航海という見立てを最後まで通す）。比喩の混在（mixed metaphor）が最上段の落とし穴。ここまで来ると誤りでなく効果が評価軸になる ── how well の語彙では測り切れない段。",
 "構築梯子の終点：統合（236）→ **聞き手の記憶に残る効果**へ。can-do の記述が品質語彙（clear, smoothly flowing, memorable）とほぼ一体化する ── 梯子の上端が横串（一貫性・流暢さ）へ溶ける現象（第1柱C2帯と同型）。",
),
}

DISCUSSION = [
 # ¶1 背骨＝構築梯子（仮・第5梯子型）
 "この28件の梯子は、管理課題（第1柱の管理梯子型）にも型の履行（定型履行型）にも宿らない。宿っているのは**談話の組み立ての複雑化**である：準備した定型句・孤立句（Pre-A1）→ 単文の連なり（A1）→ 話題領域の拡張（A2）→ 列挙 list of points（A2+・248）→ 線形連鎖 linear sequence（B1・241）→ 出来事＋感情の二重線と理由づけ（B1〜B1+・242/239）→ 意味づけ personal significance（B2・238）→ 下位テーマ統合と結論の締め（C1・236）→ 聞き手の記憶に残る効果（C2・234）。各段はCEFRの原文語彙（list / sequence / detailed / significance / integrating sub-themes / memorable）がそのまま段名になる。これを**構築梯子型（仮）**として第5の梯子型に立てる ── 確定は本範型の承認と ladder_templates への追記をもって行う。deltaの読みは「組み立ての複雑化」、背骨はこの段名列、型固有必須項目は（i）段名のCEFR原文語彙への係留（ii）談話課題糸の記録（iii）モード間並行対の記録、型式標本は247（語りの自立）と238（意味づけ）。",
 # ¶2 糸の構造（二層設計の実地）
 "スケール内部には談話課題の糸が4本＋統合が走る（作業タグ、正準化は課題層ファイル新設時）：**自己提示**（260→258→254→256。第1柱「自己に関する情報提供」と地続きの下段専用糸）、**静的描写**（259→255→249→252→240→237→235。対象の幅→比較→観点の一貫→複雑さ、と解像度が上がる）、**語り**（257→248→250→251→241→243→244→245→246→247。未来の予定に始まり、過去・習慣・不測の出来事・作品の再話・想像を経て、247「物語る」で素材から自立する）、**感情・評価**（261→253→239→242→238。気持ちの表出→好悪の説明→理由→意味づけ。第1柱「感情の表出」（叙述解像度）および「意見・見解の表明」評価相（253↔480/448）との柱間接続点）、**統合**（236→234。B2以降、糸の区別は観点の下に薄れ、C1で下位テーマ統合として合流する）。糸は多対多で交差する（242は語り×感情、252は描写×評価の芽）── 第1柱の「比較の三つ巴蝶番」と同型の現象がスケール内でも起きており、二層（ジャンル×談話課題）の設計を支持する。",
 # ¶3 mode
 "mode は全行「口頭」（Sustained monologue）で一様 ── シート＝スケール（mode一様）の裁定どおり。書面側の対は Creative writing にあり、**モード間並行対7組**（254↔342・249↔339・250↔340・240↔335・242↔336・247↔338・237↔331、いずれも同一レベル）を確認、うち**247/338「Can narrate a story.」は完全同文＝型式標本**。対はスケール再掲重複対（第1柱466/512型）の第2柱・モード間版として二行保持＋相互参照で扱う。口頭固有の課題は**時間拘束**：推敲できない一方向の時間の中で結束を保つ（241の fluently が本スケール唯一の流暢さ明記であることが内部証拠）。書面側は同じ課題を推敲可能性と明示結束（Creative writing 333 の chronological signalling）で解く ── mode の差は課題の差でなく解法の差、というのが並行対の読みである。なお第1柱の窓口 No.680（書面・オンライン投稿）は本スケール（口頭）でなく叙述**課題**を指すと読むのが正確で、課題層の正準化時に参照の張り替えを検討する。",
 # ¶4 L1注意の梯子
 "L1注意は三段の質的転換をなす。**下段（〜A2）＝統語**：主語の明示・be動詞・単文を並べる勇気・冠詞と単複（描写で一斉顕在化）。**中段（A2+〜B1）＝談話**：「〜て、〜て」連鎖から談話標識による列挙へ（248）、時制の一貫と切り替えの明示（251/243）、相槌待ちの共同構築から一人で運ぶ monologue への転換（241）、プロット再話の現在形規約（244）。**上段（B1+〜）＝修辞と開示**：evaluation の明示 ── 日本語の語りは感情・意味を聞き手の推論に委ねるが、英語の語りは「どう感じたか・何を意味したか」の言語化を要求する（242/239/238）。ただし247（物語のオチ）では推論委任が正しい側に働く ── 委任の全面禁止でなく、**どこで明示しどこで委ねるかの再配置**が上段の本体である。この三段転換は第1柱・授受の「統語→談話」転換の産出版で、位置（A2+/B1境界と B1+以降）も一致する。",
 # ¶5 横串
 "効く how well 軸の主役は**一貫性・結束性**と**話題の展開**であり、後者が主軸に立つのは全カタログを通じて本スケールが初 ── 第1柱の主軸（社会言語的適切さ・文法的正確さ）との明確な対照をなす。叙述は対立を含まないため社会言語的適切さの関与は低く、代わりに**叙述の正確さ**（感情の解像度：242/239）と**語彙範囲**（描写の解像度：237。第1柱・感情の表出と共有）、**流暢さ**（241）が段ごとに前景化する。最上段では can-do 記述が品質語彙とほぼ一体化し（234：clear, smoothly flowing, memorable）、梯子の上端が横串へ溶ける ── (a)裁定で見た総括系＝束の再記述と同じ力学がスケール内部の終端にも働いている。なお(b)裁定1の軽量点検の結果、本スケールに「質のみ行」は無い（234も memorable な**描写をする**という行為核を保持）── フラグ0件。",
]

def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    # 全数性：スケール所属集合＝ORDER集合（第2柱インベントリ未整備のためスケール所属で代替 ── (c)設計3）
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 28
    # 糸タグの完全分割（作業層の自己検証）
    tagged = [n for v in THREADS.values() for n in v]
    assert sorted(tagged) == sorted(ORDER), "糸タグが完全分割でない"
    # 糸の正準照合（判断(aa)：jsonが正準、pyはassertで追随 ── mode_pairs方式）
    th = json.load(open(os.path.join(ROOT, "data", "p2_threads.json"), encoding="utf-8"))["scales"][SCALE]
    assert {k: sorted(v) for k, v in THREADS.items()} == {k: sorted(v) for k, v in th["主タグ"].items()}, "THREADSがp2_threads.jsonと不一致"
    assert {k: sorted(v) for k, v in SUBTAGS.items()} == {k: sorted(v) for k, v in th["副タグ"].items()}, "SUBTAGSがp2_threads.jsonと不一致"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        if no in MODE_PAIRS:
            delta += f"（モード間並行対：Creative writing No.{MODE_PAIRS[no]}）"
        rows.append({
            "mode": "口頭", "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "叙述・経験の語り（Sustained monologue: describing experience）── 第2柱第一号範型・全数シート",
        "scope": "全数（28件。口頭28 ── mode一様、(d)裁定1）",
        "type": "第2柱（産出・談話構築）。梯子型＝構築梯子型（仮・第5型、CEFRカタログ7）。談話課題糸＝自己提示／静的描写／語り／感情・評価／統合（作業層）",
        "essence": "一人で、時間軸と観点をもった談話を組み立てて、経験・出来事・対象を聞き手に手渡す。梯子は組み立ての複雑化（定型句→列挙→線形連鎖→意味づけ→統合→効果）に宿る。第1柱の窓口はNo.680（経験・出来事の叙述）。",
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}

if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p2_describing_experience.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
