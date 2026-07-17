# -*- coding: utf-8 -*-
"""第3周-5第三陣：伝言の授受7件の全数シート（管理梯子型）。
No.612（Using telecommunications・口頭）は判断(v)で採用 ── 篩266・ADOPT183。
実行すると prototypes/catalog_message.json を生成する。"""
import json, os

ACT = '伝言の授受'
TITLE = '伝言の授受（Taking & leaving messages）── 全数シート'
SCOPE = '全数（7件。口頭1＋書面6。No.612は判断(v)で採用）'
TYPE_ = '主張的（assertive）── 人から人へ、内容を損なわずに言葉を運ぶ。下位系＝情報授受系、梯子型＝管理梯子型（管理課題＝中継内容の複雑化、A1〜B2。第3周-5第三陣で確定）'
ESSENCE = '人から人へ、内容を損なわずに言葉を運ぶ。梯子は中継内容の複雑化と中継の完結性 ── 一行のメモから、電話の受領・確認・伝達のループ、複数の要点、そして複雑な用件へ。'

ROWS = [
(662, '書面', ["Shopping. Back at 5 p.m.", "Gone to the bank. Back soon."],
 "どこへ行ったか・何時に戻るかなどの情報を伝える簡単な伝言を残す。",
 "電報体の最小情報（場所＋時刻）。",
 "主語省略の電報体はここでは正用 ── 完全文の強迫を外し、名詞＋時刻で足りることを知る。",
 "（起点）残す側の最小形。伝言は文でなく情報の粒。"),
(612, '口頭', ["OK — your flight is late, and you'll arrive at ten. I'll tell them.", "（関係者へ電話）Ken called. His flight is late. He'll arrive at ten."],
 "簡単な伝言を理解し、内容を確認し、電話で関係者に伝える。",
 "中継ループの完結 ── 受領・復唱確認・伝達の三手。",
 "復唱確認（So your flight is ...?）を省くと誤伝の責任が中継者に落ちる ── 確認は失礼でなく中継の義務。人称の付け替え（I→he）が第二の関門。",
 "口頭系列の唯一の行 ── 受→確認→伝の中継ループが一つの記述文で完結する（採否の判定は⑤）。"),
(658, '書面', ["（聞きながらメモ）Mr. Tanaka — meeting — 3 p.m. Could you say that again?", "Sorry, how do you spell the name?"],
 "繰り返し・言い直しを求められる条件で、短く簡単な伝言を受ける。",
 "書き取りと修復要求の併用。",
 "聞き取れないままメモの空欄を勘で埋めない ── 空欄＋聞き返し（→明確化シート）が正確な伝言を作る。",
 "受ける側の起点。修復（繰り返し・言い直し）という支え条件つき。"),
(657, '書面', ["（電話を聞きながら）Order 415 — delivery Friday — call back before 12.", "Let me check: Friday morning, right?"],
 "相手が明瞭に配慮して口述してくれれば、複数の要点を含む電話の伝言を受ける。",
 "要点の分離と列挙 ── 複数情報の並列管理。",
 "全文の書き取りでなく要点の粒に落とす ── 日本語のメモ術がそのまま効く数少ない地点。ただし固有名詞の綴りが穴になる。",
 "一粒（658）から複数要点へ。口述配慮という支え条件つき。"),
(654, '書面', ["Professor Lee's office called: tomorrow's class is moved to Room 302.", "Message from IT: the system will be down tonight, 10–11 p.m."],
 "個人的・職業的・学術的な文脈で起こりそうな日常的な伝言を受ける。",
 "文脈語彙（職場・大学）の在庫と定型運用。",
 "文脈が広がっても核は同じ「誰から・何を・いつ」── 文脈語彙の不足は構造（5W）で補える。",
 "657の口述配慮条件が外れ、通常の職業・学術文脈で機能する（562/557型の条件緩和）。"),
(655, '書面', ["Ms. Ito called: have the parts arrived? Please call her back.", "Note: the customer says the amount on the bill is wrong. Details tomorrow."],
 "問い合わせを伝え、問題を説明する伝言を受ける。",
 "用件種別（問い合わせ／問題）の識別と再構成。",
 "伝言が「問い合わせ」「問題」という行為を運ぶ段 ── 原話者の意図（訊きたい・困っている）を保存して書くことが正確さの中身になる。",
 "伝言の中身が情報から行為へ ── 問い合わせ・問題説明シートと交差する中継版（→各シート相互参照）。"),
(653, '書面', ["Let me check before I pass this on: you can come on the 12th, but you need the plan before then — correct?", "（伝言メモ）For Anna: the client accepts the new terms except point 3. Please call her before signing."],
 "必要に応じて明確化・詳述を求めつつ、複雑な個人的・職業的な伝言を受け、また残す。",
 "複雑な内容の構造化と確認 ── 明確化要求の運用。",
 "複雑な伝言ほど「自分の要約で確認」してから運ぶ ── 738（明確化シートの照合メタ発話）が中継の品質保証になる。",
 "到達点で受ける・残すの両側が複雑な内容で完備し、明確化要求（→明確化シート）が標準装備になる。"),
]

