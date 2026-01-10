from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

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

DATA_PATH = Path(".github/data/leetcode_problems.json")


def normalize_title(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


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

    for p in folder.iterdir():
        if not p.is_file():
            continue
        if p.suffix in PY_EXTS:
            py_files.append(p)
        elif p.suffix in CPP_EXTS:
            cpp_files.append(p)

    return {"py": pick_best(py_files), "cpp": pick_best(cpp_files)}


def load_problem_map(repo_root: Path) -> dict[str, dict[str, Any]]:
    """
    Optional mapping file.
    Returns: normalized_title -> { id: int, difficulty: str }
    """
    path = repo_root / DATA_PATH
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

    out: dict[str, dict[str, Any]] = {}

    # Support two formats:
    # 1) list of objects: [{"id":1,"title":"Two Sum","difficulty":"Easy"}, ...]
    # 2) dict mapping: {"two sum": {"id":1,"difficulty":"Easy"}, ...}
    if isinstance(data, list):
        for row in data:
            if not isinstance(row, dict):
                continue
            title = row.get("title")
            pid = row.get("id")
            diff = row.get("difficulty")
            if not title:
                continue
            key = normalize_title(str(title))
            out[key] = {
                "id": pid if isinstance(pid, int) else None,
                "difficulty": str(diff) if diff is not None else None,
            }
    elif isinstance(data, dict):
        for k, v in data.items():
            if not isinstance(v, dict):
                continue
            key = normalize_title(str(k))
            pid = v.get("id")
            diff = v.get("difficulty")
            out[key] = {
                "id": pid if isinstance(pid, int) else None,
                "difficulty": str(diff) if diff is not None else None,
            }

    return out


def generate_table(repo_root: Path) -> str:
    problem_map = load_problem_map(repo_root)

    problem_dirs: list[Path] = []
    for p in repo_root.iterdir():
        if not p.is_dir():
            continue
        if p.name in IGNORE_DIRS or p.name.startswith("."):
            continue
        problem_dirs.append(p)

    rows = []

    for d in problem_dirs:
        found = scan_problem_folder(d)
        if not (found["py"] or found["cpp"]):
            continue

        title = d.name
        key = normalize_title(title)
        meta = problem_map.get(key)

        pid = meta.get("id") if meta else None
        diff = meta.get("difficulty") if meta else None

        # Blank if unknown (your request)
        pid_display = str(pid) if isinstance(pid, int) else ""
        diff_display = diff if isinstance(diff, str) else ""

        py_cell = md_link(found["py"].name, repo_root, found["py"]) if found["py"] else "null"
        cpp_cell = md_link(found["cpp"].name, repo_root, found["cpp"]) if found["cpp"] else "null"
        folder_cell = md_link("OPEN", repo_root, d)

        # Sort key: known IDs first by number, unknowns at the end.
        sort_key = (0, pid) if isinstance(pid, int) else (1, 10**9)

        rows.append(
            {
                "sort_key": sort_key,
                "id": pid_display,
                "problem": title,
                "difficulty": diff_display,
                "py": py_cell,
                "cpp": cpp_cell,
                "folder": folder_cell,
            }
        )

    # Known IDs first, then unknown at bottom. Stable tie-breaker by name.
    rows.sort(key=lambda r: (r["sort_key"], r["problem"].lower()))

    out: list[str] = []
    out.append("| # | Problem | Difficulty | Python | C++ | Folder |\n")
    out.append("|---:|:--|:--:|:--:|:--:|:--:|\n")

    if not rows:
        out.append("|  | (none yet) |  | null | null | null |\n")
        return "".join(out)

    for r in rows:
        out.append(
            f"| {r['id']} | {r['problem']} | {r['difficulty']} | {r['py']} | {r['cpp']} | {r['folder']} |\n"
        )

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
        lines += ["\n", "## Solutions\n\n", f"{START}\n", f"{END}\n"]

    return lines


def replace_block(lines: list[str], new_block: str) -> list[str]:
    start_idx = next(i for i, ln in enumerate(lines) if ln.strip() == START)
    end_idx = next(i for i, ln in enumerate(lines) if ln.strip() == END)

    if end_idx < start_idx:
        raise RuntimeError("README marker order invalid: END appears before START.")

    out: list[str] = []
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
