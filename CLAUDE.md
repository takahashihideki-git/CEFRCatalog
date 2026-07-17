# CLAUDE.md

CEFRカタログ（株式会社トピックメーカー）。プロジェクトの中身は `README.md` に、設計と作業仕様は `deliverables/` の2文書にある。ここには**作業を始める前に知っておくべき規律**だけを書く。

## 作業前に必ず読む（順序が重要）

1. `deliverables/CEFR全貌カタログ_企画書.md` ── グランドデザイン（何を作るか）
2. `deliverables/CEFRカタログ_引き継ぎ書.md` ── 作業仕様（どう作り続けるか）。§4に周回計画と現在地

**引き継ぎ書だけで作業を始めないこと。** 企画書未読のまま、確定済みの設計判断へ揺り戻しが起きかけた実績がある（引き継ぎ書 設計判断(j)）。

## 変更したら必ず検証を通す

```bash
python3 restore.py            # 1224件／篩265・ADOPT182／行為22／二相31+17+31／分類22・下位系12／範型4照合／検証範型5照合／区分分割7／全数シート意見31・苦情9照合
python3 analysis/partition.py # block_partition_1224.json を再生成し7区分の件数を検証
```

新しい範型（`prototypes/*_prototype.py`）を追加・変更したときは、機械検証も併せて行う。周をまたぐ不変条件は引き継ぎ書§4にある通り：

- **No. が正準ID**。原文（`en`）とレベルは `data/descriptors_en_1224.json` と一致すること
- **範型は10列＋DISCUSSION 5段落**。`.py` と統合JSON（`prototypes_4types.json`＝4範型／各 `verification_*.json`＝検証範型①〜⑤）の内容が完全一致すること。統合JSONは行為名をトップキーにした dict、行dictの列キーは `mode,level,no,en,jp,exponents,scene,howwell,l1,delta`（py注記の `l1_note` ではなく **`l1`** が正準）。`restore.py` は統合JSONの行を原典と照合するが、**`.py`↔統合JSONの完全一致は restore.py の範囲外**（範型を触ったら別途突き合わせる）
- **第3周の全数シート（`catalog_*.json`、現状 opinion／complaint。`restore.py` の `CATALOGS` 登録表が正）は生成物**。ソースは `prototypes/<act>_full_prototype.py`（en/jp は data から構築時取得＝単一情報源）。`restore.py` が原文・レベル・訳・行為所属に加え**全数性**（シートの行集合＝インベントリの当該行為の所属集合）を照合する。突き合わせは**「適用→コミット→再生成→`git diff` が空」の順**（コミット前に `git diff --exit-code` を使うとパッチ自身の差分で必ず失敗する。コミットを挟まないなら再生成前後のファイル比較で行う）。あわせて `tools/exponent_level_check.py` を通す（第3周-0の品質ゲート）

**作業訳を直すときは二重管理に注意**。作業訳は生成ソース `analysis/ja_tr1〜9.py`（`JA1〜JA9` dict）と成果物 `data/working_translations_1224.json` の両方にある。片方だけ直すと生成経路がずれる。両方を同期修正し、`ja_tr*.py` 合成 == JSON 全1,224件一致を確認してから `restore.py` を通す。

解像度を上げるのは中身であって器ではない。器（スキーマ）を変えるときは引き継ぎ書に判断を書き足す。

## 原典ファイルはコミットしない

CoE配布の `CEFR Descriptors (2020).xlsx` とゲーテ版PDFは `.gitignore` で除外済み。**通常の作業では原典xlsxは不要**（原文テキストは `data/descriptors_en_1224.json` に収録済み、CoEが出典明記のもとで再利用を許諾）。ファイル名のゆらぎに注意 — 除外パターンは `*Descriptors*.xlsx`。

## 成果物の受け取りと統合（このリポジトリでの主な役割）

カタログ本体（範型・データ・ドキュメント）の執筆は**別スレッド（Windows側）**で行われ、ここでの役割は**検証・整合確認・コミット**。成果物は通常、`roundN_M.diff`（パッチ）＋`申し送り_ClaudeCode.md`（コミット用の説明）の2ファイルで届く。手順：

1. `bash tools/clean_zone_identifier.sh` で `*:Zone.Identifier` を掃除
2. `申し送り_ClaudeCode.md` を読み、`git apply --stat` / `--check` と **diff本文の目視**で内容を申し送りと突き合わせる
3. `git apply roundN_M.diff` → `python3 restore.py` と `python3 analysis/partition.py`（＋範型を触ったら `.py`↔統合JSON照合）を通す
4. 申し送りの表題でコミット → push → 作業用ファイル（`*.diff`・`申し送り_ClaudeCode.md`）を削除

**ドキュメントの散文と実データの食い違いは必ず指摘する**（レベル帯・件数など）。ただし直す向きは正準データで確かめること — 過去に指摘は正しく向きを誤った実績がある。パッチ運用と競合するので、パッチ対象外の行を勝手に書き換えず申し送りに回す。

## WSL運用（毎回効いてくる）

ファイルはWindows側で作成され、このディレクトリにコピーされる。そのため：

- **コピー漏れを疑うこと。** ドキュメントが更新されたのに参照先の範型ファイルが来ていない、ということが実際に起きた。ドキュメントの記述と実ファイルを突き合わせてからコミットする
- **調査・検証のPythonは複数行の `python3 -c` で書かない**（この環境で固まる）。スクラッチパッドに `.py` を書いて `python3 file.py` で実行する

## git

リモートは `gh` のトークンを使うHTTPS（この環境にSSH鍵がないため）。`git push` は追加設定なしで通る。
