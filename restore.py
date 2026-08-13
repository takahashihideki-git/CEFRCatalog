"""新スレッドでの復元ヘルパー。ローカルのdata/ から、または raw URL から主要データを読む。
使い方: from restore import load_all; D = load_all()  （ローカル実行）
raw URL版が要るときは BASE を使って個別に web_fetch する。"""
import json, os, re
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
    lt_p1 = lt["第三層（型別差分）"]["第1柱（発語内行為）"]
    assert set(lt_p1.keys()) == set(D["cross_axes"]["横断軸"]["縦横分業"]["梯子型の値"]), "テンプレートと梯子型の値の不一致"
    for t, body in lt_p1.items():
        expected_acts = {a for a, c in cx.items() if c["梯子型"] == t}
        assert set(body["適用行為"]) == expected_acts, f"テンプレート適用行為の不一致 {t}"
    for axis in lt["運用注記"]["横断軸参照"]:
        assert axis in D["cross_axes"]["横断軸"], f"テンプレートが参照する横断軸が不在 {axis}"
    ext_acts = set(lt_p1["外部化型"]["適用行為"])
    assert all(cx[a].get("外部化先") for a in ext_acts), "外部化型行為に外部化先の欠落"
    assert set(D["cross_axes"]["横断軸"]["書面フォーマル一段"]["再現"].keys()) == {"632", "633", "628"}, "書面フォーマル一段の再現記録の不一致"
    # 第2柱インベントリ（判断(ah)、CEFRカタログ12）── 132件の完全分割（範型115＋留置17）を正とする
    P2INV = json.load(open(os.path.join("data", "p2_inventory_132to7.json"), encoding="utf-8"))
    p2_block = {n for n, v in D["partition"].items() if v["block"] == "産出・談話構築"}
    inv_h, inv_r = P2INV["範型"], P2INV["留置"]
    assert len(inv_h) == 115 and len(inv_r) == 17, "p2インベントリ件数不一致"
    assert set(inv_h.keys()) | set(inv_r.keys()) == p2_block and not set(inv_h) & set(inv_r), "p2インベントリが区分分割132件の完全分割でない"
    for n, sc in inv_h.items():
        assert D["descriptors"][n]["scale"] == sc, f"p2インベントリ範型のスケール不整合 No.{n}"
    ov_counts = {}
    for n, row in inv_r.items():
        assert D["descriptors"][n]["scale"] == row["scale"], f"p2インベントリ留置のスケール不整合 No.{n}"
        assert D["descriptors"][n]["level"] == row["level"], f"p2インベントリ留置のレベル不整合 No.{n}"
        assert row["note"], f"p2インベントリ留置に行別noteの欠落 No.{n}"
        ov_counts[row["scale"]] = ov_counts.get(row["scale"], 0) + 1
    assert ov_counts == {"Overall oral production": 8, "Overall written production": 9}, "p2留置のスケール構成不一致"
    # 第2柱シート（一号=CEFRカタログ7、二号=CEFRカタログ8、三号四号=CEFRカタログ9・論証族、五号=CEFRカタログ10・教示族）── 全数性は帳簿（p2_inventory）で照合
    P2_SHEETS = [
        ("Sustained monologue: describing experience", "catalog_p2_describing_experience.json", "口頭", 28),
        ("Creative writing", "catalog_p2_creative_writing.json", "書面", 24),
        ("Sustained monologue: putting a case (e.g. in a debate)", "catalog_p2_putting_a_case.json", "口頭", 13),
        ("Reports and essays", "catalog_p2_reports_essays.json", "書面", 18),
        ("Sustained monologue: giving information", "catalog_p2_giving_information.json", "口頭", 10),
        ("Addressing audiences", "catalog_p2_addressing_audiences.json", "口頭", 18),
        ("Public announcements", "catalog_p2_public_announcements.json", "口頭", 4),
    ]
    p2_rows_by_scale = {}
    for p2_scale, p2_fn, p2_mode, p2_n in P2_SHEETS:
        P2 = list(json.load(open(os.path.join("prototypes", p2_fn), encoding="utf-8")).values())[0]
        p2_seen = set()
        for r in P2["rows"]:
            no = str(r["no"])
            assert r["en"] == D["descriptors"][no]["en"], f"p2原文不一致 No.{no}"
            assert r["level"] == D["descriptors"][no]["level"], f"p2レベル不一致 No.{no}"
            assert r["jp"] == D["translations"][no], f"p2訳不一致 No.{no}"
            assert r["mode"] == p2_mode, f"p2 modeが{p2_mode}でない No.{no}"
            assert D["descriptors"][no]["scale"] == p2_scale, f"p2スケール所属不一致 No.{no}"
            p2_seen.add(no)
        p2_members = {n for n, sc in inv_h.items() if sc == p2_scale}
        assert p2_seen == p2_members and len(P2["rows"]) == p2_n, f"p2全数性不一致（帳簿照合） {p2_scale}"
        assert len(P2["discussion"]) == 5, f"p2 DISCUSSION段落数不一致 {p2_scale}"
        p2_rows_by_scale[p2_scale] = p2_seen
    p2_mode_by_scale = {sc: md for sc, _fn, md, _n in P2_SHEETS}
    # 糸の正準記録（判断(aa)、CEFRカタログ8。判断(ad)で語彙二層を族糸へ再編）を先に読む
    TH = json.load(open(os.path.join("data", "p2_threads.json"), encoding="utf-8"))
    # モード間並行対（判断(y)裁定d-2。判断(ac)で系構造化、判断(ad)で系＝族へ）
    #   ── 族ごとに両No実在・レベル一致・完全同文はen一致。スケールは所属から導出し、族宣言と口頭／書面の別を照合
    MP = json.load(open(os.path.join("data", "mode_pairs.json"), encoding="utf-8"))
    assert [s["族"] for s in MP["systems"]] == ["叙述族", "論証族", "教示族"], "並行対の族構成不一致"
    assert [len(s["pairs"]) for s in MP["systems"]] == [7, 4, 1], "並行対件数不一致"
    assert all(s["族"] in TH["族糸"] for s in MP["systems"]), "mode_pairsの族がp2_threadsの族糸に未登録"
    mp_all_pairs = []
    for s in MP["systems"]:
        fam = s["族"]
        for p in s["pairs"]:
            o, w = str(p["oral"]), str(p["written"])
            do, dw = D["descriptors"][o], D["descriptors"][w]
            assert do["level"] == dw["level"] == p["level"], f"並行対レベル不一致 {o}/{w}"
            if p["relation"] == "完全同文":
                assert do["en"] == dw["en"], f"完全同文が同文でない {o}/{w}"
            # 両側が第2柱シートの行として実在し、口頭側は口頭シート・書面側は書面シートに属する（判断(aa)の不変条件を族横断で維持）
            so, sw = do["scale"], dw["scale"]
            assert o in p2_rows_by_scale.get(so, set()), f"並行対の口頭側がシートに不在 {o}"
            assert w in p2_rows_by_scale.get(sw, set()), f"並行対の書面側がシートに不在 {w}"
            assert p2_mode_by_scale[so] == "口頭" and p2_mode_by_scale[sw] == "書面", f"並行対のモード配置不正 {o}/{w}"
            # 両側のスケールが当該族を宣言していること（束スケールが複数族に属することを許す ── 判断(ad)）
            assert fam in TH["scales"][so]["族"] and fam in TH["scales"][sw]["族"], f"並行対の族宣言不一致 {o}/{w}（{fam}）"
            mp_all_pairs.append((fam, so, sw, p))
    sys_narr = next(s for s in MP["systems"] if s["族"] == "叙述族")
    assert any(p["oral"] == 247 and p["written"] == 338 and p["relation"] == "完全同文" for p in sys_narr["pairs"]), "型式標本247/338の欠落"
    sys_arg = next(s for s in MP["systems"] if s["族"] == "論証族")
    assert any(p["oral"] == 277 and p["written"] == 356 for p in sys_arg["pairs"]), "論証族型式標本277/356の欠落"
    assert {(p["oral"], p["written"]) for p in sys_arg["pairs"]} == {(277, 356), (305, 359), (303, 356), (299, 354)}, "論証族の並行対帳簿不一致（判断(af)）"
    # 段差（並行対でない同文級・同課題のレベル非対称、判断(ac)）── 両No実在・レベル記載一致・非同レベル
    for g in sys_arg.get("段差", []):
        o, w = str(g["oral"]), str(g["written"])
        assert D["descriptors"][o]["level"] == g["oral_level"] and D["descriptors"][w]["level"] == g["written_level"], f"段差レベル記載不一致 {o}/{w}"
        assert g["oral_level"] != g["written_level"], f"段差が同レベル（並行対とすべき） {o}/{w}"
    assert {(g["oral"], g["written"]) for g in sys_arg["段差"]} == {(278, 354), (280, 358)}, "論証族の段差帳簿不一致"
    sys_ins = next(s for s in MP["systems"] if s["族"] == "教示族")
    for g in sys_ins.get("段差", []):
        o, w = str(g["oral"]), str(g["written"])
        assert D["descriptors"][o]["level"] == g["oral_level"] and D["descriptors"][w]["level"] == g["written_level"], f"段差レベル記載不一致 {o}/{w}"
        assert g["oral_level"] != g["written_level"], f"段差が同レベル（並行対とすべき） {o}/{w}"
    assert {(g["oral"], g["written"]) for g in sys_ins["段差"]} == {(267, 357)}, "教示族の段差帳簿不一致"
    # 固有糸の規則（meta「固有糸の規則」の機械化、判断(ad)(ag)）──
    #   ①固有糸名は全スケールで一意（同名の糸が二スケールに現れるなら族糸でなければならない）
    #   ②固有糸名は族糸名と衝突しない ③族宣言が空のスケールは並行対を持たない
    _own_names = [t for ts in TH["固有糸"].values() for t in ts]
    assert len(_own_names) == len(set(_own_names)), "固有糸名がスケール間で重複（族糸化が必要）"
    _fam_names = {t for ts in TH["族糸"].values() for t in ts}
    assert not (set(_own_names) & _fam_names), "固有糸名が族糸名と衝突"
    _paired_scales = {D["descriptors"][str(p["oral"])]["scale"] for _f, _so, _sw, p in mp_all_pairs} | {D["descriptors"][str(p["written"])]["scale"] for _f, _so, _sw, p in mp_all_pairs}
    for sc, rec in TH["scales"].items():
        if not rec["族"]:
            assert sc not in _paired_scales, f"族宣言が空なのに並行対を持つ {sc}"
    # 糸の正準記録 ── 主タグ完全分割／語彙正準（宣言した族の族糸∪固有糸）／副タグ実在／並行対の糸保存
    for sc, rec in TH["scales"].items():
        assert all(f in TH["族糸"] for f in rec["族"]), f"未登録の族を宣言 {sc}"
        allowed = set(TH["固有糸"].get(sc, []))
        for f in rec["族"]:
            allowed |= set(TH["族糸"][f])
        assert set(rec["主タグ"].keys()) <= allowed, f"糸語彙が正準（宣言族の族糸∪固有糸）を逸脱 {sc}"
        tagged = [str(n) for v in rec["主タグ"].values() for n in v]
        assert sorted(tagged) == sorted(p2_rows_by_scale[sc]), f"主タグが完全分割でない {sc}"
        for vs in rec["副タグ"].values():
            assert all(str(n) in p2_rows_by_scale[sc] for n in vs), f"副タグに帳簿外No {sc}"
    # 構築梯子型（第三層・第2柱、判断(ab)）── 適用スケール＝p2_threadsの登録スケール
    KO = lt["第三層（型別差分）"]["第2柱（産出・談話構築）"]["構築梯子型"]
    assert set(KO["適用スケール"]) == set(TH["scales"].keys()), "構築梯子型の適用スケールとp2_threadsの不一致"
    def _main_tag(sc, no):
        for t, ns in TH["scales"][sc]["主タグ"].items():
            if no in ns:
                return t
    for fam, so, sw, p in mp_all_pairs:
        to = _main_tag(so, p["oral"])
        tw = _main_tag(sw, p["written"])
        assert to is not None and to == tw, f"並行対の糸不一致 {p['oral']}/{p['written']}: {to}/{tw}"
        # 保存された糸は当該族の族糸であること（判断(ad)：糸保存＝族の内部で成り立つ写像）
        assert to in TH["族糸"][fam], f"並行対の糸が族外 {p['oral']}/{p['written']}: {to} ∉ {fam}"
    # 参照台帳（判断(ai)、CEFRカタログ12）── 設計条件①所有排他・②正準向き・③散文同期を機械検証
    CRF = json.load(open(os.path.join("data", "crossrefs.json"), encoding="utf-8"))
    assert set(CRF["edges"].keys()) == set(CRF["meta"]["kind定義"].keys()), "crossrefs: kind語彙がmeta定義と不一致"
    _cited = lambda no, text: re.search(r"(?<!\d)" + re.escape(no) + r"(?!\d)", text) is not None  # 桁境界つき（4桁Noの部分文字列誤ヒット防止）
    # 全数シートの行散文・DISCUSSION索引（本ブロック内で自己完結に再読）
    import glob as _glob
    _prose, _disc, _sheet_of, _act_keys = {}, {}, {}, set()
    for _fn in _glob.glob(os.path.join("prototypes", "catalog_*.json")):
        _J = json.load(open(_fn, encoding="utf-8"))
        _act, _body = next(iter(_J.items()))
        _act_keys.add(_act)
        _disc[_act] = " ".join(_body.get("discussion", []))
        for _r in _body["rows"]:
            _no = str(_r["no"])
            _sheet_of[_no] = _act
            _prose[_no] = " ".join(str(_r.get(_k, "") or "") for _k in ("delta", "l1", "scene", "howwell"))
    # ①所有排他：既存帳簿の所有エッジ（並行対・段差・書面フォーマル一段）と無向集合で非交差
    _owned = {frozenset((str(p["oral"]), str(p["written"]))) for _f, _so, _sw, p in mp_all_pairs}
    for _sys in MP["systems"]:
        for _g in _sys.get("段差", []):
            _owned.add(frozenset((str(_g["oral"]), str(_g["written"]))))
    for _x in ("632", "633"):
        for _y in ("633", "628"):
            if _x != _y:
                _owned.add(frozenset((_x, _y)))
    _owned.add(frozenset(("632", "628")))
    _sym_kinds = ("スケール再掲重複対", "口頭スケール再掲対", "柱間対", "族間対", "行為内対", "留置対")
    _seen_edges = set()
    for _kind in _sym_kinds:
        for _e in CRF["edges"][_kind]:
            _a, _b = str(_e["a"]), str(_e["b"])
            assert int(_a) < int(_b), f"crossrefs: 正準向き違反（a<bでない） {_kind} {_a}/{_b}"
            _fs = frozenset((_a, _b))
            assert _fs not in _owned, f"crossrefs: 既存帳簿所有エッジの重複登載 {_kind} {_a}/{_b}"
            assert _fs not in _seen_edges, f"crossrefs: 台帳内のエッジ重複 {_a}/{_b}"
            _seen_edges.add(_fs)
            if _kind == "留置対":
                assert _a in inv_r and _b in inv_r, f"crossrefs: 留置対のNoが留置帳簿外 {_a}/{_b}"
                assert _cited(_b, inv_r[_a]["note"]) or _cited(_a, inv_r[_b]["note"]), f"crossrefs: 留置対の散文証拠なし {_a}/{_b}"
            else:
                assert _a in _prose and _b in _prose, f"crossrefs: エッジのNoがシート外 {_kind} {_a}/{_b}"
                _ev = _cited(_b, _prose[_a]) or _cited(_a, _prose[_b]) or (
                    _cited(_a, _disc[_sheet_of[_a]]) and _cited(_b, _disc[_sheet_of[_a]])) or (
                    _cited(_a, _disc[_sheet_of[_b]]) and _cited(_b, _disc[_sheet_of[_b]]))
                assert _ev, f"crossrefs: 散文証拠なし（設計条件③） {_kind} {_a}/{_b}"
            if _kind == "行為内対":
                assert _sheet_of[_a] == _sheet_of[_b], f"crossrefs: 行為内対が同一シートでない {_a}/{_b}"
                assert _e.get("axis") in ("口頭書面", "Informal-Formal"), f"crossrefs: 行為内対のaxis語彙外 {_a}/{_b}"
            elif _kind != "留置対":
                assert _sheet_of[_a] != _sheet_of[_b] or _kind == "スケール再掲重複対", f"crossrefs: {_kind}が同一シート内 {_a}/{_b}"
    # 有向kind：行為間参照 ── from実在・field語彙・to実在・③fromの当該散文に「相互参照」
    for _e in CRF["edges"]["行為間参照"]:
        _f = str(_e["from"])
        assert _f in _prose, f"crossrefs: 行為間参照のfromがシート外 {_f}"
        assert _e["field"] in ("delta", "l1"), f"crossrefs: 行為間参照のfield語彙外 {_f}"
        assert _e["to_acts"] or _e["to_nos"] or _e.get("to_pillar"), f"crossrefs: 行為間参照のto空 {_f}"
        for _ta in _e["to_acts"]:
            assert _ta in _act_keys, f"crossrefs: 行為間参照のto_actsが正準行為名でない {_f}→{_ta}"
        for _tn in _e["to_nos"]:
            assert str(_tn) in D["descriptors"], f"crossrefs: 行為間参照のto_nosが原典外 {_f}→{_tn}"
        assert _e.get("to_pillar") in (None, "仲介"), f"crossrefs: 行為間参照のto_pillar語彙外 {_f}"
        assert "相互参照" in _prose[_f], f"crossrefs: 行為間参照の散文証拠なし（設計条件③） {_f}"
    assert len(CRF["edges"]["行為間参照"]) == 28, "crossrefs: 行為間参照の件数不一致"
    # 検出裁定：ADOPTは対応エッジ実在・DROPはエッジ不在・語彙
    for _pk, _v in CRF["検出裁定"].items():
        _a, _b = _pk.split("-")
        assert _v["verdict"] in ("ADOPT", "DROP"), f"crossrefs: 裁定語彙外 {_pk}"
        if _v["verdict"] == "ADOPT":
            assert frozenset((_a, _b)) in _seen_edges, f"crossrefs: ADOPT裁定にエッジ不在 {_pk}"
        else:
            assert frozenset((_a, _b)) not in _seen_edges, f"crossrefs: DROP裁定なのにエッジ実在 {_pk}"
    # ladder_templates第二層のスケール再掲重複対 ── 正準はcrossrefs（判断(ai)追随）。標本の対は台帳エッジ⊆であること
    _dup_edges = {frozenset((str(_e["a"]), str(_e["b"]))) for _e in CRF["edges"]["スケール再掲重複対"]}
    _dup_sec = lt["第二層（柱別の必須点検）"]["第1柱（発語内行為）"]["スケール再掲重複対"]
    assert "crossrefs.json" in _dup_sec.get("正準", ""), "ladder_templates: 重複対の正準指し先がcrossrefsでない"
    for _sp in _dup_sec["型式標本"].values():
        _m = re.match(r"(\d{3})/(\d{3})", _sp)
        assert _m and frozenset(_m.groups()) in _dup_edges, f"ladder_templates: 型式標本が台帳外 {_sp}"
    # 軸台帳（判断(aj)、CEFRカタログ12）── 182件の13軸完全分割＋シート主軸（宣言は散文証拠つき）
    AX = json.load(open(os.path.join("data", "howwell_axes_182to13.json"), encoding="utf-8"))
    _hw_block = {n for n, v in D["partition"].items() if v["block"] == "how well"}
    _ax_nos, _sc_owner = set(), {}
    for _a, _rec in AX["軸"].items():
        for _n in _rec["nos"]:
            assert str(_n) not in _ax_nos, f"軸台帳: No重複 {_n}"
            _ax_nos.add(str(_n))
            assert D["descriptors"][str(_n)]["scale"] in _rec["scales"], f"軸台帳: スケール写像不整合 No.{_n}"
        for _sc in _rec["scales"]:
            assert _sc not in _sc_owner, f"軸台帳: スケールが二軸に所属 {_sc}"
            _sc_owner[_sc] = _a
    assert _ax_nos == _hw_block, "軸台帳: how well区分182件の完全分割でない"
    assert len(AX["軸"]) == 13 and len(_sc_owner) == 15, "軸台帳: 13軸15スケールの構成不一致"
    assert len(AX["軸"]["音韻"]["scales"]) == 3, "軸台帳: 音韻の3スケール束ね不一致"
    _decl, _undecl = AX["シート主軸"]["宣言"], AX["シート主軸"]["未宣言"]
    assert set(_decl.keys()) | set(_undecl) == _act_keys and not set(_decl.keys()) & set(_undecl), "軸台帳: シート主軸が29シートの完全分割でない"
    _sheet_blob = {}
    for _no, _p in _prose.items():
        _sheet_blob.setdefault(_sheet_of[_no], []).append(_p)
    for _act2 in _act_keys:
        _sheet_blob[_act2] = _disc.get(_act2, "") + " " + " ".join(_sheet_blob.get(_act2, []))
    for _act2, _rec in _decl.items():
        assert _rec["主軸"], f"軸台帳: 主軸が空 {_act2}"
        for _a in _rec["主軸"]:
            assert _a in AX["軸"], f"軸台帳: 主軸が13軸語彙外 {_act2}:{_a}"
            assert _a in _sheet_blob[_act2], f"軸台帳: 主軸の散文証拠なし {_act2}:{_a}"
    # 出自類型の表示訳（判断(ak)）── 写像のkey集合＝行為分類の出自類型語彙
    _disp = D["cross_axes"]["出自類型の表示訳"]["写像"]
    assert set(_disp.keys()) == {c["出自類型"] for c in D["cross_axes"]["行為分類"].values()}, "表示訳: 出自類型語彙と不一致"
    assert len(set(_disp.values())) == 4, "表示訳: 4門の重複"
    # レベル・ポートレート素材台帳（判断(al)）── 幕間6本×素材63件の完全分割＝導出集合と一致
    LP = json.load(open(os.path.join("data", "level_portraits.json"), encoding="utf-8"))
    _lp_src = {}
    for _n, _v in D["partition"].items():
        if _v["block"] == "やり取り" and _n not in D["verdicts"] and D["descriptors"][_n]["scale"].startswith("Overall"):
            _lp_src[_n] = "柱1総括"
    for _n in P2INV["留置"]:
        _lp_src[_n] = "柱2総括"
    for _n, _v in D["verdicts"].items():
        if _v["verdict"] == "DROP" and _v["reason"] == "R1":
            _lp_src[_n] = "R1質"
    assert len(_lp_src) == 63, f"幕間台帳: 導出素材が63件でない ({len(_lp_src)})"
    _fold = LP["meta"]["畳み込み規則"]["写像"]
    _lp_seen = {}
    for _ik, _rec in LP["幕間"].items():
        assert set(_rec["levels"]) == {_L for _L, _v in _fold.items() if _v == _ik}, f"幕間台帳: levels欄が畳み込み写像と不整合 {_ik}"
        for _cat, _nos in _rec["素材"].items():
            for _n in _nos:
                _n = str(_n)
                assert _n not in _lp_seen, f"幕間台帳: No重複割り付け {_n}"
                _lp_seen[_n] = (_ik, _cat)
                assert _lp_src.get(_n) == _cat, f"幕間台帳: 素材区分不整合 No.{_n} ({_cat}≠{_lp_src.get(_n)})"
                assert _fold[D["descriptors"][_n]["level"]] == _ik, f"幕間台帳: 級の畳み込み不整合 No.{_n}"
    assert set(_lp_seen) == set(_lp_src), "幕間台帳: 素材63件の完全分割でない"
    assert list(LP["幕間"].keys()) == LP["meta"]["幕間順序"] and len(LP["幕間"]) == 6, "幕間台帳: 幕間6本の順序不一致"
    print("復元検証OK: descriptors1224 / translations1224 / 篩266・ADOPT183 / 行為22 / 二相31+17+31 / 分類22・下位系12 / テンプレート4型整合 / 範型4照合 / 検証範型5照合 / 区分分割7" + cat_msg + " / 第2柱インベントリ132＝範型115＋留置17（Overall口頭8書面9・レベル・ポートレート素材・行別note、区分分割と完全分割一致〔判断(ah)〕）/ 第2柱範型7枚＝範型母集団115件完（一号28口頭・二号24書面・三号13口頭・四号18書面・五号10口頭・六号18口頭・七号4口頭、帳簿全数・mode一様）/ 並行対3族12（叙述族7・型式標本247-338／論証族4・型式標本277-356＋判断(af)の305-359/303-356/299-354／教示族1・270-364、両側実在・モード配置・族宣言・糸保存・段差3帳簿＝軸は準備・推敲可能性〔判断(af)〕）/ 糸正準7スケール（完全分割・語彙正準＝宣言族の族糸∪固有糸、族糸3族〔叙述5・論証4・教示3〕・族無所属1〔告知、判断(ag)〕・固有糸規則照合）/ テンプレート三層（第1柱4型＋構築梯子型・適用スケール一致）/ 参照台帳7種46エッジ（重複対4・口頭再掲1・柱間3・族間1・行為内5・留置4・行為間参照28、所有排他・正準向き・散文同期・検出裁定17〔判断(ai)〕）/ 軸台帳13軸182件（完全分割・音韻3スケール束ね・15スケール一意所属・シート主軸＝宣言18〔散文証拠つき〕＋未宣言11＝29完全分割〔判断(aj)〕）/ 出自類型の表示訳4門（述べる・働きかける・表す・つなぐ＝語彙一致〔判断(ak)〕）/ 幕間台帳6本63件（柱1総括18＋柱2総括17＋R1質28の完全分割・素材区分整合・プラス級畳み込み〔判断(al)〕）")
