# 📋 초안 (Drafts)

이 폴더는 날짜별로 발행 예약된 학습 내용을 보관합니다.

## 사용 방법

### 폴더 구조

```
drafts/
  YYYYMMDD/
    카테고리명/
      파일.md
```

### 예시

```
drafts/
  20250102/
    코딩테스트/
      문제풀이.md
    자바/
      학습정리.md
```

### 동작 방식

1. `drafts/20250102/` 폴더를 생성하고 내용 작성
2. `main` 브랜치에 커밋 & 푸시
3. **2025년 1월 2일 자정(KST)** 에 GitHub Actions가 자동으로:
   - `코딩테스트/` 폴더로 파일 이동
   - `자바/` 폴더로 파일 이동
   - 사이드바(`_sidebar.md`) 자동 업데이트
   - 커밋 메시지: `📅 2025-01-02 학습 내용 자동 발행`

### 즉시 발행

GitHub Actions → **날짜별 자동 발행** → **Run workflow** → 날짜 입력

### 로컬에서 백데이트 커밋

```bash
bash scripts/auto-commit.sh         # 날짜 폴더 기반 백데이트 커밋
bash scripts/auto-commit.sh --push  # 커밋 후 자동 푸시
```
