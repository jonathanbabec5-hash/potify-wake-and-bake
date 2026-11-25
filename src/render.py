from pathlib import Path
import json
import sys

def render(path):
    issue = json.loads(Path(path).read_text())
    heading = issue['title'].strip()
    if not heading:
        raise ValueError('The issue needs a title')
    lines = ['# ' + heading, '', 'Editorial draft', '']
    for section in issue['sections']:
        note = section['note'].strip() or 'Awaiting observation'
        source = section.get('source')
        lines.extend(['## ' + section['heading'], '', note, ''])
        if source:
            if not source.startswith('https://'):
                raise ValueError('Use an HTTPS source')
            lines.extend(['Source: ' + source, ''])
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render(sys.argv[1]))
