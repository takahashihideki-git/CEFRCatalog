# -*- coding: utf-8 -*-
"""第3周-5第三陣：取引（購入・注文）12件の全数シート（管理梯子型）。
Pre-A1起点の最長帯行為。オンライン5件は670先例に従い書面。
実行すると prototypes/catalog_transaction.json を生成する。"""
import json, os

ACT = '取引（購入・注文）'
TITLE = '取引（購入・注文）（Transactions: purchasing & ordering）── 全数シート'
SCOPE = '全数（12件。口頭7＋書面5）'
TYPE_ = '指示的（directive）── 欲しいものを言い、取引を成立させる。下位系＝取引系、梯子型＝管理梯子型（管理課題＝取引の複雑化、Pre-A1〜C1。第3周-5第三陣で確定）'
ESSENCE = '欲しいものを言い、値段を尋ね、注文し、取引を閉じる。梯子は取引の複雑化 ── 指差しで足りる購買から、定型の取引、問題への対応、条件の交渉、そしてサービスを提供する側へ。'

ROWS = [
(549, '口頭', ["This one, please. （指差して）", "Two coffees, please."],
 "指差しなどの身振りで言葉を補いながら、簡単な買い物・飲食物の注文をする。",
 "最小定型（..., please.）と身振りの併用。",
 "「すみません」で店員を呼ぶ習慣のまま Excuse me を落として無言で指すと、要求でなく独り言に見える ── 指差しは発話の補助であって代替ではない。",
 "（起点）取引は全行為の中で最も早くPre-A1で始まる ── 身振りが正規の支えとして明記される。"),
(543, '口頭', ["I'll have the chicken, please.", "Can I get a coffee?"],
 "レストラン・カフェで食事を注文する。",
 "注文の動詞枠（I'll have ... / Can I get ...）の在庫。",
 "「〜をお願いします」の直訳で Chicken, please. だけでも通じるが、動詞枠に乗せると注文が大人になる ── 名詞投げからの卒業がこの段。",
 "549から身振りの支えが外れ、注文が言葉だけで立つ。"),
(542, '口頭', ["I'd like this one. How much is it?", "How much are these shoes?"],
 "何が欲しいかを述べ、値段を尋ねて簡単な買い物をする。",
 "要求＋価格質問の二手の接続。",
 "How much ...? は言えても答えの数字が聞き取れないと取引が閉じない ── 価格の聞き取り（thirteen/thirty）が裏の関門。",
 "「欲しい＋いくら」という取引の最小二手が揃う。"),
(540, '口頭', ["I'd like to send this to Japan.", "Can I change this into euros?"],
 "店・郵便局・銀行で物事を尋ね、簡単な取引をする。",
 "窓口の用件定型（send / change / open）。",
 "窓口では用件を結論から言う ── 事情の説明から入る日本語の順序を裏返し、I'd like to ... を第一声にする。",
 "取引の場が商店から窓口機関（郵便局・銀行）へ広がる。"),
(539, '口頭', ["A ticket to the airport, please.", "Which bus goes to the station?"],
 "旅行の簡単な情報を得て、公共交通機関を使い、道順を尋ね教え、切符を買う。",
 "移動場面の定型束（切符・路線・道順）の即応運用。",
 "交通の窓口・車内は速い ── 定型を塊で出せないと列の圧力で崩れる。聞き返し（→明確化シート）とセットで在庫する。",
 "単品の購買から、移動という複合場面のやりくりへ。道順の授受を含む（→道案内シート相互参照）。"),
(545, '口頭', ["I'd like to see a doctor, please.", "My stomach hurts. （お腹を押さえて）"],
 "対面で診察の予約を求めて返答を理解し、医療従事者に問題の性質を示す。",
 "予約要求＋症状の最小表示の接続。",
 "症状は正しい病名でなく部位＋hurts で足りる ── 語彙不足を理由に受診をためらわないことが、この記述文の実務的な核心。",
 "取引が身体・健康という切実な領域へ。後半は598（問題・事情の説明）とほぼ同文言のスケール再掲対 ── 二行保持・相互参照。"),
(705, '書面', ["Name: Ken Sato / Address: 2-1 Sakura Street ...（フォームに記入）", "No, thank you.（追加サービスのチェックを外す）"],
 "オンラインの用紙・質問票に記入し、規約への同意を確認し、追加サービスを断って簡単な取引（商品注文・講座登録）をする。",
 "フォームの規約（姓名・住所の並び、必須欄、同意チェック）の運用。",
 "First name / Last name の取り違えと住所の逆順は、ここで初めて実害になる ── フォームは間違いを訂正してくれない対話相手である。",
 "書面系列の起点。取引の相手が人からフォームへ替わる。"),
(537, '口頭', ["What time does the castle open?", "Is there a bus from the station? And how much is it?"],
 "率直で専門的でない内容なら、観光案内所で必要な情報をすべて得る。",
 "質問の網羅性 ── 必要事項（時間・行き方・料金）を尋ね切る。",
 "一問で遠慮して切り上げない ── 「すべて得られる」がこの段の要求で、質問の連鎖（531＝明確化シートの取引文脈）と同じ壁を持つ。",
 "個別の質問から、用件の完遂へ ── 取引の単位が一往復から一件になる。"),
(703, '書面', ["Do you still have this model?", "Could you change the delivery date to Friday?"],
 "オンライン取引で生じる日常的な問題（在庫・特価品・配達日・住所）に定型表現で対応する。",
 "取引トラブルの定型在庫（delivery date / change ... to ...）。",
 "問題の連絡は謝罪から入らず用件から ── 非が自分にない事務連絡に I'm so sorry を冠する癖は、責任の所在を曖昧にする。",
 "順調な取引（705）から問題が生じた取引へ ── ただし定型で対応できる日常的な範囲。"),
(700, '書面', ["I'd like to register for the beginners' course. Which documents do I need?", "What happens if I need to cancel?"],
 "講座・ツアー・行事への登録や会員申請など、詳細の簡単な明確化・説明を要するオンライン取引をする。",
 "明確化要求と説明の往復運用（→明確化シート702/699と同帯）。",
 "規約・条件の確認質問を「手間をかけて悪い」と省くと後で困るのは自分 ── 確認は手続の一部であって迷惑ではない。",
 "定型（703）で足りない、案件固有の詳細のやりとりが要求に入る。"),
(695, '書面', ["We can accept the price if delivery is within two weeks.", "Our requirements are as follows: ..."],
 "条件の交渉、込み入った詳細・特別要件の説明を要する、専門領域内のオンライン取引をする。",
 "条件の構造化提示（if節・箇条書き・番号）。",
 "条件の明示を「わがまま」と感じてぼかすと交渉は遅くなる ── 条件は早く明確に出すほど相手の手間も減る、が英語取引の作法。",
 "明確化（700）から交渉へ ── 自分の側の条件を立てる段。専門領域という支えつき。"),
(691, '書面', ["Thank you for your application. Could you clarify one point about your documents?", "In that case, we can offer you an alternative plan."],
 "サービス提供者の立場で、複雑な要件のある申請など複雑なオンライン取引に対応し、議論・交渉を運ぶために言葉を柔軟に調整する。",
 "柔軟な言語調整 ── 相手の理解度・状況に合わせた運び。",
 "客を卒業して応対する側に立つ段 ── 日本語の接客敬語の直訳ではなく、明快さと配慮の両立（plain but polite）が英語の接客規範。",
 "到達点で役割が反転する ── 客からサービス提供者へ。明確化668の「与える側」出現と同型の最上段役割反転。"),
]

