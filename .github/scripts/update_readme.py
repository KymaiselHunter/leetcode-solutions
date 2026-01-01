from __future__ import annotations

import os
from pathlib import Path

START = "<!-- SOLUTIONS:START -->"
END = "<!-- SOLUTIONS:END -->"

EXTS = {".py", ".cpp", ".cc", ".cxx"}


def collect_solution_links(root_dir: Path) -> list[str]:
    links: list[str] = []

    for path in sorted(root_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in EXTS:
            continue

        # Make link relative to repo root (README is at repo root)
        rel = path.as_posix()

        # Display text: keep it simple (filename)
        display = path.name

        links.append(f"- [{display}]({rel})\n")

    return links


def update_readme(readme_path: Path, solutions_dir: Path) -> None:
    readme_path.parent.mkdir(parents=True, exist_ok=True)

    if readme_path.exists():
        lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    else:
        lines = []

    # Ensure markers exist (append them if missing)
    stripped = [ln.strip() for ln in lines]
    if START not in stripped:
        # Add a small header + markers at end if you want
        if lines and not lines[-1].endswith("\n"):
            lines[-1] = lines[-1] + "\n"
        lines += ["\n", "## Solutions\n", f"{START}\n", f"{END}\n"]
        stripped = [ln.strip() for ln in lines]

    # Recompute after potential insertion
    start_idx = next(i for i, ln in enumerate(lines) if ln.strip() == START)
    end_idx = next(i for i, ln in enumerate(lines) if ln.strip() == END)

    if end_idx < start_idx:
        raise RuntimeError("README marker order is invalid: END appears before START.")

    links = collect_solution_links(solutions_dir)

    new_lines = []
    new_lines.extend(lines[: start_idx + 1])  # include START line
    new_lines.append("\n")
    new_lines.extend(links if links else ["- (No solutions yet)\n"])
    new_lines.append("\n")
    new_lines.extend(lines[end_idx:])  # include END line and everything after

    readme_path.write_text("".join(new_lines), encoding="utf-8")


if __name__ == "__main__":
    repo_root = Path(os.getenv("GITHUB_WORKSPACE", ".")).resolve()
    readme = repo_root / "README.md"
    solutions = repo_root / "leetcode"  # adjust if you use leetcode-solutions/leetcode, etc.

    if not solutions.exists():
        # If leetcode folder doesn't exist yet, still ensure markers exist
        solutions.mkdir(parents=True, exist_ok=True)

    update_readme(readme, solutions)
