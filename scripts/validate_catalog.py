"""Check case metadata, local Markdown links, and exact inline prompt copies.

Run from any directory with Python 3. No third-party packages are required.
"""

import json
import re
import hashlib
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def markdown_anchors(body):
    """GitHub-style anchors for this collection's Markdown headings."""
    body = re.sub(r'```.*?```', '', body, flags=re.S)
    anchors = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', body))
    for heading in re.findall(r'^#{1,6}\s+(.+)$', body, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = unescape(re.sub(r'<[^>]*>', '', heading)).strip().lower()
        slug = re.sub(r'[^\w\-\s]', '', heading).replace(' ', '-')
        candidate, suffix = slug, 0
        while candidate in anchors:
            suffix += 1
            candidate = f'{slug}-{suffix}'
        anchors.add(candidate)
    return anchors


def readme_case_section(body, anchor):
    """Return one README case without treating prompt headings as case boundaries."""
    marker = f'<a id="{anchor}"></a>'
    start = body.find(marker)
    if start < 0:
        return ''
    # Prompt 正文可能包含 Markdown 标题；案例边界以仓库维护的显式锚点为准。
    remainder = body[start + len(marker):]
    next_anchor = re.search(r'^<a id="[^"]+"></a>$', remainder, re.M)
    end = start + len(marker) + next_anchor.start() if next_anchor else len(body)
    return body[start:end]


def main():
    entries = json.loads((ROOT / 'catalog.json').read_text())['entries']
    errors = []
    seen = set()
    statuses = {'prompt-only', 'gif-included', 'stills-included-video-pending',
                'image-included', 'video-included'}
    required = ['## 👀 Preview', '## 👇 Workflow', '## 🔖 Full Prompt']
    homepage = (ROOT / 'README.md').read_text()
    chinese_homepage = (ROOT / 'README_zh.md').read_text()
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    from datetime import date
    updated = date.fromisoformat(catalog['updated'])
    standalone_count = sum(e['id'].startswith('P') for e in entries)
    creative_count = len(entries) - standalone_count
    expected_en = f'{creative_count} creative workflows · {standalone_count} standalone prompts · Updated {updated.strftime("%B")} {updated.day}, {updated.year}'
    expected_zh = f'{creative_count} 个创意工作流 · {standalone_count} 条独立提示词 · 更新于 {updated.year} 年 {updated.month} 月 {updated.day} 日'
    if expected_en not in homepage or expected_zh not in chinese_homepage:
        errors.append('Bilingual counts or content dates disagree with catalog')
    homepage_anchors = markdown_anchors(homepage)
    source_keys = set()
    prompt_hashes = {}
    for entry in entries:
        key = entry['id']
        if key in seen:
            errors.append(f'Duplicate ID: {key}')
        seen.add(key)
        if entry['status'] not in statuses:
            errors.append(f'{key}: unknown status')
        path = ROOT / entry['case']
        if not path.is_file():
            errors.append(f'{key}: missing case {path}')
            continue
        body = path.read_text()
        chinese_case = ROOT / 'cases/zh-CN' / path.name
        chinese_body = chinese_case.read_text() if chinese_case.is_file() else ''
        chinese_section = readme_case_section(chinese_homepage, entry['readme_anchor'])
        if not chinese_body.startswith(f'# {key}. {entry.get("title_zh", "")}') or not chinese_section:
            errors.append(f'{key}: missing Chinese title, case or inline section')
        for heading in ['👀 预览', '👇 工作流', '🔖 完整提示词']:
            if f'## {heading}' not in chinese_body or f'#### {heading}' not in chinese_section:
                errors.append(f'{key}: missing Chinese {heading}')
        english_images = re.findall(r'<img\s+src="([^"]+)"', body)
        chinese_images = re.findall(r'<img\s+src="([^"]+)"', chinese_body)
        if [x.removeprefix('../') for x in english_images] != [x.removeprefix('../../') for x in chinese_images]:
            errors.append(f'{key}: Chinese preview images differ from English')
        section = readme_case_section(homepage, entry['readme_anchor'])
        if not section:
            errors.append(f'{key}: missing inline homepage section')
        if not body.startswith(f"# {key}. {entry['title']}"):
            errors.append(f'{key}: title disagrees with catalog')
        if entry['readme_anchor'] not in homepage_anchors:
            errors.append(f'{key}: README anchor does not match a heading')
        if path.stem != entry['slug']:
            errors.append(f'{key}: case slug mismatch')
        for heading in required:
            if heading not in body:
                errors.append(f'{key}: missing {heading}')
        plain_credit = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1',
                              homepage if key.startswith('P') else body)
        source = entry.get('source')
        collection_credit = source and source.get('credit_role') == 'collection'
        if not collection_credit and entry['author'] != 'Author unconfirmed' and f"by {entry['author']}" not in plain_credit:
            errors.append(f'{key}: missing author')
        if source:
            if collection_credit:
                original = source.get('original_source', {})
                if not original.get('publisher') or urlsplit(original.get('url', '')).scheme != 'https':
                    errors.append(f'{key}: collection credit requires original-source provenance')
            url = source.get('url', '')
            parsed = urlsplit(url)
            if parsed.scheme != 'https' or not parsed.netloc or 'feishu.cn' in parsed.netloc:
                errors.append(f'{key}: source must be a public HTTPS source')
            if source.get('author_status') not in {'unconfirmed', 'credited-by-source'}:
                errors.append(f'{key}: unknown author status')
            if source.get('relationship') not in {'collected', 'adapted'}:
                errors.append(f'{key}: unknown source relationship')
            source_key = (url, source.get('item_key'))
            if not source_key[1] or source_key in source_keys:
                errors.append(f'{key}: missing or duplicate source item key')
            source_keys.add(source_key)
            line = next(iter(re.findall(r'<sub>(.*?)</sub>', section, re.S)), '')
            if f"[Source: {source['platform']}]({url})" not in line:
                errors.append(f'{key}: missing platform-labelled source below full prompt')
        for media in entry.get('media', []):
            asset = ROOT / media['path']
            if not asset.is_file():
                errors.append(f'{key}: missing media {media["path"]}')
            elif hashlib.sha256(asset.read_bytes()).hexdigest() != media['sha256']:
                errors.append(f'{key}: media hash mismatch {media["path"]}')
            if media['path'] not in body or media['path'] not in section:
                errors.append(f'{key}: media missing from case or README section')
        if entry['inspiration'] and entry['inspiration']['url'] not in homepage:
            errors.append(f'{key}: missing inspiration URL')
        if entry['preview'] and not (ROOT / entry['preview']).is_file():
            errors.append(f'{key}: missing preview')
        prompt_texts = set()
        for name in entry['prompts']:
            prompt = ROOT / name
            if not prompt.is_file():
                errors.append(f'{key}: missing {name}')
                continue
            if prompt.parent.name != entry['slug']:
                errors.append(f'{key}: prompt slug mismatch')
            translated = ROOT / entry.get('prompts_zh', {}).get(name, '__missing__')
            if not translated.is_file():
                errors.append(f'{key}: missing Chinese prompt for {name}')
            else:
                chinese_text = translated.read_text().strip()
                if not chinese_text or chinese_text not in chinese_body or chinese_text not in chinese_section:
                    errors.append(f'{key}: Chinese prompt differs from its case or README')
                placeholders = lambda text: set(re.findall(r'\[[^\]\n]+\]', text))
                if placeholders(prompt.read_text()) != placeholders(chinese_text):
                    errors.append(f'{key}: placeholder mismatch between prompt languages')
            source_hash = hashlib.sha256(prompt.read_bytes()).hexdigest()
            if entry.get('translation_source_sha256', {}).get(name) != source_hash:
                errors.append(f'{key}: English prompt changed; review Chinese translation and update translation_source_sha256')
            prompt_texts.add(prompt.read_text().strip())
            if prompt.read_text().strip() not in body or prompt.read_text().strip() not in section:
                errors.append(f'{key}: full prompt missing from case or README: {name}')
            if source:
                normalized = ' '.join(prompt.read_text().split()).casefold()
                digest = hashlib.sha256(normalized.encode()).hexdigest()
                if digest in prompt_hashes:
                    errors.append(f'{key}: duplicate collected prompt of {prompt_hashes[digest]}')
                prompt_hashes[digest] = key
        for block in re.findall(r'```text\n(.*?)\n```', body, re.S):
            if block.strip() not in prompt_texts:
                errors.append(f'{key}: inline prompt differs from prompt files')

    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        body = path.read_text()
        # Ignore code examples; examine Markdown destinations, including images.
        prose = re.sub(r'```.*?```', '', body, flags=re.S)
        prose = re.sub(r'`[^`\n]+`', '', prose)
        for destination in re.findall(r'\]\(([^\s)]+)\)', prose):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            target = path.parent / unquote(parsed.path) if parsed.path else path
            if not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: broken link {destination}')
            elif parsed.fragment and target.suffix == '.md':
                if unquote(parsed.fragment) not in markdown_anchors(target.read_text()):
                    errors.append(f'{path.relative_to(ROOT)}: broken anchor {destination}')
        if re.search(r'^(?:<{7}|={7}|>{7})(?: |$)', body, re.M):
            errors.append(f'{path.relative_to(ROOT)}: unresolved merge marker')
        if '&#x20;' in body or '</div>' in body:
            errors.append(f'{path.relative_to(ROOT)}: stray formatting markup')
        if len(re.findall(r'^```', body, re.M)) % 2:
            errors.append(f'{path.relative_to(ROOT)}: unclosed code fence')

    if errors:
        raise SystemExit('\n'.join(errors))
    from build_chinese_readme import build_outputs
    for path, expected in build_outputs().items():
        if not path.is_file() or path.read_text() != expected:
            raise SystemExit(f'Stale Chinese page: {path.relative_to(ROOT)}; run scripts/build_chinese_readme.py')
    print(f'Validated {len(entries)} cases: metadata, prompt copies, and local file links.')


if __name__ == '__main__':
    main()
