#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""書物用字・散文規律チェッカー（CEFRカタログ16、判断(ap)）。

deliverables/book/*.md を対象に、執筆要綱の機械化可能な範囲を検査する:
  1. データ層照合   : 章⇔全数シートの No 出現・jp 無改変転写・例文無改変転写（イタリック記号除去後）・出典 No 集合一致
  2. 幕間素材照合   : 幕間⇔level_portraits の素材 No 全使用・出典包含
  3. 用字           : 裸の「記述文」禁止／「能力記述文」は巻頭の係留1回のみ／各章・幕間の初出は同段落内に CEFR 係留／
                      「Can-Do」単独・「ディスクリプタ」禁止（巻頭の「Can-doリスト」係留は許容）
  4. 呪文パターン   : 既知の比喩固有述語・帳簿圧縮表現（事故型②③の再発防止。適否の本判定は精読）
  5. 帳簿語彙       : 分析語彙の漏出（量産章・幕間のみ。範型章の命名済み語彙は対象外）
  6. 「門」残存     : 書物は「〜言葉」へ統一（判断(aq)。専門・入門・部門・関門は除外）
  7. 出典定型文     : 章・幕間の定型文（No.帰属の断り）の存在

比喩・対比の適否そのものは精読判定であり、本ツールは既知パターンの再発防止に限る
（「greenは宣言の妥当性を保証しない」）。
"""
import json, re, sys, glob, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BOOK = os.path.join(ROOT, 'deliverables', 'book')

# 章 → (全数シートjson, キー)。新章の追加時はここへ登録する。
SHEET_REGISTRY = {
    '範型章_苦情クレーム.md':      ('catalog_complaint.json', '苦情・クレーム'),
    '章_挨拶別れ安否.md':          ('catalog_greeting.json', '挨拶・別れ・安否'),
    '章_会話の開始維持.md':        ('catalog_conversation.json', '会話の開始・維持'),
    '章_事実情報の授受.md':        ('catalog_infoexchange.json', '事実情報の授受'),
    '章_自己に関する情報提供.md':  ('catalog_selfinfo.json', '自己に関する情報提供'),
    '章_経験出来事の叙述.md':      ('catalog_experience.json', '経験・出来事の叙述'),
    '章_問題事情の説明.md':        ('catalog_problemexplain.json', '問題・事情の説明'),
    '章_面接での質問と応答.md':    ('catalog_interview.json', '面接での質問と応答'),
    '章_伝言の授受.md':            ('catalog_message.json', '伝言の授受'),
    '章_明確化繰り返しの要求.md':  ('catalog_clarification.json', '明確化・繰り返しの要求'),
    '章_取引購入注文.md':          ('catalog_transaction.json', '取引（購入・注文）'),
    '章_問い合わせ.md':            ('catalog_enquiry.json', '問い合わせ'),
    '章_道案内の依頼と提供.md':    ('catalog_directions.json', '道案内の依頼と提供'),
    '章_応募出願.md':              ('catalog_application.json', '応募・出願'),
    '章_指示への応答.md':          ('catalog_instructionresponse.json', '指示への応答'),
    '章_依頼要求.md':              ('catalog_request.json', '依頼・要求'),
    '章_提案誘い計画の相談.md':    ('catalog_proposal.json', '提案・誘い・計画の相談'),
    '章_助言.md':                  ('catalog_advice.json', '助言'),
    '章_同意不同意.md':            ('catalog_agreement.json', '同意・不同意'),
}

# 幕間 → level_portraits のキー
PORTRAIT_REGISTRY = {
    '幕間_はじまりの言葉.md': 'preA1_A1',
    '幕間_A2という人.md': 'A2',
    '範型幕間_B1という人.md': 'B1',
    '幕間_B2という人.md': 'B2',
}

INCANT = ['梯子を刻', 'を刻む', 'を刻んで', '梯子の主語', '梯子の中身']  # 事故型②③の既知形
LEDGER = ['質問応答相', '情報管理相', '管理梯子', '梯子型', '外部化', '柱間',
          '消失点', '判断(', '書面フォーマル一段', '語り糸', '並行対', '重複対']
GATE_EXEMPT = ('専門', '入門', '部門', '関門')  # 「門」検査の除外複合語

SRC_CH = 'No.は本書が原典の全件に付した通し番号'

# 既知の未解消事項（検出済み・裁定待ちの免除台帳。解消したらここから消す ── restore.py の KNOWN_ISSUES 方式）
# カタログ16検出の618/698（B1範型幕間）は補遺3で織り込み解消済み。現在、免除なし。
KNOWN_GAPS = {}


def strip_marks(s):
    return s.replace('*', '')


def cited_numbers(s):
    """「No.412」「No.324, 622」等の No. 引用群から番号集合を取る。"""
    groups = re.findall(r'No\.[\d,\s、]+', s)
    return set(int(x) for g in groups for x in re.findall(r'\d+', g))


def main():
    errors = []
    files = sorted(glob.glob(os.path.join(BOOK, '*.md')))
    for f in files:
        name = os.path.basename(f)
        t = open(f, encoding='utf-8').read()
        tt = strip_marks(t)

        # 1. データ層照合
        if name in SHEET_REGISTRY:
            sheet_f, key = SHEET_REGISTRY[name]
            sheet = json.load(open(os.path.join(ROOT, 'prototypes', sheet_f), encoding='utf-8'))[key]
            rows = sheet['rows']
            body_cites = cited_numbers(t.split('出典：')[0])
            # 段のブロック（### 見出し〜次の見出し）に閉じて照合する（カタログ19検品⑬：文書全体の部分文字列一致では、
            # 見取り図に再掲された例文が段側の改変を隠す）。見出しの「（No.522・546）」のような束エントリも一つのブロック。
            #     ブロックは次の見出し（## または ###）で切る。例文は段の「例」欄＝リスト行（`- *…*`）だけを照合対象とし、
            #     落とし穴・場面の散文中の言及は照合外（カタログ19検品⑭：段内の再掲が「例」欄の改変を隠していた）。
            blocks = re.split(r'\n(?=#{2,3} )', t)
            def block_of(no):
                for b in blocks:
                    head = b.split('\n', 1)[0]
                    if head.startswith('### ') and re.search(r'No\.(?:\d+[・,\s]+)*' + str(no) + r'(?!\d)', head):
                        return b
                return None
            def example_lines(b):
                """「例」欄のリスト行を (本文, 帰属No.) で返す。帰属は「**例**（… No.N）」の節ラベル、または行末の「（No.N）」。
                束エントリ（見出しに複数No.）では帰属が必須（カタログ19検品⑯：束の中で例文がどの行のものか照合されなかった）。"""
                out, in_ex, sec_no = [], False, None
                for l in b.split('\n'):
                    if l.startswith('**例**'):
                        in_ex = True
                        nos_in_label = re.findall(r'\d+', ''.join(re.findall(r'No\.[\d・,\s]+', l)))
                        if len(nos_in_label) > 1:
                            errors.append(f"{name}: 「例」の節ラベルにNo.が複数ある（帰属は一つ：{l.strip()[:40]}）")
                        sec_no = int(nos_in_label[0]) if nos_in_label else None
                    elif l.startswith('**'):
                        in_ex = False
                    elif in_ex and l.startswith('- '):
                        s = strip_marks(l)[2:].strip()
                        m = re.search(r'（No\.(\d+)）\s*$', s)
                        no = int(m.group(1)) if m else sec_no
                        if m:
                            s = s[:m.start()].rstrip()
                        out.append((s, no))
                return out
            def bundle_nos(b):
                head = b.split('\n', 1)[0]
                return [int(x) for x in re.findall(r'\d+', re.search(r'No\.[\d・,\s]+', head).group(0))]
            for r in rows:
                if r['no'] not in body_cites:
                    errors.append(f"{name}: No.{r['no']} が本文に出現しない")
                b = block_of(r['no'])
                if b is None:
                    errors.append(f"{name}: No.{r['no']} の段ブロック（### 見出しにNo.）が見つからない")
                    continue
                if r['jp'] not in b:
                    errors.append(f"{name}: No.{r['no']} の jp が段内で無改変転写でない")
                exl = example_lines(b)
                if len(bundle_nos(b)) > 1:
                    if any(no is None for _, no in exl):
                        errors.append(f"{name}: No.{r['no']} の束エントリに、行の帰属ラベル（節「**例**（… No.N）」または行末「（No.N）」）のない例文がある")
                    mine = [s for s, no in exl if no == r['no']]
                else:
                    mine = [s for s, _ in exl]
                for ex in r['exponents']:
                    if not any(ex in l for l in mine):
                        errors.append(f"{name}: No.{r['no']} の例文が「例」欄（当該行の帰属分）で無改変転写でない: {ex[:30]}")
            m = re.search(r'出典：.*?（No\.(.*?)）', t)
            if not m:
                errors.append(f"{name}: 出典行が見つからない")
            else:
                nos = set(int(x) for x in re.findall(r'\d+', m.group(1)))
                want = set(r['no'] for r in rows)
                if nos != want:
                    errors.append(f"{name}: 出典 No 集合不一致 差分={nos ^ want}")

        # 2. 幕間素材照合
        if name in PORTRAIT_REGISTRY:
            lp = json.load(open(os.path.join(ROOT, 'data', 'level_portraits.json'), encoding='utf-8'))
            mat = set(sum(lp['幕間'][PORTRAIT_REGISTRY[name]]['素材'].values(), []))
            exempt = KNOWN_GAPS.get(name, set())
            body_cites = cited_numbers(t.split('出典：')[0])
            for n in sorted(mat - exempt):
                if n not in body_cites:
                    errors.append(f"{name}: 素材 No.{n} が未使用")
            m = re.search(r'出典：.*?（No\.(.*?)）', t)
            if m:
                nos = set(int(x) for x in re.findall(r'\d+', m.group(1)))
                if not (mat - exempt) <= nos:
                    errors.append(f"{name}: 出典に素材が欠落 {(mat - exempt) - nos}")

        # 3. 用字
        for m in re.finditer(r'記述文', t):
            pre = t[max(0, m.start() - 10):m.start()]
            if not (pre.endswith('Can-Do') or pre.endswith('能力') or pre.endswith('級総括の')):
                if not pre.endswith('のCan-Do'):
                    errors.append(f"{name}: 裸の「記述文」…{t[max(0,m.start()-15):m.start()+10]}…")
        n_official = t.count('能力記述文')
        if '範型巻頭' in name:
            if n_official != 1:
                errors.append(f"{name}: 「能力記述文」係留が{n_official}回（1回のはず）")
        elif n_official:
            errors.append(f"{name}: 「能力記述文」が{n_official}回混入")
        # 初出係留：見出し行（#…）上の出現は飛ばし、本文の初出で判定（見出しは直後の本文が係留する）
        first = -1
        for m in re.finditer('Can-Do記述文', t):
            ls = t.rfind('\n', 0, m.start()) + 1
            if not t[ls:m.start()].lstrip().startswith('#'):
                first = m.start(); break
        if first >= 0:
            para = t[t.rfind('\n\n', 0, first) + 2:first]
            if 'CEFR' not in para:
                errors.append(f"{name}: 本文初出の Can-Do記述文 に段落内 CEFR 係留がない")
        for m in re.finditer(r'Can-Do(?!記述文)', t):
            errors.append(f"{name}: 「Can-Do」単独使用 …{t[max(0,m.start()-10):m.start()+15]}…")
        if 'ディスクリプタ' in t:
            errors.append(f"{name}: 「ディスクリプタ」混入")

        # 4. 呪文パターン
        for w in INCANT:
            if w in t:
                errors.append(f"{name}: 呪文パターン「{w}」")

        # 5. 帳簿語彙（量産章・幕間のみ。範型は命名済み語彙を含むため対象外）
        if name.startswith(('章_', '幕間_')):
            for w in LEDGER:
                if w in t:
                    errors.append(f"{name}: 帳簿語彙「{w}」の漏出")

        # 5.5 級/段の混在・時代語彙（カタログ16検品第一報）
        for m in re.finditer(r'(?<!最)上段|下段|中段', t):
            errors.append(f"{name}: 帳簿語彙「{m.group(0)}」（級の範囲は「級」で言う）")
        if '電報体' in t:
            errors.append(f"{name}: 時代語彙「電報体」（→短文・主語を省いた書き方）")
        if '系列' in t:
            errors.append(f"{name}: 帳簿語彙「系列」（章内の下位区分は「〜の梯子」、判断(ar)検品）")
        # 読者の読書行為の言い切り（規律3追補、カタログ17検品＋18補遺。認知述語〔気づいただろう等〕は自章内可＝精読判定）
        for w in ('章で読んで', '読んだ読者', '読み終えた読者'):
            if w in t:
                errors.append(f"{name}: 読者行為の言い切り「{w}」（内容主語の軽い形へ：「で見た」「に登場する」）")

        # 5.7 章の外への読了前提（規律3の方向例外撤廃、判断(at)カタログ18＋補遺1。読了前提は自章内のみ）
        #     自章内の合法形（「〜の段で見た」「No.Nで見た」）は「の章」「巻頭」「幕間」を先行語に持たないため発火しない。
        #     文境界（。・改行）をまたぐ照合はしない。語形は裁定済みのもののみ登録（カタログ18検品⑥の順序）。
        for pat, lab in (
            (r'の章[^。\n]{0,30}?[でにをが](?:も)?見(?:た(?!い)|てきた)', '章への読了前提（位置中立の現在形へ：「〜の章にも現れる」「〜の章が受け持つ」）'),
            (r'巻頭[^。\n]{0,20}?[でにをが](?:も)?(?:見|数え)(?:た(?!い)|てきた)', '巻頭への読了前提（文書主語へ：「巻頭に掲げた」）'),
            (r'幕間[^。\n]{0,20}?[でにをが](?:も)?(?:見|数え)(?:た(?!い)|てきた)', '幕間への読了前提（文書主語へ：「前の幕間が描く」）'),
            (r'(?:の章|幕間|巻頭)[^。\n]{0,15}?を?思い出し', '章の外への記憶訴求（規律3：読了前提は自章内のみ）'),
            (r'まだ読んでいない章|ここまでの章|ここまでの行為|いま読み終えた', '読書状態の仮定（→「この先の章」「行為の章々」等の文書側の記述へ）'),
            (r'前章|次章', '章の位置指示（章は行為名で指す：「挨拶の章」「あちらの章」、判断(at)補遺）'),
        ):
            for m in re.finditer(pat, t):
                errors.append(f"{name}: {lab} …{t[max(0,m.start()-15):m.end()+10]}…")

        # 5.6 裸の通し番号（No.なし。連番継続・英語例・件数は許容）
        body = t.split('出典：')[0]
        for i, line in enumerate(body.split('\n'), 1):
            s = line.strip()
            if (s.startswith('- *') and not s.startswith('- **')) or s.startswith('> ') or s.startswith('- （'):
                continue
            for m in re.finditer(r'(?<![\d\-–])([2-7]\d{2})(?![\d\-–])(?!件)', line):
                back = line[:m.start()]
                if back.endswith('No.'):
                    continue
                if re.search(r'No\.\d{3}(?:[・/／、]\d{3})*[・/／、]$', back) or re.search(r'No\.[\d,\s]+$', back):
                    continue
                if re.search(r'[A-Za-z] $', back):  # 英語例文内（Room 302 等）
                    continue
                errors.append(f"{name}:{i}: 裸の通し番号 …{line[max(0,m.start()-12):m.start()+8]}…")

        # 6. 「門」残存
        for m in re.finditer('門', t):
            ctx = t[max(0, m.start() - 3):m.start() + 3]
            if not any(w in ctx for w in GATE_EXEMPT):
                errors.append(f"{name}: 「門」残存 …{t[max(0,m.start()-12):m.start()+8]}…")

        # 7. 出典定型文
        if (name.startswith(('章_', '範型章', '幕間_')) or '範型幕間' in name):
            if SRC_CH not in t:
                errors.append(f"{name}: 出典定型文（No.帰属の断り）不在")

    # 3.補: 「記述文」正規判定のやり直し（許容パターンを厳密化）
    # 上の速判定で誤許容が出ないよう、許容は「Can-Do記述文」「能力記述文」の一部のみ。
    if errors:
        print(f"書物用字検査 NG: {len(errors)}件")
        for e in errors:
            print('  -', e)
        sys.exit(1)
    print(f"書物用字検査OK: 対象{len(files)}ファイル ── データ層照合（章{len(SHEET_REGISTRY)}・幕間{len(PORTRAIT_REGISTRY)}）／用字／呪文パターン／帳簿語彙／「門」残存／出典定型文")


if __name__ == '__main__':
    main()
