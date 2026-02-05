#!/usr/bin/env python3
"""
Generiert für jede Datei in src/niveau/informationen eine formatierte Markdown-Datei
in docs/information.
"""
from pathlib import Path
import ast
import textwrap
import sys
import traceback

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / 'src' / 'niveau' / 'informationen'
OUT_DIR = ROOT / 'docs' / 'information'
OUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_CODE_LINES = 400

def first_paragraph(text: str) -> str:
    for part in text.splitlines():
        s = part.strip()
        if s:
            return s
    return ''

def collect_defs(node_list):
    funcs = []
    classes = []
    for node in node_list:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node) or ''
            funcs.append((node.name, first_paragraph(doc)))
        elif isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node) or ''
            methods = []
            for n in node.body:
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods.append((n.name, first_paragraph(ast.get_docstring(n) or '')))
            classes.append((node.name, first_paragraph(doc), methods))
    return funcs, classes

def analyze_py(path: Path):
    src = path.read_text(encoding='utf-8', errors='replace')
    try:
        mod = ast.parse(src)
        module_doc = ast.get_docstring(mod) or ''
        funcs, classes = collect_defs(mod.body)
    except Exception:
        module_doc = ''
        funcs = []
        classes = []
    stats = {
        'lines': src.count('\n') + 1,
        'size_bytes': path.stat().st_size,
        'functions': len(funcs),
        'classes': len(classes)
    }
    return module_doc, funcs, classes, stats, src

def analyze_text(path: Path):
    src = path.read_text(encoding='utf-8', errors='replace')
    stats = {
        'lines': src.count('\n') + 1,
        'size_bytes': path.stat().st_size
    }
    summary = first_paragraph(src)
    return summary, stats, src

def unique_out_path(base: str) -> Path:
    out_name = f"{base}.md"
    out_path = OUT_DIR / out_name
    counter = 1
    while out_path.exists():
        out_path = OUT_DIR / f"{base}_{counter}.md"
        counter += 1
    return out_path

def make_md_for_file(src_path: Path, rel_path: Path):
    try:
        name = src_path.name
        base = src_path.stem
        ext = src_path.suffix.lower()
        out_path = unique_out_path(base)

        parts = []
        parts.append(f"# {base}\n")
        parts.append(f"- Original: `{rel_path.as_posix()}`\n")

        if ext == '.py':
            module_doc, funcs, classes, stats, src = analyze_py(src_path)
            parts.append("## Zusammenfassung\n")
            parts.append(first_paragraph(module_doc) or "Keine Modulbeschreibung vorhanden.")
            parts.append("\n")
            parts.append("## Analyse\n")
            parts.append(f"- Zeilen: {stats['lines']}\n- Bytes: {stats['size_bytes']}\n- Funktionen: {stats['functions']}\n- Klassen: {stats['classes']}\n\n")
            if module_doc:
                parts.append("## Moduldokumentation\n")
                parts.append(textwrap.dedent(module_doc))
                parts.append("\n")
            if funcs:
                parts.append("## Funktionen (Kurzbeschreibung)\n")
                for n, d in funcs:
                    parts.append(f"- **{n}**: {d or '-'}\n")
                parts.append("\n")
            if classes:
                parts.append("## Klassen (Kurzbeschreibung)\n")
                for cname, cdoc, methods in classes:
                    parts.append(f"- **{cname}**: {cdoc or '-'}\n")
                    if methods:
                        parts.append("  - Methoden:\n")
                        for mname, mdoc in methods:
                            parts.append(f"    - **{mname}**: {mdoc or '-'}\n")
                parts.append("\n")
            parts.append("## Quellcode\n")
            code_lines = src.strip().splitlines()
            if len(code_lines) > MAX_CODE_LINES:
                snippet = "\n".join(code_lines[:MAX_CODE_LINES])
                snippet += f"\n\n# ... Datei gekürzt: {len(code_lines) - MAX_CODE_LINES} Zeilen nicht angezeigt ...\n"
            else:
                snippet = "\n".join(code_lines)
            parts.append("```python\n")
            parts.append(snippet)
            parts.append("\n```\n")
        else:
            summary, stats, src = analyze_text(src_path)
            parts.append("## Zusammenfassung\n")
            parts.append(summary or "Keine Zusammenfassung vorhanden.")
            parts.append("\n")
            parts.append("## Analyse\n")
            parts.append(f"- Zeilen: {stats['lines']}\n- Bytes: {stats['size_bytes']}\n\n")
            parts.append("## Originalinhalt\n")
            if ext == '.md':
                parts.append(src)
                parts.append("\n")
            else:
                parts.append("```\n")
                parts.append(src.strip())
                parts.append("\n```\n")

        out_text = "\n".join(parts)
        out_path.write_text(out_text, encoding='utf-8')
        print(f"Generiert: {out_path}")
    except Exception as e:
        print(f"Fehler beim Verarbeiten von {src_path}: {e}", file=sys.stderr)
        traceback.print_exc()

def main():
    if not SRC_DIR.exists():
        print(f"Quellverzeichnis nicht gefunden: {SRC_DIR}", file=sys.stderr)
        return
    count = 0
    for p in SRC_DIR.rglob('*'):
        if p.is_file() and p.suffix.lower() in ('.py', '.md', '.txt'):
            rel = p.relative_to(ROOT)
            make_md_for_file(p, rel)
            count += 1
    print(f"Fertig. Dateien verarbeitet: {count}")

if __name__ == '__main__':
    main()