"""新スレッドでの復元ヘルパー。ローカルのdata/ から、または raw URL から主要データを読む。
使い方: from restore import load_all; D = load_all()  （ローカル実行）
raw URL版が要るときは BASE を使って個別に web_fetch する。"""
import json, os
BASE = "https://raw.githubusercontent.com/takahashihideki-git/CEFRCatalog/main"
def load_all(root="."):
    d = os.path.join(root, "data")
    def L(f): return json.load(open(os.path.join(d, f), encoding="utf-8"))
    return {
        "descriptors": L("descriptors_en_1224.json"),      # No(str)->{scheme,mode,activity,scale,level,en}
        "translations": L("working_translations_1224.json"),# No(str)->和訳
        "inventory":  L("inventory_183to22.json"),          # No(str)->行為名
        "phases":     L("act_phases.json"),                 # 一行為二相の正準記録（第2周-1）
        "cross_axes": L("cross_axes.json"),                 # 横断軸＋行為分類（下位系・梯子型、第2周-4）
        "templates":  L("ladder_templates.json"),           # 梯子型別テンプレート（様式総括、第3周-4・判断(u)）
        "act_type":   L("act_to_satype.json"),              # 行為名->4類型
        "verdicts":   L("sieve_verdicts_266.json"),         # No(str)->{verdict,reason,note}
        "partition":  L("block_partition_1224.json"),        # No(str)->{block, sub?} 四本柱＋横串の区分
        "prototypes": json.load(open(os.path.join(root,"prototypes","prototypes_4types.json"),encoding="utf-8")),
        "verifications": {f: json.load(open(os.path.join(root,"prototypes",f),encoding="utf-8"))
                          for f in ("verification_expressive.json","verification_assertive.json",
                                    "verification_directive.json","verification_phatic.json")},
    }
