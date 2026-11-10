# GEA2: Divide and Conquer + Dynamic Programming

CMP_SC 4050, Group Algorithm Engineering Assignment 2. Part I counts inversions (brute force
vs. mergesort). Part II solves coin change (greedy, naive recursion, memoized DP, bottom-up DP).
See `docs/overview.md` for the assignment and `docs/plan.md` for who owns what.

**Report:** [`REPORT.md`](REPORT.md) · **AI Use Statement:** [`AI_USE.md`](AI_USE.md)

Language: **Python 3.10+**. Libraries: matplotlib, pytest.

## Machine Used for the Results

| Results | Machine | Python |
|---|---|---|
| `benchmark_inversions.*`, `exp2_pseudo_polynomial.*` | Linux cloud container (kernel 6.18, x86_64), Intel Xeon Processor @ 2.10 GHz, 4 vCPUs, 15 GB RAM | CPython 3.13.18, matplotlib 3.11.2, pytest 9.2.0 |
| `exp1_repeated_subproblems.*` | TODO(P2): add the machine Experiment 1 was run on | TODO(P2) |

Timings depend on the machine, so yours will differ. Counts (recursive calls, cache hits, DP
states) and every coin answer are exact and come out the same on any machine.

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

Outputs (CSV + PNG) go to `results/`. `REPORT.md` embeds the PNGs straight from there.

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

## Reproduce the Report's Results

Run these from the repo root with the virtual environment active. Each script overwrites its
CSV and PNG in `results/` and prints what it saved.

```bash
pytest                                   # 1. check every solver first
python src/benchmark_inversions.py       # 2. Section 2.5, Figure 1 (about 30 s)
python src/exp1_repeated_subproblems.py  # 3. Section 3.5, Figure 2, Table 5
python src/exp2_pseudo_polynomial.py     # 4. Section 3.6, Figure 3, Table 6 (about 30 s)
python src/counterexamples.py            # 5. Section 3.4, Table 4
```

| Script | Settings (top of the file) | Writes |
|---|---|---|
| `benchmark_inversions.py` | n = 2^1..2^17 plus 3·2^i midpoints, median of 7 runs, brute force stops after a run passes 1 s | `benchmark_inversions.csv`, `.png`; also prints the crossover n and log-log slopes |
| `exp1_repeated_subproblems.py` | D = {1, 3, 4}, A = 0..60 step 2, naive stops after passing 10^7 calls, median of 3 runs | `exp1_repeated_subproblems.csv`, `.png` |
| `exp2_pseudo_polynomial.py` | D = {1, 5, 12, 19}, A = 2^8..2^22, median of 7 runs | `exp2_pseudo_polynomial.csv`, `.png` |

Close other heavy programs while timing. The medians cut down noise but don't remove it.
