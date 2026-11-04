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
| _ | _ | _ |

## Contributions and Verification

One row per meaningful use. Say what the AI produced, what a human changed, and how it was checked.

| Member | Part / file | What AI produced | What we changed | How we verified it |
|---|---|---|---|---|
| _________ | Setup: `docs/overview.md`, `docs/plan.md`, `README.md`, `AGENTS.md`, `REPORT.md` skeleton, this template | Assignment summary, team plan, report outline | _ | TODO: checked against `docs/assignment.pdf` |
| _________ | Setup: `src/` scaffold | Finished `helpers.py` (seeded generators, `time_median`, `save_csv`); function stubs; all test files; `coin_cases.py` hand cases + BFS answer key; experiment script outlines | _ | TODO: hand-check every expected value in `test_inversions.py` and `coin_cases.py`; review `helpers.py` |
| Ryly Dou | P2: `greedy.py`, `recursive.py` | All of `greedy`, `naive`, and `memo`, including the stats counters, coin-list rebuild, and recursion-limit raise | Nothing so far | `pytest src/test_greedy.py src/test_recursive.py`: 22 passed. Extra check: on 500 seeded random cases, naive and memo matched the BFS answer key in `coin_cases.py`, and memo's `calls == distinct_states + cache_hits` held every time. Memo ran on A = 100,000 and its coins summed to A. TODO(P2): hand-trace D = {1, 3, 4}, A = 6 through both solvers |
| Ryly Dou | P2: `exp1_repeated_subproblems.py`, `results/exp1_repeated_subproblems.*` | Experiment script (D = {1, 3, 4}, A = 0..60 step 2, 10^7-call cutoff), CSV, and plot | Nothing so far | Ran it, then checked the CSV with a script: memo calls = 3A − 4 for every A ≥ 4, and naive and memo reached the same number of distinct amounts at every A. TODO(P2): look over the plot and spot-check a few CSV rows |
| Ryly Dou | P2: `REPORT.md` 3.1, 3.2 (greedy, naive, memo rows), 3.5, Table 5, Q4; Q6 draft | Section text, complexity rows, figure caption | Nothing so far | Every number in the text and in Table 5 was compared with `results/exp1_repeated_subproblems.csv`. TODO(P2): re-derive the Table 2 bounds by hand (naive O(k^(A/d_min)) calls and O(A²) space; memo O(kA)) |
| _________ | _ | _ | _ | _ |

## Members Who Used No Generative AI

> TODO · List names, or delete this section if everyone used AI.

## Limitations and Errors Caught

> TODO · Optional but useful: any wrong or misleading AI output we found, and how we caught it.

- P2, Experiment 1: the first version timed one run with the counters on. One memo point (A = 40)
  came out more than 60× slower than the points on either side of it. The timing was changed to the median of 3
  runs with the counters off (`time_median`), and the outlier went away.
