"""Gemeinsame Validierung der BW-Verzweigungsform (Wenn/J/, sonst/N)."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BranchValidationIssue:
    """Ein Validierungsproblem in der Verzweigungsstruktur."""

    line: int
    code: str
    message: str
    suggested_fix: Optional[str] = None


def validate_bw_branch_structure(lines: List[str]) -> List[BranchValidationIssue]:
    """Prueft die exakte BW-Form fuer Verzweigungen in textbasierter Notation."""
    issues: List[BranchValidationIssue] = []
    stack: List[dict[str, int | bool]] = []

    for line_num, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))

        while (
            stack
            and indent <= int(stack[-1]["indent"])
            and stripped != ", sonst"
            and not bool(stack[-1]["expect_n"])
        ):
            stack.pop()

        if stack and bool(stack[-1]["expect_j"]):
            if stripped != "J" or indent != int(stack[-1]["indent"]) + 4:
                issues.append(
                    BranchValidationIssue(
                        line=line_num,
                        code="BW_BRANCH_MISSING_J",
                        message="Nach 'Wenn ..., dann' muss direkt 'J' (4 Leerzeichen eingerueckt) folgen.",
                        suggested_fix="Wenn bedingung, dann -> naechste Zeile: '    J'",
                    )
                )
            stack[-1]["expect_j"] = False
            continue

        if stack and bool(stack[-1]["expect_n"]):
            if stripped != "N" or indent != int(stack[-1]["indent"]) + 4:
                issues.append(
                    BranchValidationIssue(
                        line=line_num,
                        code="BW_BRANCH_MISSING_N",
                        message="Nach ', sonst' muss direkt 'N' (4 Leerzeichen eingerueckt) folgen.",
                        suggested_fix=", sonst -> naechste Zeile: '    N'",
                    )
                )
            stack[-1]["expect_n"] = False
            continue

        if stripped.startswith("Wenn ") and stripped.endswith(", dann"):
            stack.append({"indent": indent, "expect_j": True, "expect_n": False, "line": line_num})
            continue

        if stripped == ", sonst":
            if not stack:
                issues.append(
                    BranchValidationIssue(
                        line=line_num,
                        code="BW_BRANCH_ORPHAN_ELSE",
                        message="', sonst' ohne zugehoeriges 'Wenn ..., dann'.",
                    )
                )
                continue

            expected_indent = int(stack[-1]["indent"]) + 4
            if indent != expected_indent:
                issues.append(
                    BranchValidationIssue(
                        line=line_num,
                        code="BW_BRANCH_ELSE_INDENT",
                        message="', sonst' muss auf gleicher Einrueckungsebene wie 'J'/'N' stehen (Wenn-Ebene + 4 Leerzeichen).",
                        suggested_fix="Einrueckung von ', sonst' auf die Ebene von 'J'/'N' setzen",
                    )
                )

            stack[-1]["expect_n"] = True
            continue

        if stripped in {"J", "N"}:
            issues.append(
                BranchValidationIssue(
                    line=line_num,
                    code="BW_BRANCH_ORPHAN_MARKER",
                    message=f"Unerwartete Markierung '{stripped}'. J/N nur im direkten Verzweigungskontext erlaubt.",
                )
            )

    for ctx in stack:
        if bool(ctx["expect_j"]):
            issues.append(
                BranchValidationIssue(
                    line=int(ctx["line"]),
                    code="BW_BRANCH_UNCLOSED_J",
                    message="Nach 'Wenn ..., dann' fehlt die Markierung 'J'.",
                )
            )
        if bool(ctx["expect_n"]):
            issues.append(
                BranchValidationIssue(
                    line=int(ctx["line"]),
                    code="BW_BRANCH_UNCLOSED_N",
                    message="Nach ', sonst' fehlt die Markierung 'N'.",
                )
            )

    return issues
