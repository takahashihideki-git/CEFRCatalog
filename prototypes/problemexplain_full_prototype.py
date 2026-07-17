# -*- coding: utf-8 -*-
"""第3周-5第三陣：問題・事情の説明8件の全数シート（管理梯子型）。全行口頭。
実行すると prototypes/catalog_problemexplain.json を生成する。"""
import json, os

ACT = '問題・事情の説明'
TITLE = '問題・事情の説明（Explaining problems & circumstances）── 全数シート'
SCOPE = '全数（8件。口頭8）'
TYPE_ = '主張的（assertive）── 何が起きているか、なぜ問題かを伝わる形で述べる。下位系＝叙述系、梯子型＝管理梯子型（管理課題＝説明の精密さ、A1〜B2。第3周-5第三陣で確定）'
ESSENCE = '何が起きているか、なぜ問題なのかを相手に伝わる形で説明する。梯子は説明の精密さ ── 身振り込みの一点表示から、症状の記述、理由の明示、譲歩を導く説明へ。'

ROWS = [
(600, '口頭', ["My head hurts.", "It hurts here.（押さえて） — Does that hurt? — Yes, a little."],
 "医療従事者に問題の性質を簡単な言葉で述べ、「そこは痛みますか」等の簡単な質問に答える（身振りの補強つき）。",
 "部位＋hurts の最小構文と Yes/No 応答。",
 "症状語彙の不足で受診をためらいがちだが、この段のCEFRの要求は正しい病名でなく「部位を指して hurts」── それで医療は動く。",
 "（起点）説明は一点（どこが・痛い）から始まる。質問に答える形の説明で、主導権はまだ聞き手側。"),
(598, '口頭', ["My stomach hurts.", "I feel sick.（お腹を押さえて）"],
 "医療従事者に問題の性質を簡単な言葉で示す（身振り・ボディランゲージ併用可）。",
 "部位＋hurts と I feel ... の症状枠。",
 "痛みの言い分け（hurt/ache/sick）は日本語の「痛い・気持ち悪い」と一対一に対応しない ── 枠ごと（My X hurts / I feel sick）覚える。",
 "応答（600）から自発の表示へ。545（取引）後半とほぼ同文言のスケール再掲対 ── 二行保持・相互参照。"),
(596, '口頭', ["I have a cold. I've had a cough since Monday.", "I think I have the flu."],
 "風邪やインフルエンザのようなごく基本的な症状・不調を医師に説明する。",
 "症状の複数提示と期間（since/for）の付加。",
 "「いつから」が抜けると診断情報は半減する ── since Monday / for three days は説明の必須成分で、日本語では文末に来る情報を早めに出す。",
 "一点の表示から、複数症状＋経過という記述へ。"),
(593, '口頭', ["I've had a headache for three days. Should I take anything?", "Is it serious?"],
 "医療サービス利用時に症状を簡単に説明して助言を求め、日常語での答えを理解する。",
 "説明→助言要求→理解の三手の接続。",
 "説明して黙って診てもらう型から、Should I ...? まで進む「質問する患者」への切替 ── 説明は助言を引き出すための土台になる（→助言シート相互参照）。",
 "説明が目的（助言の獲得）と結合する。回答が日常語で与えられるという支え条件つき。"),
(590, '口頭', ["The pain started after I fell. It's worse when I walk.", "It's a sharp pain. It comes and goes."],
 "面接・相談で求められる具体的な情報（医師への症状説明など）を提供する。ただし正確さは限られる。",
 "叙述の正確さ ── 性質・条件・経過の記述。",
 "痛みの性質は擬態語（ズキズキ・シクシク）の直訳では出ない ── 記述軸（鋭さ sharp／持続 comes and goes／条件 when I walk）に置き換える。",
 "説明の中身が聞き手の要求水準で測られ始める。「正確さは限られる」の但し書きが上段への余白を測る。"),
(465, '口頭', ["The problem is that we don't have enough time.", "It's a problem because the deadline is next week."],
 "なぜ問題なのかを説明する（友人との議論）。",
 "理由標識（because / The problem is that ...）の運用。",
 "「問題です」で止めて「なぜ」を言語化しない癖 ── 問題性は共有知識ではなく、明示して初めて共有される。",
 "対象が症状（身体）から事態（状況）へ一般化し、「なぜ」が説明の核心になる。511と部分同文言のスケール再掲対。"),
(511, '口頭', ["The problem is the cost. We could rent instead — it's cheaper, but slower.", "If we do it this way, we can save time."],
 "協働作業で、なぜ問題かを説明し、次に何をするか話し合い、選択肢を比較・対照する。",
 "説明→提案→比較の運び（談話の束）。",
 "問題の指摘だけで代案を出さないと非難に響く ── 説明と提案の接続が協働の作法（→提案シート467/508相互参照）。",
 "465の説明が協働の文脈に埋め込まれ、提案・比較と束になる ── 465を含む同文言のスケール再掲対、二行保持・相互参照。"),
(529, '口頭', ["The washing machine broke again a week after the repair. I think a replacement is fair.", "I understand the policy, but this is the third time."],
 "生じた問題を説明し、サービス提供者／客が譲歩すべきことを明確にする。",
 "説明と要求の分離と接続 ── 事実の積み上げで譲歩を導く。",
 "事実説明の段に感情を混ぜると苦情の「振れすぎ」に落ちる ── 説明の正確さがそのまま交渉力になる、が この段の分業。",
 "到達点で説明は交渉の道具になる ── 苦情・クレーム帯（628系）の隣接領域で、譲歩要求を支える説明（→苦情シート相互参照）。"),
]

