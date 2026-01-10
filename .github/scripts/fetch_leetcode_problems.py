from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path


OUT_PATH = Path(".github/data/leetcode_problems.json")
GRAPHQL_URL = "https://leetcode.com/graphql"

# LeetCode’s site uses this query for problem lists.
QUERY = """
query problemsetQuestionList($categorySlug: String, $skip: Int, $limit: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: problemsetQuestionList(categorySlug: $categorySlug, skip: $skip, limit: $limit, filters: $filters) {
    total: total
    questions: questions {
      title
      titleSlug
      difficulty
      frontendQuestionId
    }
  }
}
"""

# Pagination settings
LIMIT = 100
SLEEP_SECONDS = 0.25  # be polite


def post_graphql(payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            # User-Agent matters sometimes; keep it simple
            "User-Agent": "github-actions-bot/leetcode-solutions",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body)


def fetch_all() -> list[dict]:
    all_rows: list[dict] = []

    skip = 0
    total = None

    while True:
        payload = {
            "query": QUERY,
            "variables": {
                "categorySlug": "",
                "skip": skip,
                "limit": LIMIT,
                "filters": {},  # can add tags/difficulty filters later
            },
        }

        res = post_graphql(payload)

        if "errors" in res:
            raise RuntimeError(f"GraphQL errors: {res['errors']}")

        block = res["data"]["problemsetQuestionList"]
        if total is None:
            total = int(block["total"])

        questions = block["questions"] or []
        if not questions:
            break

        for q in questions:
            # Some fields come back as strings; normalize carefully
            fid = q.get("frontendQuestionId")
            try:
                fid_int = int(fid) if fid is not None else None
            except ValueError:
                fid_int = None

            all_rows.append(
                {
                    "id": fid_int,
                    "title": q.get("title", ""),
                    "difficulty": q.get("difficulty", ""),
                    "slug": q.get("titleSlug", ""),
                }
            )

        skip += LIMIT
        if total is not None and skip >= total:
            break

        time.sleep(SLEEP_SECONDS)

    # Drop any bad rows and sort by id
    cleaned = [r for r in all_rows if isinstance(r.get("id"), int) and r.get("title")]
    cleaned.sort(key=lambda r: r["id"])
    return cleaned


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    latest = fetch_all()
    new_text = json.dumps(latest, indent=2, ensure_ascii=False) + "\n"

    if OUT_PATH.exists():
        old_text = OUT_PATH.read_text(encoding="utf-8")
        if old_text == new_text:
            print("leetcode_problems.json unchanged.")
            return

    OUT_PATH.write_text(new_text, encoding="utf-8")
    print(f"Wrote {len(latest)} problems to {OUT_PATH}")


if __name__ == "__main__":
    main()
