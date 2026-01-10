from __future__ import annotations

from pathlib import Path

START = "<!-- SOLUTIONS:START -->"
END = "<!-- SOLUTIONS:END -->"

# Top-level folders to ignore
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


def md_link(text: str, path: Path) -> str:
    return f"[{text}]({path.as_posix()})"


def pick_best(files: list[Path]) -> Path | None:
    """
    Choose a 'best' solution file if multiple exist.
    Preference: shortest name, then alphabetical.
    """
    if not files:
        return None
    return sorted(files, key=lambda p: (len(p.name), p.name.lower()))[0]


def scan_problem_folder(folder: Path) -> dict[str, Path | None]:
    """
    Returns paths (relative-to-repo) for:
      - python solution
      - cpp solution
      - notes/readme inside the folder (optional)
    """
    py_files = []
    cpp_files = []
    notes = None

    # Only scan files directly inside the folder (matches your screenshot)
    for p in folder.iterdir():
        if not p.is_file():
            continue

        if p.suffix in PY_EXTS:
            py_files.append(p)
        elif p.suffix in CPP_EXTS:
            cpp_files.append(p)
        elif p.name.lower() == "notes.md":
            notes = p

    return {
        "py": pick_best(py_files),
        "cpp": pick_best(cpp_files),
        "notes": notes,
    }


def generate_table(repo_root: Path) -> str:
    rows = []

    # Identify top-level problem folders
    problem_dirs = []
    for p in repo_root.iterdir():
        if not p.is_dir():
            continue
        if p.name in IGNORE_DIRS:
            continue
        if p.name.startswith("."):
            continue
        problem_dirs.append(p)

    # Sort folders alphabetically (clean + predictable)
    problem_dirs = sorted(problem_dirs, key=lambda d: d.name.lower())

    # Table header
    out = []
    out.append("| Problem | Python | C++ | Notes | Folder |\n")
    out.append("|:--|:--:|:--:|:--:|:--:|\n")

    for d in problem_dirs:
        found = scan_problem_folder(d)

        # Skip folders that clearly aren't problems (no solutions + no notes)
        if not (found["py"] or found["cpp"] or found["notes"]):
            continue

        problem = d.name
        py_cell = md_link(found["py"].name, found["py"]) if found["py"] else ""
        cpp_cell = md_link(found["cpp"].name, found["cpp"]) if found["cpp"] else ""
        notes_cell = md_link("NOTES", found["notes"]) if found["notes"] else ""
        folder_cell = md_link("open", d)

        out.append(f"| {problem} | {py_cell} | {cpp_cell} | {notes_cell} | {folder_cell} |\n")

    # If empty, keep a placeholder row
    if len(out) == 2:
        out.append("| (none yet) |  |  |  |  |\n")

    return "".join(out)


def ensure_readme_has_markers(readme_path: Path) -> list[str]:
    if readme_path.exists():
        lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    else:
        # Create a minimal README if it doesn't exist
        lines = [
            "# leetcode-solutions\n\n",
            "## LeetCode\n\n",
            f"{START}\n",
            f"{END}\n",
        ]

    stripped = [ln.strip() for ln in lines]
    if START not in stripped or END not in stripped:
        # Append markers if user had a custom README without them
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines += ["\n", "## LeetCode\n\n", f"{START}\n", f"{END}\n"]

    return lines


def replace_block(lines: list[str], new_block: str) -> list[str]:
    start_idx = next(i for i, ln in enumerate(lines) if ln.strip() == START)
    end_idx = next(i for i, ln in enumerate(lines) if ln.strip() == END)

    if end_idx < start_idx:
        raise RuntimeError("README marker order invalid: END appears before START.")

    out = []
    out.extend(lines[: start_idx + 1])  # include START line
    out.append("\n")
    out.append(new_block)
    out.append("\n")
    out.extend(lines[end_idx:])  # include END line and everything after
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
