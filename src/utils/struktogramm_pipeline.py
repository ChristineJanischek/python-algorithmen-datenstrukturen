"""
Struktogramm Pipeline für Rendering und Validierung.

Dieses Modul stellt eine erweiterbare Core-Pipeline bereit, die
- Struktogramm-Blöcke aus Markdown extrahiert,
- gegen die BW-Operatornotation validiert,
- als SVG rendert,
- strukturierte Reports für Automatisierung erzeugt.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Optional
import html
import json
import re
import xml.etree.ElementTree as ET

from src.utils.struktogramm_helper import StruktogrammValidator as HelperValidator


@dataclass
class ValidationIssue:
    line: int
    message: str
    severity: str


@dataclass
class StruktogrammBlock:
    index: int
    source_file: str
    start_line: int
    end_line: int
    heading: str
    lines: list[str]


@dataclass
class RenderArtifact:
    block_index: int
    output_file: str
    issues: list[ValidationIssue]
    rendered: bool


@dataclass
class PipelineReport:
    source_file: str
    output_dir: str
    stencil_file: str
    stencil_ok: bool
    block_count: int
    artifacts: list[RenderArtifact]

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_file": self.source_file,
            "output_dir": self.output_dir,
            "stencil_file": self.stencil_file,
            "stencil_ok": self.stencil_ok,
            "block_count": self.block_count,
            "artifacts": [
                {
                    "block_index": artifact.block_index,
                    "output_file": artifact.output_file,
                    "issues": [asdict(issue) for issue in artifact.issues],
                    "rendered": artifact.rendered,
                }
                for artifact in self.artifacts
            ],
        }


class PipelineSecurityError(ValueError):
    pass


class DrawioStencilRegistry:
    def __init__(self, stencil_file: Path):
        self.stencil_file = stencil_file

    def validate(self) -> tuple[bool, str]:
        if not self.stencil_file.exists():
            return False, f"Stencil-Datei fehlt: {self.stencil_file}"
        try:
            tree = ET.parse(self.stencil_file)
            root = tree.getroot()
            shapes = root.findall(".//shape")
            if not shapes:
                return False, "Stencil enthält keine <shape>-Definitionen"
        except ET.ParseError as exc:
            return False, f"Stencil XML ungültig: {exc}"
        return True, "ok"


class BwNotationValidator:
    def __init__(self) -> None:
        self.validator = HelperValidator()

    def validate_block(self, block: StruktogrammBlock) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        for offset, line in enumerate(block.lines, start=0):
            normalized = line.strip()
            if not normalized:
                continue
            valid, _, error = self.validator.validate_line(normalized)
            if not valid and error:
                issues.append(
                    ValidationIssue(
                        line=block.start_line + offset,
                        message=error,
                        severity="error",
                    )
                )
        return issues


class BwSvgRenderer:
    def render(self, block: StruktogrammBlock, title: str) -> str:
        width = 980
        row_height = 52
        top = 70
        usable_lines = [line for line in block.lines if line.strip()]
        height = top + max(1, len(usable_lines)) * row_height + 40

        chunks: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            "  <style>",
            "    .box { stroke: #000; stroke-width: 2; fill: #fff; }",
            "    .text { font-family: Arial, sans-serif; font-size: 13px; fill: #000; }",
            "    .label { font-size: 11px; fill: #666; }",
            "    .bold { font-weight: bold; }",
            "  </style>",
            f'  <text x="{width // 2}" y="30" class="text bold" text-anchor="middle" font-size="16">{html.escape(title)}</text>',
            f'  <line x1="30" y1="50" x2="{width - 30}" y2="50" stroke="#000" stroke-width="1"/>',
        ]

        y = top
        for raw in usable_lines:
            normalized = raw.strip()
            label, value = self._split_operator(normalized)
            indent = max(0, (len(raw) - len(raw.lstrip(" "))) // 4)
            x = 40 + indent * 20
            box_width = width - x - 40
            chunks.append(f'  <rect x="{x}" y="{y}" width="{box_width}" height="{row_height}" class="box"/>')
            if label:
                chunks.append(f'  <text x="{x + 10}" y="{y + 18}" class="text label">{html.escape(label)}</text>')
            chunks.append(f'  <text x="{x + 10}" y="{y + 36}" class="text">{html.escape(value)}</text>')
            y += row_height

        chunks.append("</svg>")
        return "\n".join(chunks)

    def _split_operator(self, line: str) -> tuple[str, str]:
        if ":" in line:
            left, right = line.split(":", 1)
            return f"{left.strip()}:", right.strip()
        return "Anweisung:", line


class StruktogrammPipeline:
    def __init__(
        self,
        repo_root: Optional[Path] = None,
        stencil_file: Optional[Path] = None,
    ) -> None:
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        default_stencil = self.repo_root / "apps" / "drawio-extension" / "stencil.xml"
        self.stencil_file = stencil_file or default_stencil
        self.stencil_registry = DrawioStencilRegistry(self.stencil_file)
        self.notation_validator = BwNotationValidator()
        self.renderer = BwSvgRenderer()

    def extract_blocks(self, markdown_file: Path) -> list[StruktogrammBlock]:
        markdown_file = self._safe_path(markdown_file)
        lines = markdown_file.read_text(encoding="utf-8").splitlines()
        blocks: list[StruktogrammBlock] = []

        in_block = False
        block_start = 0
        block_lines: list[str] = []
        index = 0

        for i, line in enumerate(lines, start=1):
            fence = line.strip().lower()
            if not in_block and fence.startswith("```struktogramm"):
                in_block = True
                block_start = i + 1
                block_lines = []
                continue
            if in_block and fence == "```":
                in_block = False
                index += 1
                blocks.append(
                    StruktogrammBlock(
                        index=index,
                        source_file=str(markdown_file),
                        start_line=block_start,
                        end_line=i - 1,
                        heading=self._find_heading(lines, block_start),
                        lines=block_lines.copy(),
                    )
                )
                continue
            if in_block:
                block_lines.append(line)

        return blocks

    def render_markdown(
        self,
        markdown_file: Path,
        output_dir: Optional[Path] = None,
        prefix: str = "",
        strict: bool = False,
        write_report: Optional[Path] = None,
    ) -> PipelineReport:
        markdown_file = self._safe_path(markdown_file)
        resolved_output = self._prepare_output_dir(output_dir)

        stencil_ok, _ = self.stencil_registry.validate()
        blocks = self.extract_blocks(markdown_file)
        artifacts: list[RenderArtifact] = []

        stem = self._slugify(prefix) if prefix else self._slugify(markdown_file.stem)

        for block in blocks:
            issues = self.notation_validator.validate_block(block)
            has_errors = any(issue.severity == "error" for issue in issues)
            output_name = f"{stem}_block_{block.index:02d}.svg"
            output_path = resolved_output / output_name
            rendered = not (strict and has_errors)

            if rendered:
                title = f"{block.heading} (Block {block.index})" if block.heading else f"Block {block.index}"
                svg_content = self.renderer.render(block, title)
                output_path.write_text(svg_content, encoding="utf-8")

            artifacts.append(
                RenderArtifact(
                    block_index=block.index,
                    output_file=str(output_path),
                    issues=issues,
                    rendered=rendered,
                )
            )

        report = PipelineReport(
            source_file=str(markdown_file),
            output_dir=str(resolved_output),
            stencil_file=str(self.stencil_file),
            stencil_ok=stencil_ok,
            block_count=len(blocks),
            artifacts=artifacts,
        )

        if write_report is not None:
            report_path = self._safe_path(write_report)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(
                json.dumps(report.to_dict(), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        return report

    def _prepare_output_dir(self, output_dir: Optional[Path]) -> Path:
        target = output_dir or (self.repo_root / "struktogramme" / "generated" / "svg" / "cli")
        resolved = self._safe_path(target)
        resolved.mkdir(parents=True, exist_ok=True)
        return resolved

    def _safe_path(self, path: Path) -> Path:
        expanded = path.expanduser()
        resolved = expanded if expanded.is_absolute() else (self.repo_root / expanded)
        resolved = resolved.resolve()

        repo_root_resolved = self.repo_root.resolve()
        if not str(resolved).startswith(str(repo_root_resolved)):
            raise PipelineSecurityError(
                f"Unsicherer Pfad außerhalb des Repositorys: {resolved}"
            )
        return resolved

    def _find_heading(self, lines: list[str], start_line: int) -> str:
        index = max(0, start_line - 2)
        for i in range(index, -1, -1):
            stripped = lines[i].strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip()
        return ""

    def _slugify(self, value: str) -> str:
        value = value.strip().lower()
        value = re.sub(r"[^a-z0-9äöüß_-]+", "_", value)
        value = re.sub(r"_+", "_", value)
        return value.strip("_") or "struktogramm"
