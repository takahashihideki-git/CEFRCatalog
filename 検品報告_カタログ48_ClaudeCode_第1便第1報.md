# 検品報告 ── CEFRカタログ48 第1便 第1報（Claude Code）

対象：`catalog48_1.diff`（基底 `c952371`、9ファイル）。受け取り経路＝Artifact（申し送り・パッチ・精読用の3ファイル）。こちらの HEAD は基底の2コミット先（`.gitignore`・`gatekeeper/` のみ）で、`git apply --check` は通った。

## 検証

- `restore.py`・`analysis/partition.py`・`tools/source_sync_check.py`（全数シート43枚を照合、既知の警告3件）・`tools/book_style_check.py` すべて green
- **破壊テストの再現**（1種）：深さの要点⇄全体で 844⇄845 を等数交換 → `p4 テキストをまとめて伝える（書面）の要点・全体の段が帳簿と不一致` で落ち、復元後 green・JSON はバイト一致
- **レベル帯の照合**（観点③、正準 `descriptors_en_1224.json` で引いた）：条件の区分の級順／「条件なしがB2+で始まり、C1に用語の但し書きが一つ戻る」／A1〜B1の各級に原文の言葉を運ぶ段と自分の言葉の段が一つずつ（851/850・849/848・847/846・845/844）／級の割れる三対（840 B2+↔815 B2、841 B2+↔812 C1、836 C2↔815 B2＝三つ上）／Language A／B を持たない段＝836・845・847・849・851 の五つ ── すべて一致
- **限定句の保存**（観点⑥、抜き取り）：844 の但し書き *provided oral texts are clearly articulated* は scene・delta・D2 に、838 の *for a specific audience, respecting the style and register* は howwell・delta に残っている
- **語彙チェッカー**：CEFR-J データを置いて実行した（監査 1074→1091文、超過 48→52文、未収録 26→32文）。新規分は下の2

## 1. 要修正（小）── README「開発体制」の全数シート数の追随漏れ

`README.md:134`（開発体制、`source_sync_check.py` の照合対象の説明）が「全数シート42枚〔第1柱22＋第2柱7＋第3柱11＋第4柱2〕」のまま。正しくは **43枚〔…＋第4柱3〕**（`source_sync_check.py` 自身が「全数シート 43枚を照合」と出す）。CLAUDE.md の散文追随チェックリストで「ツールの照合対象を説明した散文」として名指しされている箇所。パッチは同じ数を CLAUDE.md・README の復元検証値・軸台帳・引き継ぎ書§4 で追随させているが、ここだけ漏れた。

## 2. 要判定 ── 語彙チェッカーの新規フラグ（10文）

**超過（4文）**

| No. | 級 | 語 | 出る場所 | 所見 |
|---|---|---|---|---|
| 843 | B1+ | secondary(B2)・attendance(B2) | You 行（学習者が書いた要約） | 学習者の出力に B2 の語が二つ。書き換え候補（*secondary schools*→*high schools* か *schools*、*better attendance*→*students miss fewer days* 等） |
| 851 | A1 | centre(A2)×2 | 入力の掲示と You 行（書き写し） | 書き写す段なので、語を知らなくても形は運べる。allowlist か入力の差し替えかは判断を |
| 846 | A2+ | main(B1)×2 | 入力と You 行（*main gate*） | 拾って書き出す段。同上 |
| 847 | A2+ | per(B1) | 入力だけ（*Printing 10p per page*。You 行は落としている） | 入力の語。同上 |

**未収録（6文）**

- 略記・大文字：*english*（849）・*fri*（846）・*mon*（847）── 既存の口頭シート No.830 の *mon* と同じ扱いで、基底フラグとして残っている型
- 上の級の語：*outright*・*unfunded*（841、B2+）・*enforcement*（837、C1）・*untested*（838、C1）── allowlist 候補。申し送りの候補 *novelty*（840）と *assembled*（835）は CEFR-J 側で拾えたのでフラグにならず、*unfunded* だけが出た

## 参考（指摘ではない）

- README ディレクトリ構成の新行が「Language A＝B＝英語」と書いている。No.850 の例文（英語の入力を辞書で読む）とあわせて、判断(cx) の遡及（申し送り§4・引き継ぎ書§7「第1便の再提出と第2便」）で直る見込みと読んだ。再提出のときに、この行も対象に入っているかだけ確かめてほしい
- 再提出が同じ基底のフルパッチで来れば、こちらは差し替えの手順（worktree で増分を作る）で受ける
