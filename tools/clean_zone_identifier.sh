#!/usr/bin/env bash
# WSLでWindows側からコピーしたファイルに付く ADS メタデータ（*:Zone.Identifier）を再帰的に削除する。
# 使い方:
#   tools/clean_zone_identifier.sh [対象ディレクトリ] [-n|--dry-run]
#   （対象ディレクトリ省略時はリポジトリルート）
set -euo pipefail

target="."
dry_run=0
for arg in "$@"; do
  case "$arg" in
    -n|--dry-run) dry_run=1 ;;
    -h|--help) sed -n '2,5p' "$0"; exit 0 ;;
    *) target="$arg" ;;
  esac
done

[ -d "$target" ] || { echo "ディレクトリがありません: $target" >&2; exit 1; }

# ':Zone.Identifier' で終わるものだけを対象にする（Identifier.py のような正規ファイルを巻き込まないため）。
mapfile -d '' -t files < <(find "$target" -type f -name '*:Zone.Identifier' -print0)

if [ ${#files[@]} -eq 0 ]; then
  echo "対象なし（$target）"
  exit 0
fi

for f in "${files[@]}"; do
  if [ "$dry_run" -eq 1 ]; then
    echo "[dry-run] $f"
  else
    rm -- "$f"
    echo "削除: $f"
  fi
done

echo "${#files[@]} 件$([ "$dry_run" -eq 1 ] && echo "（dry-run、未削除）" || echo "を削除")"
