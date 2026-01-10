from __future__ import annotations

from pathlib import Path

START = "<!-- SOLUTIONS:START -->"
END = "<!-- SOLUTIONS:END -->"

IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

PY_EXTS = {".py"}
CPP_EXTS = {".cpp", ".cc", ".cxx"}


def to_repo_href(repo_root: Path, target: Path) -> str:
    rel = target.relative_to(repo_root).as_posix()
    return rel.replace(" ", "%20")


def md_link(text: str, repo_root: Path, target: Path) -> str:
    return f"[{text}]({to_repo_href(repo_root, target)})"


def pick_best(files: list[Path]) -> Path | None:
    if not files:
        return None
    return sorted(files, key=lambda p: (len(p.name), p.name.lower()))[0]


def scan_problem_folder(folder: Path) -> dict[str, Path | None]:
    py_files: list[Path] = []
    cpp_files: list[Path] = []
    notes: Path | None = None

    # only scan direct children (matches your screenshot)
    for p in folder.iterdir():
        if not p.is_file():
            continue

        if p.suffix in PY_EXTS:
            py_files.append(p)
        elif p.suffix in CPP_EXTS:
            cpp_files.append(p)
        elif p.name.lower() == "notes.md":
            notes = p

    return {"py": pick_best(py_files), "cpp": pick_best(cpp_files), "notes": notes}


def generate_table(repo_root: Path) -> str:
    problem_dirs = []
    for p in repo_root.iterdir():
        if not p.is_dir():
            continue
        if p.name in IGNORE_DIRS:
            continue
        if p.name.startswith("."):
            continue
        problem_dirs.append(p)

    problem_dirs = sorted(problem_dirs, key=lambda d: d.name.lower())

    out = []
    out.append("| Problem | Python | C++ | Notes | Folder |\n")
    out.append("|:--|:--:|:--:|:--:|:--:|\n")

    any_rows = False

    for d in problem_dirs:
        found = scan_problem_folder(d)

        # skip random folders that aren't problems
        if not (found["py"] or found["cpp"] or found["notes"]):
            continue

        any_rows = True
        problem = d.name

        py_cell = md_link(found["py"].name, repo_root, found["py"]) if found["py"] else "null"
        cpp_cell = md_link(found["cpp"].name, repo_root, found["cpp"]) if found["cpp"] else "null"
        notes_cell = md_link("NOTES", repo_root, found["notes"]) if found["notes"] else "null"
        folder_cell = md_link("open", repo_root, d)

        out.append(f"| {problem} | {py_cell} | {cpp_cell} | {notes_cell} | {folder_cell} |\n")

    if not any_rows:
        out.append("| (none yet) | null | null | null | null |\n")

    return "".join(out)


def ensure_readme_has_markers(readme_path: Path) -> list[str]:
    if readme_path.exists():
        lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    else:
        lines = [
            "# leetcode-solutions\n\n",
            "## Solutions\n\n",
            f"{START}\n",
            f"{END}\n",
        ]

    stripped = [ln.strip() for ln in lines]
    if START not in stripped or END not in stripped:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines += ["\n", "## Solutions\n\n", f"{START}\n", f"{END}\n"]

    return lines


def replace_block(lines: list[str], new_block: str) -> list[str]:
    start_idx = next(i for i, ln in enumerate(lines) if ln.strip() == START)
    end_idx = next(i for i, ln in enumerate(lines) if ln.strip() == END)

    if end_idx < start_idx:
        raise RuntimeError("README marker order invalid: END appears before START.")

    out = []
    out.extend(lines[: start_idx + 1])
    out.append("\n")
    out.append(new_block)
    out.append("\n")
    out.extend(lines[end_idx:])
    return out


def main() -> None:
    repo_root = Path(".").resolve()
    readme_path = repo_root / "README.md"

    lines = ensure_readme_has_markers(readme_path)
    table = generate_table(repo_root)
    updated = replace_block(lines, table)

    readme_path.write_text("".join(updated), encoding="utf-8")


if __name__ == "__main__":
    main()
