# -*- coding: utf-8 -*-
"""第3周-3：挨拶・別れ・安否（9件）の全数範型（様式昇格）。

既存範型（prototypes_4types.json）の著述フィールドを継承し、全数シート様式へ昇格：jp を作業訳に正準化
（構築時取得）、第2周以降の点検軸（(n)往復・応答／(o)書面フォーマル一段／
判断(s)語彙裁定）を DISCUSSION に適用。旧範型は歴史的サンプルとして凍結。

単一情報源の設計：en / jp は data から構築時取得。
実行すると prototypes/catalog_greeting.json を生成する。
"""
import json, os

TITLE = '挨拶・別れ・安否（Greeting, Leave-taking & Phatic exchange）── 全数シート'
SCOPE = '全数（9件。口頭6＋書面3）'
TYPE_ = '交話・儀礼（phatic）── 接触の確認そのものを目的とする定型の履行。下位系＝定型履行系（第一分類層）、出自類型＝交話・儀礼、梯子型＝定型履行型（型の履行で完結、難所は横＝レジスター・テンポへ）'
ESSENCE = '出会いと別れの区切りに定型表現を交わし、相手との社会的接触を開き・保ち・閉じる。内容の正しさより、型の適切さとテンポが行為の成否を決める。'

R = [
(453,
 '口頭',
 ["Yes. / No.", "Thank you. / No thank you.", "Excuse me. / Sorry.", "Please."],
 "あらゆる接触の潤滑油となる最小の定型語を、適切な場面で口にする。",
 "社会言語的適切さ（最小単位）：型を型として口に出せるか。",
 "No thank you を「いいえ、結構です」の丁寧な断りとして使えず、単に No と言って冷たく響くことがある。また Sorry と Excuse me の使い分け（謝罪／呼びかけ・断り）が日本語の「すみません」に一括されるため混同しやすい。",
 "（起点）語彙ですらなく「機能語の塊」。関係の潤滑油の最小部品。"),
(455,
 '口頭',
 ["Hello. / Hi.", "I'm Kenji.", "Goodbye. / Bye.", "See you."],
 "初対面や店・受付で、挨拶し名乗り、辞去する。会話の開閉の枠。",
 "社会言語的適切さ：出会いと別れの型をペアで押さえられるか。",
 "別れ際の See you. や Bye. を言わずに立ち去る、あるいは Goodbye だけで済ませて素っ気なくなる。日本語の「じゃあ」「どうも」に当たる軽い辞去表現の層が薄い。",
 "定型語から「会話の開閉」へ。挨拶と別れは対で機能する。"),
(451,
 '口頭',
 ["Good morning. / Good afternoon.", "This is my friend, Aya.", "Nice to meet you.", "Have a nice day!"],
 "他者を紹介し、時間帯に応じた挨拶と、別れ際の一言を添える。",
 "社会言語的適切さ：時間帯・相手による型の選択。",
 "Nice to meet you.（初対面）と Nice to see you.（再会）の別を知らず、再会でも meet を使ってしまう。Have a nice day! のような別れ際の「気遣いの一言」を添える習慣が乏しく、挨拶が短く切れる。",
 "Pre-A1からの差分：時間帯別（morning/afternoon）と紹介（This is...）が加わり、型が場面分化する。"),
(452,
 '口頭',
 ["How are you? — Fine, thanks. And you?", "How's it going?", "That's great! / Oh, I'm sorry to hear that."],
 "相手の近況・体調を尋ね、返ってきた知らせに感情で応じる。",
 "社会言語的適切さ＋テンポ：定型的な問い返し（And you?）の即応。",
 "How are you? を「本当に体調を訊く質問」と受け取り、長々と実際の状態を答えてしまう。英語では儀礼的な往復（Fine, thanks. And you?）が基本で、中身より往復のテンポが大事。この phatic な性質が日本語話者に最も伝わりにくい。",
 "一方向の挨拶から「往復」へ。相手の応答に反応する対話性が入る。"),
(444,
 '口頭',
 ["Good evening, Mr. Tanaka.", "Excuse me, sir. / Excuse me, madam.", "How do you do?（改まった初対面）"],
 "目上や公的な相手に、丁寧なレジスターで挨拶し呼びかける。",
 "社会言語的適切さ（レジスター）：親しさ／改まりで型を選び分けられるか。",
 "英語の呼びかけには sir/madam や Mr./Ms.＋姓があるが、日本語の「〜さん」を万能に使う感覚で first name を使い、目上に馴れ馴れしく響く。逆に過度に Mr. を連発して不自然になることも。相手との距離に応じた呼称選択は明示的な学習を要する。",
 "A1からの差分：中立な挨拶から「丁寧なレジスター」の選択へ。呼びかけ（address）が加わる。"),
(438,
 '口頭',
 ["Hi, I don't think we've met — I'm Kenji.", "It was really nice talking to you.", "Thanks so much for having me. / Let's keep in touch."],
 "パーティや職場で、自ら関係を開き、会話を交わし、良い印象で閉じる一連。",
 "社会言語的適切さ＋柔軟さ：開始・維持・終了を状況に合わせて束ねる。",
 "関係を自分から「開く」定型（I don't think we've met）や、良い印象で「閉じる」定型（It was nice talking to you / keep in touch）の層が薄く、挨拶が入口だけで終わりがち。日本語では別れの挨拶が定型的に厚いのに、英語ではその機能表現を別途習得しないと使えない。",
 "個別の挨拶から「社交的接触の確立」へ。開始〜維持〜終了を一続きの営みとして統合する到達点。"),
(686,
 '書面',
 ["Happy birthday! 🎉", "Good luck! 😊", "Congrats!"],
 "SNSやチャットで、定型句＋絵文字の短い挨拶を投稿する。",
 "社会言語的適切さ（オンライン・レジスター）：くだけた場の型と絵文字の運用。",
 "日本語のオンライン儀礼（「おめでとう🎊」）の感覚は近いが、英語の Congrats! / Happy belated birthday!（遅れた誕生日祝い）のような口語省略形を知らず、硬い Congratulations に留まる。絵文字の使用も控えめすぎることがある。",
 "（書面起点）口頭の定型語が、オンラインでは絵文字と結んで機能する。"),
(648,
 '書面',
 ["Dear Aya, Greetings from Kyoto! The temples are beautiful. See you soon, Kenji", "Hi Mom, Having a great time here. Weather is lovely. Love, Kenji"],
 "旅先などから、近況の一言を添えた短いはがきを書く。",
 "社会言語的適切さ（書面枠）：Dear... と結び（Love/See you soon）の枠を守れるか。",
 "はがき・手紙の結びの語（Love, / Best, / See you soon,）の層が薄く、日本語の「それでは」を直訳して不自然になる。宛名の Dear は日本語の「親愛なる」より軽く日常的、という温度感も掴みにくい。",
 "オンライン挨拶からの差分：書面の「枠」（宛名・本文・結び）が加わる。"),
(682,
 '書面',
 ["Congratulations on your new job! So happy for you.", "Long time no see! How have you been?", "Shall we meet around 7? — Sounds good, see you then!"],
 "オンラインで、祝い・近況・約束の確認まで含む社交的なやりとりをする。",
 "社会言語的適切さ＋テンポ：非同期のやりとりで型と応答を回す。",
 "Long time no see! のような口語定型や、約束確認の Sounds good, see you then! のテンポある応答が出てこず、事務的な確認に終始しがち。日本語のオンライン社交の「クッション」を英語の口語定型に置き換える必要がある。",
 "はがきの一方向から、オンラインの「往復する社交」へ。約束の設定・確認まで機能が広がる書面系列の到達点。"),
]

