# -*- coding: utf-8 -*-
"""第3周-5：事実情報の授受（31件）の全数シート ── 二相接続型テンプレートの初回適用（全数シート第2号）。

検証範型③（verification_assertive.json、情報管理相15行）の著述フィールドを継承し、
質問応答相（構造）15行＋C1（No.489）の16行を新規作成して全数へ昇格。
継承行のうち統合前（判断(k)以前）の枠組みで書かれた delta 2箇所（541・557）を統合後の視点に編集。
DISCUSSION は ladder_templates.json 二相接続型配分（①一本読み ②場面 ③往復 ④口頭書面＋(o) ⑤統合根拠＋総括）で新規著述。
旧検証範型は歴史的サンプルとして凍結。

単一情報源の設計：en / jp は data から構築時取得。継承フィールドは verification_assertive.json から読取。
実行すると prototypes/catalog_infoexchange.json を生成する。
"""
import json, os

ACT = '事実情報の授受'
TITLE = '事実情報の授受（Giving & receiving factual information）── 全数シート'
SCOPE = '全数（31件。口頭24＋書面7。二相：質問応答相〔構造〕15＋情報管理相〔運用〕16）'
TYPE_ = '主張的（assertive）── 世界の事実を尋ね、答え、確実に引き渡す。下位系＝情報授受系、梯子型＝二相接続型（下段＝質問応答相〔構造〕、上段＝情報管理相〔運用〕。判断(k)・第2周-1統合）'
ESSENCE = '事実を尋ね、答え、引き渡す。下段では「尋ねる文が作れる」ことが、上段では「情報を確実に運べる」ことが梯子を刻む。レベルが上がるとは、主語が疑問文から情報そのものへ移ることである。'

