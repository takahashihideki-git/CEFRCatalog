#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第2柱（産出・談話構築）第五号範型：Sustained monologue: giving information 10件の全数シート。

CEFRカタログ10・判断(ae)。教示族の口頭スケール。裁定：
- 糸3本（報告4／手順4／説明2）の完全分割 ── いずれも厳密単調
- 教示族糸（報告・手順・説明）は書面（Reports and essays）と共有＝糸はモードに先立つ（第三族での再現）
- 並行対は270↔364のみ（同レベル・同課題。文言でなく課題で採った初の対、類似度0.355）
- 段差は267↔357（B2→B2+。類似度0.661は全比較中の最高値だがレベル非対称）
- 271は質フラグにしない（資源の例示＝書面366と同処理）── 口頭3スケール目の質フラグ0件
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCALE = "Sustained monologue: giving information"
ACT = "情報のまとまった提供（第2柱：Sustained monologue: giving information）"
FAMILY = ["教示族"]  # 判断(ad)：系＝族。p2_threads.jsonのscales[SCALE]["族"]と照合
SYSTEM = "教示族"

# レベル順→No昇順（表示順の正準）
ORDER = [272, 271, 270, 268, 269, 266, 267, 265, 263, 264]

# 談話課題タグ（正準は data/p2_threads.json、本表はbuild()内assertで照合）
THREADS = {
    "報告": [272, 270, 266, 265],
    "手順": [271, 269, 267, 264],
    "説明": [268, 263],
}
SUBTAGS = {
    "結束条件句": [271],
    "支援条件":   [272, 270],
    "静的描写":   [272, 263],
}

# モード間並行対（口頭側の実装。相手は Reports and essays）
MODE_PAIRS = {270: 364}

