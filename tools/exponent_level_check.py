# -*- coding: utf-8 -*-
"""実例（exponent）語彙レベルチェッカー ── 第3周-0の品質保証装置。

範型の実例文の各語を CEFR-J Wordlist（A1〜B2）＋ Octanove Vocabulary
Profile（C1〜C2）に照合し、行の目標レベルを超える語彙・未収録語を検出する。

設計原則（restore.py 文化の延長）:
- 依存ゼロ・決定論的。レンマ化は不規則表＋規則のみ（統計モデル不使用）。
- 本ツールは**検出器であって裁定者ではない**。超過語の採否（固有名詞・
  定型句・意図的な高級語）は人間が判定する。
- レベルは**全候補（表層形＋語形変化の復元候補）の最小**を採用（寛容側。
  品詞タグ付けを持たないための設計判断。moving/planning のような
  「活用形が独立見出しで高レベル」の偽陽性を抑える。副作用として
  friendly[B2] が friend[A1]+ly に割れる過小評価はありうる）。
- 文中（非文頭）で大文字始まりの未収録語は固有名詞と推定し、指摘しない。
- 人間の裁定は tools/exponent_allowlist.txt に「語<TAB>理由」で保全し、
  以後の監査で抑制する（裁定の機械可読な単一情報源）。

出典（データは本リポジトリに含めない。同階層に clone して使う）:
- The CEFR-J Wordlist Version 1.5. Compiled by Yukio Tono, Tokyo University
  of Foreign Studies. Retrieved from http://www.cefr-j.org/download.html
  （東京外国語大学 投野由紀夫研究室。出典明記のもと研究・商用利用可）
- Octanove Vocabulary Profile C1/C2 (ver 1.0), Octanove Labs. CC BY-SA 4.0.
- 配布リポジトリ: https://github.com/openlanguageprofiles/olp-en-cefrj

使い方:
  python3 tools/exponent_level_check.py                # 全範型JSONを監査
  python3 tools/exponent_level_check.py --sent B1 "I see your point, ..."
"""
import csv, json, os, re, sys

LEVEL_ORDER = {"A1": 1, "A2": 2, "B1": 3, "B2": 4, "C1": 5, "C2": 6}
INV_LEVEL = {v: k for k, v in LEVEL_ORDER.items()}

def base_level(row_level: str) -> str:
    """範型の行レベル（Pre-A1/A1/A2+/B1+...）→ 照合用の基底レベル。"""
    lv = row_level.replace("Pre-A1", "A1").rstrip("+")
    if lv not in LEVEL_ORDER:
        raise ValueError(f"未知のレベル表記: {row_level}")
    return lv