ORDER = [549, 543,542,540,539,545,705, 537,703, 700, 695, 691]

DISCUSSION = [
"【管理課題の梯子 ── 取引の複雑化、Pre-A1からC1へ】 全行為で最も早い起点（Pre-A1・549）と、C1の役割反転（691）までを持つ最長帯の管理梯子。梯子の実体は、指差し購買（549）→注文・購買の定型（543/542）→窓口取引（540）→複合場面（539）→切実な領域（545）→用件の完遂（537）→問題対応（703）→詳細の明確化（700）→条件交渉（695）→サービス役（691）という取引そのものの複雑化であり、cross_axesの管理課題と一致する。支えの脱落（549の身振り→543）と場・内容の負荷増が交互にレベルを刻む。",
"【場面の広がり ── 生活の全域を貫く行為】 商店・飲食・郵便局・銀行・交通・医療・観光・オンライン取引と、場面は全行為中で最も多彩。ただしレベルを刻むのは場面ではなく取引の複雑さで、同じA2に商店も医療（545）も並ぶ。545の症状表示は598（問題・事情の説明）とのスケール再掲対で、取引と説明が医療窓口で交差することを帳簿自身が示す。",
"【往復・応答の点検 ── 片側往復の最上段反転】 客⇄提供者の役割行為で、受け手＝サービス提供者役割ゆえ基本は片側往復（苦情と同じ）。ただし最上段691で学習者がサービス役として受け側に立ち、片側往復が反転する ── 明確化（668で与える側が出現）と同型の「最上段役割反転」であり、苦情（628まで客側のまま）との対照が、対立を含む行為は反転せず、協働的取引は反転するという分業を示す。する側の定型＝要求・注文・照会の在庫、断る・返す型＝No, thank you.（705の追加サービス拒否が最初の「断り」）。",
"【口頭は対面窓口、書面はオンライン取引 ── (o)判定＝非成立（Correspondence系列欠如型）】 口頭7＋書面5。書面系列はすべてGoal-oriented online系でCorrespondence系列を欠き、書面梯子の実体は取引実務の複雑化（フォーム→定型対応→明確化→交渉→サービス役）であってレジスターの制度化段ではない。判定＝非成立（Correspondence系列欠如型、明確化と同区分）。オンライン5件のmodeは670先例に従い書面。",
"【点検総括・語彙裁定】 スケール再掲対1件（545/598、二行保持・相互参照）。梯子型＝管理梯子型で確定（仮判定どおり）。語彙裁定（判断(s)）：delivery（703・A2+行）＝記述文由来（delivery dates）として保持。固有名詞（Ken/Sakura・705行）はallowlist裁定。stock は実例の書き換えで回避。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    by_no = {r[0]: r for r in ROWS}
    rows = []
    for no in ORDER:
        _, mode, ex, scene, hw, l1, delta = by_no[no]
        d = desc[str(no)]
        rows.append({"mode": mode, "level": d["level"], "no": no, "en": d["en"], "jp": tr[str(no)],
                     "exponents": ex, "scene": scene, "howwell": hw, "l1": l1, "delta": delta})
    return {ACT: {"title": TITLE, "scope": SCOPE, "type": TYPE_, "essence": ESSENCE,
                  "rows": rows, "discussion": DISCUSSION}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
    data = build(root)
    json.dump(data, open(os.path.join(here, 'catalog_transaction.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 12 and len(DISCUSSION) == 5
    print(f"catalog_transaction.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
