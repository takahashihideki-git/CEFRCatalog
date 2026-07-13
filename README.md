# CEFRカタログ

CEFR（ヨーロッパ言語共通参照枠）増補版2020の全能力記述文を、**発語内行為・受容・仲介の三カタログ＋横串のhow well**として再構造化し、日本の英語学習者に「CEFRの全貌」を具体とともに手渡すプロジェクト。株式会社トピックメーカー（enhack.app）。

このリポジトリは、生成AIとの探求セッション（スレッド「CEFRカタログ0, 1, …」）を横断して、設計判断・分析データ・成果物を共有するための単一情報源（single source of truth）。

## いまどこにいるか

- **第0層：分析台帳**（全数集計・作業訳・言語行為論的篩・発語内行為インベントリ）── 完成
- **第1層：カタログ**（発語内行為×レベル×実例×L1注意＋DISCUSSION）── 四類型の範型を1つずつ作成済み。類型内の汎用性検証はこれから
- **第2層：問題集**（カタログを種に生成AIが増殖させるインスタンス）── 未着手

詳細は `deliverables/CEFRカタログ_引き継ぎ書.md`（作業仕様書）と `deliverables/CEFR全貌カタログ_企画書.md`（グランドデザイン）を参照。

## ディレクトリ構成

```
data/          参照用の一次データ（JSON）
  descriptors_en_1224.json      No.→原文英語descriptor＋level＋scale＋scheme＋mode（音声言語1,224件）
  working_translations_1224.json No.→作業訳（自前・CoE許諾下・商用クリーン）
  inventory_170to25.json         採用170記述文→25発語内行為の写像
  act_to_satype.json             25行為→サール4類型
  sieve_verdicts_244.json        言語行為論的篩の判定（244件：ADOPT170/DROP74＋理由）
prototypes/    第1カタログの範型
  prototypes_4types.json         四類型の範型（全10列＋DISCUSSION）を統合したJSON
  *_prototype.py                 各範型のソース（苦情/挨拶/事実Q&A/意見表明）
analysis/      分析の生モジュール（監査・再実行用）
  ja_tr1〜9.py                   作業訳のソース
  verdicts.py                    篩判定のソース
  acts.py                        170→164個別行為タグ
deliverables/  成果物
  CEFR記述文_全数集計_実例付き.xlsx  12シートの分析台帳＋範型
  CEFR全貌カタログ_企画書.md          グランドデザイン（対外文書）
  CEFRカタログ_引き継ぎ書.md          作業仕様書（設計判断＋根拠＋次手順）
```

## 原典について（重要）

CEFR記述文の**原文テキスト**は `data/descriptors_en_1224.json` に収録済み（欧州評議会がCEFR記述文の再利用を出典明記のもとで許諾しているため）。**通常の作業ではこれで足り、原典xlsxのアップロードは不要**。

原典のExcelファイル `CEFR_Descriptors__2020_.xlsx` そのものは、CoEの配布ファイルであり本リポジトリには含めない。手話を含む全1,712件の再集計やxlsx実体処理など例外的な作業でのみ必要で、その際は欧州評議会公式（https://www.coe.int/en/web/common-european-framework-reference-languages ）から入手する。

**出典**: Council of Europe (2020), *Common European Framework of Reference for Languages: Learning, teaching, assessment – Companion volume*. 作業訳はトピックメーカーによる自前訳であり、ゲーテ・インスティトゥート東京の公式日本語版（2024）とは独立（照合のみに使用）。

## 新スレッドでの再開手順

1. 新スレッドに `deliverables/CEFRカタログ_引き継ぎ書.md` を貼る。
2. 必要なデータはこのリポジトリのraw URLから取得（例：`https://raw.githubusercontent.com/takahashihideki-git/CEFRCatalog/main/data/descriptors_en_1224.json`）。
3. 引き継ぎ書§4の検証キュー（表出型の下位分化）から続行。

## 復元検証値

- `descriptors_en_1224.json`: 1,224件、Noは `working_translations_1224.json` と完全一致
- `sieve_verdicts_244.json`: ADOPT 170／DROP 74
- `inventory_170to25.json`: ユニーク行為数 25
- `prototypes_4types.json`: 4類型、各DISCUSSIONに5段落
