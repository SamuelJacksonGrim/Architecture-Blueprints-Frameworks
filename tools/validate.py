#!/usr/bin/env python3
"""Check the rules in SCHEMA.md and SELECTOR.md mechanically.

    python tools/validate.py              # check this framework repo
    python tools/validate.py PROJECT_DIR  # check a project built from it

Standard library only. Works the same on Linux, macOS, Windows, and WSL.
Exit 0 = clean, 1 = problems found, 2 = bad usage.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ARTIFACTS = ["Architecture", "Flows", "Contracts", "Types", "Schemas",
             "Interfaces", "Modules", "Dependencies", "DecisionLog", "README"]
THIN = {"Architecture", "Flows", "Contracts", "DecisionLog", "README"}
REQUIRED = {  # SELECTOR Step C
    "thin": THIN,
    "standard": THIN | {"Types", "Interfaces", "Modules"},
    "full": set(ARTIFACTS),
}
STATUSES = {"stub", "partial", "complete"}
ROOT = Path(__file__).resolve().parent.parent


def read(path: Path) -> str:
    # utf-8-sig drops a BOM; splitlines() handles \r\n from Windows checkouts.
    return "\n".join(path.read_text(encoding="utf-8-sig").splitlines())


def frontmatter(path: Path) -> dict[str, str] | None:
    text = read(path)
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    fields = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields


def deps(fields: dict[str, str]) -> list[str]:
    raw = fields.get("depends_on", "[]").strip("[] ")
    return [d.strip() for d in raw.split(",") if d.strip()]


def load_set(folder: Path) -> dict[str, dict[str, str]]:
    found = {}
    for name in ARTIFACTS:
        f = folder / f"{name}.md"
        if f.is_file():
            fm = frontmatter(f)
            if fm and fm.get("artifact") == name:
                found[name] = fm
    return found


# --- framework self-check ---------------------------------------------------

def check_edges(label: str, arts: dict[str, dict[str, str]], problems: list[str]) -> None:
    """SCHEMA depth self-consistency, for every depth."""
    for depth, required in REQUIRED.items():
        for name, fm in arts.items():
            if name not in required:
                continue
            for d in deps(fm):
                if "/" in d or d.endswith(".md"):
                    continue  # variant pointing at its base skeleton
                if d not in ARTIFACTS:
                    problems.append(f"{label}/{name}.md: depends_on unknown artifact {d!r}")
                elif d not in required and not (name == "README" and depth == "thin"):
                    # README at thin is covered explicitly by PIPELINE.md.
                    problems.append(f"{label}/{name}.md: at {depth}, depends on optional {d}")


LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def check_links(files: list[Path], problems: list[str]) -> None:
    for f in files:
        for target in LINK.findall(read(f)):
            if re.match(r"^[a-z]+:", target):
                continue  # http:, mailto:, ...
            if not (f.parent / target).exists():
                problems.append(f"{f.relative_to(ROOT).as_posix()}: broken link {target}")


def check_framework(problems: list[str]) -> None:
    sets = [ROOT / "templates"] + sorted(p.parent for p in ROOT.glob("skeletons/**/Flows.md")) \
        + sorted(p.parent for p in ROOT.glob("examples/**/Architecture.md"))
    for folder in sets:
        check_edges(folder.relative_to(ROOT).as_posix(), load_set(folder), problems)
    ai_path = [ROOT / n for n in ("README.md", "AGENTS.md", "SELECTOR.md", "PIPELINE.md", "SCHEMA.md",
                                  "QUALITY-BAR.md", "SECURITY.md", "KAIZEN.md", "CONTRIBUTING.md")]
    check_links([f for f in ai_path if f.is_file()], problems)
    for loader in ("CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", ".cursor/rules/front-door.mdc"):
        f = ROOT / loader
        if f.is_file() and "AGENTS.md" not in read(f):
            problems.append(f"{loader}: loader does not point at AGENTS.md")


# --- project check ----------------------------------------------------------

def find_artifacts(project: Path) -> Path | None:
    for candidate in [project, *sorted(project.glob("*/")), *sorted(project.glob("*/*/"))]:
        if candidate.name.startswith(".") or not candidate.is_dir():
            continue
        f = candidate / "Architecture.md"
        if f.is_file() and (frontmatter(f) or {}).get("artifact") == "Architecture":
            return candidate
    return None


def check_project(project: Path, problems: list[str], notes: list[str]) -> None:
    intent = project / "INTENT.md"
    folder = find_artifacts(project)
    if folder is None:
        problems.append("no Architecture.md with frontmatter found (instantiate the ten artifacts)")
        return
    if not intent.is_file():
        intent = folder / "INTENT.md"
    if not intent.is_file():
        problems.append("INTENT.md missing (SELECTOR Step A)")
        return
    text = read(intent)
    m = re.search(r"^depth:\s*(thin|standard|full)\b", text, re.M)
    if not m:
        problems.append("INTENT.md: no `depth: thin|standard|full`")
        return
    depth = m.group(1)
    required = REQUIRED[depth]
    notes.append(f"artifacts in {folder.relative_to(project).as_posix() or '.'}, depth {depth}")

    arts = load_set(folder)
    for name in ARTIFACTS:
        if name not in arts:
            problems.append(f"{name}.md missing or without frontmatter (structural validity)")
    for name, fm in arts.items():
        status = fm.get("status")
        if status not in STATUSES:
            problems.append(f"{name}.md: status {status!r} is not stub|partial|complete")
            continue
        if name in required and status != "complete":
            problems.append(f"{name}.md: {depth} requires complete, found {status}")
        if status == "complete":
            for d in deps(fm):
                # SCHEMA: an edge to an artifact this depth leaves optional does not gate.
                if d in arts and d in required and arts[d].get("status") == "stub":
                    problems.append(f"{name}.md: complete but depends on stub {d}")

    if not re.search(r"^exposure:\s*(local-single|local-shared|networked|multi-tenant)\b", text, re.M):
        problems.append("INTENT.md: no `exposure:` profile (SELECTOR Step C)")
    if not re.search(r"\|\s*(include|exclude)\s*\|", text, re.I):
        problems.append("INTENT.md: implied-counterparts table has no include/exclude rows (SELECTOR Step A)")


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        print(__doc__.strip())
        return 2
    problems: list[str] = []
    notes: list[str] = []
    if argv:
        project = Path(argv[0]).resolve()
        if not project.is_dir():
            print(f"not a directory: {project}")
            return 2
        check_project(project, problems, notes)
        what = f"project {project.name}"
    else:
        check_framework(problems)
        what = "framework"
    for n in notes:
        print(f"note: {n}")
    for p in problems:
        print(f"FAIL: {p}")
    print(f"{what}: {'OK' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
