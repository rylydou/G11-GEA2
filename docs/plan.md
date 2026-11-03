# Team Plan: GEA2

See `overview.md` for the full assignment summary. This doc covers **who does what**.

**How to use:** Put your name in a role, check off tasks as you finish them, and post in the group chat when something someone else needs is ready.

## Roles

| Role | Name | What you do | Depends on | You deliver |
|---|---|---|---|---|
| **P1: Inversions** | _________ | Write the brute-force counter and the mergesort counter. Validate them against each other: 10+ hand arrays and 200+ random arrays. Write the correctness explanation and complexity analysis. | Nobody | Both counters, validation tests, report section for Part 1A and the Part 1B validation |
| **P2: Recursive Coin Solvers** | _________ | Write the greedy, naive recursion, and memoized DP solvers, with counters for calls, distinct states, and cache hits. Run Exp 1 (repeated subproblems). Write the complexity analysis for these 3 solvers. | Nobody | 3 solvers, Exp 1 script, CSV, and table/plot, report section for 2A (these solvers) and 2C Exp 1 |
| **P3: Bottom-Up DP + Timing** | _________ | Write the bottom-up DP and its complexity analysis. Benchmark both inversion counters and find the crossover point. Run Exp 2 (pseudo-polynomial scaling). Write the README. | **P1** (counters for the benchmark) | Bottom-up solver, benchmark and Exp 2 scripts, CSVs, and plots, report section for 2A (bottom-up), the 1B runtime results, and 2C Exp 2, README |
| **P4: Coin Checker + Integrator** | _________ | Write the solution validator and the shared coin test cases. Cross-check the exact solvers: 10+ hand cases and 100+ random cases. Build the greedy counterexample search, find 3+ failures, and explain one. Merge the final report. | **P2** (greedy, naive, memo) and **P3** (bottom-up) | Validator, coin test cases, validation tests, counterexample search and results, report section for 2B, final merged report |

## Before Anyone Starts (Whole Team)

The code scaffold is already in the repo, in `src/`. Setup steps are in `README.md`.

- [ ] Everyone runs `pip install -r requirements.txt`, then `pytest` (unfinished parts fail with `NotImplementedError`)
- [ ] Read the comment at the top of `src/helpers.py` (coin result format and `stats` counters)
- [ ] Random-seed rule: use `random.Random(SEED)` (`SEED` is in `helpers.py`), never the global `random`

### Your Files (all in `src/`)

**Only edit files you own.** Fill in the `TODO(P#)` stubs, then make your tests pass. If you need a change in someone else's file, ask them.

| Role | Code | Tests | Experiment script |
|---|---|---|---|
| P1 | `inversions.py` | `test_inversions.py` | none |
| P2 | `greedy.py`, `recursive.py` (naive + memo) | `test_greedy.py`, `test_recursive.py` | `exp1_repeated_subproblems.py` |
| P3 | `bottom_up.py` | `test_bottom_up.py` | `benchmark_inversions.py`, `exp2_pseudo_polynomial.py` |
| P4 | `validate.py`, `coin_cases.py` (shared test cases) | `test_validate.py` | `counterexamples.py` |
| Shared | `helpers.py`: already finished (seeds, random inputs, `time_median`, `save_csv`, `IMPOSSIBLE`, `new_stats`). Ask the team before changing it. | | |

P2 and P3 tests read the hand cases from P4's `coin_cases.py`, but never edit it.

### Shared Function Signatures

```python
# inversions.py (P1)
brute_force(arr) -> int
sort_and_count(arr) -> (sorted_arr, count)

# greedy.py, recursive.py (P2) | bottom_up.py (P3) | validate.py (P4)
IMPOSSIBLE = None                      # from helpers.py
greedy(D, A)                -> (count, coins) | IMPOSSIBLE
naive(D, A, stats=None)     -> (count, coins) | IMPOSSIBLE
memo(D, A, stats=None)      -> (count, coins) | IMPOSSIBLE
bottom_up(D, A, stats=None) -> (count, coins) | IMPOSSIBLE
is_valid(D, A, result)      -> True / False
# stats = new_stats() from helpers.py: calls, distinct_states, cache_hits, states_processed
```

## Part III Reflection Split

| Question | Owner |
|---|---|
| Q1: What work does D&C avoid? | P1 |
| Q2: Why are inversion subproblems independent but coin subproblems overlap? | P3 |
| Q3: What role does sorting play? | P1 |
| Q4: Same recurrence, why such different runtimes? | P2 |
| Q5: How did baselines help validate? | P4 |
| Q6: When to try D&C vs. DP? | Everyone drafts a few sentences, P4 merges |

## Progress Tracker

**P1: Inversions**
- [ ] Brute-force counter
- [ ] Mergesort counter (returns the sorted array and the count)
- [ ] 10+ hand-checked arrays
- [ ] 200+ random cross-checks pass
- [ ] Correctness explanation
- [ ] Complexity analysis
- [ ] Part III Q1 and Q3

**P2: Recursive Coin Solvers**
- [ ] Greedy
- [ ] Naive recursion
- [ ] Memoized DP with reconstruction
- [ ] Counters (calls, distinct states, cache hits)
- [ ] Exp 1 run, with the safety cutoff documented
- [ ] Complexity analysis (greedy, naive, memo)
- [ ] Part III Q4

**P3: Bottom-Up DP + Timing**
- [ ] Bottom-up DP with reconstruction and a states counter
- [ ] Fair timing setup (sizes, repeats, brute-force cutoff), using `time_median` from `helpers.py`
- [ ] Inversion benchmark, plot, and crossover point
- [ ] Exp 2 run (A = 2^8, 2^9, ...)
- [ ] Complexity analysis (bottom-up)
- [ ] README (Python version, setup, exact commands to reproduce results)
- [ ] Part III Q2

**P4: Coin Checker + Integrator**
- [ ] Solution validator (coins sum to A and the count matches)
- [ ] 10+ hand cases (target 0, impossible, multiple optimal answers)
- [ ] 100+ random cross-checks pass
- [ ] Greedy counterexample search finds `D={1,3,4}, A=6`
- [ ] 3+ counterexamples, with one explained
- [ ] Part III Q5, then merge Q6
- [ ] Introduction, then final `REPORT.md` merged (8 pages max) and all TODO blocks removed
- [ ] `docs/ai_use.md` merged

**Everyone**
- [ ] Your sections of `REPORT.md` written, within their word targets
- [ ] Your line in the Contribution Statement (end of `REPORT.md`)
- [ ] Your rows in `docs/ai_use.md` (tools used, what they produced, how you checked it)
