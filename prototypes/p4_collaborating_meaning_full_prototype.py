#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第4柱（仲介）第二号範型：Collaborating to construct meaning 18件の全数シート（CEFRカタログ46、判断(cs)⑧／(ct)）。

概念の仲介・コミュニケーションの仲介（二群・7スケール99件）の器をこの一枚で確定する（第一号＝テクストの仲介の器は判断(cs)）。
- 段＝場の条件×役割。テクストの仲介の「渡す中身の深さ（七層）」の代わりに、**役割**（話し合いの中で自分の言葉が果たす働き）が段の中身になる。
  深さの軸はこの群には立たない（渡すものがテクストの中身でなく、話し合いそのものだから）。
- シート＝スケール（mode一様＝「口頭」）。章名〔仮〕「意味を共に構築する」（p4_inventory の章〔仮〕）
- 列10は不変。第4柱・概念系での読み替え：
    exponents … 一要素＝二行以上。相手のラベル（Colleague A / Friend / Group member / Chair …）に続けて英語の相手の言葉、
                 You (to the group / to Colleague A): に続けて自分が話し合いに入れた英語の言葉。
                 第一号と同じ形で、入力が「テクスト」から「他の人の寄与」に、出力が「渡した言葉」から「場に入れた言葉」になる。
    scene     … 「受けるもの」＝どんな話し合いの、どんな場面か（記述文の条件句＝準備できれば・簡単な言葉で、を含む）と、相手から来ているもの
    howwell   … 「渡すもの」＝役割（自分の言葉が話し合いに対して果たす働き）と、その段でその役割を果たすことの意味
    l1        … 「日本語話者の落とし穴」＝自分が場に入れた言葉の側の失敗だけ（判断(cs)⑤）。判定は規律6-1の産出版（四水準）。
                 本シートの6欄＝953 相槌「そうですね」を *That's right* で返す／954「〜したほうがいい」を *had better* で出す／950「どうして」を裸の *Why?* で投げる／
                 947「賛否両論ある」で締める／941 異論を「ちょっと違う気がする」の婉曲で留める／944 他人の発言を一人ずつ「〜さんは〜と言った」で並べる
    delta     … 前の段から。やりとりする言葉の側（第1部）との対は散文で先に記録（判断(ai)③）。収載は一括
- **四欄は書物の本文として書く**（読者語彙。帳簿語を出さない）
- 条件（CONDITION、完全分割、級順）：準備できれば → 簡単な言葉で → 条件なし
- 役割（ROLE、完全分割、級順。語彙はスケールごと）：出す → 示す → 確かめる → 尋ねる → 整理する → 発展させ量る → 結ぶ
- 語彙裁定（判断(s)）：例文は相手の英語と You 行の英語を照合対象とする。ラベルと括弧は照合外。
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Collaborating to construct meaning"
ACT = "意味を共に構築する（第4柱：Collaborating to construct meaning）"
MODE = "口頭"

ORDER = [955, 953, 954, 952, 950, 951, 948, 949, 945, 946, 947, 942, 943, 944, 939, 940, 941, 938]

CONDITION = {
    "準備できれば":   [955],
    "簡単な言葉で":   [953, 954],
    "条件なし":       [952, 950, 951, 948, 949, 945, 946, 947, 942, 943, 944, 939, 940, 941, 938],
}
ROLE = {
    "出す":         [955, 954],              # 自分の考えと提案を場に入れる
    "示す":         [953],                   # ついていっていることを示す
    "確かめる":     [952, 951],              # 相手が分かったか、自分が分かったかを確かめる
    "尋ねる":       [950, 946],              # 理由を、反応を、尋ねる
    "整理する":     [948, 949, 942, 944, 939],  # 的と論点を立て、まとめ、軌道に戻す
    "発展させ量る": [945, 947, 943, 940, 941],  # 他人の考えを発展させ、比べ、評価し、異を唱える
    "結ぶ":         [938],                   # 寄与を結んで合意へ
}

