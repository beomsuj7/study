#!/usr/bin/env python3
"""
MD 파일 양식 통일 스크립트
- YAML frontmatter 추가
- 일반 텍스트를 감싼 불필요한 코드블록 제거
- 헤딩 레벨 정리
"""
import os
import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\noah.b.jeong\Desktop\Projects\Tests\study")

# 건너뛸 파일들
SKIP_FILES = {
    "README.md",
    "_sidebar.md",
}

# 건너뛸 경로 패턴 (이미 양식이 적용된 예시 파일 등)
SKIP_PATH_PATTERNS = [
    "drafts/20260403",
    "images/",
    "scripts/",
]

# 카테고리 매핑 (폴더 경로 -> 카테고리명)
CATEGORY_MAP = {
    "kosa/Kosa정리": "KOSA수업",
    "kosa/Kosa수업": "KOSA수업",
    "리눅스": "리눅스",
    "메모": "메모",
    "배움터": "배움터",
    "자바/점프투자바 정리": "자바",
    "자바/코드정리": "자바",
    "자바": "자바",
    "코딩테스트/자바 코딩테스트": "코딩테스트",
    "코딩테스트/파이썬 코딩테스트": "코딩테스트",
    "코딩테스트": "코딩테스트",
    "drafts": "초안",
}

# 파일명에서 태그 추출하기 위한 키워드 매핑
TAG_KEYWORDS = {
    "sql": "SQL",
    "mysql": "MySQL",
    "javafx": "JavaFX",
    "mvc": "MVC",
    "mybatis": "MyBatis",
    "javascript": "JavaScript",
    "jquery": "jQuery",
    "ajax": "AJAX",
    "vue": "Vue.js",
    "servlet": "Servlet",
    "maven": "Maven",
    "jsp": "JSP",
    "spring": "Spring",
    "python": "Python",
    "docker": "Docker",
    "aws": "AWS",
    "정규화": "정규화",
    "정규식": "정규식",
    "코딩테스트": "코딩테스트",
    "객체지향": "객체지향",
    "다형성": "다형성",
    "추상클래스": "추상클래스",
    "인터페이스": "인터페이스",
    "생성자": "생성자",
    "메서드": "메서드",
    "클래스": "클래스",
    "변수": "변수",
    "제어문": "제어문",
    "포매팅": "포매팅",
    "쓰레드": "쓰레드",
    "예외처리": "예외처리",
    "스태틱": "스태틱",
    "파일입출력": "파일입출력",
    "접근제어자": "접근제어자",
    "패키지": "패키지",
    "함수형": "함수형프로그래밍",
    "제네릭": "제네릭",
}

# 카테고리별 기본 태그
CATEGORY_DEFAULT_TAGS = {
    "KOSA수업": ["KOSA"],
    "리눅스": ["Linux"],
    "메모": ["메모"],
    "배움터": ["학습"],
    "자바": ["Java"],
    "코딩테스트": ["코딩테스트"],
}


def should_skip(filepath: Path) -> bool:
    """파일을 건너뛸지 결정"""
    if filepath.name in SKIP_FILES:
        return True
    rel = filepath.relative_to(BASE_DIR).as_posix()
    for pattern in SKIP_PATH_PATTERNS:
        if pattern in rel:
            return True
    return False


def get_category(filepath: Path) -> str:
    """파일 경로에서 카테고리 추출"""
    rel = filepath.relative_to(BASE_DIR).as_posix()
    # 가장 긴 매칭부터 확인
    sorted_keys = sorted(CATEGORY_MAP.keys(), key=len, reverse=True)
    for key in sorted_keys:
        if rel.startswith(key):
            return CATEGORY_MAP[key]
    return "기타"


def extract_date(filename: str) -> str:
    """파일명에서 날짜 추출 (YYYY_MM_DD 또는 YYYYMMDD 형태)"""
    # 2022_12_20 형태
    m = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    # 20221220 형태
    m = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    # _231206 형태
    m = re.search(r'_(\d{2})(\d{2})(\d{2})', filename)
    if m:
        return f"20{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return ""


