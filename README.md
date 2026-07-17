# CEFRカタログ

CEFR（ヨーロッパ言語共通参照枠）増補版2020の全能力記述文を、**発語内行為・受容・仲介の三カタログ＋横串のhow well**として再構造化し、日本の英語学習者に「CEFRの全貌」を具体とともに手渡すプロジェクト。株式会社トピックメーカー（enhack.app）。

このリポジトリは、生成AIとの探求セッション（スレッド「CEFRカタログ0, 1, …」）を横断して、設計判断・分析データ・成果物を共有するための単一情報源（single source of truth）。

## いまどこにいるか

- **グランドデザイン**：CEFRカタログ2で**四本柱＋横串へ補正**（発語内行為／産出・談話構築／受容／仲介＋how well。全1,224件の完全分割被覆を機械検証済み：`data/block_partition_1224.json`）
- **第0層：分析台帳**（全数集計・作業訳・言語行為論的篩・発語内行為インベントリ・区分分割）── 完成
- **第1層：カタログ** ── 四類型の範型作成済み。**周回方式**で進行中：**第1周（5検証）完了**・**第2周（横断判定5件）完了**（下位系12系が第一分類層／採用182）。**第3周進行中**：第3周-0（品質保証装置＝CEFR-J実例語彙チェッカー、判断(s)）と**第3周-1（意見表明の全数範型31行）完了** ── 好悪統合の三条件が成立し**「好悪の表明」を「意見・見解の表明」へ一行為二相（評価相＋対立管理相）として統合、23→22行為**（判断(t)、三例目の二相接続型）。次は**第3周-2：次行為の全数範型**
- **第2層：問題集**（カタログを種に生成AIが増殖させるインスタンス）── 未着手

詳細は `deliverables/CEFRカタログ_引き継ぎ書.md`（作業仕様書）と `deliverables/CEFR全貌カタログ_企画書.md`（グランドデザイン）を参照。

## ディレクトリ構成

```
data/          参照用の一次データ（JSON）
  descriptors_en_1224.json      No.→原文英語descriptor＋level＋scale＋scheme＋mode（音声言語1,224件）
  working_translations_1224.json No.→作業訳（自前・CoE許諾下・商用クリーン）
  inventory_182to22.json         採用182記述文→22発語内行為の写像
  act_to_satype.json             22行為→サール4類型
  act_phases.json                一行為二相の正準記録×3（事実情報の授受31＝質問応答相＋情報管理相／明確化・繰り返しの要求17＝理解表明相＋明確化要求相／意見・見解の表明31＝評価相＋対立管理相）
  cross_axes.json                横断軸の定義＋全22行為の下位系・梯子型・判定状態（第2周-4、第3周-1更新）
  sieve_verdicts_265.json        言語行為論的篩の判定（265件：ADOPT182/DROP83＋理由）
  block_partition_1224.json      全1,224件の区分分割（やり取り/産出・談話構築/受容/仲介/how well/方略/複言語）
prototypes/    第1カタログの範型と検証範型
  prototypes_4types.json         四類型の範型（全10列＋DISCUSSION）を統合したJSON
  catalog_opinion.json           第3周の全数シート第1号：意見・見解の表明31行（好悪統合済み）
  opinion_full_prototype.py      全数シートのソース（en/jpはdataから構築時取得）
  verification_expressive.json   周回検証で作成した検証範型の統合JSON（感謝詫び祝意/感情の表出）
  *_prototype.py                 各範型のソース（苦情/挨拶/事実Q&A/意見表明/感謝詫び祝意/感情）
analysis/      分析の生モジュール（監査・再実行用）
  ja_tr1〜9.py                   作業訳のソース
  verdicts.py                    篩判定のソース
  acts.py                        170→164個別行為タグ
  partition.py                   区分分割の生成・検証ソース（→ data/block_partition_1224.json）
tools/         品質保証ツール
  exponent_level_check.py        実例（exponent）語彙レベルチェッカー（CEFR-J照合、第3周-0）
  exponent_allowlist.txt         チェッカーの裁定保全ファイル（語＋理由）
deliverables/  成果物
  CEFR記述文_全数集計_実例付き.xlsx  12シートの分析台帳＋範型
  CEFR全貌カタログ_企画書.md          グランドデザイン（対外文書）
  CEFRカタログ_引き継ぎ書.md          作業仕様書（設計判断＋根拠＋次手順）
```

## 原典について（重要）

CEFR記述文の**原文テキスト**は `data/descriptors_en_1224.json` に収録済み（欧州評議会がCEFR記述文の再利用を出典明記のもとで許諾しているため）。**通常の作業ではこれで足り、原典xlsxのアップロードは不要**。

