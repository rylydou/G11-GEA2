"""Part 2C Exp 2: pseudo-polynomial scaling of bottom-up DP.  Owner: P3

Keep k fixed and small; grow A geometrically (2^8, 2^9, ...).

Run:     python experiments/exp2_pseudo_polynomial.py
Output:  results/exp2_pseudo_polynomial.csv (+ .meta.json)
Plot:    python experiments/plot_results.py results/exp2_pseudo_polynomial.csv \
             --x bit_length --y median_seconds --logy
"""

from coins import bottom_up, new_stats  # noqa: F401
from results import results_path, write_csv, write_metadata
from timing import time_call  # noqa: F401

DENOMINATIONS = (1, 5, 12, 19)          # TODO(P3): pick and justify (k fixed and small)
EXPONENTS = range(8, 21)                # A = 2^8 ... 2^20; TODO(P3): extend as far as practical
REPEATS = 5

COLUMNS = ["denominations", "k", "A", "bit_length", "states_processed", "median_seconds", "repeats"]


def run() -> list[dict]:
    """One row per A. bit_length is A.bit_length() (= floor(log2 A) + 1)."""
    # TODO(P3): for each A: count states once with new_stats(), then time_call the solver
    raise NotImplementedError("P3: exp2.run")


def main() -> None:
    rows = run()
    out = write_csv(rows, results_path("exp2_pseudo_polynomial.csv"), COLUMNS)
    write_metadata(out, denominations=DENOMINATIONS, exponents=list(EXPONENTS), repeats=REPEATS)
    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