ORDER = [662, 612, 658, 657, 654, 655, 653]

DISCUSSION = [
"【管理課題の梯子 ── 中継内容の複雑化と中継の完結性】 一行のメモ（662）→口頭中継ループ（612）→書き取りの最小形（658）→複数要点（657）→文脈の拡大（654）→行為を運ぶ伝言（655）→複雑な用件の双方向（653）。梯子の実体は運ぶ内容の複雑さ（cross_axesの管理課題と一致）で、支え条件の脱落（657の口述配慮→654）が中段を刻む。",
"【三者行為 ── 唯一の非二者構造】 伝言は原話者→中継者→受領者の三者行為で、学習者の役割は中継者 ── 話し手でも聞き手でもなく、他人の言葉の運搬人である。ここから固有の技能（人称の付け替え、原話者の意図の保存、自分の解釈と原文の分離）が生じ、これは第4柱・仲介（mediation）の最小形がやり取りの帳簿に顔を出したものと読める ── カタログ横断の接続点。",
"【往復・応答の点検 ── (n)の病理は「確認の省略」】 受ける（658〜655）と残す（662・653）が揃い、653で双方向が完備する対称構造。中継における応答の作法は復唱確認（612・657・653）で、これを省く誤伝が(n)の病理のこの行為での現れ ── 相槌の欠落（会話維持）や無言実行（指示への応答）と同族の「受けの信号の省略」。",
"【口頭1・書面6 ── (o)判定＝非成立（Correspondence系列欠如型）】 書面はすべてNotes, messages and forms系で、電話口述の書き取りを含む混成帳簿。653はB2に達するが、その梯子は内容の複雑化でありレジスターの制度化段ではない。判定＝非成立（Correspondence系列欠如型）。口頭は612のみで、電話伝言という行為の原風景を帳簿につなぎ止める。",
"【No.612の採否判定（判断(v)）── 採用】 (r)で留置したUsing telecommunications 6件のうち612のみを単独で掛け直し、採用（篩266・ADOPT183）。理由：(a) 受領→確認→中継の行為核が一つの記述文で完結して読め、実例可能。(b) 本行為の既存6件は全て書面系で、行為の原風景（口頭の電話伝言）が帳簿に不在 ── この欠落を埋める唯一の記述文。(c) (r)の留置理由「チャネル条件を除けば既存記述文の再記述」が当てはまらない ── 中継ループ（confirm and pass on）は658（受ける）にも662（残す）にも書かれていない固有の核。残るUsing telecommunications 5件は留置のまま（対象外40件）。語彙裁定（判断(s)）：固有名詞（Ken・612行）はallowlist裁定。beforehand は実例の書き換えで回避、他フラグなし。",
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
    json.dump(data, open(os.path.join(here, 'catalog_message.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 7 and len(DISCUSSION) == 5
    print(f"catalog_message.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