原典のExcelファイル `CEFR_Descriptors__2020_.xlsx` そのものは、CoEの配布ファイルであり本リポジトリには含めない。手話を含む全1,712件の再集計やxlsx実体処理など例外的な作業でのみ必要で、その際は欧州評議会公式（https://www.coe.int/en/web/common-european-framework-reference-languages ）から入手する。

**出典**: Council of Europe (2020), *Common European Framework of Reference for Languages: Learning, teaching, assessment – Companion volume*. 作業訳はトピックメーカーによる自前訳であり、ゲーテ・インスティトゥート東京の公式日本語版（2024）とは独立（照合のみに使用）。

## 語彙レベル照合データ（CEFR-J / Octanove）

実例（exponent）の語彙レベル検証（`tools/exponent_level_check.py`）には以下のデータセットを使用する。**CSVは本リポジトリに含めない**（Octanove分のCC BY-SAのSA義務をリポジトリに混入させないため）。リポジトリと**同階層**に clone して使う：

```
git clone https://github.com/openlanguageprofiles/olp-en-cefrj.git
```

（別の場所に置く場合は環境変数 `OLP_CEFRJ_DIR` で指定。）

**出典**:
- The CEFR-J Wordlist Version 1.5. Compiled by Yukio Tono, Tokyo University of Foreign Studies.（東京外国語大学 投野由紀夫研究室。出典明記のもと研究・商用利用可。 http://www.cefr-j.org/ ）
- The CEFR-J Grammar Profile Version 20180315.（同上。現時点では未使用・将来の文法レベル照合の候補）
- Octanove Vocabulary Profile C1/C2 (ver 1.0), Octanove Labs. CC BY-SA 4.0.
- 配布リポジトリ: Open Language Profiles https://github.com/openlanguageprofiles/olp-en-cefrj

## 開発体制（claude.aiスレッド ↔ Claude Code の循環）

```
リモートリポジトリ (GitHub)
   │  pull（clone / raw URL 参照）
   ▼
claude.ai「CEFRカタログn」スレッド
   │  分析・設計判断（Hidekiと合意）・生成・検証
   │  成果は 申し送り_ClaudeCode.md＋パッチ＋更新ファイル として download
   ▼
Claude Code on Hideki local PC（ローカルリポジトリ）
   │  申し送りに従って適用 → 検証（restore.py ほか）→ commit → push
   ▼
リモートリポジトリ ──（次スレッドが pull して再開）
```

- **claude.aiスレッドはリポジトリへ直接pushしない**。変更は必ずパッチセット（申し送り＋diff＋必要に応じ更新ファイル実体）として渡す。
- **Claude Code が適用・検証・コミットを担う**。適用後の検証は `python3 restore.py`（第3周-0以降は `python3 tools/exponent_level_check.py` の実行確認を含む）。
- 設計判断はスレッド側で合意してから実装する（confirm → agree → edit → verify → output）。判断と根拠は引き継ぎ書§2に、周回の進捗はREADME「いまどこにいるか」と引き継ぎ書§1に反映する。

## 新スレッドでの再開手順

1. **必読2文書を必ずこの順で読む**：`deliverables/CEFR全貌カタログ_企画書.md`（グランドデザイン＝何を作るか）→ `deliverables/CEFRカタログ_引き継ぎ書.md`（作業仕様＝どう作り続けるか）。**引き継ぎ書だけで作業を始めないこと**（CEFRカタログ2で、企画書未読のまま確定済み設計判断への揺り戻しが起きかけた実績あり）。
2. 必要なデータはこのリポジトリのraw URLから取得（例：`https://raw.githubusercontent.com/takahashihideki-git/CEFRCatalog/main/data/descriptors_en_1224.json`）。
3. 引き継ぎ書§4の周回計画の続きから再開。

## 復元検証値

- `descriptors_en_1224.json`: 1,224件、Noは `working_translations_1224.json` と完全一致
- `sieve_verdicts_265.json`: 判定265件、ADOPT 182／DROP 83
- `inventory_182to22.json`: ユニーク行為数 22
- `act_phases.json`: 二相行為3件を完全分割（重複なし）── 事実情報の授受31件（15＋16）／明確化・繰り返しの要求17件（3＋14）／意見・見解の表明31件（4＋27）
- `cross_axes.json`: 行為分類22＝インベントリと一致、出自類型＝act_to_satypeと一致、下位系12、検証済8、二相接続型3＝act_phasesと一致
- `prototypes_4types.json`: 4類型、各DISCUSSIONに5段落
- `catalog_opinion.json`: 31行（口頭23＋書面8）、全行の原文・レベル・訳・行為所属を照合、DISCUSSION 5段落
- `block_partition_1224.json`: 全1,224件を7区分に完全分割（やり取り306＝採用182＋除外83＋対象外41／産出・談話構築132／受容197／仲介251／how well 182／方略104／複言語52）
