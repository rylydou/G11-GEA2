# Part 1B: runtime of brute force vs. divide and conquer as n grows.  Owner: P3
#
#   python src/benchmark_inversions.py
#
# Outputs: results/benchmark_inversions.csv   median seconds per algorithm and n
#          results/benchmark_inversions.png   time vs n on log-log axes

import math
import random

import matplotlib.pyplot as plt

from helpers import RESULTS_DIR, SEED, random_array, save_csv, time_median
from inversions import brute_force, sort_and_count

# Powers of 2 plus the halfway point 1.5 * 2^i, so the crossover (around n = 50 on our
# machine) is pinned down more finely than doubling alone would allow.
SIZES = sorted({2**i for i in range(1, 18)} | {3 * 2**i for i in range(0, 16)})  # 2 .. 131,072
REPEATS = 7                 # median of 7 timed calls per point
BRUTE_CUTOFF_SECONDS = 1.0  # stop running brute force after its median passes 1 s
FIT_MIN_N = 256             # fit log-log slopes only where Python's fixed overhead is small


def main():
    rng = random.Random(SEED)
    rows = []
    brute_on = True
    for n in SIZES:
        arr = random_array(n, rng)  # built before timing, and shared by both algorithms
        algorithms = [sort_and_count] + ([brute_force] if brute_on else [])
        for fn in algorithms:
            seconds = time_median(fn, arr, repeats=REPEATS)
            rows.append({"algorithm": fn.__name__, "n": n, "median_seconds": seconds})
            print(rows[-1])
            if fn is brute_force and seconds > BRUTE_CUTOFF_SECONDS:
                brute_on = False
                print(f"brute force passed {BRUTE_CUTOFF_SECONDS} s at n={n}; stopping brute force")

    path = save_csv(rows, "benchmark_inversions.csv")
    print("saved", path)
    crossover = find_crossover(rows)
    print("crossover: divide and conquer is faster for every tested n >=", crossover)
    for name in ("brute_force", "sort_and_count"):
        print(f"log-log slope ({name}, n >= {FIT_MIN_N}): {fit_slope(rows, name):.2f}")
    plot(rows, crossover)


def times_by_n(rows, name):
    return {r["n"]: r["median_seconds"] for r in rows if r["algorithm"] == name}


def find_crossover(rows):
    # Smallest n where divide and conquer is faster there and at every larger n
    # that both algorithms ran on.
    brute, fast = times_by_n(rows, "brute_force"), times_by_n(rows, "sort_and_count")
    crossover = None
    for n in sorted(brute, reverse=True):
        if fast[n] >= brute[n]:
            break
        crossover = n
    return crossover


def fit_slope(rows, name):
    # Least-squares slope of log(time) vs log(n). About 2 means n^2; a little over 1 means n log n.
    pts = [(math.log(n), math.log(t)) for n, t in times_by_n(rows, name).items() if n >= FIT_MIN_N]
    mx = sum(x for x, _ in pts) / len(pts)
    my = sum(y for _, y in pts) / len(pts)
    return sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)


def plot(rows, crossover):
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    styles = {
        "brute_force": ("brute force", "#2a78d6", "o"),
        "sort_and_count": ("divide and conquer", "#eb6834", "s"),
    }
    for name, (label, color, marker) in styles.items():
        xs, ys = zip(*sorted(times_by_n(rows, name).items()))
        ax.plot(xs, ys, color=color, marker=marker, markersize=4, linewidth=2, label=label)
        ax.annotate(label, (xs[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", color="#52514e")
    if crossover is not None:
        ax.axvline(crossover, color="#8a8984", linestyle="--", linewidth=1)
        ax.annotate(f"crossover ≈ {crossover}", (crossover, ax.get_ylim()[1]), xytext=(4, -12),
                    textcoords="offset points", fontsize=8, color="#52514e")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xlabel("Array size n (log scale)")
    ax.set_ylabel("Median time, s (log scale)")
    ax.set_title(f"Inversion counting: median of {REPEATS} runs per n")
    ax.grid(True, which="major", color="#e4e3df", linewidth=0.8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    out = RESULTS_DIR / "benchmark_inversions.png"
    fig.savefig(out, dpi=200)
    print("saved", out)


if __name__ == "__main__":
    main()