# ------------------------------------------------------------ 語彙表のロード
def load_lexicon(data_dir: str):
    """word → 最小レベル。多語表現（スペース含む headword）は語列タプル辞書。"""
    single, multi = {}, {}
    for fn in ("cefrj-vocabulary-profile-1.5.csv",
               "octanove-vocabulary-profile-c1c2-1.0.csv"):
        with open(os.path.join(data_dir, fn), encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                lv = r["CEFR"].strip()
                if lv not in LEVEL_ORDER:
                    continue
                for h in r["headword"].split("/"):
                    h = h.strip().lower()
                    if not h:
                        continue
                    if " " in h:
                        key = tuple(h.split())
                        if key not in multi or LEVEL_ORDER[lv] < LEVEL_ORDER[multi[key]]:
                            multi[key] = lv
                    else:
                        if h not in single or LEVEL_ORDER[lv] < LEVEL_ORDER[single[h]]:
                            single[h] = lv
    return single, multi

def load_allowlist(path: str):
    """人間裁定の保全ファイル: 「語<TAB>理由」。無ければ空。"""
    allow = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t", 1)
            allow[parts[0].lower()] = parts[1] if len(parts) > 1 else ""
    return allow

# ------------------------------------------------------------ レンマ化（決定論）
IRREG_VERBS = {
    "was": "be", "were": "be", "been": "be", "am": "be", "is": "be", "are": "be",
    "has": "have", "had": "have", "having": "have",
    "did": "do", "does": "do", "done": "do", "doing": "do",
    "went": "go", "gone": "go", "goes": "go",
    "said": "say", "says": "say", "made": "make", "got": "get", "gotten": "get",
    "took": "take", "taken": "take", "came": "come", "saw": "see", "seen": "see",
    "knew": "know", "known": "know", "thought": "think", "told": "tell",
    "gave": "give", "given": "give", "found": "find", "felt": "feel",
    "left": "leave", "kept": "keep", "held": "hold", "brought": "bring",
    "began": "begin", "begun": "begin", "wrote": "write", "written": "write",
    "stood": "stand", "heard": "hear", "let": "let", "meant": "mean",
    "met": "meet", "paid": "pay", "put": "put", "ran": "run", "read": "read",
    "sat": "sit", "spoke": "speak", "spoken": "speak", "spent": "spend",
    "understood": "understand", "won": "win", "wore": "wear", "worn": "wear",
    "ate": "eat", "eaten": "eat", "drank": "drink", "drunk": "drink",
    "drove": "drive", "driven": "drive", "flew": "fly", "flown": "fly",
    "forgot": "forget", "forgotten": "forget", "chose": "choose", "chosen": "choose",
    "broke": "break", "broken": "break", "bought": "buy", "built": "build",
    "caught": "catch", "cost": "cost", "cut": "cut", "dealt": "deal",
    "fell": "fall", "fallen": "fall", "grew": "grow", "grown": "grow",
    "hit": "hit", "hurt": "hurt", "lost": "lose", "sent": "send", "set": "set",
    "showed": "show", "shown": "show", "slept": "sleep", "sold": "sell",
    "taught": "teach", "threw": "throw", "thrown": "throw", "woke": "wake",
    "sang": "sing", "sung": "sing", "swam": "swim", "swum": "swim",
    "rang": "ring", "rung": "ring", "rose": "rise", "risen": "rise",
    "led": "lead", "lent": "lend", "lay": "lie", "lain": "lie", "laid": "lay",
    "sought": "seek", "shook": "shake", "shaken": "shake", "stuck": "stick",
    "struck": "strike", "swore": "swear", "sworn": "swear", "tore": "tear",
    "torn": "tear", "beat": "beat", "beaten": "beat", "bent": "bend",
    "bet": "bet", "bound": "bind", "bit": "bite", "bitten": "bite",
    "blew": "blow", "blown": "blow", "burnt": "burn", "burst": "burst",
    "dreamt": "dream", "dug": "dig", "fed": "feed", "fought": "fight",
    "forgave": "forgive", "forgiven": "forgive", "froze": "freeze",
    "frozen": "freeze", "hid": "hide", "hidden": "hide", "hung": "hang",
    "learnt": "learn", "lit": "light", "quit": "quit", "rode": "ride",
    "ridden": "ride", "shot": "shoot", "shut": "shut", "spelt": "spell",
    "spread": "spread", "stole": "steal", "stolen": "steal", "swept": "sweep",
    "wound": "wind",
}
IRREG_NOUNS = {
    "men": "man", "women": "woman", "children": "child", "people": "person",
    "feet": "foot", "teeth": "tooth", "mice": "mouse", "geese": "goose",
    "lives": "life", "wives": "wife", "knives": "knife", "leaves": "leaf",
    "halves": "half", "shelves": "shelf", "loaves": "loaf", "thieves": "thief",
    "selves": "self",
}
IRREG_ADJ = {
    "better": "good", "best": "good", "worse": "bad", "worst": "bad",
    "further": "far", "furthest": "far", "farther": "far", "farthest": "far",
    "less": "little", "least": "little", "more": "many", "most": "many",
}
# n't 系の特例（機械的に n't を剥がすと can't→ca になる）
NT_SPECIAL = {"can't": ["can", "not"], "won't": ["will", "not"],
              "shan't": ["shall", "not"], "ain't": ["be", "not"]}

def _suffix_candidates(w):
    """規則変化の復元候補（全候補を返し、呼び出し側で最小レベルを採る）。"""
    c = []
    if w.endswith("ies") and len(w) > 4: c.append(w[:-3] + "y")
    if w.endswith("es"):
        c += [w[:-2], w[:-1]]                 # boxes→box / houses→house
    if w.endswith("s") and not w.endswith("ss"): c.append(w[:-1])
    if w.endswith("ing") and len(w) > 4:
        stem = w[:-3]
        c += [stem, stem + "e"]               # going→go / making→make
        if len(stem) > 2 and stem[-1] == stem[-2]: c.append(stem[:-1])  # running→run
    if w.endswith("ied") and len(w) > 4: c.append(w[:-3] + "y")
    if w.endswith("ed") and len(w) > 3:
        stem = w[:-2]
        c += [stem, w[:-1]]                   # opened→open / liked→like
        if len(stem) > 2 and stem[-1] == stem[-2]: c.append(stem[:-1])  # stopped→stop
    if w.endswith("ier") and len(w) > 4: c.append(w[:-3] + "y")
    if w.endswith("iest") and len(w) > 5: c.append(w[:-4] + "y")
    if w.endswith("er") and len(w) > 3: c += [w[:-2], w[:-1]]   # nicer→nice
    if w.endswith("est") and len(w) > 4: c += [w[:-3], w[:-2]]  # nicest→nice
    if w.endswith("ly") and len(w) > 4:
        c.append(w[:-2])                      # really→real
        if w.endswith("ily"): c.append(w[:-3] + "y")            # easily→easy
    return c

def lookup(word: str, single: dict):
    """語 → 最小レベル（表層形＋不規則表＋規則復元の全候補から）/ 未収録なら None。"""
    w = word.lower()
    cands = [w, IRREG_VERBS.get(w), IRREG_NOUNS.get(w), IRREG_ADJ.get(w)]
    cands += _suffix_candidates(w)
    levels = [LEVEL_ORDER[single[c]] for c in cands if c and c in single]
    if levels:
        return INV_LEVEL[min(levels)]
    # ハイフン語: 全部分が収録済みなら最大部分レベル（three-week, double-check）
    if "-" in w:
        parts = [p for p in w.split("-") if p]
        plv = [lookup(p, single) for p in parts]
        if plv and all(plv):
            return INV_LEVEL[max(LEVEL_ORDER[l] for l in plv)]
    return None

# ------------------------------------------------------------------ 文の照合
TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]+(?:'[A-Za-z]+)?(?:-[A-Za-z]+)*")

ABBREV = {"mr", "mrs", "ms", "dr", "prof", "st", "no", "vs", "etc", "e.g", "i.e"}

def _tokens(text):
    """(表層形, 文頭か) のリスト。文頭＝直前が文字列頭または .!?:/引用符のみ。
    Mr./Ms. 等の略記ピリオドは文末と見なさない。"""
    toks, sent_start = [], True
    for m in TOKEN_RE.finditer(text):
        toks.append((m.group(0), sent_start))
        tail = text[m.end():m.end() + 3]
        is_abbrev = m.group(0).lower() in ABBREV and tail.startswith(".")
        sent_start = (not is_abbrev and bool(re.match(r"\s*[.!?—:/]", tail))) \
                     or m.end() >= len(text)
    return toks

def check_sentence(sentence: str, row_level: str, single: dict, multi: dict,
                   allow: dict = None):
    """戻り値: {"over": [(語, レベル)], "unknown": [語], "proper": [語],
               "max_level": str}"""
    allow = allow or {}
    limit = LEVEL_ORDER[base_level(row_level)]
    text = sentence.replace("’", "'")
    toks = _tokens(text)
    lowers = [t.lower() for t, _ in toks]
    # 多語表現の n-gram 照合（当たった区間は語照合から除外）
    consumed = [False] * len(toks)
    hits = []
    maxn = max((len(k) for k in multi), default=1)
    for n in range(min(maxn, 4), 1, -1):
        for i in range(len(toks) - n + 1):
            key = tuple(lowers[i:i + n])
            if key in multi and not any(consumed[i:i + n]):
                hits.append((" ".join(key), multi[key]))
                for j in range(i, i + n):
                    consumed[j] = True
    over, unknown, proper, maxlv = [], [], [], 0
    for idx, (surf, is_head) in enumerate(toks):
        if consumed[idx]:
            continue
        lw = lowers[idx]
        # 短縮形の分離
        if lw in NT_SPECIAL:
            parts = NT_SPECIAL[lw]
        elif lw.endswith("n't"):
            parts = [lw[:-3], "not"]
        else:
            parts = [lw]
            for suf, lemma in (("'m", "be"), ("'re", "be"), ("'ve", "have"),
                               ("'ll", "will"), ("'d", "would"), ("'s", None)):
                if lw.endswith(suf) and len(lw) > len(suf):
                    parts = [lw[: -len(suf)]] + ([lemma] if lemma else [])
                    break
        for p in parts:
            if len(p) <= 1 or p in allow:
                continue
            lv = lookup(p, single)
            if lv is None:
                # 文中の大文字始まり＝固有名詞と推定
                if surf[0].isupper() and not is_head:
                    proper.append(surf)
                else:
                    unknown.append(p)
                continue
            maxlv = max(maxlv, LEVEL_ORDER[lv])
            if LEVEL_ORDER[lv] > limit:
                over.append((p, lv))
    for mw, lv in hits:
        maxlv = max(maxlv, LEVEL_ORDER[lv])
        if LEVEL_ORDER[lv] > limit:
            over.append((mw, lv))
    return {"over": over, "unknown": sorted(set(unknown)),
            "proper": sorted(set(proper)), "max_level": INV_LEVEL.get(maxlv, "-")}

# -------------------------------------------------------------- 範型の一括監査
def audit_prototypes(repo_dir: str, single: dict, multi: dict, allow: dict):
    """prototypes/*.json の全実例を照合してレポート。行は10列のdict
    （mode/level/no/en/jp/exponents/scene/howwell/l1/delta）。"""
    n_sent = n_over = n_unk = 0
    for fn in sorted(os.listdir(os.path.join(repo_dir, "prototypes"))):
        if not fn.endswith(".json"):
            continue
        data = json.load(open(os.path.join(repo_dir, "prototypes", fn), encoding="utf-8"))
        for act, body in (data.items() if isinstance(data, dict) else []):
            rows = body.get("rows") if isinstance(body, dict) else None
            if not isinstance(rows, list):
                continue
            for row in rows:
                if not (isinstance(row, dict) and isinstance(row.get("exponents"), list)):
                    continue
                for s in row["exponents"]:
                    n_sent += 1
                    r = check_sentence(s, row["level"], single, multi, allow)
                    if r["over"] or r["unknown"]:
                        n_over += bool(r["over"]); n_unk += bool(r["unknown"])
                        flags = []
                        if r["over"]:
                            flags.append("超過: " + ", ".join(f"{w}({lv})" for w, lv in r["over"]))
                        if r["unknown"]:
                            flags.append("未収録: " + ", ".join(r["unknown"]))
                        print(f"[{fn} | {act} | {row['mode']} {row['level']} No.{row['no']}] {s}")
                        print("    " + " / ".join(flags))
    print(f"\n監査完了: 実例 {n_sent} 文 ── レベル超過あり {n_over} 文 / 未収録語あり {n_unk} 文")
    print("（超過・未収録は要人間判定。裁定済みの語は tools/exponent_allowlist.txt へ）")

# ------------------------------------------------------------------------ CLI
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    data_dir = os.environ.get("OLP_CEFRJ_DIR",
                              os.path.join(os.path.dirname(repo), "olp-en-cefrj"))
    if not os.path.isdir(data_dir):
        sys.exit(f"CEFR-Jデータが見つかりません: {data_dir}\n"
                 "git clone https://github.com/openlanguageprofiles/olp-en-cefrj.git を"
                 "リポジトリと同階層に置くか、環境変数 OLP_CEFRJ_DIR を設定してください。")
    single, multi = load_lexicon(data_dir)
    assert len(single) > 8000 and len(multi) >= 100, \
        f"語彙表のロード件数が想定外: single={len(single)} multi={len(multi)}"
    allow = load_allowlist(os.path.join(here, "exponent_allowlist.txt"))
    if len(sys.argv) >= 4 and sys.argv[1] == "--sent":
        r = check_sentence(" ".join(sys.argv[3:]), sys.argv[2], single, multi, allow)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        audit_prototypes(repo, single, multi, allow)

if __name__ == "__main__":
    main()
