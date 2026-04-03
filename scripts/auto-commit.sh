#!/usr/bin/env bash
# auto-commit.sh
#
# YYYYMMDD 형식의 날짜 폴더를 탐색하여 해당 날짜로 백데이트된 커밋을 자동 생성합니다.
#
# 사용법:
#   bash scripts/auto-commit.sh          # 모든 날짜 폴더 처리
#   bash scripts/auto-commit.sh --push   # 처리 후 git push 실행
#
# 예시 폴더 구조:
#   코딩테스트/20250102/문제풀이.md
#   자바/20250103/학습정리.md

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PUSH=false
if [[ "${1:-}" == "--push" ]]; then
  PUSH=true
fi

COMMITTED=0

# YYYYMMDD 형식의 폴더를 모두 탐색 (8자리 숫자 폴더명)
while IFS= read -r -d '' dir; do
  FOLDER_NAME="$(basename "$dir")"

  if [[ "$FOLDER_NAME" =~ ^([0-9]{4})([0-9]{2})([0-9]{2})$ ]]; then
    YEAR="${BASH_REMATCH[1]}"
    MONTH="${BASH_REMATCH[2]}"
    DAY="${BASH_REMATCH[3]}"
    DATE="${YEAR}-${MONTH}-${DAY}"
    COMMIT_DATE="${DATE}T00:00:00+09:00"

    # 해당 폴더 내 변경사항 스테이징
    git add "$dir"

    # 스테이징된 변경사항이 있는지 확인
    if git diff --cached --quiet; then
      echo "⏭️  변경 없음: $dir"
      continue
    fi

    echo "📅 커밋 생성: $dir (날짜: $DATE)"
    GIT_AUTHOR_DATE="$COMMIT_DATE" \
    GIT_COMMITTER_DATE="$COMMIT_DATE" \
      git commit -m "📅 ${DATE} 학습 내용 추가

폴더: ${dir#"$ROOT/"}"
    COMMITTED=$((COMMITTED + 1))
  fi
done < <(find . -not -path "./.git/*" -type d -name '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' -print0 | sort -z)

if [[ $COMMITTED -eq 0 ]]; then
  echo "✅ 커밋할 변경사항이 없습니다."
else
  echo "✅ ${COMMITTED}개의 커밋이 생성되었습니다."
  if $PUSH; then
    echo "🚀 원격 저장소에 푸시합니다..."
    git push
  else
    echo "💡 원격 저장소에 푸시하려면 'git push' 또는 '--push' 옵션을 사용하세요."
  fi
fi
