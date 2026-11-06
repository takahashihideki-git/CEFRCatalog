# 検品係（Claude Code）の作業ノート

CLAUDE.md の後半（「成果物の受け取りと統合」以降）を、どのマシンでも同じに引けるように補うノート。CLAUDE.md が正で、ここには CLAUDE.md に書いていない細部と、現在地だけを置く。執筆スレッドは読まなくてよい。

## 読む順

1. `CLAUDE.md`（全文。前半は両者の規律、後半が検品係の作業）
2. [current-state.md](current-state.md) ── いまどのカタログのどの便まで統合したか。次に何が来るか
3. 届いたものに応じて
   - パッチの受け取り → [receiving-notes.md](receiving-notes.md)
   - 書物層（`deliverables/book/`）の章・肖像の受け取り → [book-inspection-recipe.md](book-inspection-recipe.md)
   - セッションのクローズ → [roadmap-measure.md](roadmap-measure.md)

## 書き足す場所

検品で得た教訓や現在地の更新は、**このディレクトリに書いてコミットする**。Claude Code のOSローカルの自動メモリ（`~/.claude/projects/<パス>/memory/`）には書かない ── そこはマシンごと・パスごとに別物で、別の機械からは見えない。

- 現在地は current-state.md の先頭の節を書き換える。履歴は残す必要がない（正準の履歴は README「いまどこ」と引き継ぎ書§1・§2にある）
- 教訓は、どの手順で使うかで receiving-notes.md か book-inspection-recipe.md の「教訓」に一行で足す。CLAUDE.md に昇格させる価値があるものは、CLAUDE.md の後半へ書き、ここからは消す（二重管理にしない）

## 新しいマシンでの準備

- `python3`（3.9以上。外部パッケージは不要）
- CEFR-J データ：`tools/exponent_level_check.py` が参照する。リポジトリと同じ階層に `git clone https://github.com/openlanguageprofiles/olp-en-cefrj.git` するか、環境変数 `OLP_CEFRJ_DIR` で場所を渡す。これがないと語彙チェッカーだけ回らない（実際にMacで「未検証」になった例がある）
- 原典xlsx・ゲーテ版PDFは不要（CLAUDE.md「原典ファイルはコミットしない」）
- 増補版（Companion Volume）PDF：英語版 `CEFR Companion Volume_eng.pdf`・日本語版 `cefr-cv-jap-*.pdf` をリポジトリ直下に置いてよい（どちらも `.gitignore` 済み）。執筆スレッドから原文の引用を頼まれたときに使う。抽出は PyMuPDF（`import fitz`、ユーザーsite にあるので `python3 -I` では読めない）。日本語版の抽出テキストは漢字が化ける（「泺動」等）ので、ページの対応を取るだけにして、引用は画面で確かめてもらう。英語版は印刷ページ＝PDFページ、日本語版は印刷ページ＋20＝PDFページ
- Artifact版ロードマップの再発行には、同じ claude.ai アカウントでログインしていること（roadmap-measure.md）
