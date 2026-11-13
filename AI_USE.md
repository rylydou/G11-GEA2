# AI Use Statement

## Tools

| Tool (model) | Used by |
|---|---|
| Claude Code (Claude Opus 5.5) | Ryly Dou (setup, P2, final review), Prajit (P3), Micky Sheridan (P4) |
| Antigravity (Gemini 3.8 Flash) | Solomon Canoy (P1) |

## How We Used It and How We Checked It

AI wrote most of the code, tests, and experiment scripts, and first drafts of the report. We did
not treat its output as evidence of correctness. Every fast algorithm was checked against a
separately written slow one (brute force for inversions; naive recursion and a BFS answer key for
coins) on hand-checked and seeded random inputs, all 79 tests pass, and every number in the report
was compared with our own CSVs.

| Member | What AI produced | How we checked it |
|---|---|---|
| Solomon Canoy | Inversion counters, extra test cases, drafts of 2.1–2.4, Q1, Q3 | Reviewed the algorithm logic and rewrote the induction proof. 27 tests pass (12 hand arrays, 200 random arrays) |
| Ryly Dou | Setup: assignment summary, team plan, report outline, `helpers.py`, stubs, starter tests and hand cases | The 12 hand cases match the separate BFS answer key, and every solver passes against them |
| Ryly Dou | `greedy`, `naive`, `memo` with counters; Experiment 1; drafts of 3.1, 3.2, 3.5, Q4 | 22 tests pass. On 500 extra seeded cases, naive and memo matched the BFS key and memo's calls = distinct states + cache hits. Checked the CSV by script (memo calls = 3A − 4) |
| Prajit | `bottom_up` and tests; inversion benchmark; Experiment 2; README; drafts of 2.5, 3.6, Q2 | 12 tests pass. Hand-traced D = {1, 3, 4}, A = 6. Checked inputs are built before timing. Recomputed the crossover and slopes from the CSV with a separate script |
| Micky Sheridan | `is_valid`, 4 hand cases, validator tests, counterexample search; drafts of 1, 3.3, 3.4, Q5, Q6 merge | Planted 8 bugs in a scratch copy; the tests caught all 8. Re-checked every counterexample row against the BFS key, and a recount gave the same 322. Table 3 came from real solver runs |
| Ryly Dou | Final review of the report: fixed the merge proof (2.2) and complexity wording (2.3), changed the LaTeX math in Part I to plain text, shortened this statement and the Contribution Statement | Recomputed every report number from the CSVs with a script |

## Errors Caught

- Experiment 1: timing one run with counters on gave a 60× outlier. Fixed by timing the median of
  3 runs with counters off.
- Experiment 2: an AI-written comment gave a fake greedy failure. Replaced with a real one
  (A = 15) found by running `greedy` against `bottom_up`.
- Experiment 2: one noisy point at 5 repeats, so repeats were raised to 7. The next run was kept
  as measured.
- `is_valid` tests missed a too-small count. A mutation check found it, and an assert was added.
