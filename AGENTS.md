# AGENTS.md

CMP_SC 4050 group assignment (4 people): inversion counting (divide and conquer) and coin change (dynamic programming).

## Start here

1. `docs/overview.md`: what the assignment asks for (the full spec is `docs/assignment.pdf`).
2. `docs/plan.md`: roles P1-P4, which files each role owns, and progress checklists.
3. `README.md`: setup, the file table, and run commands.
4. `src/helpers.py`: the shared coin result format (`IMPOSSIBLE`, the `stats` counters) is documented at the top.

## Layout

All code is flat in `src/`: modules, tests (`test_*.py`), and experiment scripts. There's no packaging,
so modules import each other directly (`from helpers import SEED`). Output CSVs and PNGs go in `results/`
(committed, since they're a deliverable).

## Report

- `REPORT.md` is the report we turn in. Each `> TODO(P#)` block says who writes it, what to
  cover, and a word target. Find what's left with `grep -n "TODO(" REPORT.md`.
- **Page limit: about 6-8 pages, and 8 is the hard cap.** The budget is about 2,600 words + 3 figures +
  5 tables. Keep each section within its word target, and cut rather than add.
- Figures are embedded from `results/*.png`. Use only numbers from our `results/*.csv`. Never make up
  or estimate results.
- `AI_USE.md` is the AI Use Statement template. The Contribution Statement is at the end of
  `REPORT.md`. Neither counts toward the page limit.
- Writing Style: Keep language plain, simple and most importantly concise. Don't ramble or include irrelevant information. Use simple language that everyone can understand while being sure to fit the requirements of the assignment.

## Commands (from repo root)

```bash
source .venv/bin/activate        # or: python3 -m venv .venv && pip install -r requirements.txt
pytest                           # all tests
pytest src/test_recursive.py     # one owner's tests
python src/<script>.py           # run an experiment
```

Unfinished stubs raise `NotImplementedError("P#: name")` and their tests fail. That's expected.

## Rules

- **Find out which role (P1-P4) you're working for, and edit only that role's files** (see the table in
  `docs/plan.md`). `helpers.py` is finished and shared, so don't change it without asking. `coin_cases.py` belongs to P4.
- Keep it simple: small functions, short `#` comments, Python 3.10+, standard library plus matplotlib and pytest.
  Don't add packaging, config files, or new dependencies.
- Use `random.Random(SEED)` for randomness, never the global `random` module.
- Keep timing separate from input generation, plotting, and file I/O.
- Don't weaken or delete tests to make them pass. A failing test means the code is wrong, or the test needs
  discussing with its owner.
- Testing doesn't prove correctness. Don't write claims like that into the report or comments.
- AI use must be disclosed. When you generate code or text, tell the user so they can add a row to
  `docs/ai_use.md` and verify it independently.
