#!/usr/bin/env python3
"""
_sidebar.md 자동 생성 스크립트.
저장소 폴더 구조를 순회하여 docsify용 사이드바를 생성합니다.
"""

import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

IGNORE_DIRS = {'.git', '.github', 'scripts', '__pycache__', 'node_modules', 'drafts', 'images', 'image'}
IGNORE_FILES = {'.nojekyll', '.gitignore', '.gitattributes'}

CATEGORY_ICONS = {
    'kosa': '📚',
    '리눅스': '🐧',
    '메모': '📝',
    '배움터': '🎓',
    '자바': '☕',
    '코딩테스트': '💻',
}


def encode_path(path: Path) -> str:
    """루트 기준 상대 경로를 URL 인코딩합니다."""
    rel = path.relative_to(ROOT)
    parts = [urllib.parse.quote(str(p), safe='') for p in rel.parts]
    return '/' + '/'.join(parts)


def clean_title(name: str) -> str:
    """파일명을 사람이 읽기 좋은 제목으로 변환합니다. 날짜 접두사는 [YYYY-MM-DD] 형식으로 표시합니다."""
    # YYYY_MM_DD_ 패턴
    m = re.match(r'^(\d{4}_\d{2}_\d{2})[_.]?(.*)$', name)
    if m:
        date = m.group(1).replace('_', '-')
        rest = m.group(2).strip('_').strip()
        return f'[{date}] {rest}' if rest else date
    # YYYYMMDD_ 패턴
    m2 = re.match(r'^(\d{8})_?(.*)$', name)
    if m2:
        d = m2.group(1)
        date = f'{d[:4]}-{d[4:6]}-{d[6:8]}'
        rest = m2.group(2).strip('_').strip()
        return f'[{date}] {rest}' if rest else date
    return name


def has_markdown(path: Path) -> bool:
    """디렉터리에 마크다운 파일이 하나 이상 있는지 확인합니다."""
    for item in path.rglob('*.md'):
        if not any(p in IGNORE_DIRS for p in item.parts):
            return True
    return False


def process_dir(path: Path, depth: int, lines: list):
    """디렉터리를 재귀적으로 처리하여 사이드바 항목을 생성합니다."""
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        return

    for item in items:
        if item.name in IGNORE_DIRS or item.name in IGNORE_FILES:
            continue
        if item.name.startswith('.'):
            continue

        indent = '  ' * depth

        if item.is_dir():
            if not has_markdown(item):
                continue
            lines.append(f"{indent}* **{item.name}**")
            process_dir(item, depth + 1, lines)

        elif item.is_file() and item.suffix.lower() == '.md':
            title = clean_title(item.stem)
            enc = encode_path(item.with_suffix(''))
            lines.append(f"{indent}* [{title}]({enc})")


def generate_sidebar():
    lines = ['* [🏠 홈](/)\n']

    top_level = sorted(
        [d for d in ROOT.iterdir()
         if d.is_dir() and d.name not in IGNORE_DIRS and not d.name.startswith('.')],
        key=lambda x: x.name.lower()
    )

    for category in top_level:
        icon = CATEGORY_ICONS.get(category.name, '📁')
        lines.append(f"* **{icon} {category.name}**")
        process_dir(category, 1, lines)
        lines.append('')

    sidebar_path = ROOT / '_sidebar.md'
    sidebar_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✅ 사이드바 생성 완료: {sidebar_path}")


if __name__ == '__main__':
    generate_sidebar()
