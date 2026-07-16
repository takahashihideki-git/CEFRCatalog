# CEFRカタログ

CEFR（ヨーロッパ言語共通参照枠）増補版2020の全能力記述文を、**発語内行為・受容・仲介の三カタログ＋横串のhow well**として再構造化し、日本の英語学習者に「CEFRの全貌」を具体とともに手渡すプロジェクト。株式会社トピックメーカー（enhack.app）。

このリポジトリは、生成AIとの探求セッション（スレッド「CEFRカタログ0, 1, …」）を横断して、設計判断・分析データ・成果物を共有するための単一情報源（single source of truth）。

## いまどこにいるか

- **グランドデザイン**：CEFRカタログ2で**四本柱＋横串へ補正**（発語内行為／産出・談話構築／受容／仲介＋how well。全1,224件の完全分割被覆を機械検証済み：`data/block_partition_1224.json`）
- **第0層：分析台帳**（全数集計・作業訳・言語行為論的篩・発語内行為インベントリ・区分分割）── 完成
- **第1層：カタログ** ── 四類型の範型作成済み。**周回方式**で進行中：**第1周（5検証）完了** ── 四類型すべてが内部分化を持つと確定（表出型三分割／主張型二相／指示型は苦情・依頼別立て／儀礼型二分）、類型横断軸3候補（往復・応答／書面フォーマル一段／縦横分業）。**第2周（横断判定）完了**：判定1〜5（授受↔Q&A統合／帰属判定／横断軸昇格／類型再編＝**下位系12系が第一分類層**／篩対象外62件の精査＝**Formal discussion 21件を掛け直しADOPT12・DROP9、採用170→182**）。次は**第3周：テンプレート確定と量産**
- **第2層：問題集**（カタログを種に生成AIが増殖させるインスタンス）── 未着手

詳細は `deliverables/CEFRカタログ_引き継ぎ書.md`（作業仕様書）と `deliverables/CEFR全貌カタログ_企画書.md`（グランドデザイン）を参照。

## ディレクトリ構成

```
data/          参照用の一次データ（JSON）
  descriptors_en_1224.json      No.→原文英語descriptor＋level＋scale＋scheme＋mode（音声言語1,224件）
  working_translations_1224.json No.→作業訳（自前・CoE許諾下・商用クリーン）
  inventory_182to23.json         採用182記述文→23発語内行為の写像
  act_to_satype.json             23行為→サール4類型
  act_phases.json                一行為二相の正準記録（事実情報の授受30件＝質問応答相＋情報管理相／明確化・繰り返しの要求17件＝理解表明相＋明確化要求相）
  cross_axes.json                横断軸の定義＋全23行為の下位系・梯子型・判定状態（第2周-4）
  sieve_verdicts_265.json        言語行為論的篩の判定（265件：ADOPT182/DROP83＋理由）
  block_partition_1224.json      全1,224件の区分分割（やり取り/産出・談話構築/受容/仲介/how well/方略/複言語）
prototypes/    第1カタログの範型と検証範型
  prototypes_4types.json         四類型の範型（全10列＋DISCUSSION）を統合したJSON
  verification_expressive.json   周回検証で作成した検証範型の統合JSON（感謝詫び祝意/感情の表出）
  *_prototype.py                 各範型のソース（苦情/挨拶/事実Q&A/意見表明/感謝詫び祝意/感情）
analysis/      分析の生モジュール（監査・再実行用）
  ja_tr1〜9.py                   作業訳のソース
  verdicts.py                    篩判定のソース
  acts.py                        170→164個別行為タグ
  partition.py                   区分分割の生成・検証ソース（→ data/block_partition_1224.json）
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

1. **必読2文書を必ずこの順で読む**：`deliverables/CEFR全貌カタログ_企画書.md`（グランドデザイン＝何を作るか）→ `deliverables/CEFRカタログ_引き継ぎ書.md`（作業仕様＝どう作り続けるか）。**引き継ぎ書だけで作業を始めないこと**（CEFRカタログ2で、企画書未読のまま確定済み設計判断への揺り戻しが起きかけた実績あり）。
2. 必要なデータはこのリポジトリのraw URLから取得（例：`https://raw.githubusercontent.com/takahashihideki-git/CEFRCatalog/main/data/descriptors_en_1224.json`）。
3. 引き継ぎ書§4の周回計画の続きから再開。

## 復元検証値

- `descriptors_en_1224.json`: 1,224件、Noは `working_translations_1224.json` と完全一致
- `sieve_verdicts_265.json`: 判定265件、ADOPT 182／DROP 83
- `inventory_182to23.json`: ユニーク行為数 23
- `act_phases.json`: 二相行為2件を完全分割（重複なし）── 事実情報の授受30件（15＋15）／明確化・繰り返しの要求17件（3＋14）
- `cross_axes.json`: 行為分類23＝インベントリと一致、出自類型＝act_to_satypeと一致、下位系12、検証済8、二相接続型＝act_phasesと一致
- `prototypes_4types.json`: 4類型、各DISCUSSIONに5段落
- `block_partition_1224.json`: 全1,224件を7区分に完全分割（やり取り306＝採用182＋除外83＋対象外41／産出・談話構築132／受容197／仲介251／how well 182／方略104／複言語52）