R = {  # no -> (exponents, scene=受けるもの, howwell=渡すもの, l1, delta)
955: (
 ["Group member: So — the party. Ideas?\nYou (to the group, from a note you prepared): I have one idea. A picnic in the park. Is it good? What do you think?"],
 "仲間との簡単な話し合い。自分の考えをあらかじめ用意しておける（言う文をメモに書いておく、前の晩に考えておく）。",
 "出す ── 用意した考えを一つ場に入れ、ごく簡単な語で、他の人はどう思うかと尋ねる。話し合いに加わる最初の形で、出す言葉はその場で作らない。",
 "",
 "この章の起点。やりとりする言葉のA1の段と変わらない短さの文で、違いは、考えのあとに「どう思うか」を添えて、話し合いを他の人へ渡すこと ── 自分の用事ではなく、みんなで決めることの最初の一手。「提案・誘い・計画の相談」の章はA2（No.478）から始まり、A1の段を持たない。",
),
953: (
 ["Colleague A: … so if we start at nine, we finish before lunch.\nYou (to Colleague A): OK. Nine. And then lunch?\nColleague A: Yes.\nYou: Good."],
 "仲間の簡単な話し合い。他の人が話を進めていて、自分は聞いている側。",
 "示す ── 短い一言と時折の問いで、ついていっていることを示す。中身を足すのではなく、聞いているという合図を場に入れる段。",
 "日本語の相槌「そうですね」「はい」をそのまま *That's right.* *Yes.* で返すと、英語では相手の内容に同意したと受け取られ、ついていっているだけの合図にならない。英語で聞いている合図は *OK. / Right. / I see.* のような、同意を含まない短い語で出す。",
 "出す（No.955）に対して、こちらは何も出さずに場にいる段。同じA2に、簡単な提案を出す段（No.954）が並び、二つで「入れる」と「ついていく」の両側がA2に揃う。",
),
954: (
 ["Friend: We need a present for Anna.\nYou (to the group): How about a book? She likes reading. Or flowers?"],
 "仲間との話し合い。何かを決めようとしている。",
 "出す ── 簡単な言い方で提案を出す。用意なしに、その場で。",
 "日本語の「〜したほうがいいと思います」をそのまま *We had better buy a book.* *You had better…* で出すと、英語では警告か命令に聞こえ、簡単な提案にならない。英語の提案は *How about…? / We could… / Why don't we…?* の形で出す。",
 "用意した一つの考え（No.955）から、その場の提案へ。「提案・誘い・計画の相談」の章のA2・A2+（No.478・475＝何をするかを相談し、提案をして受ける）と同じ言葉で、ここでは話し合いの一手として立つ。",
),
952: (
 ["Colleague A: Tomorrow, then.\nYou (to Colleague A): So we meet at the station, not the office. Is that clear? Do you know which exit?\nColleague A: The north one?\nYou: Yes, the north exit."],
 "二人か少人数の話し合い。自分が何かを言い、相手がそれを分かったかどうかを確かめたい場面。",
 "確かめる ── 相手が自分の言ったことを分かったかを、適切な問いで確かめる。言いっぱなしにしないこと。",
 "",
 "ここから、言葉が自分と相手の間を往復する。「明確化・繰り返しの要求」の章が聞き返す側を立てるのに対して、こちらは言った側から相手の理解を確かめる。",
),
950: (
 ["Group member: I think we should drop the Friday session.\nYou (to the group member): Why do you say that? What's the problem with Friday?"],
 "グループの話し合い。誰かが意見を出した。",
 "尋ねる ── 意見を出した人に、その理由を尋ねる。意見を意見のまま置かず、理由を場に出させる。",
 "日本語の「どうしてですか」は一語で柔らかく聞けるが、そのまま裸の *Why?* で投げると、英語では詰問か反対に聞こえ、理由を出してもらう問いにならない。英語では *Why do you say that? / What makes you think so?* のように、理由を聞いていることが分かる形にする。",
 "確かめる（No.952）から尋ねるへ。相手の理解でなく、相手の理由を場に出させる。「意見・見解の表明」の章が意見を言う側、ここはその理由を引き出す側。",
),
951: (
 ["Colleague A: … and the budget goes to the training, not the equipment.\nYou (to Colleague A): Training, not equipment — so we keep the old machines for now?\nColleague A: Exactly."],
 "グループの話し合い。考えが積み上がっている途中。",
 "確かめる ── 相手の言ったことの一部を繰り返して、互いの理解が合っていることを確かめ、考えの積み上がりを軌道に乗せたままにする。繰り返しが、話を前へ進める道具になる。",
 "",
 "相手の理解を確かめる段（No.952）に対して、自分の理解を確かめる段。繰り返しは「明確化・繰り返しの要求」の章では聞き返しの道具だが、ここでは互いの理解を合わせて話し合いを進める道具になる。",
),
948: (
 ["Group member: Where do we start?\nYou (to the group): OK, our job is to choose the venue by Friday. The main question is cost — we have two hundred pounds. So: which places are under that?"],
 "率直な協働の作業。これから話し合いを始めるところ。",
 "整理する ── 的を述べ、解決すべき主な論点を簡単に説明して、作業を組み立てる。話し合いの枠を自分の言葉で立てる最初の段。",
 "",
 "尋ねる（No.950）から整理するへ。相手の考えに働きかけるのでなく、話し合い全体の枠を立てる。同じB1+に、話し合いを枠に戻す段（No.949）が並ぶ。",
),
949: (
 ["Colleague B: … and my cousin went there once, it was raining, and —\nYou (to the group): So the question is still: is it under two hundred? Does anyone know the price?"],
 "率直な協働の作業の話し合い。話が逸れる、広がる。",
 "整理する ── 問い、一言のコメント、簡単な言い換えで、話し合いの焦点を保つ。逸れた話を、争わずに枠へ戻す。",
 "",
 "枠を立てる段（No.948）の、保つ側。立てた問いに戻す言葉を、問いとコメントと言い換えで出す。",
),
945: (
 ["Colleague A: Maybe we could ask the new people to present something.\nYou (to the group): I like that — and if each of them picks one thing they learned in their first month, it stays short and it's useful for us too."],
 "グループの話し合い。他の人の考えや意見が出ている。",
 "発展させ量る ── 他の人の考えや意見を、さらに発展させる。自分の案を出すのでなく、出ている案を伸ばす。",
 "",
 "ここから、自分の言葉が他人の考えに手を加える。B1までの段が、出す・示す・確かめる・尋ねる・整理すると、自分と他人の考えを別々に扱っていたのに対して、B2の三段は他人の考えに直接働きかける。",
),
946: (
 ["Chair: Any other ideas?\nYou (to the group): Here's my suggestion: we move the deadline a week. Anna, from the client's side, how would that look? Tom, does it cause you a problem on the delivery side?"],
 "グループの話し合い。自分の考えを出す番。",
 "尋ねる ── 自分の考えをグループに示し、他の人がそれぞれの立場から反応できるような問いを添える。出すと尋ねるが一つになる段。",
 "",
 "出す（No.955・954）と尋ねる（No.950）が一つの発話で立つ。反応を求める相手を一人ずつ、その人の立場で指名するのが、A1の「どう思うか」との違い。",
),
947: (
 ["Group member: We can't agree on the date.\nYou (to the group): The case for June is the weather and the price; the case for September is that more people can come. If more people is what matters, September — but we book now, while it's still cheap."],
 "グループの話し合い。意見が二つに割れている。",
 "発展させ量る ── 問題の二つの側を考え、賛否の論拠を出し、解決か妥協を提案する。割れた意見を自分の言葉で並べたうえで、一歩先へ出す。",
 "日本語の話し合いでは、割れた意見を「どちらにも一理ある」「賛否両論ありますが」と並べて締めるのが礼にかなった形で、その型を持ち込むと、*Both sides have a point.* で止まり、解決か妥協を提案するという段の課題に届かない。英語でこの段に求められるのは、論拠を両側で並べたうえで、どちらに、どういう形で、と言い切ること。",
 "他人の考えを伸ばす段（No.945）の隣に、割れた考えを量る段。「論の提示」の章のB2（No.280＝利点と欠点を挙げて見解を説明する）と同じ組み立てが、ここでは話し合いをまとめるために立つ。",
),
942: (
 ["Colleague B: … so the price is the thing.\nYou (to the group): Before we go on — the real issue isn't the price, it's the timeline. Two things we have to keep in mind: the client's launch date, and that half the team is away in August."],
 "複雑な作業の話し合い。論点が複数あり、どれが主かが見えにくい。",
 "整理する ── 複雑な作業で解決すべき主な論点と、考慮すべき重要な側面を際立たせる。何が主で何が従かを、自分の言葉で立てる。",
 "",
 "枠を立てる段（No.948）の、複雑な作業への拡張。率直な作業では的と論点が一つだったものが、ここでは複数の論点から主を選び出す。",
),
943: (
 ["Group member: The smaller venue is cheaper, but it only takes forty.\nYou (to the group): So if we go with the smaller venue, we'd need two sessions. I could take the morning one. And we should tell the client this week, not after the booking."],
 "グループでの決定と問題解決。考えが共同で作られていく。",
 "発展させ量る ── 考えを出し、共に発展させ、細部を説明し、次に取る行動を提案して、共同の決定と問題解決に寄与する。考えを出すところから行動の提案まで、一続きで。",
 "",
 "伸ばす（No.945）と量る（No.947）が、決定と行動の提案まで一続きになる。B2+の三段はどれも、話し合いを決定へ運ぶ段。",
),
944: (
 ["Chair: We've been going round for a while.\nYou (to the group): Let me pull this together. Anna wants June for the price; Tom and Lee want September for attendance; nobody's against the smaller venue. So the only open question is the month — and the price difference is about three hundred."],
 "グループの話し合い。発言が積み上がり、整理が要る。",
 "整理する ── 他の人の発言を報告し、要約し、敷衍し、異なる見解を比較検討して、話し合いの組み立てを助ける。言われたことを自分の言葉で並べ直す段。",
 "日本語では他人の発言を「田中さんは〜とおっしゃっていました。鈴木さんは〜と言っていました」と一人ずつ順に並べる報告の型が自然で、その型を持ち込むと、要約でなく発言の読み上げになり、比較検討まで届かない（*Mr Tanaka said… Mr Suzuki said… Ms Lee said…*）。英語の要約は、立場でまとめる（*Anna wants June; Tom and Lee want September*）── 誰がではなく、何がいくつ出ているかで並べ直す。",
 "枠を保つ段（No.949）の、積み上がった発言への拡張。報告・要約・敷衍・比較検討の四つの動詞がここで揃い、C1（No.939）で同じ四つが行動の決定の枠へ移る。",
),
939: (
 ["Colleague C: … and that's my third option.\nYou (to the group): OK. We've heard three options. Let me frame the decision: the question is whether we want speed or coverage. If speed, Anna's plan; if coverage, Tom's. Lee's point about the budget applies to both. Can we decide on that basis?"],
 "行動の方針を決める話し合い。一人の相手かグループ。",
 "整理する ── 他の人の発言を報告し、要約し、敷衍し、複数の見解を比較検討して、行動の方針を決めるための話し合いの枠を作る。要約が決定の枠になる。",
 "",
 "No.944の四つの動詞が、決定の枠を作るために使われる。B2+が話し合いを整理する段なら、C1は話し合いを決定へ向ける段。",
),
940: (
 ["Colleague A: We could outsource the testing.\nYou (to the group): The risk there is control — we'd see problems a week late. The saving is real, though. If we outsource, we need a weekly check built in; otherwise I'd keep it in-house."],
 "協働の話し合い。問題、課題、提案が出ている。",
 "発展させ量る ── 問題、課題、提案を評価して、進む道を決める。評価が、提案を取るか落とすかを決める段。",
 "",
 "量る（No.947）から評価するへ。賛否の論拠を並べるだけでなく、提案の価値を判断して、進む道を決める。",
),
941: (
 ["Colleague A: So we go for the cheaper supplier.\nYou (to Colleague A): That doesn't square with what you said earlier — you wanted delivery by March, and the cheaper one can't do March. Which matters more?"],
 "合意に至ろうとしている話し合い。考えの中に食い違いがある。",
 "発展させ量る ── 考えの不整合を際立たせ、合意に至る過程で他の人の考えに異を唱える。合意のために、異を唱える段。",
 "日本語では異論を「ちょっと違う気がするのですが」「それはどうでしょうか」と婉曲で留めるのが普通で、その型を持ち込むと *I feel it's a little different…* と曖昧なまま止まり、何が食い違っているかが場に出ない。英語でこの段に求められるのは、食い違いを名指すこと（*That doesn't square with what you said about March*）── 言い方は穏やかでよいが、中身は言い切る。",
 "評価する（No.940）の隣に、異を唱える段。他人の考えへの働きかけの、いちばん強い形。「同意・不同意」の章の不同意が自分の立場を言う段なら、ここでは相手の考えの中の食い違いを指す。",
),
938: (
 ["Chair: Can we agree on something today?\nYou (to the group): Let me put the pieces together. Anna's point — cost — and Tom's — coverage — aren't actually in conflict if we take Lee's suggestion of two shorter sessions: cheaper than one long one, and more people can come. Does that work for everyone?"],
 "解決か進む道について、合意を作ろうとしている話し合い。",
 "結ぶ ── さまざまな寄与を要約し、評価し、結びつけて、解決か進む道についての合意を助ける。寄与を結ぶことが、この章の終点。",
 "",
 "この章の終点。整理する（要約）・量る（評価）・結ぶ（結びつける）が一つになる。「やりとりを運営する」の章のC2（No.957・958＝役を使い分け、底流を見抜く）が場を導く側の終点なら、こちらは場の一員として考えを結ぶ側の終点。",
),
}

