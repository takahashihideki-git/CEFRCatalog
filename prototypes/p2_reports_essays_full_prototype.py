#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第2柱（産出・談話構築）第四号範型：Reports and essays 18件の全数シート。

CEFRカタログ9・判断(ac)。論証族の書面スケール（束：書面論証＋報告＋出典管理＋構成）。裁定：
- 糸7本の完全分割（立論1／理由づけ1／比較考量1／論構造4＋報告5／出典統合2／構成4）
- 論証族4糸は口頭（putting a case）と共有＝糸はモードに先立つ（第二系での再現）
- 並行対は356↔277のみ（同文級・型式標本）。354↔278・358↔280は梯子段差
- 351＝質フラグ（構成の技法行、C2本体行350のライダー ── Creative 325+326と同配置）
- 355の支援条件（推敲・修正の機会）＝支え型条件句が書面長文の上端C1に回帰
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Reports and essays"
ACT = "報告と小論（第2柱：Reports and essays）"
FAMILY = ["論証族", "教示族"]  # 判断(ad)：束スケール＝複数族の糸を同時に使う。教示族の糸（報告／手順357／説明353）を持つ
SYSTEM = "論証族"

# レベル順→No昇順（表示順の正準）
ORDER = [366, 367, 364, 365, 361, 362, 363, 359, 360, 356, 357, 358, 353, 354, 355, 350, 351, 352]

# 談話課題タグ（正準は data/p2_threads.json、本表はbuild()内assertで照合）
THREADS = {
    "立論":     [367],
    "理由づけ": [362],
    "比較考量": [358],
    "論構造":   [359, 356, 354, 350],
    "報告":     [364, 365, 363],
    "手順":     [357],
    "説明":     [353],
    "出典統合": [360, 352],
    "構成":     [366, 361, 355, 351],
}
SUBTAGS = {
    "ジャンル":     [364, 365, 361, 355, 350],
    "結束条件句":   [366],
    "支援条件":     [355],
    "質フラグ":     [351],
    "比較考量":     [362],
    "静的描写":     [357],
}

# モード間並行対（書面側の実装。相手は putting a case。356/277＝同文級・型式標本）
MODE_PAIRS = {356: 277}