ORDER = [600, 598, 596, 593, 590, 465, 511, 529]

DISCUSSION = [
"【管理課題の梯子 ── 説明の精密さ、一点からなぜへ】 一点表示（600）→自発表示（598）→複数症状＋経過（596）→助言要求と結合（593）→性質の記述（590）→理由の明示（465）→提案との束（511）→譲歩を導く説明（529）。梯子の実体は説明の精密さ（cross_axesの管理課題と一致）で、下段は語彙と構文（症状枠・期間）、中段から談話（理由標識・束）へ重心が移る。",
"【場面 ── 医療が下段の訓練場、B1+で議論・協働へ一般化】 A1〜B1+の主戦場は医療窓口（Interviewingスケール由来）で、身振り併用（600/598）という支えが下段を支える。B1+で対象が事態一般（465/511）へ開き、B2で取引の紛争（529）に届く ── 説明という営みが、身体から状況へ、私事から交渉へと領分を広げる。",
"【往復・応答の点検 ── 説明は応答として始まり、自発化する】 起点600は医師の質問に答える形（Does that hurt? — Yes）で、する側と受ける側が最初から往復に埋まっている。受け手は医療者・サービス提供者役割で片側往復だが、(n)の病理はここでは「言い足りない」に現れる ── 遠慮による情報の出し渋りが誤診・不利な裁定に直結する。",
"【全行口頭 ── (o)判定＝書面系列なし】 書面の問題説明は655（伝言の授受＝問題を説明する伝言）と苦情の書面系列（628帯）に吸収されており、本行為の帳簿は口頭のみ。判定＝書面系列なし（会話維持と同区分）。",
"【点検総括・語彙裁定】 スケール再掲対2件（545/598・465/511、いずれも二行保持・相互参照 ── 511は465の完全包含＋拡張という新しい形の対で、場面横断性に加えて「束への埋め込み」を示す）。梯子型＝管理梯子型で確定。語彙裁定（判断(s)）：flu（596・A2+行）＝記述文由来（such as a cold or the flu）、cough（596・A2+行）＝症状スロット（(s)-1）として保持。",
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
    json.dump(data, open(os.path.join(here, 'catalog_problemexplain.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 8 and len(DISCUSSION) == 5
    print(f"catalog_problemexplain.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}）")