# 新規16行：質問応答相（構造）15＋情報管理相C1（489）
NEW = [
(579, '口頭',
 ["My name is Ken. / I'm Ken.", "What's your name?"],
 "初対面で名乗り、相手の名前を尋ねる。最初の情報交換。",
 "定型の丸ごと運用：What's your name? を塊として言えるか。",
 "「お名前は？」の感覚で Your name? と名詞だけを上げ調子で言いがち。疑問文の枠（What's ...?）を最初から塊で入れる。",
 "（質問応答相の起点）情報交換の最小単位＝名前。疑問文はまだ文法ではなく決まり文句である。"),
(581, '口頭',
 ["What day is it today?", "What time is it?", "It's Monday. / It's ten o'clock."],
 "曜日・時刻・日付を尋ね、答える。",
 "定型＋数の語彙：曜日・月・時刻表現の在庫。",
 "日本語の「今日何曜日？」は主語不要だが、英語は What day is it? と it が要る。it を落として What day today? となりがち。",
 "名前から暦・時刻へ。答えの側に数詞体系が入り、語彙の負荷が初めて出る。"),
(582, '口頭',
 ["When is your birthday?", "My birthday is May 5th."],
 "生年月日・誕生日を尋ね、答える。",
 "序数と月名：日付の言い方の規約。",
 "日付の序数（May fifth）を基数で May five と言いがち。日本語の「5月5日」に序数の痕跡がないため。",
 "暦の一般知識から自分の情報へ。個人情報の交換が始まる。"),
(583, '口頭',
 ["What's your phone number?", "It's 090-1234-5678."],
 "電話番号を尋ね、教える。",
 "数字列の受け渡し精度：一桁ずつ読む規約と聞き取り。",
 "数字列は一桁ずつが英語の規約。zero/oh の揺れ、日本語式に二桁で区切る癖との切替が要る。",
 "情報の正確な受け渡しという、のちの「信頼性」軸の萌芽が数字列に現れる。"),
(584, '口頭',
 ["How old are you?", "I'm seven years old."],
 "年齢を言い、尋ねる。",
 "定型：How old ...? の塊。",
 "How old are you? を直訳的に失礼と感じて避けがちだが、子ども同士・学習場面では標準の情報質問である（成人相手の運用は別の作法に属す）。",
 "What 系から How 系へ疑問詞が広がる。"),
(585, '口頭',
 ["What is this? / What's that?", "It's a pen."],
 "目の前の物が何かを尋ね、1〜2語の答えを理解する。",
 "指示詞＋最小疑問文：this/that の使い分けと、単語レベルの応答理解。",
 "this/that の二分が日本語のコソアド三分（これ・それ・あれ）と食い違い、that の守備範囲（それ＋あれ）に慣れが要る。",
 "個人情報から環境の事物へ。疑問文が「世界を尋ねる道具」になる起点。"),
(574, '口頭',
 ["Do you like music? — Yes, I do. / No, I don't.", "I have a dog. — Oh, really?"],
 "ごく身近な話題で、質問し、答え、簡単な発言を切り出し、それに応じる。",
 "文法的正確さ（do 支持の骨格）：Yes, I do. の型で答えられるか。",
 "do 支持は日本語に対応物を持たない最初の壁。Do you ...? に Yes, I like. と答える誤りが、応答の型（Yes, I do.）で防げる。",
 "決まり文句の疑問文から、do 支持という「作れる疑問文」へ。質問応答相の文法的核心。"),
(575, '口頭',
 ["Where do you live?", "Who is she?", "Do you have any brothers or sisters?"],
 "自分と他者の基本情報（住まい・知人・持ち物）を尋ねあう。",
 "疑問詞疑問文の展開：Where / Who / What ＋ do 支持の組み合わせ。",
 "疑問詞疑問文の語順（疑問詞→do→主語→動詞）が日本語の語順（〜はどこ？）と逆転し、Where you live? の語順崩れが定番の穴。",
 "Yes/No 疑問文から疑問詞疑問文へ。尋ねられる情報の種類が一気に広がる。"),
(578, '口頭',
 ["What colour is your bag?", "It's blue."],
 "衣服や身近な物の色を言い、尋ねる。",
 "語彙（色彩語）＋「疑問詞＋名詞」型（What colour ...?）。",
 "What colour ...? の疑問詞＋名詞型は、日本語「何色？」が一語であるため What is colour? と分解されがち。",
 "疑問詞が名詞と結合する型（What colour / What time）の獲得。"),
(569, '口頭',
 ["What do you do in your free time?", "I usually play tennis."],
 "仕事や余暇にすることを尋ねあう。",
 "現在形の習慣用法＋頻度副詞。",
 "職業を尋ねる What do you do? は直訳では出ない塊。「仕事は何？」から What is your job? だけで止まりがち。",
 "事実の点（名前・番号）から生活の面（習慣）へ。時制の運用が入る。"),
(570, '口頭',
 ["How can I get to the station?", "Go straight and turn left at the bank."],
 "地図や見取り図を見ながら道順を尋ね、教える。",
 "空間表現の在庫＋命令形の指示。",
 "道案内の定型の前置詞選択。日本語の「銀行を左」に引かれて turn left the bank と前置詞が落ちる。",
 "情報が「答え」から「手順」へ。聞き手が実行できる形で渡す ── 上段の「確実に運ぶ」の遠い祖先。"),
(572, '口頭',
 ["When and where was it?", "Who was there?", "What was it like?"],
 "出来事について、いつ・どこで・誰が・どうだったかを尋ねあう。",
 "過去形の疑問文運用：was / did の作り分け。",
 "be 動詞過去と一般動詞過去の疑問文の作り分け（Was it ...? / Did it ...?）が混線しやすい。",
 "現在から過去へ。出来事を尋ねる基本セット（when / where / who / what ... like）が揃う。"),
(563, '口頭',
 ["How often do you play tennis?", "I go swimming twice a week."],
 "習慣や日課を尋ねあう。",
 "頻度表現の精度：How often と「回数＋a week」。",
 "頻度の答えの語順。日本語「週2回」から week twice の順になりがちで、twice a week の型を塊で要する。",
 "569 の習慣質問が頻度・定期性の精度を得る。"),
(564, '口頭',
 ["What did you do last weekend?", "Have you ever been to Kyoto?"],
 "娯楽や過去の活動を尋ねあう。",
 "過去形と経験の尋ね方の広がり。",
 "経験の Have you ever ...? と単純過去 Did you ...? の使い分け ── 日本語は両方「〜したことある？／した？」で、完了相の別が立ちにくい。",
 "572 の出来事質問が自分たちの経験へ向く。過去質問の在庫が厚くなる。"),
(565, '口頭',
 ["What are you going to do this weekend?", "Are you doing anything tonight?"],
 "計画・意図を尋ねあう。",
 "未来表現の使い分け（be going to／現在進行形）。",
 "will／be going to／現在進行形の三系統が日本語の「〜するつもり」一本に潰れ、すべて will になりがち。",
 "過去・現在に未来が加わり、質問応答相の時制三面が完成する。ここが下段の到達点 ── この先、梯子の主語は疑問文から情報そのものへ移る（相境界）。"),
(489, '口頭',
 ["Could you be more specific?", "Let me put the question another way."],
 "会議で、答えの詳細を掘り下げて追い質問し、質問が誤解されたら言い換える。",
 "談話運営の頂点：質問を道具として設計・運用し、誤解を修復する。",
 "質問の言い換えは「同じ質問の繰り返し」ではなく別ルートでの再設計。日本語の会議では質問の再構成が失礼と感じられがちで、修復をためらう。",
 "上段の到達点：情報を引き出す側の技能が、照合（B1+）→信頼性（B2）を越えて、質問そのものの設計・修復に至る。"),
]

