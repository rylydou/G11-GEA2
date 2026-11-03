# GEA2: Divide and Conquer + Dynamic Programming

CMP_SC 4050, Group Algorithm Engineering Assignment 2. Part I counts inversions (brute force
vs. mergesort). Part II solves coin change (greedy, naive recursion, memoized DP, bottom-up DP).
See `docs/overview.md` for the assignment and `docs/plan.md` for who owns what.

Language: **Python 3.10+**. Libraries: matplotlib, pytest.
TODO(P3): note the exact Python version and machine used for the final results.

## Files

All code lives in `src/`.

| File | What | Owner |
|---|---|---|
| `helpers.py` | coin result format, `IMPOSSIBLE`, `new_stats`, seeded inputs, `time_median`, `save_csv` | shared |
| `inversions.py` | brute force + divide-and-conquer inversion counters | P1 |
| `test_inversions.py` | Part I hand cases + 200 random cross-checks | P1 |
| `greedy.py` | greedy, largest coin first | P2 |
| `recursive.py` | naive recursion + top-down memoized DP | P2 |
| `test_greedy.py`, `test_recursive.py` | tests for the three solvers above | P2 |
| `exp1_repeated_subproblems.py` | Part 2C Exp 1: naive vs memo call counts | P2 |
| `bottom_up.py` | bottom-up DP | P3 |
| `test_bottom_up.py` | bottom-up tests | P3 |
| `benchmark_inversions.py` | Part 1B: runtime scaling + crossover | P3 |
| `exp2_pseudo_polynomial.py` | Part 2C Exp 2: bottom-up runtime as A doubles | P3 |
| `validate.py` | `is_valid`: independent check of a coin answer | P4 |
| `coin_cases.py` | coin hand cases + test-only answer key, used by every coin test | P4 |
| `test_validate.py` | validator, exact-solver cross-check, counterexample search tests | P4 |
| `counterexamples.py` | Part 2B: automated greedy counterexample search | P4 |

Outputs (CSV + PNG) go to `results/`. The report goes in `report/`.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
pytest                                   # all tests
pytest src/test_recursive.py -k memo     # one file, one solver
python src/benchmark_inversions.py       # Part 1B
python src/counterexamples.py            # Part 2B
python src/exp1_repeated_subproblems.py  # Part 2C Exp 1
python src/exp2_pseudo_polynomial.py     # Part 2C Exp 2
```

Until a function is written, its tests fail with `NotImplementedError: P#: name`.
All randomness uses `SEED = 4050` from `helpers.py`, so every run gives the same output.
