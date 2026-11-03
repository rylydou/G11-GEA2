# Team Plan: GEA2

See `overview.md` for the full assignment summary. This doc covers **who does what**.

**How to use:** Put your name in a role, check off tasks as you finish them, and post in the group chat when something someone else needs is ready.

## Roles

| Role | Name | What you do | Depends on | You deliver |
|---|---|---|---|---|
| **P1: Inversions** | _________ | Write the brute-force counter and the mergesort counter. Validate them against each other: 10+ hand arrays and 200+ random arrays. Write the correctness explanation and complexity analysis. | Nobody | Both counters, validation tests, report section for Part 1A and the Part 1B validation |
| **P2: Recursive Coin Solvers** | _________ | Write the greedy, naive recursion, and memoized DP solvers, with counters for calls, distinct states, and cache hits. Run Exp 1 (repeated subproblems). Write the complexity analysis for these 3 solvers. | Nobody | 3 solvers, Exp 1 script, CSV, and table/plot, report section for 2A (these solvers) and 2C Exp 1 |
| **P3: Bottom-Up DP + Timing** | _________ | Write the bottom-up DP and its complexity analysis. Build the shared timing harness. Benchmark both inversion counters and find the crossover point. Run Exp 2 (pseudo-polynomial scaling). | **P1** (counters for the benchmark) | Bottom-up solver, timing harness, benchmark and Exp 2 scripts, CSVs, and plots, report section for 2A (bottom-up), the 1B runtime results, and 2C Exp 2 |
| **P4: Coin Checker + Integrator** | _________ | Write the solution validator. Cross-check the exact solvers: 10+ hand cases and 100+ random cases. Build the greedy counterexample search, find 3+ failures, and explain one. Write the README. Merge the final report. | **P2** (greedy, naive, memo) and **P3** (bottom-up) | Validator, validation tests, counterexample search and results, report section for 2B, README, final merged report |

## Before Anyone Starts (Whole Team)

The code scaffold is already in the repo: Python 3.10+, stubs, tests, and shared helpers. Setup steps are in `README.md`.

- [ ] Everyone runs `pip install -r requirements.txt`, then `pytest` (expect passes + skips, no failures)
- [ ] Review the shared contract in `src/coin_common.py` (result format, `stats` counters)
- [ ] Agree on the CSV columns (the `COLUMNS` list at the top of each `experiments/` script)
- [ ] Random-seed rule: always use `make_rng(seed)` from `generators` and record the seed

### Your Files

Fill in the `TODO(P#)` stubs. Your tests skip until your code exists, then they must pass.

| Role | Code (`src/`) | Tests (`tests/`) | Experiments (`experiments/`) |
|---|---|---|---|
| P1 | `inversions.py` | `test_inversions.py`, inversion cases in `cases.py` | none |
| P2 | `greedy.py`, `naive.py`, `memo.py` | `test_coins_recursive.py` | `exp1_repeated_subproblems.py` |
| P3 | `bottom_up.py`, `timing.py` | `test_coins_bottom_up.py` | `inversion_benchmark.py`, `exp2_pseudo_polynomial.py` |
| P4 | `validate.py`, `counterexamples.py` | `test_coins_validation.py`, coin cases in `cases.py` | `greedy_counterexamples.py` |

Shared (ask the team before changing): `coins.py`, `coin_common.py`, `generators.py`, `results.py`, `plotting.py`, `tests/conftest.py`.

### Shared Function Signatures

```python
# from inversions import ... (P1)
count_inversions_brute(arr) -> int
sort_and_count(arr) -> (sorted_arr, count)

# from coins import ... (P2: greedy, naive, memo | P3: bottom_up | P4: validate_solution)
IMPOSSIBLE = None
greedy(D, A)                -> (count, coins) | IMPOSSIBLE
naive(D, A, stats=None)     -> (count, coins) | IMPOSSIBLE
memo(D, A, stats=None)      -> (count, coins) | IMPOSSIBLE
bottom_up(D, A, stats=None) -> (count, coins) | IMPOSSIBLE
validate_solution(D, A, result, expected_count=...) -> None, or raises ValueError
# stats = new_stats(): calls, distinct_states, cache_hits, states_processed
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
- [ ] Timing harness (repeated runs, reports the median)
- [ ] Inversion benchmark, plot, and crossover point
- [ ] Exp 2 run (A = 2^8, 2^9, ...)
- [ ] Complexity analysis (bottom-up)
- [ ] Part III Q2

**P4: Coin Checker + Integrator**
- [ ] Solution validator (coins sum to A and the count matches)
- [ ] 10+ hand cases (target 0, impossible, multiple optimal answers)
- [ ] 100+ random cross-checks pass
- [ ] Greedy counterexample search finds `D={1,3,4}, A=6`
- [ ] 3+ counterexamples, with one explained
- [ ] README
- [ ] Part III Q5, then merge Q6
- [ ] Final report merged (6–8 pages)

**Everyone**
- [ ] Your line in the Contribution Statement
- [ ] Your notes for the AI Use Statement (tools used and how you checked the output)
- [ ] Your report section handed to P4