if __name__ == "__main__":
    D = load_all()
    assert len(D["descriptors"])==1224
    assert len(D["translations"])==1224
    assert set(D["descriptors"])==set(D["translations"]), "No不一致"
    assert sum(1 for v in D["verdicts"].values() if v["verdict"]=="ADOPT")==183
    assert len(D["verdicts"])==266
    assert len(set(D["inventory"].values()))==22
    assert len(D["prototypes"])==4
    from collections import Counter
    assert dict(Counter(p["block"] for p in D["partition"].values())) == {
        "やり取り":306,"仲介":251,"受容":197,"how well":182,"産出・談話構築":132,"方略":104,"複言語":52}, "区分分割の不一致"
    # 全範型照合（引き継ぎ書§7・範型検証パッチ）
    KNOWN_ISSUES = set()        # §7(b)は第2周-1（授受↔Q&A統合）で解決済み。新規の借用が出たらここへ
    PROTO_ACT = {"苦情クレーム":"苦情・クレーム","挨拶別れ安否":"挨拶・別れ・安否",
                 "事実質問応答":"事実情報の授受","意見表明":"意見・見解の表明"}
    VERIF_ACT = {"感謝詫び祝意":"感謝・詫び・祝意","感情の表出":"感情の表出",
                 "事実情報の授受":"事実情報の授受","依頼・要求":"依頼・要求","会話の開始・維持":"会話の開始・維持"}
    def check_rows(rows, act, jp_is_tr, exempt=False):
        for r in rows:
            no = str(r["no"])
            if exempt and r["no"] in KNOWN_ISSUES:
                print(f"  警告: No.{no} は既知の借用問題（§7(b)・第2周で解決予定）── 照合を免除")
                continue
            assert r["en"] == D["descriptors"][no]["en"], f"原文不一致 No.{no}"
            assert r["level"] == D["descriptors"][no]["level"], f"レベル不一致 No.{no}"
            assert D["inventory"].get(no) == act, f"行為所属不一致 No.{no}"
            if jp_is_tr:
                assert r["jp"] == D["translations"][no], f"訳不一致 No.{no}"
    for name, proto in D["prototypes"].items():
        check_rows(proto["rows"], PROTO_ACT[name], jp_is_tr=False, exempt=True)   # 4範型のjpは手書きグロス（訳と別物）。642/643の借用免除は4範型内に限る（検証範型の642は授受の正当な行）
    n_verif_acts = 0
    for vf, V in D["verifications"].items():
        for name, proto in V.items():
            check_rows(proto["rows"], VERIF_ACT[name], jp_is_tr=True)  # 検証範型①〜⑤は作成時にjp==訳をassert済み
            n_verif_acts += 1
    assert n_verif_acts == 5, "検証範型の行為数不一致"
    # 第3周の全数シート（catalog_*.json）── 登録表で照合（第3周-1: 意見／第3周-2: 苦情）
    CATALOGS = {
        "catalog_opinion.json":       ("意見・見解の表明", 31, "意見31"),
        "catalog_complaint.json":     ("苦情・クレーム",    9, "苦情9"),
        "catalog_greeting.json":      ("挨拶・別れ・安否",  9, "挨拶9"),
        "catalog_thanksapology.json": ("感謝・詫び・祝意",  6, "感謝詫び6"),
        "catalog_request.json":       ("依頼・要求",        6, "依頼6"),
        "catalog_infoexchange.json":  ("事実情報の授受",   31, "授受31"),
        "catalog_conversation.json":  ("会話の開始・維持",  5, "会話維持5"),
        "catalog_emotion.json":       ("感情の表出",        8, "感情8"),
        "catalog_clarification.json": ("明確化・繰り返しの要求", 17, "明確化17"),
        "catalog_transaction.json":   ("取引（購入・注文）", 12, "取引12"),
        "catalog_problemexplain.json":("問題・事情の説明",    8, "問題説明8"),
        "catalog_proposal.json":      ("提案・誘い・計画の相談", 8, "提案8"),
        "catalog_interview.json":     ("面接での質問と応答",  6, "面接6"),
        "catalog_message.json":       ("伝言の授受",          7, "伝言7"),
        "catalog_selfinfo.json":      ("自己に関する情報提供", 5, "自己情報5"),
        "catalog_enquiry.json":       ("問い合わせ",          3, "問い合わせ3"),
        "catalog_directions.json":    ("道案内の依頼と提供",  3, "道案内3"),
        "catalog_advice.json":        ("助言",                3, "助言3"),
        "catalog_agreement.json":     ("同意・不同意",        3, "同意不同意3"),
        "catalog_experience.json":    ("経験・出来事の叙述",  1, "経験叙述1"),
        "catalog_application.json":   ("応募・出願",          1, "応募1"),
        "catalog_instructionresponse.json": ("指示への応答",  1, "指示応答1"),
    }
    cat_done = []
    for fn, (act, n_rows, tag) in CATALOGS.items():
        cat_path = os.path.join("prototypes", fn)
        if not os.path.exists(cat_path):
            continue
        C = json.load(open(cat_path, encoding="utf-8"))[act]
        seen = set()
        for r in C["rows"]:
            no = str(r["no"])
            assert r["en"] == D["descriptors"][no]["en"], f"catalog原文不一致 No.{no}"
            assert r["level"] == D["descriptors"][no]["level"], f"catalogレベル不一致 No.{no}"
            assert r["jp"] == D["translations"][no], f"catalog訳不一致 No.{no}"
            assert D["inventory"].get(no) == act, f"catalog行為所属不一致 No.{no}"
            seen.add(no)
        assert len(C["rows"]) == n_rows and len(seen) == n_rows, f"catalog件数不一致 {fn}"
        assert seen == {n for n, a in D["inventory"].items() if a == act}, f"catalog全数性不一致 {fn}"
        assert len(C["discussion"]) == 5, f"catalog DISCUSSION段落数不一致 {fn}"
        cat_done.append(tag)
    cat_msg = (" / 全数シート" + "・".join(cat_done) + "照合") if cat_done else ""
    PHASE_SIZES = {"事実情報の授受": 31, "明確化・繰り返しの要求": 17, "意見・見解の表明": 31}
    for act, expected in PHASE_SIZES.items():
        parts = [set(v) for v in D["phases"][act].values() if isinstance(v, list)]
        union = set().union(*parts)
        members = {int(n) for n, a in D["inventory"].items() if a == act}
        assert sum(len(p) for p in parts) == len(union) == expected and union == members, f"二相分割の不一致 {act}"
    cx = D["cross_axes"]["行為分類"]
    assert set(cx.keys()) == set(D["inventory"].values()), "行為分類とインベントリの不一致"
    for act, c in cx.items():
        assert c["出自類型"] == D["act_type"][act], f"出自類型の不一致 {act}"
        assert c["梯子型"] in {"管理梯子型","定型履行型","外部化型","二相接続型"}, f"梯子型の不正値 {act}"
    assert sum(1 for c in cx.values() if c["判定状態"]=="検証済") == 22, "検証済件数の不一致"
    assert {a for a,c in cx.items() if c["梯子型"]=="二相接続型"} == set(D["phases"].keys()), "二相接続型とact_phasesの不一致"
    assert len({c["下位系"] for c in cx.values()}) == 12, "下位系数の不一致"
    # 梯子型別テンプレート（第3周-4・判断(u)）── cross_axes・帳簿との整合
    lt = D["templates"]
    assert set(lt["梯子型"].keys()) == set(D["cross_axes"]["横断軸"]["縦横分業"]["梯子型の値"]), "テンプレートと梯子型の値の不一致"
    for t, body in lt["梯子型"].items():
        expected_acts = {a for a, c in cx.items() if c["梯子型"] == t}
        assert set(body["適用行為"]) == expected_acts, f"テンプレート適用行為の不一致 {t}"
    for axis in lt["運用注記"]["横断軸参照"]:
        assert axis in D["cross_axes"]["横断軸"], f"テンプレートが参照する横断軸が不在 {axis}"
    ext_acts = set(lt["梯子型"]["外部化型"]["適用行為"])
    assert all(cx[a].get("外部化先") for a in ext_acts), "外部化型行為に外部化先の欠落"
    assert set(D["cross_axes"]["横断軸"]["書面フォーマル一段"]["再現"].keys()) == {"632", "633", "628"}, "書面フォーマル一段の再現記録の不一致"
    # 第2柱第一号シート（CEFRカタログ7）── 全数性はスケール所属で照合（第2柱インベントリ整備までの代替）
    P2_SCALE = "Sustained monologue: describing experience"
    p2_path = os.path.join("prototypes", "catalog_p2_describing_experience.json")
    P2 = list(json.load(open(p2_path, encoding="utf-8")).values())[0]
    p2_seen = set()
    for r in P2["rows"]:
        no = str(r["no"])
        assert r["en"] == D["descriptors"][no]["en"], f"p2原文不一致 No.{no}"
        assert r["level"] == D["descriptors"][no]["level"], f"p2レベル不一致 No.{no}"
        assert r["jp"] == D["translations"][no], f"p2訳不一致 No.{no}"
        assert r["mode"] == "口頭", f"p2 modeが口頭でない No.{no}"
        assert D["descriptors"][no]["scale"] == P2_SCALE, f"p2スケール所属不一致 No.{no}"
        p2_seen.add(no)
    p2_members = {n for n, d in D["descriptors"].items() if d.get("scale") == P2_SCALE}
    assert p2_seen == p2_members and len(P2["rows"]) == 28, "p2全数性不一致"
    assert len(P2["discussion"]) == 5, "p2 DISCUSSION段落数不一致"
    # モード間並行対（判断(y)裁定d-2）── 両No実在・レベル一致・スケール正・完全同文はen一致・型式標本247/338
    MP = json.load(open(os.path.join("data", "mode_pairs.json"), encoding="utf-8"))
    assert len(MP["pairs"]) == 7, "並行対件数不一致"
    for p in MP["pairs"]:
        o, w = str(p["oral"]), str(p["written"])
        do, dw = D["descriptors"][o], D["descriptors"][w]
        assert do["level"] == dw["level"] == p["level"], f"並行対レベル不一致 {o}/{w}"
        assert do["scale"] == MP["scales"]["oral"] and dw["scale"] == MP["scales"]["written"], f"並行対スケール不一致 {o}/{w}"
        if p["relation"] == "完全同文":
            assert do["en"] == dw["en"], f"完全同文が同文でない {o}/{w}"
    assert any(p["oral"] == 247 and p["written"] == 338 and p["relation"] == "完全同文" for p in MP["pairs"]), "型式標本247/338の欠落"
    print("復元検証OK: descriptors1224 / translations1224 / 篩266・ADOPT183 / 行為22 / 二相31+17+31 / 分類22・下位系12 / テンプレート4型整合 / 範型4照合 / 検証範型5照合 / 区分分割7" + cat_msg + " / 第2柱第一号28（スケール全数・口頭一様）/ 並行対7（型式標本247-338）")