DISCUSSION = [
"【この行為に「上級」は無い ── 定型履行型の本質】 苦情がA2からC1まで長い梯子を持つのに対し、挨拶・別れ・安否はPre-A1からA2+に完全に収まり、B1以上に記述文が一つも無い。これは欠落ではなく、交話的（phatic）行為の本質である。挨拶に高度な熟達は存在しない ── C2話者も \"Hi, how are you?\" と言う。判断(p)の統一原理で言えば、この行為は管理課題を行為内に保持しない＝型の履行で完結する定型履行型であり、レベル梯子は立たず、難所は横（レジスター・テンポ＝how well系）へ移る。カタログは「レベルを上る」構造ではなく、「初級の型を、いかに場に合わせて選ぶか」という水平の広がりを持つ。",
"【難しさは「レベル」ではなく「レジスターとテンポ」にある】 日本語話者にとって易しいかというと逆で、難所がレベル軸と直交する二つの次元に潜む。第一はレジスター（親しさ・改まりの選択）。sir/madam、Mr.＋姓、first name、ニックネームの使い分けは、日本語の「〜さん」一括感覚では捌けず、相手との距離を英語の呼称体系で測り直す必要がある。第二はテンポ。How are you? — Fine, thanks. And you? の往復は、中身ではなく「間髪入れず型を返す」ことに意味がある。この二つは文法でも語彙でもなく、how well の軸でいえば社会言語的適切さに全面的に属する ── 縦横分業（判断(p)）の定型履行型版である。",
"【How are you? は質問ではない ── phatic の核心的誤解】 日本語話者が最もつまずくのは、儀礼的な問いを情報要求と受け取ることである。How are you? に実際の体調を長々答える、How's it going? に詰まる ── これは英語力ではなく、phatic communion（意味の交換ではなく接触の確認そのものが目的の発話）という概念が母語で意識されないために起こる。この行為を教えるとき、「中身より往復」「型は型として回す」という phatic の性質そのものを明示的に伝えることが、どの実例よりも効く。",
"【往復・応答の点検：型の往復そのものが行為である ── 開始は言えるが、維持と終了が言えない】 テンプレート要件（判断(n)）の点検結果：この行為では、する側／受ける側の対が定型ペアそのもの（How are you? — Fine, thanks. And you? は往復軸の最小完結形）であり、受け在庫（That's great! / Oh, I'm sorry to hear that.＝No.452）も記述文レベルで明記される ── 往復軸の教科書的な行為である。日本語話者の在庫は入口（Hello, Nice to meet you）に偏り、関係を「閉じる」定型（It was nice talking to you / Let's keep in touch / Have a nice day）の層が決定的に薄い。日本語では別れの挨拶がむしろ厚い（「それでは失礼します」）のに英語で出てこないのは、機能が同じでも表現が一対一で写らず、英語側の閉じる定型を別個の語彙として持っていないためである。カタログでは開始・維持・終了を三点セットで示し、とりわけ終了の定型を厚くする。",
"【点検総括と語彙裁定】 書面フォーマル一段（判断(o)）は非適用 ── 書面系列は648（A1）・682（A2）で消え、Correspondence がB2帯まで伸びない。精緻化条件「Correspondence系列がB2帯まで伸びる行為でのみ現れる」の不成立側と整合し、これで条件は3値で判別的に働く（伸びる→現れる：感謝詫び632・授受633・苦情628／伸びない→現れない：挨拶・意見表明）。語彙裁定（判断(s)の枠内、CEFRカタログ4）：greetings（648・A1行）＝絵葉書定型 Greetings from X! の不可分の一部として保持／madam（444・A2行）＝呼びかけ定型 Excuse me, madam の一部として保持（苦情638の Dear Sir or Madam と同語・同理由）。固有名詞（Kenji/Aya/Kyoto/Tanaka）は実例の登場人物として正当。oh/goodbye/congratulations/congrats はCEFR-J未収録の間投詞・定型として allowlist 裁定済み（判断(s)-2）。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    rows = []
    for no, mode, ex, scene, hw, l1, delta in R:
        d = desc[str(no)]
        rows.append({"mode": mode, "level": d["level"], "no": no, "en": d["en"],
                     "jp": tr[str(no)], "exponents": ex, "scene": scene,
                     "howwell": hw, "l1": l1, "delta": delta})
    return {'挨拶・別れ・安否': {"title": TITLE, "scope": SCOPE, "type": TYPE_,
                      "essence": ESSENCE, "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    data = build(root)
    out = os.path.join(here, 'catalog_greeting.json')
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data['挨拶・別れ・安否']["rows"]
    assert len(rows) == 9, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    print(f"catalog_greeting.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
