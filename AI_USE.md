# AI Use Statement

_Required deliverable. Everyone adds their own rows. P4 merges this into the final submission._

<!--
The assignment requires us to: name the tools used, describe how they contributed, and explain how
we verified the resulting code, claims, and experiments. "AI output is not evidence of correctness."
If a member used no generative AI, say so explicitly in their row.
Delete this comment and the TODO lines before submitting.
-->

## Summary

> TODO(P4) · 2–4 sentences. Which tools the group used, what for in general, and the main way we
> verified their output (independent baselines, hand-checked cases, seeded random cross-checks,
> reviewing derivations by hand).

## Tools Used

| Tool (and model/version) | Used by | Used for |
|---|---|---|
| Claude Code (Claude Opus 5.5) | _________ | Project setup: see the first row below |
| Claude Code (Claude Opus 5.5) | Ryly Dou | P2: coin solvers (greedy, naive, memo), Experiment 1, report sections 3.1, 3.2, 3.5, Q4, and the Q6 draft |
| Antigravity (Gemini 3.8 Flash) | Solomon Canoy | P1: inversions implementation, test case expansion, report sections 2.1–2.4, Q1, Q3, and Q6 draft |
| Claude Code (Claude Opus 5.5 | Prajit | P3: bottom-up solver and tests, inversion benchmark, Experiment 2, README, report sections 2.5, 3.1–3.2 (bottom-up), 3.6, Q2, and the Q6 draft |

## Contributions and Verification

One row per meaningful use. Say what the AI produced, what a human changed, and how it was checked.

| Member | Part / file | What AI produced | What we changed | How we verified it |
|---|---|---|---|---|
| _________ | Setup: `docs/overview.md`, `docs/plan.md`, `README.md`, `AGENTS.md`, `REPORT.md` skeleton, this template | Assignment summary, team plan, report outline | _ | TODO: checked against `docs/assignment.pdf` |
| _________ | Setup: `src/` scaffold | Finished `helpers.py` (seeded generators, `time_median`, `save_csv`); function stubs; all test files; `coin_cases.py` hand cases + BFS answer key; experiment script outlines | _ | TODO: hand-check every expected value in `test_inversions.py` and `coin_cases.py`; review `helpers.py` |
| Ryly Dou | P2: `greedy.py`, `recursive.py` | All of `greedy`, `naive`, and `memo`, including the stats counters, coin-list rebuild, and recursion-limit raise | Nothing so far | `pytest src/test_greedy.py src/test_recursive.py`: 22 passed. Extra check: on 500 seeded random cases, naive and memo matched the BFS answer key in `coin_cases.py`, and memo's `calls == distinct_states + cache_hits` held every time. Memo ran on A = 100,000 and its coins summed to A. TODO(P2): hand-trace D = {1, 3, 4}, A = 6 through both solvers |
| Ryly Dou | P2: `exp1_repeated_subproblems.py`, `results/exp1_repeated_subproblems.*` | Experiment script (D = {1, 3, 4}, A = 0..60 step 2, 10^7-call cutoff), CSV, and plot | Nothing so far | Ran it, then checked the CSV with a script: memo calls = 3A − 4 for every A ≥ 4, and naive and memo reached the same number of distinct amounts at every A. TODO(P2): look over the plot and spot-check a few CSV rows |
| Ryly Dou | P2: `REPORT.md` 3.1, 3.2 (greedy, naive, memo rows), 3.5, Table 5, Q4; Q6 draft | Section text, complexity rows, figure caption | Nothing so far | Every number in the text and in Table 5 was compared with `results/exp1_repeated_subproblems.csv`. TODO(P2): re-derive the Table 2 bounds by hand (naive O(k^(A/d_min)) calls and O(A²) space; memo O(kA)) |
| Prajit | P3: `bottom_up.py`, `test_bottom_up.py` | All of `bottom_up` (table fill, `choice[]` rebuild, `states_processed` counter) and two extra tests (D = {4, 7} with unreachable amounts, and A = 2^16) | Nothing so far | `pytest src/test_bottom_up.py`: 12 passed (8 hand cases, 100 seeded random cases against the BFS answer key in `coin_cases.py`, states = A + 1, the two extra tests). Spot checks: D = {1, 3, 4}, A = 6 gives (2, [3, 3]); D = {3, 5}, A = 9 gives (3, [3, 3, 3]). TODO(P3): hand-trace the best[] and choice[] tables for D = {1, 3, 4}, A = 6 |
| Prajit | P3: `benchmark_inversions.py`, `results/benchmark_inversions.*` | Script (sizes, 7 repeats, 1 s brute-force cutoff, crossover finder, log-log slope fit), CSV, and plot | Nothing so far | Ran it. Checked that arrays are built before `time_median` so only the call is timed. Recomputed the crossover (n = 48) and slopes (2.04, 1.11) from the CSV with a separate script. Timed a second full run into a scratch folder. TODO(P3): look over the plot and spot-check a few CSV rows |
| Prajit | P3: `exp2_pseudo_polynomial.py`, `results/exp2_pseudo_polynomial.*` | Script (D = {1, 5, 12, 19}, A = 2^8..2^22), CSV, and two-panel plot | Repeats raised from 5 to 7 after a noisy point (see below) | Checked from the CSV that states_processed = A + 1 in every row, and computed the time ratio for each doubling (1.7× to 2.9×). The greedy failure quoted for this D (A = 15) was found by running `greedy` against `bottom_up`. TODO(P3): look over the plot |
| Prajit | P3: `REPORT.md` 2.5, 3.1 and 3.2 (bottom-up, Table 2 row), 3.6, Table 6, Figure 1 and 3 captions, Q2, Q6 draft; `README.md` | Section text, complexity row, captions, README machine table and reproduce steps | Nothing so far | Every number in the text and Tables 2 and 6 was compared with `results/benchmark_inversions.csv` and `results/exp2_pseudo_polynomial.csv`. TODO(P3): re-derive Θ(kA) time and Θ(A) space for bottom-up by hand, and reread the sections |
| Solomon Canoy | P1: `src/inversions.py`, `src/test_inversions.py`, `REPORT.md` | Initial code for `brute_force`, `merge_and_count`, and `sort_and_count`; additional test cases; report sections 2.1–2.4, Q1, and Q3 drafts | Reviewed and verified algorithm logic, adjusted inductive proof, formatted Table 1, and ensured word targets | Ran pytest suite (27 passed: 12 hand-checked arrays and 200 random arrays); verified against assignment rubric |

## Members Who Used No Generative AI

> TODO · List names, or delete this section if everyone used AI.

## Limitations and Errors Caught

> TODO · Optional but useful: any wrong or misleading AI output we found, and how we caught it.

- P2, Experiment 1: the first version timed one run with the counters on. One memo point (A = 40)
  came out more than 60× slower than the points on either side of it. The timing was changed to the median of 3
  runs with the counters off (`time_median`), and the outlier went away.
- P3, Experiment 2: the first draft of the comment explaining the coin set had a made-up greedy
  failure that wasn't one (it listed the same coins for greedy and the best answer). It was
  replaced with a real one (A = 15) found by running `greedy` against `bottom_up`.
- P3, Experiment 2: a run with 5 repeats had one noisy point (A = 2,048 at 440 ns per state, vs
  about 300 ns for its neighbors). Repeats were raised to 7 to match the inversion benchmark, and
  the next run was kept as it came out. It has its own high point (A = 65,536 at 423 ns per state),
  which is reported as measured.
