"""Part 1B: runtime scaling of brute force vs. divide and conquer.  Owner: P3

Run:     python experiments/inversion_benchmark.py
Output:  results/inversion_benchmark.csv (+ .meta.json)
Plot:    python experiments/plot_results.py results/inversion_benchmark.csv \
             --x n --y median_seconds --group-by algorithm --logx --logy
"""

from generators import make_rng, random_distinct_array  # noqa: F401
from inversions import count_inversions_brute, sort_and_count  # noqa: F401
from results import results_path, write_csv, write_metadata
from timing import time_call  # noqa: F401

SEED = 4050
SIZES = [2**i for i in range(1, 13)]  # TODO(P3): tune so the curves clearly separate
REPEATS = 7
BRUTE_MAX_N = 4096                    # TODO(P3): skip brute force above this size (document it)

COLUMNS = ["algorithm", "n", "repeats", "median_seconds", "min_seconds", "max_seconds"]


def run() -> list[dict]:
    """One row per (algorithm, n). Generate inputs outside the timed region."""
    # TODO(P3):
    #   rng = make_rng(SEED)
    #   for n in SIZES: build one random array, then time_call each algorithm on a copy
    raise NotImplementedError("P3: inversion_benchmark.run")


def main() -> None:
    rows = run()
    out = write_csv(rows, results_path("inversion_benchmark.csv"), COLUMNS)
    write_metadata(out, seed=SEED, sizes=SIZES, repeats=REPEATS, brute_max_n=BRUTE_MAX_N)
    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