R = {  # no -> (exponents, scene, howwell, l1, delta)
272: (
 ["This is my pencil case. It is small and blue.",
  "Look. This is a lunch box. It is red and round."],
 "実物や写真を見せながら、それが何か・どんな形と色かを、準備した短い文で伝える（show and tell）。",
 "基本の物名と色・形の形容詞。This is X.／It is Y. の二文で足り、事前準備が条件句として行に書かれている。",
 "「これは私の筆箱です」を直訳して ×This is a my pencil case としない（限定詞は一つ）。色と形は It is small and blue. と文にする ── 日本語の「小さくて青い」を名詞前に積み上げない。可算名詞の a を落とさない。",
 "報告糸の起点＝一つの物について「何か・どんなものか」を提示する最小形。支え型条件句（事前準備）に支えられる。物の属性を言う点で叙述族の静的描写（259・A1）と接するが、課題は情報の提示であり主タグは報告に留置（副タグで交差記録）。",
),
271: (
 ["Go straight for two blocks. Then turn right. The station is on your left.",
  "First, go out of the shop. Next, turn left at the bank. Then walk for five minutes."],
 "駅・店・学校までの道を、順序を追って口頭で教える。",
 "命令形の連鎖と順序接続語（first / then / next）。一文一動作を守ること。",
 "日本語の「〜を行って、〜を曲がって」を長い一文に繋げない ── 英語は一文一動作を then で刻む。「まっすぐ」は straight（×straightly）。turn right / on your left の前置詞を落とさない。",
 "手順糸の起点。順序接続語（first / then / next）が行の文言に名指しされるが、これは資源の例示であって質フラグではない（書面366「linking sentences with connectors like and, because or then」と同処理、判断(ae)）。第1柱・道案内566（往復の中で道を尋ね・教える）との分業：こちらは独話で順序を組み立てる側（相互参照）。",
),
270: (
 ["The printer on the second floor is not working. It stops after two or three pages, and the screen shows an error.",
  "Take the train to Nakano and change there. Get off at the third stop. The office is five minutes from the north exit."],
 "職場や学校で、問題の状況や道順を、事前に整理してひとまとまりで報告する。",
 "事実の正確さと順序。準備があれば細部まで届く（事前準備の条件句が残っている）。",
 "問題の報告で主語を落とさない ── 日本語の「動かないんです」は The printer is not working. と主語を立てる。事実と推測を混ぜない（It shows an error. と I think it is broken. を分ける）。",
 "報告糸：一つの物（272）から身近な話題の事実情報へ。第1柱・問題説明598（医療者への症状の申告）と課題を共有するが、こちらは応酬でなく独話の報告（行の移動はせず相互参照）。",
),
268: (
 ["The main point is simple: we have too many meetings. People spend three hours a day in meetings, so they cannot finish their own work.",
  "There are two problems with the plan. First, it costs too much. Second, we do not have enough staff."],
 "考えや問題の骨子を、要点として取り出して説明する（会議の切り出し、相談の導入）。",
 "要点の抽出と、ある程度の正確さ（reasonable precision）。細部よりも骨組みが立っていること。",
 "「要点は〜です」を The main point is で先に立てる ── 日本語の「いろいろあるんですけど」から入ると要点が最後に来る。数を先に宣言する（There are two problems.）。",
 "説明糸の起点＝伝達の精度が独立した課題になる。報告（事実をそのまま渡す）から分岐し、要点を抽出するという操作が加わる。",
),
269: (
 ["First, wash the rice and put it in the cooker. Then add water and press the button. It takes about fifty minutes.",
  "Open the file, click 'share' at the top right, and type the address. Do not forget to press 'send'."],
 "やり方を最初から最後まで、詳しい指示とともに説明する（料理・機器の操作・手続き）。",
 "手順の網羅と順序の明示。動作の粒度が揃っていること。",
 "丁寧さのために命令形を弱めすぎない ── 手順では Then press the button. のほうが明快。目的語を落とさない（×Then press. ）。時間や分量は数値で言う。",
 "手順糸：道順（271）から一般の手順へ。段名は detailed instructions。第1柱・指示への応答（受け手側）と対をなす与え手側だが、与える能力の帳簿は第2柱に立つ（明確化の「与える側」＝往復の中間形と同じ分業）。",
),
266: (
 ["The delivery will arrive on Tuesday between nine and eleven. The order number is 4471, and the driver will call you before he arrives.",
  "The course has twelve classes. Each class is ninety minutes, and the fee is thirty thousand yen, including the textbook."],
 "数字・条件・手続きを含む詳細な情報を、取り違えが起きないよう確実に伝える。",
 "正確さと確実性（reliably）── 抜けと取り違えが起きないこと。",
 "数値・日時・固有名は一項目一文で言い切る ── 日本語の「〜が、〜で、〜です」の連結をそのまま英語にすると係り先が壊れる。確認を相手任せにせず、こちらから言い切る。",
 "報告糸：事実の報告（270）から詳細情報の確実な伝達へ。ここで**事前準備の条件句が脱落する**（270→266）── 支え型条件句の脱落＝744→742型の第三族での再現。",
),
267: (
 ["To apply for the card, first fill in the form and attach a copy of your ID. Then take it to the counter on the first floor. The staff check the documents, and the card arrives by post in about two weeks.",
  "The whole process has three stages. You prepare the samples, the machine runs for an hour, and then you record the results."],
 "手続きや工程の全体を、明快かつ詳細に記述する（申請・作業工程・実験手順）。",
 "段階の明示と全体像の提示。個々の動作ではなく工程としてのまとまりが立つこと。",
 "全体像を先に置く（To apply for X, there are three steps.）── 日本語の逐次列挙のまま英語にすると終わりが見えない。工程の主語で能動と受動を使い分ける（The staff check ... / The documents are checked ...）。",
 "手順糸：個々のやり方（269）から工程（procedure）の記述へ。**書面357（複雑な過程の詳細記述）と段差対**（B2→B2+）── 類似度0.661は全比較中の最高値だがレベルが非対称で、判断(ac)(v)「同課題が書面で一段上に置かれる」の第三族での再現（mode_pairs登録）。",
),
265: (
 ["Our standard warranty covers parts and labour for two years. If the unit fails after that, I would recommend the extended plan rather than a repair, because these parts are no longer produced.",
  "The two contracts differ in one important way. The first fixes the price for three years; the second follows the market. For a small team, I would recommend the first."],
 "自分の職務に関わることなら何であれ、複雑な情報と助言を相手に合わせて伝える。",
 "情報の複雑さへの対応と、助言としての妥当性。職務範囲の全域（full range）を扱えること。",
 "助言は推奨型で言う（I would recommend X）── 日本語の「〜したほうがいいかもしれません」を直訳して条件を重ねると、助言が助言として届かない。事実と推奨を分けて示す（情報 → だから推奨）。",
 "報告糸の上端＝職務範囲の全域と、助言の付加。第1柱・助言との分業がここで見える ── 助言は中抜き型（判断(x)）でB1+〜C1に独立の行を持たず、この帯では職務情報に付随する形で現れる。560（B1・身近な事柄の助言）と456/483（C2・デリケートな事柄）の中間が、本行に吸収されている。",
),
263: (
 ["Both words are about money coming in, but revenue is what you bill, while cash flow is what actually reaches the account. A company can have high revenue and still run out of cash.",
  "The difference is timing. A guarantee applies from the day of purchase; the insurance starts only after the guarantee ends."],
 "似て非なる概念・事物のあいだの細かい違いを、取り違えが起きないように明確に示す。",
 "区別の明示と対比の設計。似ているものほど、共通点を先に置いてから差分を切り出すこと。",
 "対比の枠を明示する（Both A and B ..., but A ..., while B ...）── 日本語の「〜は〜ですが、〜は〜です」の並置だけでは差分の軸が示されない。差分の軸を名詞で先に言う（The difference is timing.）。",
 "説明糸の上端＝伝達の精度の最終段。要点の抽出（268）から、酷似するものの弁別へ。叙述族の静的描写C1（235・複雑な主題の詳細な描写）と接するが、こちらは対象の記述ではなく対象間の差分の設計であり、主タグは説明に留置（副タグで交差記録）。",
),
264: (
 ["Before you run the test, check the machine with the empty plate. If the number moves by more than two percent, check it again before you add any samples.",
  "Hand over the project in this order: first the access rights, then the open issues with their owners, and last the contacts on the client side. Do not close your account until the second step is finished."],
 "職業・学術の複雑な一連の手順を、実行できる形で指示する（実験手順・業務の引き継ぎ）。",
 "一連（a series）としての順序と条件分岐。専門的な内容でも指示として成立すること。",
 "条件分岐は if 節で明示し、前に置く（日本語の「〜の場合は」を後置しない）。禁止・注意は Do not / Make sure で明示する ── 手順書では婉曲表現が誤読される。",
 "手順糸の上端＝単一の手順（267）から複雑な一連の手順へ。条件分岐が指示の内部に入る点が段の中身。本スケールはC1で打ち止めでC2行を持たず、**上端の横串溶解（234／325／351）が起きない初のスケール**となる。",
),
}

