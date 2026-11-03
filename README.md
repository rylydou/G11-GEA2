# CMP_SC 4050: Group Algorithm Engineering Assignment 2

Divide and conquer (inversion counting) and dynamic programming (coin change).
See `docs/overview.md` for the assignment and `docs/plan.md` for who owns what.

## Setup

Requires **Python 3.10+**. Final results were produced with Python `_____` on `_____` (TODO(P4): fill in).

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # pytest, matplotlib, and src/ (editable, so imports work anywhere)
```

## Run the tests

```bash
pytest                                   # everything
pytest tests/test_inversions.py          # one file
```

Tests for unfinished stubs show as **SKIPPED** with the owner and function
(e.g. `not implemented yet: P2: memo`). A **FAILED** test means real code gave a wrong answer.

## Reproduce the experiments

Each script writes `results/<name>.csv` plus `results/<name>.meta.json` (seed, parameters, machine info).

```bash
python experiments/inversion_benchmark.py
python experiments/exp1_repeated_subproblems.py
python experiments/exp2_pseudo_polynomial.py
python experiments/greedy_counterexamples.py
```

Make plots from the CSVs (saved to `results/plots/`):

```bash
python experiments/plot_results.py results/inversion_benchmark.csv --x n --y median_seconds --group-by algorithm --logx --logy
python experiments/plot_results.py results/exp1_repeated_subproblems.csv --x A --y calls --group-by solver --logy
python experiments/plot_results.py results/exp2_pseudo_polynomial.csv --x bit_length --y median_seconds --logy
```

## Layout

```
src/                         flat: every file is a top-level module (e.g. `from coins import memo`)
  inversions.py          P1  brute force + sort-and-count
  coins.py               --  one import point for all coin code (re-exports the files below)
  coin_common.py         --  shared contract: IMPOSSIBLE, stats keys, input checks
  greedy.py              P2
  naive.py               P2
  memo.py                P2
  bottom_up.py           P3
  timing.py              P3  timing harness
  validate.py            P4  independent solution validator
  counterexamples.py     P4  greedy counterexample search
  generators.py          --  seeded random inputs
  results.py             --  CSV/JSON + run metadata
  plotting.py            --  plots from CSVs
tests/                       one test file per role + shared hand cases (cases.py)
experiments/                 one script per experiment + plot_results.py
results/                     CSV/JSON outputs (committed; required deliverable)
report/                      engineering report
docs/                        assignment, overview, team plan
```
