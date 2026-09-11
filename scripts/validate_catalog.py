"""Check case metadata, local Markdown links, and exact inline prompt copies.

Run from any directory with Python 3. No third-party packages are required.
"""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def main():
    entries = json.loads((ROOT / 'catalog.json').read_text())['entries']
    errors = []
    seen = set()
    statuses = {'prompt-only', 'gif-included', 'stills-included-video-pending',
                'image-included', 'video-included'}
    required = ['## 👀 Preview', '## 👇 Workflow', '## 🔖 Full Prompt']
    homepage = (ROOT / 'README.md').read_text()
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
        if not body.startswith(f"# {key}. {entry['title']}\n"):
            errors.append(f'{key}: title disagrees with catalog')
        if '](' + '#' + entry['readme_anchor'] + ')' not in homepage:
            errors.append(f'{key}: missing from homepage')
        for heading in required:
            if heading not in body:
                errors.append(f'{key}: missing {heading}')
        if f"by {entry['author']}" not in (homepage if key.startswith("P") else body):
            errors.append(f'{key}: missing author')
        if entry['inspiration'] and entry['inspiration']['url'] not in body:
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
            prompt_texts.add(prompt.read_text().strip())
            if prompt.read_text().strip() not in body or prompt.read_text().strip() not in homepage:
                errors.append(f'{key}: full prompt missing from case or README: {name}')
        for block in re.findall(r'```text\n(.*?)\n```', body, re.S):
            if block.strip() not in prompt_texts:
                errors.append(f'{key}: inline prompt differs from prompt files')

    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        body = path.read_text()
        # Ignore code examples; examine Markdown destinations, including images.
        prose = re.sub(r'```.*?```', '', body, flags=re.S)
        for destination in re.findall(r'\]\(([^\s)]+)\)', prose):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = path.parent / unquote(parsed.path)
            if not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: broken link {destination}')
        if '&#x20;' in body or '</div>' in body:
            errors.append(f'{path.relative_to(ROOT)}: stray formatting markup')
        if len(re.findall(r'^```', body, re.M)) % 2:
            errors.append(f'{path.relative_to(ROOT)}: unclosed code fence')

    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated {len(entries)} cases: metadata, prompt copies, and local file links.')


if __name__ == '__main__':
    main()
