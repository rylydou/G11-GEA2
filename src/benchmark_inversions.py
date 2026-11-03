# Part 1B: runtime of brute force vs. divide and conquer as n grows.  Owner: P3
#
#   python src/benchmark_inversions.py
#
# Outputs: results/benchmark_inversions.csv   median seconds per algorithm and n
#          results/benchmark_inversions.png   time vs n on log-log axes

import random

import matplotlib.pyplot as plt

from helpers import RESULTS_DIR, SEED, random_array, save_csv, time_median
from inversions import brute_force, sort_and_count

SIZES = [2**i for i in range(1, 13)]  # TODO(P3): tune so the two curves clearly separate
REPEATS = 7


def main():
    rng = random.Random(SEED)
    # TODO(P3): for each n, build one random_array(n, rng), then time both algorithms
    #   on it with time_median. One row per (algorithm, n): algorithm, n, median_seconds.
    #   Skip brute force once it gets too slow, and note the cutoff in the report.
    # TODO(P3): save_csv(rows, "benchmark_inversions.csv"), then plot median_seconds vs n
    #   (log-log) for both algorithms -> RESULTS_DIR / "benchmark_inversions.png"
    raise NotImplementedError("P3: benchmark_inversions")


if __name__ == "__main__":
    main()
