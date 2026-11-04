# Part 2C Exp 1: repeated subproblems, naive recursion vs. memoization.  Owner: P2
#
#   python src/exp1_repeated_subproblems.py
#
# Outputs: results/exp1_repeated_subproblems.csv   calls, distinct states, cache hits per A
#          results/exp1_repeated_subproblems.png   calls vs A for both solvers

import matplotlib.pyplot as plt

from helpers import RESULTS_DIR, new_stats, save_csv, time_median
from recursive import memo, naive

# Small, fixed coin system. It includes 1, so every A is reachable, and with three
# coins each call branches up to 3 ways, so naive's repeated work shows up fast.
# It is also the required greedy counterexample (A = 6), so it links to Part 2B.
D = [1, 3, 4]
TARGETS = range(0, 61, 2)   # memo runs on all of these; naive stops at the cutoff (A = 34)
NAIVE_CALL_CUTOFF = 10**7   # safety cutoff: stop running naive once a run passes this many calls
TIME_REPEATS = 3            # median of 3 runs for the seconds column


def run(solver, A):
    # One run with fresh counters, then a separate timing (median of
    # TIME_REPEATS runs, counters off) so counting doesn't affect the time.
    stats = new_stats()
    result = solver(D, A, stats)
    seconds = time_median(solver, D, A, repeats=TIME_REPEATS)
    return {
        "solver": solver.__name__,
        "A": A,
        "coin_count": result[0],  # D includes 1, so never IMPOSSIBLE
        "calls": stats["calls"],
        "distinct_states": stats["distinct_states"],
        "cache_hits": stats["cache_hits"],
        "seconds": seconds,
    }


def main():
    rows = []
    naive_on = True
    for A in TARGETS:
        if naive_on:
            row = run(naive, A)
            rows.append(row)
            if row["calls"] > NAIVE_CALL_CUTOFF:
                naive_on = False
                print(f"naive passed {NAIVE_CALL_CUTOFF:,} calls at A={A}; stopping naive")
        rows.append(run(memo, A))
        print(rows[-1])

    path = save_csv(rows, "exp1_repeated_subproblems.csv")
    print("saved", path)
    plot(rows)


def plot(rows):
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    styles = {"naive": ("#2a78d6", "o"), "memo": ("#eb6834", "s")}
    for name, (color, marker) in styles.items():
        pts = [(r["A"], r["calls"]) for r in rows if r["solver"] == name and r["A"] > 0]
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=color, marker=marker, markersize=4, linewidth=2, label=name)
        ax.annotate(name, (xs[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", color="#52514e")
    ax.axhline(NAIVE_CALL_CUTOFF, color="#8a8984", linestyle="--", linewidth=1)
    ax.annotate("naive cutoff (10^7 calls)", (TARGETS[0], NAIVE_CALL_CUTOFF), xytext=(2, 4),
                textcoords="offset points", fontsize=8, color="#52514e")
    ax.set_yscale("log")
    ax.set_xlabel("Target amount A")
    ax.set_ylabel("Recursive calls (log scale)")
    ax.set_title(f"Recursive calls vs A, D = {{{', '.join(map(str, D))}}}")
    ax.grid(True, which="major", color="#e4e3df", linewidth=0.8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 0.92))
    fig.tight_layout()
    out = RESULTS_DIR / "exp1_repeated_subproblems.png"
    fig.savefig(out, dpi=200)
    print("saved", out)


if __name__ == "__main__":
    main()
