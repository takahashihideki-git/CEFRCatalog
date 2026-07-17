# -*- coding: utf-8 -*-
"""第3周-5第三陣：提案・誘い・計画の相談8件の全数シート（管理梯子型）。
697は670先例に従い書面。実行すると prototypes/catalog_proposal.json を生成する。"""
import json, os

ACT = '提案・誘い・計画の相談'
TITLE = '提案・誘い・計画の相談（Suggestions, invitations & planning）── 全数シート'
SCOPE = '全数（8件。口頭6＋書面2）'
TYPE_ = '指示的（directive）── 何をするかを一緒に決める。下位系＝協調調整系、梯子型＝管理梯子型（管理課題＝調整の複雑化、A2〜B2。第3周-5第三陣で確定）'
ESSENCE = '何をするかを一緒に決める。梯子は調整の複雑化 ── 単純な相談から、提案の往復、選択肢の比較、場の進行支援と提案の正当化へ。'

ROWS = [
(477, '口頭', ["What should we do about lunch?", "Maybe we can ask Tom."],
 "明瞭にゆっくり直接話しかけられれば、日常の実際的な問題を簡単な方法で話し合う。",
 "相談の最小往復（問題の提示と案の一言）。",
 "「どうしようか」を頭の中で抱え込まず、声に出して相談の場に載せる ── 相談は考えてから話すのでなく、話しながら考える営み。",
 "（起点）受信配慮条件つき ── 相談は聞き取れることから始まる。"),
(478, '口頭', ["Let's go to the park. — Good idea!", "See you at six at the station, OK?"],
 "何をするか・どこへ行くかを話し合い、会う約束をする。",
 "Let's 枠と約束の確定（時間・場所の数字での固定）。",
 "「じゃあまた」の曖昧な閉じは英語では約束が成立していない ── 時間・場所を数字で確定してから会話を閉じる。",
 "477から受信配慮条件が外れ、相談が決定（約束）まで届く。"),
(645, '書面', ["Do you want to come to my birthday party on Saturday?", "Sorry, I can't come on Friday. How about Sunday?"],
 "招待の送付・返信、手配の確認・変更の短く簡単なメモ・メール・メッセージを書く。",
 "招待・変更の書面定型（Do you want to ...? / How about ...?）。",
 "断りの返信は Sorry, I can't ＋ 代案 ── 理由の長い釈明は不要で、代案の提示が礼儀を担う。",
 "書面系列の唯一の行。誘い・調整が文字で完結する最小形。"),
(474, '口頭', ["What are you doing this weekend?", "Do you want to see a film tonight?"],
 "夜や週末に何をするか話し合う。",
 "誘いの打診定型（Do you want to ...? / How about ...?）。",
 "Let's（決定寄り）と Do you want to（打診）の使い分け ── 距離感の調整装置がこの二枚から始まる。",
 "478の約束から、余暇の計画という開いた相談へ。"),
(475, '口頭', ["Why don't we take a break? — That sounds good.", "Hmm, how about a bit later?"],
 "提案をし、提案に応じる。",
 "提案と応答の対 ── する側（Why don't we）と受ける側（sounds good / how about ...）の定型。",
 "提案への応答在庫が薄いと沈黙が拒否に読まれる ── (n)の受け側問題の提案版で、受けの一言（Sounds good）が調整を回す。",
 "行為核の明文化 ── make and respond が対で書かれ、往復が行為の定義に入る。"),
(467, '口頭', ["The bus is cheaper, but the train is faster.", "If we leave early, we can miss the traffic."],
 "何をするか・どこへ行くか・誰を／どれを選ぶかを話し合いながら、選択肢を比較・対照する。",
 "比較の談話型（A is X, but B is Y）と条件文の運用。",
 "比較の本丸は -er/more の形態でなく、選択肢を並べて見せる談話の型 ── 「AよりB」の一文でなく、AとBの性質を対で陳列する。",
 "提案の応酬から、選択肢の構造化（比較・対照）へ ── 511（問題説明）と隣接し、意見473の「比較」と通底する。"),
(508, '口頭', ["Ken, what do you think?", "Shall we start with the plan for Saturday?"],
 "他の人に参加を促し、考えを述べてもらうなどして、作業の進行を助ける。",
 "進行の運営 ── 発言の分配（名指しの促し）と議題の提示。",
 "名指しで意見を求める（Ken, what do you think?）は詰問でなく参加への招待 ── 会話維持の運営段（→会話維持シート）と同じ転回がここで起きる。",
 "自分の提案から、他者の提案を引き出す側へ ── 調整の主体が場の運営者になる。"),
(697, '書面', ["I suggest we use the old logo — it did better with users.", "Could you clarify the budget? Then I can update the plan."],
 "オンライン協働で、提案を正当化し、明確化を求め、支援的な役割を果たして共有課題を達成する。",
 "提案＋根拠（正当化）の書面構造。",
 "提案の裸置き（I suggest X.）で終えず根拠を接続する ── 正当化（justify）が提案をB2にする。意見表明の根拠支持と同じ転換が提案側で起きる（→意見シート相互参照）。",
 "提案が正当化を要求される段 ── 明確化要求（→明確化シート699）と束になり、協働の実務になる。"),
]

ORDER = [477, 478, 645, 474, 475, 467, 508, 697]

DISCUSSION = [
"【管理課題の梯子 ── 調整の複雑化】 相談の最小形（477、受信配慮つき）→約束の確定（478）→打診（474）→提案往復の明文化（475）→選択肢の構造化（467）→進行支援（508）・正当化（697）。梯子の実体は調整の複雑さ（cross_axesの管理課題と一致）で、下段は定型（Let's / Do you want to）、上段は談話（比較の陳列・根拠の接続・場の運営）へ移る ── 477→478の受信配慮条件の脱落は562/557型。",
"【場面 ── 友人の日常から協働・プロジェクトへ】 下段は友人との余暇（Informal discussion）、上段は協働作業（Goal-oriented）とオンラインプロジェクト（697）。フォーマル討議の提案はFormal discussion帳簿（意見表明側）にあり、本行為は私的・協働文脈を受け持つ ── 対立管理系との文脈分業（苦情＝取引／意見＝討議）の協調調整版。",
"【往復・応答の点検 ── 往復が行為の定義に書かれた行為】 475が make and respond を一つの記述文に持ち、する側・受ける側が対で梯子を上る対称往復（授受と同型）。断る・返す型＝645の「Sorry, I can't ＋ 代案」が正準で、代案の提示が断りを協調の一手に変える ── 裸の No は調整の停止として響く。",
"【口頭は往復、書面は招待と正当化 ── (o)判定＝非成立（B2未達型）】 口頭6＋書面2。Correspondence系列は645（A2）のみでB2帯に届かず、判定＝非成立（B2未達型、意見表明と同区分）。書面のもう一件697はオンライン協働系で、書面梯子の実体は正当化という談話課題。",
"【点検総括・語彙裁定】 梯子型＝管理梯子型で確定。467は意見表明473（比較＝理由の原型）・問題説明511と三つ巴で隣接し、「比較」が評価・説明・調整の三行為を貫く蝶番であることが全数シート横断で見える。語彙裁定（判断(s)）：固有名詞（Ken・508行）はallowlist裁定、他フラグなし（logo は収録内で通過）。",
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
    json.dump(data, open(os.path.join(here, 'catalog_proposal.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 8 and len(DISCUSSION) == 5
    print(f"catalog_proposal.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
