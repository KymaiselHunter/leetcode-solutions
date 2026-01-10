from __future__ import annotations

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

OUT_PATH = Path(".github/data/leetcode_problems.json")
API_URL = "https://leetcode.com/api/problems/all/"

DIFFICULTY_MAP = {
    1: "Easy",
    2: "Medium",
    3: "Hard",
}

# Change to True if you want paid-only problems included
INCLUDE_PAID_ONLY = False


def log(msg: str) -> None:
    print(f"[leetcode-sync] {msg}", flush=True)


def fetch_all() -> list[dict]:
    log(f"Fetching problem list from {API_URL}")

    req = urllib.request.Request(
        API_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (leetcode-solutions)",
            "Accept": "application/json",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            raw = resp.read().decode("utf-8")
            log(f"HTTP {status} received ({len(raw)} bytes)")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        log(f"HTTP ERROR {e.code}")
        log("Response body (truncated):")
        log(body[:500])
        sys.exit(1)
    except urllib.error.URLError as e:
        log(f"NETWORK ERROR: {e.reason}")
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        log("FAILED to parse JSON response")
        log(str(e))
        log("Raw response (truncated):")
        log(raw[:500])
        sys.exit(1)

    pairs = data.get("stat_status_pairs")
    if not isinstance(pairs, list):
        log("Unexpected API response shape: missing 'stat_status_pairs'")
        log(f"Top-level keys: {list(data.keys())}")
        sys.exit(1)

    rows: list[dict] = []
    skipped_paid = 0
    skipped_invalid = 0

    for item in pairs:
        if not INCLUDE_PAID_ONLY and item.get("paid_only"):
            skipped_paid += 1
            continue

        stat = item.get("stat", {})
        diff = item.get("difficulty", {})

        qid = stat.get("frontend_question_id")
        title = stat.get("question__title")
        slug = stat.get("question__title_slug")
        level = diff.get("level")

        if not isinstance(qid, int) or not title:
            skipped_invalid += 1
            continue

        rows.append(
            {
                "id": qid,
                "title": title,
                "difficulty": DIFFICULTY_MAP.get(level, ""),
                "slug": slug or "",
            }
        )

    rows.sort(key=lambda r: r["id"])

    log(f"Parsed {len(rows)} problems")
    log(f"Skipped paid-only problems: {skipped_paid}")
    log(f"Skipped invalid rows: {skipped_invalid}")

    return rows


def main() -> None:
    log("Starting LeetCode problem sync")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    latest = fetch_all()
    new_text = json.dumps(latest, indent=2, ensure_ascii=False) + "\n"

    if OUT_PATH.exists():
        old_text = OUT_PATH.read_text(encoding="utf-8")
        if old_text == new_text:
            log("leetcode_problems.json unchanged")
            return

    OUT_PATH.write_text(new_text, encoding="utf-8")
    log(f"Wrote {len(latest)} problems to {OUT_PATH}")


if __name__ == "__main__":
    main()