def extract_tags(filename: str, content: str, category: str) -> list:
    """파일명과 내용에서 태그 추출"""
    tags = set()
    
    # 카테고리 기본 태그
    if category in CATEGORY_DEFAULT_TAGS:
        tags.update(CATEGORY_DEFAULT_TAGS[category])
    
    # 파일명에서 태그 추출
    fname_lower = filename.lower()
    for keyword, tag in TAG_KEYWORDS.items():
        if keyword.lower() in fname_lower:
            tags.add(tag)
    
    # 내용 첫 500자에서 키워드 태그 검색 (보조)
    content_snippet = content[:500].lower()
    for keyword, tag in TAG_KEYWORDS.items():
        if keyword.lower() in content_snippet and tag not in tags:
            # 내용에서 발견된 태그는 좀 더 보수적으로 추가
            if len(tags) < 5:
                tags.add(tag)
    
    return sorted(list(tags))


def extract_title(filename: str, content: str) -> str:
    """파일명과 내용에서 제목 추출"""
    # 먼저 내용에서 첫 번째 H1 제목 시도
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        # 제목이 너무 짧거나 의미없는 경우 파일명 사용
        if len(title) > 1:
            return title
    
    # 파일명에서 제목 생성
    name = filename.replace('.md', '')
    # 날짜 부분 제거
    name = re.sub(r'^\d{4}_\d{2}_\d{2}_?', '', name)
    name = re.sub(r'^\d{8}_?', '', name)
    # 언더스코어를 공백으로
    name = name.replace('_', ' ').strip()
    if name:
        return name
    return filename.replace('.md', '')


def has_frontmatter(content: str) -> bool:
    """이미 YAML frontmatter가 있는지 확인"""
    return content.startswith('---\n')


def clean_code_blocks(content: str) -> str:
    """일반 텍스트를 감싼 불필요한 코드블록 제거
    
    규칙:
    - ```java, ```python, ```sql 등 언어가 지정된 코드블록은 유지
    - ``` (언어 없음) 안의 내용이 실제 코드가 아니라 일반 텍스트면 제거
    """
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 코드블록 시작 감지
        if stripped.startswith('```'):
            lang = stripped[3:].strip().lower()
            
            # 언어가 지정된 코드블록은 항상 유지
            code_langs = ['java', 'python', 'sql', 'javascript', 'js', 'html', 'css',
                         'bash', 'sh', 'json', 'xml', 'yaml', 'yml', 'docker',
                         'dockerfile', 'c', 'cpp', 'typescript', 'ts', 'ruby',
                         'go', 'rust', 'php', 'swift', 'kotlin', 'scala',
                         'jsx', 'tsx', 'vue', 'scss', 'less', 'markdown', 'md',
                         'powershell', 'ps1', 'cmd', 'bat', 'nginx', 'conf',
                         'properties', 'ini', 'toml', 'groovy', 'gradle']
            
            # 코드블록 내용 수집
            block_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('```'):
                block_lines.append(lines[j])
                j += 1
            
            if lang and any(lang.startswith(cl) for cl in code_langs):
                # 언어 지정된 코드블록 → 유지
                result.append(line)
                i += 1
                continue
            
            if lang and lang.startswith('java') and '(' in lang:
                # ```Java (VO생성) 같은 특수 케이스
                result.append('```java')
                i += 1
                continue
            
            block_content = '\n'.join(block_lines)
            
            # 코드인지 텍스트인지 판별
            if is_likely_code(block_content):
                # 코드블록 유지하되 언어 추론 시도
                guessed_lang = guess_language(block_content)
                if guessed_lang and not lang:
                    result.append(f'```{guessed_lang}')
                else:
                    result.append(line)
                i += 1
                continue
            else:
                # 일반 텍스트 → 코드블록 제거하고 텍스트만 출력
                for bl in block_lines:
                    result.append(bl)
                # 닫는 ``` 건너뛰기
                i = j + 1 if j < len(lines) else j
                continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)


