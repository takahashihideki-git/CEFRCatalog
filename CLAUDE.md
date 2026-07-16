# CLAUDE.md

CEFRカタログ（株式会社トピックメーカー）。プロジェクトの中身は `README.md` に、設計と作業仕様は `deliverables/` の2文書にある。ここには**作業を始める前に知っておくべき規律**だけを書く。

## 作業前に必ず読む（順序が重要）

1. `deliverables/CEFR全貌カタログ_企画書.md` ── グランドデザイン（何を作るか）
2. `deliverables/CEFRカタログ_引き継ぎ書.md` ── 作業仕様（どう作り続けるか）。§4に周回計画と現在地

**引き継ぎ書だけで作業を始めないこと。** 企画書未読のまま、確定済みの設計判断へ揺り戻しが起きかけた実績がある（引き継ぎ書 設計判断(j)）。

## 変更したら必ず検証を通す

```bash
python3 restore.py            # 1224件／ADOPT170／行為23／二相30+17／分類23・下位系12／範型4照合／検証範型5照合／区分分割7
python3 analysis/partition.py # block_partition_1224.json を再生成し7区分の件数を検証
```

新しい範型（`prototypes/*_prototype.py`）を追加・変更したときは、機械検証も併せて行う。周をまたぐ不変条件は引き継ぎ書§4にある通り：

- **No. が正準ID**。原文（`en`）とレベルは `data/descriptors_en_1224.json` と一致すること
- **範型は10列＋DISCUSSION 5段落**。`.py` と統合JSON（`prototypes_4types.json` / `verification_expressive.json` / `verification_assertive.json`）の内容が完全一致すること。統合JSONは行為名をトップキーにした dict、行dictの列キーは `mode,level,no,en,jp,exponents,scene,howwell,l1,delta`（py注記の `l1_note` ではなく **`l1`** が正準）

**作業訳を直すときは二重管理に注意**。作業訳は生成ソース `analysis/ja_tr1〜9.py`（`JA1〜JA9` dict）と成果物 `data/working_translations_1224.json` の両方にある。片方だけ直すと生成経路がずれる。両方を同期修正し、`ja_tr*.py` 合成 == JSON 全1,224件一致を確認してから `restore.py` を通す。

解像度を上げるのは中身であって器ではない。器（スキーマ）を変えるときは引き継ぎ書に判断を書き足す。

## 原典ファイルはコミットしない

CoE配布の `CEFR Descriptors (2020).xlsx` とゲーテ版PDFは `.gitignore` で除外済み。**通常の作業では原典xlsxは不要**（原文テキストは `data/descriptors_en_1224.json` に収録済み、CoEが出典明記のもとで再利用を許諾）。ファイル名のゆらぎに注意 — 除外パターンは `*Descriptors*.xlsx`。

## WSL運用（毎回効いてくる）

ファイルはWindows側で作成され、このディレクトリにコピーされる。そのため：

- コピー後は `tools/clean_zone_identifier.sh` を実行（`*:Zone.Identifier` を再帰削除。`--dry-run` あり）
- **コピー漏れを疑うこと。** ドキュメントが更新されたのに参照先の範型ファイルが来ていない、ということが実際に起きた。ドキュメントの記述と実ファイルを突き合わせてからコミットする

## git

リモートは `gh` のトークンを使うHTTPS（この環境にSSH鍵がないため）。`git push` は追加設定なしで通る。
