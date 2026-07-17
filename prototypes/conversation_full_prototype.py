# -*- coding: utf-8 -*-
"""第3周-5：会話の開始・維持（5件）の全数シート ── 管理梯子型テンプレートの適用（様式昇格）。

検証範型⑤（verification_phatic.json）の5行をそのまま継承（全数＝検証範型）。
DISCUSSION は ladder_templates.json 管理梯子型配分（①管理課題の通し読み ②L1難所
③隣接分業 ④口頭書面＋(o) ⑤点検総括）で再構成。旧検証範型は歴史的サンプルとして凍結。

単一情報源の設計：en / jp は data から構築時取得。継承フィールドは verification_phatic.json から読取。
実行すると prototypes/catalog_conversation.json を生成する。
"""
import json, os

ACT = '会話の開始・維持'
TITLE = '会話の開始・維持（Starting, maintaining & building conversation）── 全数シート'
SCOPE = '全数（5件。口頭5・書面0＝書面系列なし）'
TYPE_ = '交話的（phatic）── 下位系＝関係運営系、梯子型＝管理梯子型（管理課題＝談話運営：参加→運営→関係構築）。型の履行では済まない即興と運営の技能として深まる'
ESSENCE = '会話に加わり、始め、続くように支え、会話を通じて相手との関係を築く。レベルが上がるとは、会話への関与の主体性が上がることである ── 参加者から、運営者へ、関係の構築者へ。'

ORDER = [450, 445, 434, 432, 427]

DISCUSSION = [
"【管理梯子の背骨 ── 参加から運営へ、運営から関係構築へ】 管理課題＝談話運営。挨拶と同じ交話的行為でありながら、この行為には A1→B2+ の本物の梯子がある ── ただし梯子を上るのは定型の高度化ではなく、会話への関与の主体性である。A1（450）：予測可能な話題という補助輪つきで、支えられながら参加する。A2（445）：定番質問の在庫で、自分から会話を回す。B1（434）：unprepared ── 補助輪が外れ、準備なしで進行中の会話に入る。B1+（432）：自発的な質問・反応・意見表明で会話を途切れさせない運営者になる。B2+（427）：好意的質問・同意・共有状況への言及で、会話を通じて関係そのものを築く。参加者→運営者→関係構築者という管理課題の精緻化が delta の一本線であり、「phatic だから梯子が無い」は挨拶という行為の性質であって phatic 一般の性質ではない ── 挨拶は型の履行で完結するから梯子が消え、会話の維持には型では済まない即興と運営があるから梯子が立つ。",
"【L1難所 ── 相槌体系の写し替えと沈黙の非対称】 この行為の難所は、文法・語彙の外にある会話行動の較差に集中する。(a) 相槌問題：日本語の高頻度相槌の直移入は英語では遮りに、反応標識（Oh really? / That sounds ...）の欠落は不関心に化ける ── 双方向に事故る唯一の難所。(b) 沈黙の非対称：考える間としての沈黙が、英語の雑談では関係の失速として処理される。(c) 招かれ待ちの参入習慣：進行中の会話に自分から接続する定型（B1・434 が要求するもの）の不在。(d) 質問で会話を運営する習慣の薄さ：質問＝詮索・失礼という懸念が、関心の表明としての質問（B1+・432、B2+・427 の中核道具）の運用を妨げる。(e) safe topics と私事度の線引きの文化差。これらは感情表出で見た開示量の較差と同系の、行動様式レベルの転移であり、実例だけでは教えられず、機能の明示的説明を要する。",
"【隣接行為との境界 ── 型の分業と、部品を運用するメタ行為】 第一の境界は挨拶・別れ・安否との分業：同じ交話的行為でも、挨拶＝定型履行系（型の履行で完結、梯子なし）／本行為＝関係運営系（技能として深まる、梯子あり）と、下位系の水準で分かれる（第2周-4）。接触の開閉は挨拶が、開いたあとの本体は本行為が受け持ち、挨拶の「閉じる定型」（It was nice talking to you）は本行為の終了局面と連続する。第二の境界は運営の部品をめぐる他行為との関係：B1+（432）の自発的質問は事実情報の授受と、意見の表明は意見・見解の表明と、B2+（427）の同意の表明は意見表明の同意側と、それぞれ道具を共有する。談話運営とは他行為を部品として会話に組み込む技能であり、この行為は個々の部品でなく組み込みの運用そのものを対象とする ── 隣接行為と重なって見えるのは分類の失敗ではなく、この行為がメタ的な管理課題を持つことの帰結である。",
"【口頭書面 ── 書面系列なし、オンライン運営は他行為の帳簿へ】 書面の記述文はゼロであり、書面フォーマル一段（判断(o)）は判定対象外（3値のうち「書面系列なし」）。これは欠落ではなく帳簿の構造で、オンライン会話の運営（チャットの開始・維持）は No.679（事実情報の授受）等、話題側の行為の帳簿に吸収されている ── 依頼で見た帳簿間の吸収がここでも作動している。会話の維持そのものは CEFR にとって口頭の対面技能であり、書面性はつねに「何をやり取りするか」の側に記帳される。",
"【点検総括と語彙裁定】 往復・応答（判断(n)）の点検：この行為は往復の運営そのものが対象であり、する側＝開始・質問・話題提供、受ける側＝反応標識・相槌・経験の接ぎ木（432 の expressing reactions が受け在庫の明文化）、断る・返す型＝会話からの退出定型で、退出は挨拶の閉じる定型との分業になる。往復軸の病理（受け在庫の欠落が不関心・冷淡に化ける）は L1 難所 (a) とそのまま重なり、この行為では往復点検と L1 点検が一体化する。書面フォーマル一段：判定対象外（第4段落）。語彙裁定（判断(s)）：keynote（427・B2+ 行）は CEFR-J 未収録の会議場面名詞 ── B2+ 行の実例の場面語として保持を裁定（allowlist 記載）。他の実例は検証範型⑤から変更なし。",
]

def build(root="."):
    desc = json.load(open(os.path.join(root, "data/descriptors_en_1224.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(root, "data/working_translations_1224.json"), encoding="utf-8"))
    inherited = json.load(open(os.path.join(root, "prototypes/verification_phatic.json"), encoding="utf-8"))[ACT]["rows"]
    by_no = {r["no"]: dict(r) for r in inherited}
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
    out = os.path.join(here, 'catalog_conversation.json')
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    rows = data[ACT]["rows"]
    assert len(rows) == 5, f"行数不一致: {len(rows)}"
    assert len(DISCUSSION) == 5, "DISCUSSION段落数不一致"
    print(f"catalog_conversation.json 生成OK: {len(rows)}行（口頭{sum(1 for r in rows if r['mode']=='口頭')}）")
