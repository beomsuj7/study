#!/usr/bin/env python3
"""
_sidebar.md 자동 생성 스크립트.
마크다운 파일을 분석하여 사이드바에 연도/월별, 언어/기술별, 그리고 기존 폴더 구조별 트리를 생성합니다.
"""

import re
import urllib.parse
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent

IGNORE_DIRS = {'.git', '.github', 'scripts', '__pycache__', 'node_modules', 'drafts', 'images', 'image'}
IGNORE_FILES = {'_sidebar.md', 'README.md', '.nojekyll', '.gitignore', '.gitattributes'}

KNOWN_TAGS = {
    'java', 'python', 'c++', 'spring', 'mybatis', 'mysql', 'h2', 'sql', 'javascript', 
    'jquery', 'vue', 'ajax', 'servlet', 'maven', 'jsp', 'docker', 'linux', 'aws', 'html', 'css',
    'javafx', 'mvc'
}

def encode_path(path: Path) -> str:
    """루트 기준 상대 경로를 URL 인코딩합니다."""
    rel = path.relative_to(ROOT)
    parts = [urllib.parse.quote(str(p), safe='') for p in rel.parts]
    return '/' + '/'.join(parts)

def clean_title(name: str) -> str:
    # 2022_12_29_MVC => [2022-12-29] MVC
    m = re.match(r'^(\d{4}_\d{2}_\d{2})[_.]?(.*)$', name)
    if m:
        date = m.group(1).replace('_', '-')
        rest = m.group(2).strip('_').strip()
        return f'[{date}] {rest}' if rest else date
    m2 = re.match(r'^(\d{8})_?(.*)$', name)
    if m2:
        d = m2.group(1)
        date = f'{d[:4]}-{d[4:6]}-{d[6:8]}'
        rest = m2.group(2).strip('_').strip()
        return f'[{date}] {rest}' if rest else date
    return name

def extract_meta(path: Path):
    year, month = None, None
    tags = set()

    # 1. 파일명에서 날짜 추출
    name = path.name
    m = re.match(r'^(\d{4})_(\d{2})_\d{2}', name)
    if m:
        year, month = m.group(1), m.group(2)
    else:
        m2 = re.search(r'_(\d{2})(\d{2})\d{2}', name)
        if m2 and 'AWS' in name:
            year, month = "20" + m2.group(1), m2.group(2)

    # 2. 경로 및 파일명에서 자동 태그 추출
    search_text = str(path.relative_to(ROOT)).lower()
    for t in KNOWN_TAGS:
        if t in search_text:
            if t == 'java' and 'javascript' in search_text and '/java/' not in search_text and 'java_' not in search_text:
                continue
            tags.add(t)

    # 3. 마크다운 Frontmatter에서 tags: [커스텀] 추출
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
        if content.startswith('---'):
            fm_end = content.find('---', 3)
            if fm_end != -1:
                fm_text = content[3:fm_end]
                for line in fm_text.splitlines():
                    if line.strip().startswith('tags:'):
                        raw = line.split(':', 1)[1].strip()
                        raw = raw.strip('[]').replace('"', '').replace("'", "")
                        for t_raw in raw.split(','):
                            if t_raw.strip():
                                tags.add(t_raw.strip().lower())
    except:
        pass

    return year, month, tags

def generate_sidebar():
    md_files = []
    for item in sorted(ROOT.rglob('*.md')):
        if any(p in IGNORE_DIRS for p in item.parts): continue
        if item.name in IGNORE_FILES: continue
        md_files.append(item)

    by_date = defaultdict(lambda: defaultdict(list))
    by_tag = defaultdict(list)

    for item in md_files:
        y, m, tags = extract_meta(item)
        info = (item, clean_title(item.stem), encode_path(item.with_suffix('')))
        
        if y and m: by_date[y][m].append(info)
        else: by_date['미분류'][''].append(info)

        if not tags: by_tag['기타'].append(info)
        for t in tags: by_tag[t.capitalize()].append(info)

    lines = ['* [🏠 홈](/)', '']

    # 1. 📅 작성 연도별
    lines.append('* **📅 작성 연도별**')
    for y in sorted(by_date.keys(), reverse=True):
        if y == '미분류': continue
        lines.append(f'  * **{y}년**')
        for m in sorted(by_date[y].keys(), reverse=True):
            lines.append(f'    * **{m}월**')
            for (_, title, enc) in sorted(by_date[y][m], key=lambda x: x[0].name):
                lines.append(f'      * [{title}]({enc})')
    
    if '미분류' in by_date and by_date['미분류']['']:
        lines.append('  * **미기재/기타**')
        for (_, title, enc) in sorted(by_date['미분류'][''], key=lambda x: x[1]):
            lines.append(f'    * [{title}]({enc})')
    lines.append('')

    # 2. 🏷️ 언어 / 기술 / 커스텀 태그별
    lines.append('* **🏷️ 언어/기술/커스텀 태그별**')
    for tag in sorted(by_tag.keys()):
        if tag == '기타': continue
        lines.append(f'  * **{tag}**')
        for (_, title, enc) in sorted(by_tag[tag], key=lambda x: x[1]):
            lines.append(f'    * [{title}]({enc})')
    if '기타' in by_tag and by_tag['기타']:
        lines.append('  * **기타**')
        for (_, title, enc) in sorted(by_tag['기타'], key=lambda x: x[1]):
            lines.append(f'    * [{title}]({enc})')
    lines.append('')

    # 3. 📁 기존 폴더 구조별
    lines.append('* **📁 기존 폴더 구조별**')
    def process_dir(path: Path, depth: int):
        try: items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        except: return
        for it in items:
            if it.name in IGNORE_DIRS or it.name in IGNORE_FILES or it.name.startswith('.'): continue
            ind = '  ' * depth
            if it.is_dir():
                if any(p for p in it.rglob('*.md') if not any(i in IGNORE_DIRS for i in p.parts) and p.name not in IGNORE_FILES):
                    lines.append(f"{ind}* **{it.name}**")
                    process_dir(it, depth + 1)
            elif it.is_file() and it.suffix.lower() == '.md':
                lines.append(f"{ind}* [{clean_title(it.stem)}]({encode_path(it.with_suffix(''))})")

    top_level = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name not in IGNORE_DIRS and not d.name.startswith('.')], key=lambda x: x.name.lower())
    for category in top_level:
        if any(p for p in category.rglob('*.md') if not any(i in IGNORE_DIRS for i in p.parts) and p.name not in IGNORE_FILES):
            lines.append(f"  * **{category.name}**")
            process_dir(category, 2)

    ROOT.joinpath('_sidebar.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f"✅ 사이드바 생성 완료: {ROOT / '_sidebar.md'}")

if __name__ == '__main__':
    generate_sidebar()