DISCUSSION = [
 # ¶1 背骨
 "この10件の梯子は、叙述・論証に続く第三の族（教示）で構築梯子型の背骨を再現する ── ただし時間軸（叙述）でも論理軸（論証）でもなく、**受け手が使える形にするための精度**の軸の上で。段名列はCEFR原文語彙に係留する：名指し name / indicate（272）→ 順序接続語による道順 sequential connectors（271）→ 事実情報の報告 report straightforward factual information（270）→ 要点 main points / reasonable precision（268）・詳細な指示 detailed instructions（269）→ 確実性 reliably（266）・工程の詳細記述 detailed description of a procedure（267）→ 職務全域と助言 full range / advice（265）→ 微細な区別 detailed distinctions（263）・一連の複雑な手順 a series of complex procedures（264）。他の二族と際立って違うのは、**受け手基準が文言に現れない**ことである ── 叙述族は memorable（C2・234）、論証族は followed without difficulty（B1+・281）で聞き手が判定基準として行に入るのに対し、本スケールの基準語は reliably（266）・precision（268）・clearly（263）といずれも送り手側の精度である（聞き手を指す語は272の others のみで、これは基準ではなく実物提示の相手）。情報提示では受け手の理解が達成の定義そのものであるため、かえって独立した基準として析出しない ── 受け手基準の出現位置が族の署名になる、という判断(ac)(i)の観察の第三例。",
 # ¶2 糸
 "スケール内部には糸3本が走り、完全分割かつ**いずれも厳密単調**である（正準：data/p2_threads.json）：報告（272→270→266→265。物の提示→身近な事実→詳細情報の確実な伝達→職務全域の情報と助言）、手順（271→269→267→264。道順→やり方→工程→複雑な一連の手順）、説明（268→263。要点の抽出→酷似するものの弁別）。レベル分布は A1・A2・B1 が各1行、B1+ と B2 で二糸が一行ずつ並び、B2+ が1行、C1 で二糸が一行ずつ揃う ── 中段以上で糸が対になって立つことが、単一梯子でなく複数梯子であることの形式的証拠になる。副タグは3種：結束条件句（271の順序接続語の名指し）、支援条件（272・270の事前準備 ── 報告糸の270→266で脱落する支え型条件句）、静的描写（272・263が叙述族の静的描写糸と接する交差。主タグは教示族に留置し、書面357と同じ処理）。叙述族糸・論証族糸の主タグ使用はゼロで、**叙述族の再利用は副タグ＝交差としてのみ現れる** ── 族が主タグの層で互いに素であることの第三族での確認（判断(ae)）。",
 # ¶3 mode
 "modeは全行「口頭」（Sustained monologue）で一様。書面側の対は Reports and essays の教示族糸にあり、報告（364／365／363）・手順（357）・説明（353）が対応する（357と353は判断(ae)で報告糸から再タグ ── 口頭側の糸配置に合わせないと「糸はモードに先立つ」が第三族で破れるため）。並行対は270↔364の一組のみ（ともにB1、定型的な事実情報の報告）。ここに本族の署名がある ── **文言でなく課題で採った初の並行対**である。difflib類似度は0.355で、既存8対の帯（0.76〜1.00）から大きく外れる。叙述族・論証族では同課題が同文級で現れる（247/338は完全同文、277/356は同文級）のに対し、教示族の記述文は職務範囲・定型書式・専門手順のように**場面と制度に係留された語**で書かれるため、モードをまたぐと表現そのものが入れ替わる。段差は267↔357（B2→B2+、類似度0.661＝全比較中の最高値）で、判断(ac)(v)「同課題が書面で一段上に置かれる」が第三族でも再現する。第1柱との境界は三箇所に立つが、いずれも行の移動をせず相互参照で処理する（判断(ac)④の分業原理）：271↔566（往復の中で道を尋ね・教える vs 独話で順序を組み立てる）、270↔598（医療者への症状の申告 vs 独話としての事実報告）、265↔560（身近な事柄の助言 vs 職務情報に付随する助言）。",
 # ¶4 L1
 "L1注意は三段の質的転換をなす ── 授受・第一号・第二号・論証族に続く**六例目**で、柱・モード・族を超えた日本語話者の一般構造である。下段（〜B1）＝統語・定型：限定詞の重複（×a my pencil case）・形容詞の積み上げ（「小さくて青い」を名詞前に並べない）・一文一動作の刻み（「〜行って、〜曲がって」を一文に繋げない）・主語の復元（「動かないんです」→ The printer is not working.）。中段（B1+〜B2）＝談話：要点の先出し（The main point is / There are two problems ── 「いろいろあるんですけど」から入らない）・数の事前宣言・一項目一文（連結した長文にしない）・全体像の先置き（three steps を先に言う）。上段（B2+〜C1）＝修辞・開示の再配置：助言の推奨型化（I would recommend ── 「〜したほうがいいかもしれません」の条件の重ねを持ち込まない）・対比の枠の明示（Both ... but ... while ...）と差分の軸の名詞化（The difference is timing.）・条件分岐の前置と禁止の直言（Do not / Make sure ── 手順書では婉曲が誤読される）。本族に固有なのは上段の性格で、叙述族が「オチの委任をやめる」、論証族が「強調を設計で行う」であったのに対し、教示族は**曖昧さの許容度を下げる**方向に転換する ── 婉曲は配慮ではなく誤伝達になる、という語用論的反転がここにある。",
 # ¶5 横串
 "効く how well 軸の主軸は、他の二族と違って一貫性・結束性ではなく**叙述の正確さ**である（266 reliably・268 precision・263 clearly が直接それを言う）。次いで話題の展開（工程・一連の手順の網羅）、語彙の範囲（職務・学術の専門語彙が265／264で必須になる）。社会言語的適切さは第1柱ほど前景化しないが、上段で反転した形で効く ── 婉曲さが適切さでなく不正確さとして罰される帯があるのは、22行為のどこにも無かった配置である。流暢さは全行で明示されない（口頭第一号の241 fluently のような行を持たない）── 情報提示は言い直しても情報が届けば達成される営みだからで、口頭スケールでありながら時間拘束が課題に入らない。質フラグ該当行は**0件**：271は順序接続語を名指しするが「XからYへ道順を教える」という課題を持つ本体行であり、課題を持たない技法行（333「Can clearly signal chronological sequence」）とは別種である（書面366と同処理、判断(ae)）── これで口頭3スケールすべて0件、「質フラグは全て書面側」の規則性候補は反証テストを生き延びた。最後に、本スケールは**C1で打ち止めでC2行を持たない** ── 上端が横串に溶ける現象（234／325／351）が起きない初のスケールであり、溶解が起きるのは帯がC2まで届くスケールに限られるという条件が、ここで裏側から確認される。",
]