# 継承行の delta 編集（統合前の枠組み → 統合後の視点）
DELTA_EDITS = {
 541: "（情報管理相の起点）数値という最も裸の事実の授受。疑問文が作れるようになった学習者に、次に問われるのは運ぶ中身の管理である。",
 557: "A2+ の 562 とほぼ同文言で、「実際的な日常の要求」という条件句だけが外れる ── 行為の切れ目でなく条件の緩和でレベルが刻まれている。相境界をまたぐ接続証拠（判断(k)、562/557型）。",
}

# 表示順（レベル昇順。同レベル内は質問応答相→情報管理相、口頭→書面）
ORDER = [579,581,582,583,584,585,          # Pre-A1
         574,575,578,649,                   # A1
         569,570,572,541,568,659,           # A2
         563,564,565,562,642,679,           # A2+
         557,559,640,656,                   # B1
         555,591,                           # B1+
         554,633,                           # B2
         489]                               # C1

DISCUSSION = [
"【一本の梯子 ── 疑問文が作れることから、情報を運べることへ】 二相接続型の全数シート第2号（第1号＝意見31）。下段＝質問応答相（構造、Pre-A1〜A2+、15件）：名前・時刻・番号という決まり文句の疑問文（Pre-A1）から、do 支持（A1・574）、疑問詞疑問文の語順（575）、過去の疑問文（572・564）、未来表現の三系統（565）へと、「尋ねる文が作れる」ことが梯子を刻む。上段＝情報管理相（運用、A1〜C1、16件）：limited（A2・568）→ straightforward（A2+・562／B1・557）→ more detailed（559）→ check and confirm（B1+・555）→ detailed reliably（B2・554）→ 質問の設計・修復（C1・489）という情報の量・粒度・信頼性の階段であって、文法の段階ではない。相境界は A2+/B1 帯にあり、562→557 の条件緩和（条件句が外れるだけの同文言対）が、切れ目のない一本の梯子である証拠になっている（判断(k)の接続証拠、562/557型＝意見の 480→448 と同型）。how well の主役も相境界で交代する ── 下段は文法的正確さ（do 支持・語順・時制）、上段は談話運営と伝達の信頼性。",
"【場面の広がり ── 自分の半径から制度の場へ】 下段の場面は自分の半径（名前・年齢・住まい・色・習慣・計画）に閉じ、尋ねる相手も対面の知り合いである。上段に入ると、使いの往復（562）・業務の段取り（568）・準備した面接（591）・会議での追及（489）と、情報が制度的な場で運用されるようになる。ただしレベルを刻むのは場のフォーマルさではなく情報管理の精度である ── 面接（B1+・591）は新しい道具を増やさず既存の軸を場面に固定するだけであり、C1 の頂点（489）も改まった言い方ではなく、質問の再設計という運用技能である。フォーマルさの梯子ではなく精度の梯子 ── この点が、同じ上段でも管理課題が対人対立に向かう苦情との違いになる。",
"【往復・応答の点検 ── ask and answer が対で書かれた行為】 テンプレート要件（判断(n)）の点検：下段の記述文はほぼすべて ask and answer / ask and tell と往復を明記し、する側と受ける側が最初から対で梯子を上る ── 四役完備（依頼）とも片側往復（苦情）とも異なる、対称往復の行為である。断る・返す型に相当するのは、答えられないときの返し（I'm not sure. / Let me check.）と聞き返し・確認（Could you say that again? / Just to confirm ...）であり、B1+ の照合・確認（555）が受け側在庫の中核をなす。日本語話者最大の敵は聞き返し回避（分かったふり）で、確認のメタ発話を恥ではなく手続きとして運用できるかが上段の分水嶺になる。日本語では確認が相槌と復唱で暗黙に行われるのに対し、英語では明示的なメタ発話で行う ── この明示化の型は統語でも語彙でもなく、確認行動の文化差という L1 難所である。伝聞・情報源の標識（they said / apparently）を落とすと他者の情報が自分の断定にすり替わる ── 受けた情報を第三者へ渡すときの受け側作法もここに属す。",
"【口頭は往復、書面は自己完結 ── 書面フォーマル一段の成立】 口頭系列24件が対話の往復で深まるのに対し、書面系列7件は文脈補完が効かないぶん自己完結性が階段になる：情報1粒＋質問1つの最小形（A1・649）→ 電報体の規約（A2・659）→ 質問との対応づけ（A2+・642）とオンラインの同期的往復（679）→ 用件別の型（B1・640）と重要度順の情報選別（656）→ そして書面 B2（633）で「適切な構造と内容」というレジスターの制度化に至る。書面フォーマル一段（判断(o)）は成立 ── 633 は3値判別の成立側3例の一つ（632・633・628）であり、業務書簡というフォーマル系列が B2 帯に達している。633 の但し書き「事実の事柄に限る」は本質的で、CEFR 自身が事実伝達と意見・交渉の間に引いた境界線として、この行為の輪郭を外から確定している。",
"【統合根拠と点検総括・語彙裁定】 統合根拠：判断(k)（第2周-1、質問応答↔授受の一行為二相統合）。証拠は (1) レベル帯の相補性（下段 Pre-A1〜A2+／上段 A1〜C1）、(2) 562/557 の条件緩和型接続、(3) 同一 Information exchange スケールの分有。相境界で L1 注意は質的に転換する ── 下段は統語（do 支持・疑問詞語順・時制の疑問文・it の脱落）、上段は談話（確認のメタ発話・伝聞標識・重要度順の再構成）。この転換点ゆえに、統合後も二相の別立て記述を保つ（一行為二相、act_phases.json が正準）。語彙裁定（判断(s)）：新規16行の実例は各レベルの語彙枠内で作成（スロット語彙の固有名詞 Ken / Kyoto は実例の登場人物・地名として正当、判断(s)-1 の枠）。継承15行のうち検証範型③で未裁定だった超過3語を量産時裁定（判断(s)-3）：pharmacy（562・A2+行）＝場所スロット、workshop（642・A2+行）＝行事スロット、plumber（656・B1行）＝職業スロット ── いずれもレベル保証は行為の枠（The X closes at ... — I checked. 等）に適用し、スロット名詞は可変域として保持（判断(s)-1）。keynote（会話維持427）は未収録につき allowlist 記載。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    inherited = json.load(open(os.path.join(root, "prototypes/verification_assertive.json"), encoding="utf-8"))[ACT]["rows"]
    by_no = {r["no"]: dict(r) for r in inherited}
    for no, mode, ex, scene, hw, l1, delta in NEW:
        by_no[no] = {"mode": mode, "no": no, "exponents": ex, "scene": scene,
                     "howwell": hw, "l1": l1, "delta": delta}
    for no, d in DELTA_EDITS.items():
        by_no[no]["delta"] = d
    rows = []
    for no in ORDER:
        r = by_no[no]
        d = desc[str(no)]
        rows.append({"mode": r["mode"], "level": d["level"], "no": no, "en": d["en"],
                     "jp": tr[str(no)], "exponents": r["exponents"], "scene": r["scene"],
                     "howwell": r["howwell"], "l1": r["l1"], "delta": r["delta"]})
    return {ACT: {"title": TITLE, "scope": SCOPE, "type": TYPE_,
                  "essence": ESSENCE, "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    data = build(root)
    out = os.path.join(here, 'catalog_infoexchange.json')
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 31, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    # 相所属の全数一致（二相接続型テンプレート必須項目）
    ph = json.load(open(os.path.join(root, "data/act_phases.json"), encoding="utf-8"))[ACT]
    parts = {k: set(v) for k, v in ph.items() if isinstance(v, list)}
    union = set().union(*parts.values())
    assert {r["no"] for r in rows} == union, "act_phases との不一致"
    print(f"catalog_infoexchange.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}／"
          f"質問応答相{sum(1 for r in rows if r['no'] in parts['質問応答相（構造）'])}＋情報管理相{sum(1 for r in rows if r['no'] in parts['情報管理相（運用）'])}）")
