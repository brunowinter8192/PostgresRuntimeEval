import re
from pathlib import Path

# INFRASTRUCTURE
INPUT_FILE = Path(__file__).parent / "specification.md"
OUTPUT_FILE = Path(__file__).parent / "specification_clean.md"

# ORCHESTRATOR
def main():
    content = INPUT_FILE.read_text(encoding="utf-8")
    content = convert_html_tables(content)
    content = clean_latex_artifacts(content)
    content = clean_headings(content)
    content = fix_broken_numbering(content)
    content = clean_toc_references(content)
    content = clean_empty_table_rows(content)
    content = unify_bullets(content)
    content = remove_image_refs(content)
    content = clean_whitespace(content)
    OUTPUT_FILE.write_text(content, encoding="utf-8")

# FUNCTIONS

# Convert HTML tables to Markdown tables
def convert_html_tables(content: str) -> str:
    table_pattern = re.compile(r'<table>.*?</table>', re.DOTALL)
    return table_pattern.sub(lambda m: parse_html_table(m.group(0)), content)

# Parse HTML table and return MD table
def parse_html_table(html: str) -> str:
    cell_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)
    row_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
    rows = []
    for row_match in row_pattern.finditer(html):
        cells = [cell.group(1).strip() for cell in cell_pattern.finditer(row_match.group(1))]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    max_cols = max(len(row) for row in rows)
    for row in rows:
        while len(row) < max_cols:
            row.append("")
    col_widths = [max(max(len(row[i]) for row in rows), 3) for i in range(max_cols)]
    md_lines = []
    md_lines.append("| " + " | ".join(rows[0][i].ljust(col_widths[i]) for i in range(max_cols)) + " |")
    md_lines.append("| " + " | ".join("-" * col_widths[i] for i in range(max_cols)) + " |")
    for row in rows[1:]:
        md_lines.append("| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(max_cols)) + " |")
    return "\n" + "\n".join(md_lines) + "\n"

# Remove LaTeX artifacts like $=$, ${ \bf \equiv 0 }$, $\mathrm{...}$
def clean_latex_artifacts(content: str) -> str:
    content = re.sub(r'\$\s*=\s*\$', '=', content)
    content = re.sub(r'\$\s*\{\s*\\bf\s+\\equiv\s+0\s*\}\s*\$', '= o', content)
    content = re.sub(r'\$\s*=\s*\\mathrm\s*\{\s*([^}]+)\s*\}\s*\$', r'= \1', content)
    content = re.sub(r'\$\s*=\s*\{\s*\\tt\s*\}\s*([a-zA-Z0-9_.]+)\s*\$', r'= \1', content)
    content = re.sub(r'\$\s*=\s*\\mathrm\s*\{\s*([^}]+)\s*\}\s*\.?\s*\$', r'= \1', content)
    content = re.sub(r'\$\{\s*\\mathfrak\s*\{\s*([^}]+)\s*\}\s*\}\s*\.\s*\{\s*\\mathfrak\s*\{\s*([^}]+)\s*\}\s*\}\s*\$', r'\1.\2', content)
    content = re.sub(r'\$\s*\{\s*\}\s*=\s*\\mathbf\s*\{\s*([^}]+)\s*\}\s*\$', r'= \1', content)
    content = re.sub(r'\$\s*=\s*\{\s*\\mathfrak\s*\{\s*([^}]+)\s*\}\s*\}\s*\.\s*\{\s*\\mathfrak\s*\{\s*([^}]+)\s*\}\s*\}\s*\$', r'= \1.\2', content)
    content = re.sub(r'\$\s*\\%\s*\$', '%', content)
    content = re.sub(r'\$\s*<\s*=\s*\\mathtt\s*\{\s*([^}]+)\s*\}\s*\$', r'<= \1', content)
    content = re.sub(r'\$\s*\^\s*\{\s*([^}]+)\s*\}\s*\$', r'^(\1)', content)
    content = re.sub(r'\$\s*\^\s*\+\s*\$', '+', content)
    content = re.sub(r'\$\s*([0-9]+)\s*\\mathrm\s*\{\s*~\s*X\s*~\s*\}\s*([0-9]+)\s*\$', r'\1x\2', content)
    content = re.sub(r'\$\s*7\s*\\mathrm\s*\{\s*~\s*x\s*~\s*\}\s*24\s*\$', '7x24', content)
    content = re.sub(r'\$\s*7\s*\\mathrm\s*\{\s*x\s*\}\s*24\s*\$', '7x24', content)
    content = re.sub(r'\$\s*\\\$\s*([0-9,]+)\s*\$', r'$\1', content)
    content = re.sub(r'\$\s*#\s*\$', '#', content)
    content = re.sub(r'\$\s*\+\s*\$', '+', content)
    content = re.sub(r'\$\s*\*\s*\$', '*', content)
    content = re.sub(r'\\\*', '*', content)
    content = re.sub(r'\$\s*\\lceil\s*=\s*\\mathrm\s*\{\s*([^}]+)\s*\}\s*\\rceil\s*\$', r'= \1', content)
    content = re.sub(r'\$\s*\\Gamma\s*\\mathrm\s*\{\s*([^}]+)\s*\}\s*=\s*\\mathrm\s*\{\s*([^}]+)\s*\}\s*\{\s*\}\s*([a-zA-Z]+)\s*\$', r'\1 = \2\3', content)
    content = re.sub(r'\$[^$]{0,50}\$', lambda m: clean_simple_latex(m.group(0)), content)
    return content

# Clean simple LaTeX expressions
def clean_simple_latex(latex: str) -> str:
    inner = latex.strip('$').strip()
    inner = re.sub(r'\\mathrm\s*\{([^}]*)\}', r'\1', inner)
    inner = re.sub(r'\\mathtt\s*\{([^}]*)\}', r'\1', inner)
    inner = re.sub(r'\\mathbf\s*\{([^}]*)\}', r'\1', inner)
    inner = re.sub(r'\\text\s*\{([^}]*)\}', r'\1', inner)
    inner = re.sub(r'\\bf\s+', '', inner)
    inner = re.sub(r'\{|\}', '', inner)
    inner = re.sub(r'\\', '', inner)
    inner = re.sub(r'\s+', ' ', inner).strip()
    if inner and not re.match(r'^[\s=<>+\-*/^]+$', inner):
        return inner
    return inner if inner else ''

# Clean headings: remove page numbers, fix formatting
def clean_headings(content: str) -> str:
    content = re.sub(r'^(#+\s*[\d.:]+\s*[A-Za-z][A-Za-z\s,&()-]+?)\.+\s*\d+\s*$', r'\1', content, flags=re.MULTILINE)
    content = re.sub(r'^(#+\s*)(\d+:?\s*)([A-Z][A-Z\s,&()-]+)\s*$',
                     lambda m: m.group(1) + m.group(2) + m.group(3).title(),
                     content, flags=re.MULTILINE)
    return content

# Fix broken numbering like .5.8 -> 1.5.8
def fix_broken_numbering(content: str) -> str:
    content = re.sub(r'^\.(\d+\.\d+)', r'1.\1', content, flags=re.MULTILINE)
    return content

# Remove ToC page references like ".. 8", ". .11", etc
def clean_toc_references(content: str) -> str:
    content = re.sub(r'\.{1,}\s*\.{0,}\s*\d+\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\s+\.\s*\d+\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\.{2,}', '', content)
    return content

# Remove empty table rows
def clean_empty_table_rows(content: str) -> str:
    content = re.sub(r'^\|\s*\|\s*$\n?', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\|\s*-+\s*\|\s*$\n?', '', content, flags=re.MULTILINE)
    return content

# Unify bullet points to use -
def unify_bullets(content: str) -> str:
    content = re.sub(r'^(\s*)•\s*', r'\1- ', content, flags=re.MULTILINE)
    return content

# Remove image references
def remove_image_refs(content: str) -> str:
    content = re.sub(r'!\[.*?\]\(images/[^)]+\)\s*', '', content)
    return content

# Clean excessive whitespace
def clean_whitespace(content: str) -> str:
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    content = re.sub(r' {2,}', ' ', content)
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    return content.strip() + "\n"

if __name__ == "__main__":
    main()
