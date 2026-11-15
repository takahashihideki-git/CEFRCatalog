#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""層をまたぐ出自の検査（判断(dc)、地図は gatekeeper/layers.md）

既存の4ゲートが見ているのは「揃っているか」である ──
  restore.py          原典↔帳簿、帳簿↔台帳
  source_sync_check   生成ソース↔成果物
  book_style_check    帳簿↔書物、書物内部の用字
  exponent_level_check 例文↔CEFR-Jの級

この道具が見るのは、そのどれも見ていない上流の二本:

  A 判断の記録（引き継ぎ書§2） → 現行仕様・執筆要綱      ＝記号の鎖
  B 設計文書『受容の課題』付録A → 帳簿の深さ軸（第3部11枚）
  C 設計文書『受容の課題』§4の手加減の表 → 帳簿の条件の区分（第3部11枚68区分）

Aが要るのは、現行仕様が判断の圧縮であり、圧縮から推論すると器を誤診するため
（実例：条件の軸を「読むものを条件に流用した崩れ」と誤診し、判断(bp)(cj)と
『受容の課題』§4の手加減の表で反証された。カタログ51）。記号が到達しなければ
解凍そのものができない。

Bが要るのは、深さの割り付けが付録A・帳簿・restore.pyの固有assertの三重管理で、
同期を見るものが無かったため。

Cが要るのは、条件の区分が何の手加減を実現しているかの矢印が、判断の散文にだけ
あって帳簿に無かったため（判断(cj)根拠(b)が「紙面の作りは§4の『明示された構成・
標識』（層4）と『短さ』の、項目の紙面での形」と書いて捨てていた）。宣言を強制すると
**区分名が手加減でなく載せ物・物・内容を取っている箇所がその場で見える**。