DISCUSSION = [
    # 1 梯子
    "この章の梯子は、テクストを渡す章の梯子とは違う形をしている。入力の側の条件は三段で尽きる ── 準備できれば（No.955）→ 簡単な言葉で（953・954）→ 条件なし（952以上の15段）── A2+から上に但し書きが一つもない。段を区切るのは条件ではなく、役割、すなわち自分の言葉が話し合いに対して果たす働きである。役割を級順に並べると七つになる ── 出す（955・954）→ 示す（953）→ 確かめる（952・951）→ 尋ねる（950・946）→ 整理する（948・949・942・944・939）→ 発展させ量る（945・947・943・940・941）→ 結ぶ（938）。A1からB1までの役割は、自分の考えと他人の考えを別々に扱う（出す・示す・確かめる・尋ねる）。B1+で話し合いの枠を立てる役割（整理する）が加わり、B2から自分の言葉が他人の考えに手を加える（発展させ量る）。C2で、寄与を結んで合意へ運ぶ。役割は級に対して単調でない：整理するはB1+からC1まで五段にわたり、尋ねるはB1とB2に割れる。渡す中身の深さ（七層）はこの章に立たない ── 渡しているのはテクストの中身ではなく、話し合いそのものだから。",
    # 2 CEFRの企図
    "増補版第4章は概念の仲介を二対の尺度に分ける ── グループで協働する（仲間との協働を促す／意味を共に構築する）と、グループの作業を導く（やりとりを運営する／概念的な話し合いを促す）。対の一つめは場と条件を作る尺度、二つめは新しい意味と概念を作る尺度で、この章は協働する側の、意味を作る方である（p.109）。原典が挙げる鍵概念は、グループの一員として考えを刺激し発展させること ── 他人の考えと意見をさらに発展させる、共同で考えを作る、問題と提案を評価する、理由を尋ねる、不整合を際立たせる。本書の読みはこれを役割の梯子として級順に並べたもので、七つの役割の語はCEFRの動詞から取ってある。この章の記述文に Language A／B はなく、話し合いは一つの言語の中で起きる ── 英語の話し合いの中で、英語で寄与する。",
    # 3 境目と対
    "やりとりする言葉の側に、この章の段と同じ言葉を使う段がある ── 提案（954＝「提案・誘い・計画の相談」のNo.478・475）、不同意（941＝「同意・不同意」の章の段）、賛否の論拠（947＝「論の提示」のNo.280、B2）。理由を尋ねる（950）に当たる段は、やりとりする言葉の二十二の章にはない ── 向こうにあるのは理由を言う側（「意見・見解の表明」のNo.514＝簡単な理由を添えて意見を分からせる）だけで、他人に理由を言わせる言葉は仲介の側に置かれている。違いは、向こうが自分の用事を果たすための言葉であるのに対して、こちらは話し合いを前へ進めるための言葉であること。同じ *How about…?* が、向こうでは自分の誘いで、こちらではグループの決定の一手になる。同じ概念の仲介の「仲間との協働を促す」（14行）とは、向こうが場を開く側（人を招き入れる、意見を求める）、こちらが意味を作る側で、CEFRの一対の二つ。「やりとりを運営する」（13行）は場を導く側で、C2の終点どうし（938↔957・958）が、一員として結ぶ／導く者として役を使い分ける、と向きが違う。全1,224件に同文はない。対の収載は第4部の範型二枚のあと一括（判断(cs)⑦）。",
    # 4 落とし穴
    "日本語話者の落とし穴は、この章では自分が場に入れた言葉の側に立ち、六段に欄がある。聞いている合図の「そうですね」を *That's right* で返して同意になる（953）。「〜したほうがいい」を *had better* で出して警告になる（954）。「どうして」を裸の *Why?* で投げて詰問になる（950）。割れた意見を「賛否両論ある」で締めて提案に届かない（947）。他人の発言を一人ずつ「〜さんは〜と言った」で並べて要約にならない（944）。異論を「ちょっと違う気がする」で留めて食い違いが場に出ない（941）。六つのうち四つ（953・954・950・941）は、日本語では柔らかく通じる短い決まり文句が、英語では別の働き ── 同意、警告、詰問、曖昧 ── になる形で、話し合いの一手を出す言葉の持ち込みに集まる。穴のない十二段は、役割の難しさが話し合いの組み立ての側にあり、自分の言葉の形で外す失敗が日本語の形で指せない段である。",
    # 5 何がこの梯子を測るか
    "この梯子を測るものさしは、テクストを渡す章と違って、入力の条件ではない（A2+で尽きる）。測るのは役割 ── 自分の言葉が話し合いの中で何をするか ── と、その言葉が他人の考えにどれだけ手を加えるかである。A1の「どう思うか」からC2の「結びつける」まで、自分の考えを出すだけの段から、他人の考えを伸ばし、量り、異を唱え、結ぶ段へ上がる。段を上がるとは、自分の言葉が、自分のものから話し合いのものになっていくことである。この章が第1部のやりとりの章と違うのは、同じ提案や不同意の言葉が、自分の用事でなく話し合いの進行のために使われる点で、それが仲介の名の意味である。上端が「結ぶ」で閉じるのは、場の一員にできる最後のことが、他人の寄与どうしを結んで合意の形を示すことだからで、それより先 ── 場を導き、役を使い分ける ── は「やりとりを運営する」の章の終点になる。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 18
    for name, m in (("CONDITION", CONDITION), ("ROLE", ROLE)):
        tagged = [n for v in m.values() for n in v]
        assert sorted(tagged) == sorted(ORDER), f"{name}が完全分割でない"
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    for name, m in (("条件", CONDITION), ("役割", ROLE)):
        prev_min = -1
        for c, nos in m.items():
            lv = sorted(order_lv.index(desc[str(n)]["level"]) for n in nos)
            assert lv[0] >= prev_min, f"{name}の列が級順でない: {c}"
            prev_min = lv[0]
    assert ORDER == sorted(ORDER, key=lambda n: (order_lv.index(desc[str(n)]["level"]), n)), "ORDERが級順→No昇順でない"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        for e in ex:
            assert "\nYou (to " in e, f"例に You (to …): の行がない No.{no}"
        rows.append({
            "mode": MODE, "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "意味を共に構築する（Collaborating to construct meaning）── 第4柱第二号範型・全数シート",
        "scope": "全数（18件。口頭18 ── mode一様）",
        "type": "第4柱（仲介）・概念の仲介。梯子＝役割の列（出す→示す→確かめる→尋ねる→整理する→発展させ量る→結ぶ）、入力の側の条件は三区分（準備できれば→簡単な言葉で→条件なし）でA2+で尽きる。深さ（七層）は立てない。四欄（scene＝受けるもの・howwell＝渡すもの・l1・delta）は書物の本文そのもの。Language A／Bなし。",
        "essence": "グループの一員として、自分の言葉で話し合いを前へ進める。段を区切るのは役割 ── 自分の考えを出すところから、他人の考えを伸ばし、量り、異を唱え、結ぶところへ。同じ提案や不同意の言葉が、自分の用事でなく話し合いの進行のために使われる。",
        "axes": {"条件": CONDITION, "役割": ROLE},
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p4_collaborating_meaning.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
    print("落とし穴欄:", sum(1 for r in sheet["rows"] if r["l1"]), "/ 空欄:", [r["no"] for r in sheet["rows"] if not r["l1"]])