def build(root="."):
    desc = json.load(open(os.path.join(ROOT, "data", "descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(ROOT, "data", "working_translations_1224.json"), encoding="utf-8"))
    members = {int(no) for no, d in desc.items() if d.get("scale") == SCALE}
    assert members == set(ORDER), f"全数性不一致: {members ^ set(ORDER)}"
    assert len(ORDER) == 10
    tagged = [n for v in THREADS.values() for n in v]
    assert sorted(tagged) == sorted(ORDER), "主タグが完全分割でない"
    assert all(n in set(ORDER) for v in SUBTAGS.values() for n in v), "副タグに帳簿外のNo"
    th = json.load(open(os.path.join(ROOT, "data", "p2_threads.json"), encoding="utf-8"))["scales"][SCALE]
    assert th["族"] == FAMILY, "FAMILYがp2_threads.jsonの族宣言と不一致"
    assert {k: sorted(v) for k, v in THREADS.items()} == {k: sorted(v) for k, v in th["主タグ"].items()}, "THREADSがp2_threads.jsonと不一致"
    assert {k: sorted(v) for k, v in SUBTAGS.items()} == {k: sorted(v) for k, v in th["副タグ"].items()}, "SUBTAGSがp2_threads.jsonと不一致"
    mp = json.load(open(os.path.join(ROOT, "data", "mode_pairs.json"), encoding="utf-8"))
    sys_rec = next(s for s in mp["systems"] if s["族"] == SYSTEM)
    canon = {p["oral"]: p["written"] for p in sys_rec["pairs"]}
    assert MODE_PAIRS == canon, "並行対がmode_pairs.json（教示族）と不一致"
    # 糸の厳密単調（判断(ae)の裁定根拠を機械化）
    order_lv = ["Pre-A1", "A1", "A2", "A2+", "B1", "B1+", "B2", "B2+", "C1", "C2"]
    for t, ns in THREADS.items():
        lv = [order_lv.index(desc[str(n)]["level"]) for n in ns]
        assert all(lv[i] < lv[i + 1] for i in range(len(lv) - 1)), f"糸が単調でない: {t}"
    rows = []
    for no in ORDER:
        d = desc[str(no)]
        ex, scene, hw, l1, delta = R[no]
        if no in MODE_PAIRS:
            delta += f"（モード間並行対：書面 Reports and essays No.{MODE_PAIRS[no]}）"
        rows.append({
            "mode": "口頭", "level": d["level"], "no": no,
            "en": d["en"], "jp": tr[str(no)],
            "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta,
        })
    sheet = {
        "title": "情報のまとまった提供（Sustained monologue: giving information）── 第2柱第五号範型・全数シート",
        "scope": "全数（10件。口頭10 ── mode一様、(d)裁定1）",
        "type": "第2柱（産出・談話構築）。梯子型＝構築梯子型（第5型・本採用＝判断(ab)。教示族での再現＝判断(ae)・CEFRカタログ10）。談話課題糸＝報告／手順／説明（教示族3糸、書面Reports and essaysと共有）＋副タグ（結束条件句・支援条件・静的描写）",
        "essence": "一人で、相手が使える形にして情報を渡す。梯子は組み立ての複雑化に宿るが、その軸は時間でも論理でもなく精度（名指し→順序→事実の報告→要点と詳細な指示→確実な伝達と工程→職務全域と助言→微細な区別と一連の複雑な手順）。受け手基準が文言に現れない唯一の族で、上端では婉曲が誤伝達として罰される。並行対の書面側はReports and essays（270/364、文言でなく課題で採った初の対）。",
        "rows": rows,
        "discussion": DISCUSSION,
    }
    return {ACT: sheet}


if __name__ == "__main__":
    out = build()
    path = os.path.join(HERE, "catalog_p2_giving_information.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    sheet = out[ACT]
    from collections import Counter
    print(f"生成OK: {path}")
    print(f"行数: {len(sheet['rows'])} / DISCUSSION: {len(sheet['discussion'])}段落")
    print("レベル分布:", dict(Counter(r["level"] for r in sheet["rows"])))