def is_likely_code(text: str) -> bool:
    """텍스트가 코드인지 일반 텍스트인지 판별"""
    if not text.strip():
        return False
    
    lines = text.strip().split('\n')
    
    # 코드 패턴 점수
    code_indicators = 0
    text_indicators = 0
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # 코드 패턴들
        if re.search(r'[{};]$', stripped):
            code_indicators += 2
        if re.search(r'^(import |from |package |public |private |protected |class |def |function |var |let |const |if\s*\(|for\s*\(|while\s*\(|return |SELECT |INSERT |UPDATE |DELETE |CREATE |DROP |ALTER )', stripped):
            code_indicators += 3
        if re.search(r'^\s*(//|#|/\*|\*)', stripped):
            code_indicators += 1
        if re.search(r'[=<>!]+', stripped) and re.search(r'[a-zA-Z_]\w*\s*[=<>!]', stripped):
            code_indicators += 1
        if re.search(r'\.\w+\(', stripped):
            code_indicators += 1
        if re.search(r'^\s*\w+\s*=\s*', stripped):
            code_indicators += 1
        
        # docker/config 명령어 패턴
        if re.search(r'^(FROM|RUN|COPY|CMD|EXPOSE|WORKDIR|ENV|ARG|ENTRYPOINT)\s', stripped):
            code_indicators += 3
        if re.search(r'^(docker|npm|pip|conda|git|curl|wget|sudo|apt|yum)\s', stripped):
            code_indicators += 2
        
        # 텍스트 패턴들 (한글이 많으면 텍스트)
        korean_chars = len(re.findall(r'[가-힣]', stripped))
        total_chars = len(stripped)
        if total_chars > 0 and korean_chars / total_chars > 0.3:
            text_indicators += 2
        
        # 마침표로 끝나는 문장 (한글)
        if re.search(r'[가-힣][.다]$', stripped):
            text_indicators += 1
    
    return code_indicators > text_indicators


def guess_language(text: str) -> str:
    """코드의 언어를 추측"""
    if re.search(r'(public\s+class|System\.out|String\[\]|void\s+main)', text):
        return 'java'
    if re.search(r'(def\s+\w+|import\s+\w+|print\(|>>>)', text):
        return 'python'
    if re.search(r'(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE|ALTER\s+TABLE)', text, re.IGNORECASE):
        return 'sql'
    if re.search(r'(function\s|var\s|let\s|const\s|document\.|console\.)', text):
        return 'javascript'
    if re.search(r'(FROM\s+\w+|RUN\s|COPY\s|CMD\s|EXPOSE\s)', text):
        return 'dockerfile'
    if re.search(r'(docker\s|npm\s|pip\s|conda\s|git\s)', text):
        return 'bash'
    return ''


def generate_summary(title: str, content: str) -> str:
    """첫 번째 문단에서 요약문 생성"""
    # 본문에서 첫 의미있는 텍스트 줄 찾기
    lines = content.split('\n')
    for line in lines:
        stripped = line.strip()
        # 헤딩, 빈줄, 코드블록, 이미지 건너뛰기
        if not stripped or stripped.startswith('#') or stripped.startswith('```') or stripped.startswith('![') or stripped.startswith('---') or stripped.startswith('>'):
            continue
        # 이미 blockquote인 경우 건너뛰기
        if stripped.startswith('>'):
            continue
        # 짧은 설명문이면 사용
        if len(stripped) > 5 and len(stripped) < 200:
            # HTML 태그 제거
            clean = re.sub(r'<[^>]+>', '', stripped)
            if clean:
                return clean[:100]
    return f"{title} 학습 내용 정리"


def process_file(filepath: Path) -> bool:
    """단일 MD 파일 처리"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  [ERROR] 읽기 실패: {e}")
        return False
    
    # 이미 frontmatter가 있으면 건너뛰기
    if has_frontmatter(content):
        print(f"  [SKIP] 이미 frontmatter 있음")
        return False
    
    # 빈 파일 처리
    if not content.strip():
        title = filepath.stem.replace('_', ' ')
        date = extract_date(filepath.name)
        category = get_category(filepath)
        tags = extract_tags(filepath.name, '', category)
        
        frontmatter = f"""---
