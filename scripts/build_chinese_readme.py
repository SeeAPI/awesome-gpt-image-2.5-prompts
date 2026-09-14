"""Render the Chinese README and case pages from reviewed translations.

Run after editing both language prompt files and docs/i18n/zh-CN.json.
Use --check to detect stale Chinese pages without writing files.
"""

import argparse
import json
import re
from pathlib import Path

from validate_catalog import markdown_anchors

ROOT = Path(__file__).resolve().parents[1]


def build_outputs():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    phrases = json.loads((ROOT / 'docs/i18n/zh-CN.json').read_text())
    pattern = re.compile('|'.join(re.escape(x) for x in sorted(phrases, key=len, reverse=True)))
    prompts = {}
    for entry in catalog['entries']:
        for original in entry['prompts']:
            translated = entry['prompts_zh'][original]
            prompts[(ROOT / original).read_text().strip()] = (ROOT / translated).read_text().strip()

    def translate(body, anchors=False):
        parts = re.split(r'(```.*?```)', body, flags=re.S)
        for index, part in enumerate(parts):
            if part.startswith('```'):
                match = re.fullmatch(r'```text\n(.*?)\n```', part, re.S)
                if not match or match[1].strip() not in prompts:
                    raise ValueError('Missing reviewed translation for a prompt block')
                parts[index] = '```text\n' + prompts[match[1].strip()] + '\n```'
                continue
            if anchors:
                def heading(match):
                    if part[:match.start()].rstrip().endswith('</a>'):
                        return match[0]
                    anchor = next(iter(markdown_anchors(match[0])))
                    return f'<a id="{anchor}"></a>\n\n{match[0]}'
                part = re.sub(r'^#{2,3} .+$', heading, part, flags=re.M)
            # Paths, fragments and source URLs remain exactly as published.
            fragments = re.split(r'(\]\([^\n)]*\)|(?:src|href)="[^"]*"|<a id="[^"]*"></a>)', part)
            for i in range(0, len(fragments), 2):
                fragments[i] = pattern.sub(lambda match: phrases[match[0]], fragments[i])
            parts[index] = ''.join(fragments)
        return ''.join(parts)

    homepage = translate((ROOT / 'README.md').read_text(), anchors=True)
    outputs = {ROOT / 'README_zh.md': homepage}
    for entry in catalog['entries']:
        body = translate((ROOT / entry['case']).read_text())
        # English cases live in cases/; Chinese cases are one directory deeper.
        body = re.sub(r'(\]\(|src=")\.\./', r'\1../../', body)
        title, rest = body.split('\n', 1)
        nav = f'\n\n[English](../{entry["slug"]}.md) | [简体中文]({entry["slug"]}.md)\n'
        outputs[ROOT / 'cases/zh-CN' / f'{entry["slug"]}.md'] = title + nav + rest
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, content in build_outputs().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    if stale:
        raise SystemExit('Stale bilingual content: ' + ', '.join(stale))
    print('Chinese README and 47 case pages are in sync.' if args.check else 'Rendered Chinese README and case pages.')


if __name__ == '__main__':
    main()