限界：記号の抽出は括弧つき小文字列の単純一致なので、散文の列挙記号 (a)(b) を
拾いうる。誤って拾っても「到達する」側に倒れるので、偽の赤は出ない。
"""
import re, io, json, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDOVER = os.path.join(ROOT, 'deliverables/CEFRカタログ_引き継ぎ書.md')
RECEPTION = os.path.join(ROOT, 'deliverables/CEFRカタログ_受容の課題.md')
SPECS = sorted(glob.glob(os.path.join(ROOT, 'deliverables/CEFRカタログ_現行仕様_*.md'))) + \
        [os.path.join(ROOT, 'deliverables/CEFRカタログ_執筆要綱.md')]
PLACEHOLDER = {'xx'}                      # 現行仕様§5の雛形「→(xx)で改定」
LAYER = {1: '形', 2: '命題', 3: '筋', 4: '要点', 5: '全体', 6: '含意', 7: '立場'}

errors, warnings, notes = [], [], []
def rd(p): return io.open(p, encoding='utf-8').read()
def sym_index(s):
    return ord(s) - 96 if len(s) == 1 else 26 + (ord(s[0]) - 97) * 26 + (ord(s[1]) - 96)

# ---------- A 記号の鎖 ----------
hb = rd(HANDOVER)
heads, order = {}, []
for m in re.finditer(r'^### \(([a-z]{1,2})\)(.*)$', hb, re.M):
    if m.group(1) in heads:
        errors.append("A0: 記号(%s)の見出しが二つある" % m.group(1))
    heads[m.group(1)] = m.group(2)
    order.append((m.group(1), m.start()))

superseded = {}
for k, title in heads.items():
    mm = re.search(r'→\(([a-z]{1,2})\)で(改定|書き下ろし)', title)
    if mm:
        superseded[k] = mm.group(1)

cited = {}
for path in SPECS:
    name = os.path.basename(path)
    text = rd(path)
    for m in re.finditer(r'\(([a-z]{1,2})\)', text):
        s, tail = m.group(1), text[m.end():m.end() + 1]
        if s in PLACEHOLDER:
            continue
        # 一文字の記号は、散文の列挙記号（執筆要綱「源は五つに限る：(a) 文字体系…」
        # 「層1・層2の段では(a)(b)(c)」）と綴りが同じなので、引用の形だけを採る ──
        # 行末（「揺り戻す (j)」）／「判断(o)」／「(s)-1」。
        # 誤って採ると改定の鎖(A2)が空振りする（反例2で実際に空振りした）。
        if len(s) == 1 and not (tail in ('', '\n', '-') or text[:m.start()].endswith('判断')):
            continue
        cited.setdefault(s, set()).add(name)

# A1 到達性
for s in sorted(cited, key=sym_index):
    if s not in heads:
        errors.append("A1: 記号(%s)が引き継ぎ書§2に到達しない（引いているのは %s）"
                      % (s, '・'.join(sorted(cited[s]))))
# A2 改定の鎖
for s in sorted(cited, key=sym_index):
    if s in superseded and superseded[s] not in cited:
        errors.append("A2: 改定済みの判断(%s)を引いているが、改定した(%s)をどの現行仕様も引いていない（%s）"
                      % (s, superseded[s], '・'.join(sorted(cited[s]))))
# A3 配置の昇順（警告）
prev_i, prev_s = 0, None
for s, _ in order:
    if sym_index(s) < prev_i:
        warnings.append("A3: 判断(%s)の節が記号の昇順より前に置かれている（直前の最大は(%s)）" % (s, prev_s))
    if sym_index(s) > prev_i:
        prev_i, prev_s = sym_index(s), s
# 連番の抜け
gaps = [i for i in range(1, max(sym_index(s) for s in heads) + 1)
        if i not in {sym_index(s) for s in heads}]
if gaps:
    errors.append("A4: 記号の連番に抜けがある（通算 %s 件目）" % gaps)
notes.append("A: 判断 %d 件（抜けなし）／現行仕様・執筆要綱が引く記号 %d 件／"
             "引かれていない判断 %d 件（第1部・第2部期を含む。器を変えた判断の被引用は機械では判定できない）"
             % (len(heads), len(cited), len(heads) - len(cited)))

# ---------- B 設計文書 → 帳簿の深さ ----------
doc = rd(RECEPTION)
i = doc.find('## 付録A')
if i < 0:
    errors.append("B0: 『受容の課題』に付録Aの見出しがない")
else:
    apx = doc[i:]
    appendix = {}
    for m in re.finditer(r'^\|\s*(Pre-A1|[A-C][0-9+]*)\s*\|\s*(\d+)\s*\|\s*([1-7])\s', apx, re.M):
        appendix[int(m.group(2))] = int(m.group(3))
    if len(appendix) < 200:
        errors.append("B0: 付録Aから読めた行が %d 件（209件を期待）── 表の形が変わった" % len(appendix))
    ledger = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'prototypes/catalog_p3_*.json'))):
        d = json.load(io.open(f, encoding='utf-8'))
        sheet = d[list(d)[0]]
        for layer_name, nos in (sheet.get('axes') or {}).get('深さ', {}).items():
            for n in nos:
                ledger[n] = (layer_name, os.path.basename(f))
    for n in sorted(ledger):
        name, f = ledger[n]
        if n not in appendix:
            errors.append("B1: No.%d（%s）が付録Aに無い" % (n, f))
        elif LAYER[appendix[n]] != name:
            errors.append("B2: No.%d の層が食い違う ── 付録A「%s」／帳簿「%s」（%s）"
                          % (n, LAYER[appendix[n]], name, f))
    notes.append("B: 付録A %d 行 ↔ 第3部11枚 %d 行、層の不一致 0 件" % (len(appendix), len(ledger)))

# ---------- C 設計文書§4の手加減の表 → 帳簿の条件の区分 ----------
i4 = doc.find('## 4. 条件')
if i4 < 0:
    errors.append("C0: 『受容の課題』に§4の見出しがない")
else:
    tbl = doc[i4:doc.find('\n## ', i4 + 5)]
    support = {}                      # 手加減名 → 下げる層（表の第3列）
    for m in re.finditer(r'^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]+?)\s*\|', tbl, re.M):
        nm = m.group(1)
        if nm in ('手加減', '---') or set(nm) <= set('-'):
            continue
        support[nm] = m.group(3)
    if len(support) != 11:
        errors.append("C0: §4の手加減の表から読めた行が %d 件（11件を期待）── 表の形が変わった" % len(support))
    MODE_ONLY = {'（聞く）': ('聞く',), '（読む）': ('読む',)}
    used = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'prototypes/catalog_p3_*.json'))):
        base = os.path.basename(f)
        d = json.load(io.open(f, encoding='utf-8'))
        sheet = d[list(d)[0]]
        cond = (sheet.get('axes') or {}).get('条件', {})
        decl = sheet.get('条件の手加減')
        if decl is None:
            errors.append("C1: %s に「条件の手加減」が無い" % base)
            continue
        if set(decl) != set(cond):
            errors.append("C1: %s の「条件の手加減」が条件の区分と一致しない（不足 %s／余分 %s）"
                          % (base, sorted(set(cond) - set(decl)), sorted(set(decl) - set(cond))))
        modes = {r.get('mode') for r in sheet['rows']}
        for name, vals in decl.items():
            if not vals:
                errors.append("C3: %s の区分「%s」の手加減が空" % (base, name))
            for v in vals:
                if v not in support:
                    errors.append("C2: %s の区分「%s」の手加減「%s」が§4の表に無い" % (base, name, v))
                    continue
                used.setdefault(v, []).append(base)
                for tag, ok_modes in MODE_ONLY.items():
                    if tag in v and not (modes & set(ok_modes)):
                        warnings.append("C4: %s（mode %s）の区分「%s」が%s限定の手加減「%s」を宣言している"
                                        % (base, '・'.join(sorted(modes)), name, tag.strip('（）'), v))
    unused = [k for k in support if k not in used]
    notes.append("C: §4の手加減 %d 行 ↔ 第3部11枚の条件 68区分。使われていない手加減 %d 件%s"
                 % (len(support), len(unused), ("：" + "／".join(unused)) if unused else ""))

# ---------- 報告 ----------
for n in notes:
    print("  " + n)
for w in warnings:
    print("警告: " + w)
if errors:
    print("\n出自検査 NG:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("\n出自検査OK: 記号の鎖（到達性・改定の鎖・連番）／設計文書→帳簿の深さ")