R = {  # no -> (exponents, scene, howwell, l1, delta)
366: (
 ["I like my town. It is small, but it is nice. There is a river, and in summer we swim there. Then we eat ice cream by the water. I love summer because we can swim every day."],
 "関心のある身近な主題について、and・because・then のような接続語で文をつないだ簡単なテキストを書く。",
 "接続語（and / because / then）の選択。単文を並べてからつなぐ、という順序。",
 "「〜て、〜て」を and の連打で写さない ── then（順序）・because（理由）で文間の関係を選ぶ。because 節を独立文にしない。書き出しに凝らず、単文で始めてよい。",
 "書面梯子の起点＝接続語。Creative writing 344（and/but/because）と同段の装置 ── 書面の背骨は系（叙述／論証）をまたいで接続から始まる。構成糸の最下段。",
),
367: (
 ["I watched a film about a dog last night. I think it is a very good film. The story is simple, but I cried at the end. The music is beautiful too."],
 "個人的関心のある話題（生活様式・文化・物語など）について、基本的な日常語彙で印象や意見を書く。",
 "I think の枠と印象語（good / beautiful / simple）。感想と意見の書き分けはまだ求められない。",
 "印象は短くてよいが立場は書き切る（I think it is a very good film.）── 「よかったです」の一語で止めない。but で感想に片影を添える（simple, but I cried）のが最初の陰影。",
 "立論糸の書面起点＝印象と意見を書き言葉で残す。口頭287と同帯（A2）だが条件句（相手の忍耐）を持たない ── 書面は待ってくれる媒体そのものであり、mode差（解法の差）が条件句の不在に現れる。",
),
364: (
 ["Weekly Report — Sales Team / Date: 12 May / This week we visited four shops. Two shops ordered the new product. We could not visit Green Store because the manager was away. Next week: visit Green Store and send the new price list."],
 "日常的な事実情報を伝え、行動の理由を述べる、標準的な定型書式のごく簡単な報告を書く。",
 "定型書式（見出し・日付・短文の並び）への充填。事実と理由（because）の最小接続。",
 "書式が構成を肩代わりする ── 見出し・日付・箇条の型を先に置き、埋める。「〜しました」の連続を恐れない（報告の文体は単調でよい）。できなかったことも理由つきで書く（could not ... because）。",
 "報告糸の起点＝定型書式（conventionalised format）が組み立てを代行する段。構成をジャンルから借りる ── 自前の構成（構成糸）が育つ前の支え。",
),
365: (
 ["OUR SCHOOL GARDEN (poster) / [photo] What we grow: tomatoes, beans and flowers. / [photo] Who works there: Class 2B, every Friday. / Why it matters: we eat what we grow, and the garden makes our school beautiful."],
 "写真と短い文章ブロックを使って、短い報告やポスターで話題を提示する。",
 "テキストブロックの機能分担（What / Who / Why の見出し化）。写真との説明関係。",
 "文章で全部を語らない ── 写真に語らせ、テキストは見出しと一〜二文で添える。名詞句見出し（What we grow:）は文でなくてよい、というのが掲示ジャンルの慣習。",
 "報告糸：構成の負荷を紙面設計と視覚素材へ逃がす ── 定型書式（364）と並ぶ、もう一つの借り物の構成。",
),
361: (
 ["My Favourite Season (essay) / Winter is my favourite season, and I have three reasons. First, I love snow — the town becomes quiet and white. Second, the food is best in winter: hot soup and mikan by the stove. Finally, winter has New Year, when my whole family meets. For these reasons, winter is special to me."],
 "関心のある話題について、短く簡単なエッセイを書く。",
 "エッセイの最小三部構成（主張→理由の本体→結び）。列挙標識（First / Second / Finally）。",
 "序文・本体・結びの器を最初に立てる ── 書きながら構成を探さない。結び（For these reasons）は本体の理由を回収する定型で足りる。パラグラフの頭に主張文（topic sentence）を置く習慣をここで作る。",
 "構成糸：接続語（366）→ エッセイという器の獲得。ジャンル（essay）が構成の型を与える最後の段 ── 以降は構成を自分で設計する側に回る（355序論結論→351論理構造）。",
),
362: (
 ["Should our school use tablets instead of books? Tablets are light, and students can find information fast. On the other hand, they are expensive, and some students play games in class. Books are cheap and easy on the eyes, but heavy. I think we should use both: books for reading, tablets for research, because each is good at a different job."],
 "個人的関心のある時事的な主題について、簡単な言葉で利点と欠点を並べ、意見を述べて正当化するテキストを書く。",
 "利欠点の対比標識（On the other hand / but）と、考量を受けた意見の正当化（I think ... because）。",
 "利欠点は対で書く ── 良い点だけ並べて結論に飛ばない。on the other hand は選択肢間、but は同一物の中の対比。結論は both のような折衷でもよいが、because で理由を必ず付ける。",
 "理由づけ糸の書面起点＝利欠点の列挙と意見の正当化が一行に同居 ── 口頭で三行（286比較→284理由→282列挙）に分かれた課題を一行に折り畳む、束スケールの実例（副タグ・比較考量）。",
),
363: (
 ["In the last three months, we received 42 customer messages about the new app. Most messages (31) are about login problems. Nine ask for a dark mode. In my view, we should fix the login first, because it stops people using the app at all."],
 "自分の分野の身近な事柄について、蓄積した事実情報をある程度自信をもって要約・報告し、意見を添える。",
 "数量の正確な要約（42 / 31 / Nine）と、要約→報告→意見の三段の連結。",
 "数字は文に埋め込む（Most messages (31) are ...）── 表を貼って終わりにしない。意見は In my view で報告から区画して始める ── 事実と意見の混線は報告の信用を落とす。",
 "報告糸：定型書式（364）から自前の要約へ。要約は仲介（第4柱・テクストの仲介）と境界を接するが、ここでは自分の報告のための要約 ── 他者の理解を助ける仲介と区別（柱間相互参照）。",
),
359: (
 ["(essay) Should the city centre be car-free? Supporters point to cleaner air and safer streets, and the experience of other cities supports them. Opponents answer that shops depend on drivers — yet deliveries can be scheduled, and car parks can move to the edge. Of the three options — full closure, weekend closure, and a charge — the charge balances both sides best: traffic falls, but access remains. On balance, the arguments for action outweigh those against."],
 "ある見解への賛否の理由を挙げ、さまざまな選択肢の利点・欠点を説明しながら、論を展開するエッセイや報告を書く。",
 "賛否両論の展開（Supporters / Opponents ... yet）と選択肢の考量、結論の宣言（On balance）。",
 "反対側の論も自分の文章で立ててから返す（Opponents answer that ... — yet ...）── 賛成材料だけの「主張文」にしない。On balance のような考量の締め語で、比較したことを結論に刻む。",
 "論構造糸の書面起点＝賛否両論の展開と選択肢の考量が一体化 ── 口頭280（同じB2）の考量を論の展開に折り畳む。束スケールでは糸の複数課題が一行に同居する。",
),
360: (
 ["The three reports agree on the facts but not the cause. The city survey shows rents rising fastest near the new line; the university study links this to shorter commutes; the newspaper's interviews add that landlords improved their buildings early. Read together, they suggest the line raised rents through expectation before it opened."],
 "複数の情報源からの情報と論点を統合する。",
 "情報源ごとの帰属の明示（the survey / the study / the interviews）と、統合の一文（Read together）。",
 "出典を主語にする（The city survey shows ...）── 「〜と言われている」の主語なし伝聞に流さない。統合は並記で終えず、Read together, they suggest ... の一文で自分の像を結ぶ。",
 "出典統合糸の起点＝複数源をひとつの像へ。仲介（第4柱）との境界に立つが、ここでは自分の論のための統合（他者の理解のための仲介と区別）。",
),
356: (
 ["(report) This report argues that the fall in sales has one main cause: the January price change. Three findings support this, and the second is decisive. First, sales fell in all regions at once, ruling out local factors. Second — and this is the key point — the fall began in the same week as the new prices. Third, departing customers name the price in most exit surveys. Each finding alone could be chance; together they point one way."],
 "重要な点を適切に強調し、関連する裏づけの詳細を添えて、体系的に論を展開するエッセイや報告を書く。",
 "強調の設計（the second is decisive / this is the key point）と体系性（予告・配列・回収）。",
 "強調を構成そのもので行う ── 要の論点を宣言し（and this is the key point）、段落の配置で見せる。書面では語気の強調が使えないぶん、設計の強調が全てになる。",
 "論構造糸：体系化＋強調 ── 口頭277と同文級（develops an argument systematically with appropriate highlighting ... が完全共通）＝論証族の型式標本対（モード間並行対、mode_pairs登録）。",
),
357: (
 ["How our bread reaches the shops: flour arrives at the factory at night and is tested for quality. The dough is then mixed and left to rise twice — once all together, and once shaped in tins. After baking, the loaves cool for exactly one hour; warm bread cannot be sliced cleanly. Finally, the vans load at five in the morning, following a route that puts the farthest shop first."],
 "複雑な過程の詳細な記述を書く。",
 "工程の順序標識（then / After / Finally）と受動態の運用（is tested / is mixed）。細部の理由の添え書き。",
 "工程は受動態が基調（The dough is then mixed）── 動作主を毎回書かない。細部には理由を一言添える（warm bread cannot be sliced cleanly）── 記述が説明に変わる瞬間。",
 "手順糸：過程の詳細記述 ── 叙述族の静的描写糸に最も近づく行だが、時間順の工程＝手順の課題（判断(ae)で報告糸から再タグ。口頭267と段差対、mode_pairs登録）。副タグ・静的描写で交差を記録。",
),
358: (
 ["Three fixes have been proposed for the login problem. Rewriting the module is cleanest but takes a quarter. A quick patch ships this week but adds debt we must repay later. Buying a licensed component is fast and solid, yet then we depend on an outside company. Judged by user impact per week, the patch wins now — provided the rewrite is scheduled, not forgotten."],
 "問題に対する異なるアイディアや解決策を評価する。",
 "評価基準の明示（Judged by user impact per week）と選択肢ごとの利欠点の対。条件つき結論（provided ...）。",
 "評価には基準を宣言する ── 基準なしの「総合的に判断して」を書かない。結論に条件を付けてよい（provided ...）── 留保は弱さでなく精密さ。",
 "比較考量糸の書面独立行＝考量が論証（359）から切り出されて単独の課題になる。口頭280（B2）と課題を共有するが半段上（B2+）── 書面が上に置かれる段差の第二例（判断(ac)、mode_pairs段差帳簿）。",
),
353: (
 ["(from an exposition on urban water supply) Three issues deserve particular attention. The first is loss: nearly a third of treated water never reaches a tap, leaking from pipes laid before 1970. The second is pricing, which currently rewards high use. The third — and the least visible — is governance: responsibility is split across four agencies, so no one owns the problem."],
 "関連する重要な問題を強調しながら、複雑な主題の明快でよく構成された論説を書く。",
 "論点の階層化（Three issues ... The first / The second / The third）と強調の運用（the least visible）。",
 "論説は主張でなく問題の見取り図 ── 立場を売り込まずに要点を立てる。強調は評言で行う（and the least visible ──）── 挿入句の評言は日本語の論説文にない道具。",
 "報告糸の上端＝論説（exposition）。事実の伝達が論点の強調（underlining salient issues）を獲得し、論構造糸（356 highlighting）と同じ装置に合流する ── 報告と論証の上端収斂。",
),
354: (
 ["(from an essay) The four-day week deserves serious study, not because workers want it — of course they do — but because the output evidence keeps surprising us. Trials in several countries found productivity held steady; one bank even reported fewer errors, presumably because tired staff make mistakes. There are subsidiary benefits too: lower commuting costs, easier childcare, and — less obviously — better retention, which saves rehiring costs that rarely appear in the headline numbers."],
 "補助的な論点・理由・適切な例を挙げて、見解をある程度の長さで展開し裏づける。",
 "主論点と補助論点の階層（There are subsidiary benefits too）、挿入句による譲歩と評言（— of course they do —）。",
 "補助論点は「too」で格を下げて足す ── 全部を主論点の顔で並べない。挿入句（— of course they do —）で譲歩を文中に畳み込む ── 文を分けずに反対材料を処理する書面固有の技術。",
 "論構造糸：肉づけ（補助論点・理由・実例）── 口頭278（B2）と同文級だが一段上（C1）＝並行対でなく梯子段差（判断(ac)）。推敲可能な媒体では、同じ肉づけ操作に読み手の密度要求が加わる。",
),
355: (
 ["(introduction) This report examines why the pilot scheme succeeded in one district and failed in the other, drawing on interviews with both teams. It argues that the difference lay not in funding but in timing. / (conclusion) The evidence reviewed here points to a simple rule: schemes succeed when training comes before the change, not after it. The report closes with three recommendations."],
 "話題が関心分野内で、推敲・修正の機会があれば、複雑な学術的・職業的話題の長めの報告・記事・論文にふさわしい序論と結論を書く。",
 "序論の機能定型（examines ... / It argues that ...）と結論の機能定型（The evidence reviewed here points to ...）。本体との呼応。",
 "序論は予告、結論は回収 ── どちらも本体の要約ではない。It argues that ... で主張を序論の末尾に置く（結論まで隠さない）のが英語論文の型。「まとめ」と書いて本体を繰り返さない。",
 "構成糸：器（361）→ 序論・結論の設計。支援条件（推敲・修正の機会）＝支え型条件句が書面長文の上端C1に回帰する ── 叙述族では下段の装置（口頭260事前準備・書面345辞書）だった支えが、長大なテキストでは上端に戻る（判断(ac)）。",
),
350: (
 ["(from a review-essay) The proposal is elegant, and its elegance is the problem. By funding the library through a hotel tax, the council ties culture to tourism — a marriage that flatters both parties until the first bad season. The plan deserves support, but only with a floor: a guaranteed minimum from the general budget, so that the library's opening hours do not rise and fall with the price of a hotel room."],
 "主張を提示したり、提案や文学作品への批評的評価を述べたりする、明快でよどみない複雑な報告・記事・エッセイを書く。",
 "文体の統御（its elegance is the problem の転倒）と論の流れの継ぎ目のなさ（smoothly flowing）。批評的評価の精密さ。",
 "批評は要約＋感想ではなく、対象の構造への評言（ties culture to tourism）── 何がどう作られているかを言い当てる。譲歩つき支持（deserves support, but only with ...）の条件は具体で書く。",
 "論構造糸の上端＝主張の提示と批評的評価が「よどみない」文章として一体化。critical appreciation は Creative writing の批評糸（334→332→329）と合流する書面上端 ── 系をまたぐ糸の再結合（柱内相互参照）。",
),
351: (
 ["構成の設計そのものが課題の行。型の標本：主張を冒頭段落の末尾に置く／各段落の第一文を論点文にする／転換点に予告を置く（Two objections remain; I take the weaker first.）／結論で論点を同じ順序で回収する（To return to the three claims in order: ...）。",
  "This essay makes three claims: that the policy is affordable, that it is popular, and — most importantly — that it is already working elsewhere."],
 "読み手が重要な点を見つけやすい、適切で効果的な論理構造を与える。",
 "一貫性・結束性の書面上端＝構成の設計。予告と回収の対応、段落機能の一貫。",
 "構造は読み手への奉仕 ── 自分の思考の順でなく、読み手が要点を拾える順に組む。予告（I take the weaker first）は日本語の論述文化では過剰に感じられるほど明示するのが英語の規範。",
 "質フラグ（構成そのものの技法行）＝C2本体行350に付随するライダー行（Creative writing 325＋326と同配置の再現）。構成糸の上端：接続語（366）→器（361）→序論結論（355）→読者のための論理構造。上端の横串溶解（一貫性・結束性）の書面論証版 ── 234（口頭叙述）・325（書面叙述）に続く三例目。",
),
352: (
 ["Some economists find little effect of the minimum wage on jobs; others report the opposite. One recent study argues the dispute is really about regions, not the wage itself. My own view is narrower than any of these: in high-cost cities the evidence supports increases, and the national debate obscures exactly this point."],
 "自分のアイディアや意見を出典のそれと明確に区別しながら、複雑な学術的・職業的話題についての複数の視点を提示する。",
 "視点の帳簿管理（Some ... others ... One recent study ... My own view）。帰属の一貫と自他の区画。",
 "誰の主張かを毎文で明示する（Some economists find / One study argues / My own view is）── 日本語の「〜とされる」の帰属ぼかしを持ち込まない。自分の見解は My own view で区画してから述べ、出典の要約と地続きにしない。",
 "出典統合糸の上端＝統合（360）に自他の区別が加わる。視点の帳簿管理は仲介（第4柱・複数視点の提示）と最も近づく書面上端 ── ただしここでは自分の立場の輪郭を切るための区別（柱間相互参照）。",
),
}

