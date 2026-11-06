# Team Plan: GEA2

`overview.md` covers what the assignment asks for; this doc covers **who does what**.
Claim a role by adding your name, and check off tasks as you finish them. Post in the group chat
when something another person is waiting on is ready.

**Only edit files you own** (all in `src/`). If you need a change in someone else's file, ask them.
Fill in the `TODO(P#)` stubs, then make your tests pass. Tasks starting with **Wait on:** need someone else's work first.

## P1: Inversions · Name: _________

Write both inversion counters and check them against each other. Then explain why the fast one
is correct and how fast each one is.

**Owns:** `inversions.py`, `test_inversions.py`
**Waits on:** nobody

- [x] `brute_force` and `sort_and_count` (returns the sorted array and the count)
- [x] 10+ hand-checked arrays, and 200+ random cross-checks pass
- [x] Report 2.1–2.4: algorithms, correctness, complexity, validation (Table 1)
- [x] Reflection Q1 and Q3

## P2: Recursive Coin Solvers · Name: Ryly Dou

Write the greedy, naive recursive, and memoized coin solvers, including call counters. Then run
Experiment 1 to show how much repeated work memoization saves.

**Owns:** `greedy.py`, `recursive.py`, `test_greedy.py`, `test_recursive.py`, `exp1_repeated_subproblems.py`
**Waits on:** nobody

- [x] `greedy`, `naive`, and `memo` (with reconstruction of the coin list)
- [x] Counters: calls, distinct states, cache hits
- [x] Exp 1 run (CSV + plot), with the safety cutoff documented
- [x] Report 3.1 and 3.2 (greedy, naive, memo), and 3.5: Exp 1
- [x] Reflection Q4

## P3: Bottom-Up DP + Timing · Name: _________

Write the bottom-up coin solver. Then do all the timing: the inversion benchmark and Experiment 2.
Also own the README.

**Owns:** `bottom_up.py`, `test_bottom_up.py`, `benchmark_inversions.py`, `exp2_pseudo_polynomial.py`, `README.md`
**Waits on:** P1 (`brute_force`, `sort_and_count`), but only for the benchmark

- [ ] `bottom_up` (with reconstruction and the `states_processed` counter)
- [ ] Exp 2 run (A = 2^8, 2^9, …), CSV + plot
- [ ] **Wait on: P1** · inversion benchmark (sizes, repeats, brute-force cutoff, `time_median`), plot, and crossover point
- [ ] README: Python version, machine, and exact commands to reproduce results
- [ ] Report 3.1 and 3.2 (bottom-up), 2.5: runtime, and 3.6: Exp 2
- [ ] Reflection Q2

## P4: Coin Checker + Integrator · Name: _________

Write the answer checker and the shared coin test cases. Then cross-check all the exact solvers
and search for cases where greedy fails. Finally, merge the report.

**Owns:** `validate.py`, `coin_cases.py`, `test_validate.py`, `counterexamples.py`, `REPORT.md` (final merge), `AI_USE.md` (final merge)
**Waits on:** P2 and P3 solvers for the cross-check and counterexamples; everyone for the merge

- [ ] `is_valid` (coins sum to A, the count matches, every coin is in D)
- [ ] 10+ hand cases in `coin_cases.py` (target 0, impossible, multiple optimal answers)
- [ ] **Wait on: P2 + P3** · 100+ random cross-checks pass (`naive`, `memo`, `bottom_up` agree)
- [ ] **Wait on: P2 + P3** · counterexample search (`greedy` vs `bottom_up`) finds `D={1,3,4}, A=6`, plus 3+ shown, with one explained
- [ ] Report 1: Introduction, 3.3: validation (Table 3), and 3.4: counterexamples (Table 4)
- [ ] Reflection Q5
- [ ] **Wait on: everyone** · merge Q6
- [ ] **Wait on: everyone** · final `REPORT.md` merged (8 pages max, no `TODO(` left) and `AI_USE.md` merged

## Shared

`helpers.py` is finished and shared (seed, random inputs, `time_median`, `save_csv`,
`IMPOSSIBLE`, `new_stats`), so ask the team before changing it. P2 and P3 tests read
P4's `coin_cases.py`, but never edit it.

**Everyone:**
- [ ] Your report sections, each within its word target
- [ ] A 1–2 sentence draft for Q6, sent to P4
- [ ] Your line in the Contribution Statement (end of `REPORT.md`)
- [ ] Your rows in `AI_USE.md` (tools used, what they produced, how you checked it)

## Function Signatures

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
