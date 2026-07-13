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
        "inventory":  L("inventory_170to25.json"),          # No(str)->行為名
        "act_type":   L("act_to_satype.json"),              # 行為名->4類型
        "verdicts":   L("sieve_verdicts_244.json"),         # No(str)->{verdict,reason,note}
        "partition":  L("block_partition_1224.json"),        # No(str)->{block, sub?} 四本柱＋横串の区分
        "prototypes": json.load(open(os.path.join(root,"prototypes","prototypes_4types.json"),encoding="utf-8")),
    }
if __name__ == "__main__":
    D = load_all()
    assert len(D["descriptors"])==1224
    assert len(D["translations"])==1224
    assert set(D["descriptors"])==set(D["translations"]), "No不一致"
    assert sum(1 for v in D["verdicts"].values() if v["verdict"]=="ADOPT")==170
    assert len(set(D["inventory"].values()))==25
    assert len(D["prototypes"])==4
    from collections import Counter
    assert dict(Counter(p["block"] for p in D["partition"].values())) == {
        "やり取り":306,"仲介":251,"受容":197,"how well":182,"産出・談話構築":132,"方略":104,"複言語":52}, "区分分割の不一致"
    print("復元検証OK: descriptors1224 / translations1224 / ADOPT170 / 行為25 / 範型4 / 区分分割7")