DISCUSSION = [
 # ¶1 背骨
 "この18件の梯子は、書面の構築梯子の外枠を Creative writing と共有しながら、中身を叙述から論証へ差し替える。段名列はCEFR原文語彙に係留する：接続 connectors（366）→ 定型書式 conventionalised format（364）→ 器 essays（361）→ 展開 develops an argument（359）→ 統合 synthesise（360）→ 体系化と強調 systematically / highlighting（356）→ 構成の設計 introduction and conclusion（355）→ 読者のための論理構造 logical structure / reader（351）・視点の区別 distinguishing（352）・よどみない一体化 smoothly flowing（350）。書面の背骨は二層をなす：接続に始まり読者適合に終わる外枠は系に依存せず（Creative と共有）、その中身（叙述の結束／論証の体系化）が系ごとに差し替わる ── 構築梯子型の背骨定義（判断(ab)）は「系非依存の外枠＋系依存の中身」へ精緻化を要する（ladder_templates追随、判断(ac)）。",
 # ¶2 糸
 "スケール内部には糸7本が走る（正準：data/p2_threads.json）。論証族4糸（立論367／理由づけ362／比較考量358／論構造359→356→354→350）は口頭 putting a case と共有 ── 糸はモードに先立つ（判断(z)の発見が第二の族で再現）。ただし書面側は各糸が萎縮し（立論1行・理由づけ1行・比較考量1行）、口頭で三行に分かれた課題が一行に折り畳まれる（362＝286比較＋284理由＋282列挙）── Creative の感情・評価糸（口頭5行→書面1行）と同じ束スケールの萎縮。残る5本のうち3本は**教示族**の糸で、その口頭側は Sustained monologue: giving information（判断(ad)(ae)）── 報告（364→365→363。定型書式→紙面設計→自前の要約）、手順（357。複雑な過程の詳細記述 ── 口頭267との類似度0.661が全比較中の最高値で、判断(ae)で報告糸から再タグ）、説明（353。論説＝expositions であって報告ではない、同じく判断(ae)で再タグ）。本スケールは論証族と教示族を同時に宣言する束スケールである。スケール固有糸は2本：出典統合（360→352。統合→自他の区別）、構成（366→361→355→351。接続語→器→序論結論→論理構造）。叙述族糸の使用ゼロは口頭側と同じ（357の過程記述が静的描写と接するが報告に留置・副タグで交差記録）。束の構造：Creative＝書面叙述＋創作＋批評、本スケール＝書面論証＋報告＋出典管理＋構成。ライダー行の再現：351（質フラグ＝構成の技法行）が本体行350に付随する ── Creative の C1=327+328・C2=325+326 と同配置。説明糸（353論説）は論構造糸の装置（強調）に合流する ── 教示族と論証族の上端収斂（判断(ac)(vii)の所見は再タグ後も維持される）。",
 # ¶3 mode
 "modeは全行「書面」で一様。並行対は356↔277の一組のみ（同文級・論証族の型式標本、mode_pairs登録）。叙述族の同レベル7対と対照的に、論証族では書面が一段上に置かれる段差が2件（354 C1↔278 B2の同文級／358 B2+↔280 B2の同課題）── 読み（仮）：推敲可能な媒体では肉づけ・考量に読み手の密度要求が加わり、同じ操作の格が上がる。367（A2）が口頭287の条件句「相手の辛抱強さ」を持たないことも mode差の解法を示す ── 書面は待ってくれる媒体そのものである。柱間の境界が二箇所で立つ：363の要約・360の統合は仲介（第4柱）と接する（自分の論のための統合 vs 他者の理解のための仲介、の分業）。350の批評的評価は Creative writing の批評糸（334→332→329）と合流 ── 単独構築の作品評という書面上端で、叙述族と論証族の糸が再結合する。",
 # ¶4 L1
 "L1注意は三段の質的転換をなす ── 五例目（授受・第一号・第二号・第三号・本シート）。下段（〜B1）＝統語・接続：and/because/then の選択・because節の独立禁止・定型書式への充填。中段（B1+〜B2）＝談話・パラグラフ：topic sentence 先行・利欠点の対比標識（on the other hand と but の使い分け）・反対側の論を自分の文章で立ててから返す・数字を文に埋め込む・出典を主語にする（「〜と言われている」の主語なし伝聞の禁止）。上段（B2+〜C2）＝修辞・帳簿：強調を構成そのもので行う（語気が使えない媒体の帰結）・挿入句による譲歩の畳み込み・序論＝予告／結論＝回収の機能定型（「まとめ」で本体を繰り返さない）・自他の視点の区画（My own view の明示 ── 日本語アカデミック作文でも課題だが、英語は帰属明示の規範が一段強い）。",
 # ¶5 横串
 "効く how well 軸の主軸は一貫性・結束性 ── ただし書面論証ではこの軸が上端で行そのものになる（351＝読み手のための論理構造）。横串溶解の三例目（234口頭叙述＝流暢さ・一貫性へ／325書面叙述＝文体へ／351書面論証＝結束性・構成へ）であり、C2の smoothly flowing（350）は流暢さの書面版。話題の展開と叙述の正確さ（数量・工程の精密な報告：363/357）も広く効く。社会言語的適切さは読者適合・レジスターとして355/350に潜在する（応酬の適切さではない）。質フラグ1件（351）── 第2柱の質フラグは全て書面側に現れている（Creative 3件＋本シート1件、口頭2スケールは0件）：技法・資源が行として析出するのは推敲可能な媒体の側、という規則性の候補（次の書面スケールで検証）。",
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
    canon = {p["written"]: p["oral"] for p in sys_rec["pairs"]}
    assert MODE_PAIRS == canon, "並行対がmode_pairs.json（論証族）と不一致"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        if no in MODE_PAIRS:
            delta += f"（モード間並行対：口頭 putting a case No.{MODE_PAIRS[no]}）"
        rows.append({
            "mode": "書面", "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "報告と小論（Reports and essays）── 第2柱第四号範型・全数シート",
        "scope": "全数（18件。書面18 ── mode一様、(d)裁定1）",
        "type": "第2柱（産出・談話構築）。梯子型＝構築梯子型（第5型・本採用＝判断(ab)。論証族での再現＝判断(ac)・CEFRカタログ9）。談話課題糸＝立論／理由づけ／比較考量／論構造（論証族4糸、口頭putting a caseと共有）＋報告／出典統合／構成（スケール固有）＋副タグ（ジャンル・結束条件句・支援条件・質フラグ・比較考量・静的描写）",
        "essence": "一人で、不在の読者に向けて、論・報告・小論を書き上げる。梯子は組み立ての複雑化（接続→書式→器→展開→統合→体系化→構成設計→読者のための論理構造）に宿り、書面背骨の外枠（接続に始まり読者適合に終わる）はCreative writingと共有される。並行対の口頭側はputting a case（型式標本356/277）。",
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p2_reports_essays.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
