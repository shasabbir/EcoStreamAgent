from pathlib import Path
import re
from difflib import SequenceMatcher

root = Path(__file__).resolve().parents[1] / 'paper'
main_path = root / 'main.tex'
lit_path = root / 'sections' / 'literature-review.tex'
main = main_path.read_text(encoding='utf-8')
lit = lit_path.read_text(encoding='utf-8')
human = (root / 'humanized.txt').read_text(encoding='utf-8')
blocks = [x.strip() for x in re.split(r'\n\s*\n', human) if x.strip()]

assert len(blocks) == 42, f'Unexpected humanized block count: {len(blocks)}'
assert blocks[0].startswith('abstract:\n')
assert blocks[1].startswith('introduction:\n')
assert blocks[14].startswith('Literature review:\n')

def sentences(text):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

def words(text):
    return re.findall(r'[a-z0-9]+', text.lower())

def merge_citations(source, rewritten):
    pieces = re.split(r'(~?\\cite\{[^}]+\})', source)
    source_clean = ''.join(p for p in pieces if not re.fullmatch(r'~?\\cite\{[^}]+\}', p))
    original_sentences = sentences(source_clean)
    new_sentences = sentences(rewritten)
    groups = re.findall(r'(?:~?\\cite\{[^}]+\})+', source)
    for group in groups:
        preceding = source.split(group, 1)[0]
        preceding = re.sub(r'~?\\cite\{[^}]+\}', '', preceding)
        source_index = min(len(sentences(preceding)) - 1, len(original_sentences) - 1)
        target_index = max(range(len(new_sentences)), key=lambda i: SequenceMatcher(None, words(original_sentences[source_index]), words(new_sentences[i]), autojunk=False).ratio())
        new_sentences[target_index] = new_sentences[target_index].rstrip() + group
    return ' '.join(new_sentences)

abstract = blocks[0].split('\n', 1)[1]
main = re.sub(r'(?<=\\begin\{abstract\}\n).*?(?=\n\\end\{abstract\})', lambda _: abstract, main, count=1, flags=re.S)

intro_start = main.index('\\section{Introduction}')
intro_end = main.index('\\input{sections/literature-review}')
intro_original = main[intro_start:intro_end]
intro_parts = [x.strip() for x in re.split(r'\n\s*\n', intro_original.split('\\section{Introduction}\n', 1)[1]) if x.strip()]
assert len(intro_parts) == 13
intro_human = [blocks[1].split('\n', 1)[1]] + blocks[2:7]
assert len(intro_human) == 6
intro_out = []
for i in range(6):
    old = re.sub(r'^\\label\{sec:introduction\}\n', '', intro_parts[i])
    intro_out.append(merge_citations(old, intro_human[i]))
intro_out[0] = '\\label{sec:introduction}\n' + intro_out[0]
rq_heading, rq_lead = blocks[7].split('\n', 1)
assert rq_heading == 'A. Research questions'
intro_out.append('\\subsection{Research Questions}\n' + rq_lead)
for old, block in zip(intro_parts[7:11], blocks[8:12]):
    block = re.sub(r'^(RQ\d \([^)]*\):)', r'\\textbf{\1}', block)
    intro_out.append(merge_citations(old, block))
contrib_heading, contrib_text = blocks[12].split('\n', 1)
assert contrib_heading == 'B. Planned contributions'
segments = contrib_text.split('; ')
assert len(segments) == 4, f'Unexpected contribution segments: {len(segments)}'
intro_out.append('\\subsection{Planned Contributions}\n' + segments[0].split(': ', 1)[0] + ':\n\\begin{itemize}\n' + '\n'.join('    \\item ' + item.rstrip('.') + ';' for item in [segments[0].split(': ', 1)[1]] + segments[1:3]) + '\n    \\item ' + segments[3] + '\n\\end{itemize}')
intro_out.append(blocks[13])
main = main[:intro_start] + '\\section{Introduction}\n' + '\n\n'.join(intro_out) + '\n\n' + main[intro_end:]

lit_parts = [x.strip() for x in re.split(r'\n\s*\n', lit) if x.strip()]
assert len(lit_parts) == 29
lit_human = [blocks[14].split('\n', 1)[1], blocks[15]]
for i in range(16, len(blocks)):
    block = blocks[i]
    if re.match(r'^[A-F]\. ', block):
        if '\n' in block:
            lit_human.append(block.split('\n', 1)[1])
    else:
        lit_human.append(block)
assert len(lit_human) == 28, f'Unexpected literature paragraph count: {len(lit_human)}'
lit_out = []
j = 0
for part in lit_parts:
    if part.startswith('\\begin{table*}'):
        lit_out.append(part)
        continue
    heading = ''
    match = re.match(r'^(\\(?:section|subsection)\{[^}]+\}\n(?:\\label\{[^}]+\}\n)?)', part)
    if match:
        heading = match.group(1)
        part = part[len(heading):]
    lit_out.append(heading + merge_citations(part, lit_human[j]))
    j += 1
assert j == 28
lit = '\n\n'.join(lit_out) + '\n'

old_keys = set(re.findall(r'\\cite\{([^}]+)\}', main_path.read_text(encoding='utf-8') + lit_path.read_text(encoding='utf-8')))
new_keys = set(re.findall(r'\\cite\{([^}]+)\}', main + lit))
assert old_keys == new_keys, (old_keys - new_keys, new_keys - old_keys)
assert lit.count('\\begin{table*}') == lit.count('\\end{table*}') == 1
main_path.write_text(main, encoding='utf-8')
lit_path.write_text(lit, encoding='utf-8')
print('Merged humanized prose; preserved citation groups and comparison table.')
