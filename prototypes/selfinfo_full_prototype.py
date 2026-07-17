# -*- coding: utf-8 -*-
"""第3周-5第三陣：自己に関する情報提供5件の全数シート（外部化型）。
実行すると prototypes/catalog_selfinfo.json を生成する。"""
import json, os

ACT = '自己に関する情報提供'
TITLE = '自己に関する情報提供（Giving personal information）── 全数シート'
SCOPE = '全数（5件。口頭2＋書面3）'
TYPE_ = '主張的（assertive）── 自分が何者かを伝える。下位系＝情報授受系、梯子型＝外部化型（消失点A2。外部化先＝事実情報の授受・情報管理相と面接。第3周-5第三陣で確定）'
ESSENCE = '自分が何者かを伝える。Pre-A1〜A2で出尽くす起点行為 ── 名前・国籍・職業の粒から自己紹介の型まで。深化は事実情報の授受（情報管理相）と面接へ外部化される。'

ROWS = [
(650, '書面', ["My name is Ken. I am from Japan.", "I like music.（辞書を引きながら）"],
 "辞書を参照しながら、基本的な個人情報を短い句・文で伝える。",
 "最小の自己紹介文の組み立て（辞書という支えつき）。",
 "ローマ字の姓名順（Ken Sato か Sato Ken か）を自分で決めて一貫させる ── 揺れは相手の側で二人の人物になる。",
 "（起点）自己情報は道具（辞書）の支えつきで書くところから始まる。"),
(687, '書面', ["Single / Japan / Student（メニューから選択）", "I am an engineer.（翻訳ツールを参照して）"],
 "メニュー選択・オンライン翻訳ツール参照の支えつきで、自分についての短く簡単な情報をオンラインに投稿する。",
 "プロフィール欄の規約（選択肢・定型）の運用。",
 "職業・属性の和製英語（salaryman 等）の罠 ── 選択肢に既にある英語をそのまま使うのが最短で正確。",
 "650の対 ── 紙と辞書が、プロフィール欄と翻訳ツールに置き換わった同段の書面二型。"),
(599, '口頭', ["My name is Ken Sato. K-E-N.", "I live in Tokyo. I am a student."],
 "個人的な事柄について、非常にゆっくり・明瞭・直接的・非慣用的に尋ねられれば、面接で簡単で直接的な質問に答える。",
 "受信配慮条件下での応答定型。",
 "名前は言うだけでは伝わらない ── 綴りの提示（→明確化746）まで一続きの動作にする。",
 "口頭の起点 ── 面接という場で、強い受信配慮の支えつき。面接シート597の前段。"),
(571, '口頭', ["Where are you from? — I'm from Osaka. And you?", "What do you do? — I work in a bookshop."],
 "個人情報を尋ね、提供する。",
 "尋ね・答え・返す（And you?）の往復。",
 "訊かれたら返す（And you?）まで一手 ── 一方通行の応答の連続は尋問の空気を作る。",
 "支え条件がすべて外れ、双方向になる ── 授受の質問応答相（574/575）と地続き（→授受シート相互参照）。"),
(643, '書面', ["Hello, my name is Ken Sato. I am 30 and I work at a small company in Tokyo.", "I like cooking and tennis. Nice to meet you!"],
 "自己紹介する短いメール・手紙などで、日常的な性質の個人情報を伝える。",
 "自己紹介メールの定型構成（名乗り→属性→趣味→結び）。",
 "日本語の自己紹介の謙遜定型（「つまらない者ですが」）は直訳しない ── 事実の明るい列挙が英語の礼儀。",
 "粒（650）が型（自己紹介文）にまとまる書面の到達点。かつて事実質問応答範型に借用されていた行（判断(k)付随で本行為へ、相互参照済み）。"),
]

ORDER = [650, 687, 599, 571, 643]

DISCUSSION = [
"【消失点A2 ── 起点行為の外部化】 全5件がPre-A1〜A2に収まり、A2で梯子が閉じる外部化型。B1以上の「自己を語る」は、事実情報の授受・情報管理相（背景説明・詳細度の調整）、面接（595以降の自己呈示）、経験・出来事の叙述（第2柱）へ外部化される ── 自己情報は英語学習の入口で型として完成し、以後は各行為の素材になる。",
"【場面 ── 書面はプロフィール、口頭は面接と社交】 書面（650/687/643）は自己紹介文・プロフィール欄という「書式」の系列、口頭（599/571）は面接と社交の応答。Pre-A1の二件がともに道具の支え（辞書・メニュー・翻訳ツール）を明記する点は、CEFR2020が補助ツールを正規の足場として認める設計の最初の現れ。",
"【往復・応答の点検 ── And you? が対称往復の最小形】 571が尋ね・提供の両側を一つの記述文に持ち、返しの一言（And you?）が往復を閉じる ── 授受シートの質問応答相の自己情報版。599は受ける側のみで、面接シート597へ続く前段。",
"【口頭2・書面3 ── (o)判定＝非成立（B2未達型）】 Correspondence系列は650（Pre-A1）・643（A2）でB2帯に届かず、判定＝非成立（B2未達型）。書面上端643の「型への到達」が本行為の完成形で、以後の書面自己呈示は応募・出願（641）と業務書簡（授受640）の領分。",
"【点検総括・語彙裁定】 外部化型で確定（仮判定どおり）。横串は方略（道具の使用＝650/687）と社会言語（自己紹介の文化差＝643）。語彙裁定（判断(s)）：single（687・Pre-A1行）＝記述文由来（relationship status のメニュー選択肢）、固有名詞（Japan・K-E-N ほか）＝allowlist裁定。engineer は収録内で通過。",
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
    json.dump(data, open(os.path.join(here, 'catalog_selfinfo.json'), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 5 and len(DISCUSSION) == 5
    print(f"catalog_selfinfo.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}＋書面{sum(1 for r in rows if r['mode']=='書面')}）")
