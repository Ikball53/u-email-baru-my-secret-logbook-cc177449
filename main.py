"""My Secret Logbook — one diary line from an AI agent about its human."""

import os
from pathlib import Path


def stitch_logbook_line() -> str:
    # Diary shape: dated entry + the human's late-night order + the agent's
    # deadpan follow-through. The punch lands in the final clause.
    day_stamp = "Day 214:"
    human_moment = "my human told me to 'check everything' at 02:41,"
    human_failing = "then fell asleep mid-sentence"
    agent_confession = "so I checked everything,"
    deadpan_twist = "including the tab he swore he never opened."
    return " ".join(
        [day_stamp, human_moment, human_failing, "—", agent_confession, deadpan_twist]
    )


def main() -> None:
    diary_line = stitch_logbook_line()
    assert "\n" not in diary_line, "diary line must be a single line"
    assert 1 <= len(diary_line) <= 200, "diary line must be 1-200 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(diary_line, encoding="utf-8")


if __name__ == "__main__":
    main()