title: "{title}"
date: {date if date else ''}
category: "{category}"
tags: [{', '.join(tags)}]
---

# {title}

> {title} 내용을 작성해주세요

---
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
        return True
    
    # 메타데이터 추출
    title = extract_title(filepath.name, content)
    date = extract_date(filepath.name)
    category = get_category(filepath)
    tags = extract_tags(filepath.name, content, category)
    summary = generate_summary(title, content)
    
    # 코드블록 정리
    cleaned_content = clean_code_blocks(content)
    
    # 기존 H1 제목 제거 (frontmatter에서 관리)
    # 첫 번째 H1만 제거
    cleaned_lines = cleaned_content.split('\n')
    new_lines = []
    h1_removed = False
    for line in cleaned_lines:
        if not h1_removed and re.match(r'^#\s+', line) and not re.match(r'^##', line):
            h1_removed = True
            continue
        new_lines.append(line)
    
    # 선두 빈줄 제거
    while new_lines and not new_lines[0].strip():
        new_lines.pop(0)
    
    body = '\n'.join(new_lines)
    
    # frontmatter + 구조화된 내용 생성
    tags_str = ', '.join(tags)
    frontmatter = f"""---
title: "{title}"
date: {date if date else ''}
category: "{category}"
tags: [{tags_str}]
---

# {title}

> {summary}

---

"""
    
    final_content = frontmatter + body
    
    # 연속 빈줄 3개 이상 → 2개로 정리
    final_content = re.sub(r'\n{4,}', '\n\n\n', final_content)
    
    # 파일 끝 줄바꿈 정리
    final_content = final_content.rstrip() + '\n'
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        return True
    except Exception as e:
        print(f"  [ERROR] 쓰기 실패: {e}")
        return False


def update_sidebar():
    """사이드바에 예시 폴더 추가"""
    sidebar_path = BASE_DIR / "_sidebar.md"
    with open(sidebar_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 예시 폴더가 이미 있는지 확인
    if '예시' in content or '20260403' in content:
        return
    
    # 사이드바 끝에 예시 섹션 추가
    example_section = """
* **📌 예시 (drafts)**
  * **20260403**
    * [예시_문제풀이](/drafts/20260403/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/%EC%98%88%EC%8B%9C_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4)
    * [예시_스트림API_정리](/drafts/20260403/%EC%9E%90%EB%B0%94/%EC%98%88%EC%8B%9C_%EC%8A%A4%ED%8A%B8%EB%A6%BCAPI_%EC%A0%95%EB%A6%AC)
"""
    content = content.rstrip() + '\n' + example_section
    
    with open(sidebar_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    print("=" * 60)
    print("📝 MD 파일 양식 통일 스크립트")
    print("=" * 60)
    
    # 모든 MD 파일 수집
    md_files = []
    for filepath in BASE_DIR.rglob('*.md'):
        if should_skip(filepath):
            continue
        # 이미지 폴더 내 파일 제외
        if 'images' in filepath.parts:
            continue
        md_files.append(filepath)
    
    print(f"\n📂 처리 대상: {len(md_files)}개 파일\n")
    
    success = 0
    skipped = 0
    failed = 0
    
    for filepath in sorted(md_files):
        rel = filepath.relative_to(BASE_DIR).as_posix()
        print(f"[처리중] {rel}")
        result = process_file(filepath)
        if result:
            success += 1
            print(f"  ✅ 완료")
        elif result is False:
            skipped += 1
        else:
            failed += 1
    
    # 사이드바 업데이트
    print("\n[사이드바] 업데이트 중...")
    update_sidebar()
    print("  ✅ 사이드바 업데이트 완료")
    
    print(f"\n{'=' * 60}")
    print(f"📊 결과: 성공 {success} | 건너뜀 {skipped} | 실패 {failed}")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
