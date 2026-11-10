# Part 2C Exp 2: pseudo-polynomial scaling of bottom-up DP.  Owner: P3
#
#   python src/exp2_pseudo_polynomial.py
#
# Keep the coin system fixed and small, and double A each step: 2^8, 2^9, ...
#
# Outputs: results/exp2_pseudo_polynomial.csv   A, bit length, states, runtime
#          results/exp2_pseudo_polynomial.png   runtime vs A, and runtime vs bit length

import matplotlib.pyplot as plt

from bottom_up import bottom_up
from helpers import RESULTS_DIR, new_stats, save_csv, time_median

# k = 4, fixed for every A. It includes 1, so every amount is reachable and the whole
# table is filled (no IMPOSSIBLE answers). The other values are mixed sizes, and greedy
# fails on this system (A = 15: greedy 12+1+1+1, best 5+5+5), so an exact DP is needed.
# The work is (A + 1) states x k coins whatever the values are, so only k and A matter.
D = [1, 5, 12, 19]
EXPONENTS = range(8, 23)  # A = 2^8 ... 2^22; 2^22 takes about 1.5 s per run on our machine
REPEATS = 7               # median of 7 timed runs per A (same as the inversion benchmark)


def main():
    rows = []
    for e in EXPONENTS:
        A = 2**e
        stats = new_stats()
        count, _ = bottom_up(D, A, stats)              # one counted run (D has 1, never IMPOSSIBLE)
        seconds = time_median(bottom_up, D, A, repeats=REPEATS)  # separate timing, counters off
        rows.append({
            "A": A,
            "bit_length": A.bit_length(),              # floor(log2 A) + 1
            "k": len(D),
            "states_processed": stats["states_processed"],
            "coin_count": count,
            "median_seconds": seconds,
            "ns_per_state": seconds / stats["states_processed"] * 1e9,
        })
        print(rows[-1])

    path = save_csv(rows, "exp2_pseudo_polynomial.csv")
    print("saved", path)
    plot(rows)


def plot(rows):
    # Left: time vs A (linear axes) is a straight line, so the work is linear in A.
    # Right: the same points vs bit length (log y) are also a straight line, so the
    # time doubles with each extra bit: exponential in the input size.
    A = [r["A"] for r in rows]
    bits = [r["bit_length"] for r in rows]
    secs = [r["median_seconds"] for r in rows]
    fig, (left, right) = plt.subplots(1, 2, figsize=(6.5, 3.0))
    for ax in (left, right):
        ax.grid(True, which="major", color="#e4e3df", linewidth=0.8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)

    left.plot([a / 1e6 for a in A], secs, color="#2a78d6", marker="o", markersize=4, linewidth=2)
    left.set_xlabel("Target A (millions)")
    left.set_ylabel("Median time (s)")
    left.set_title("(a) vs A: linear", fontsize=10)

    right.plot(bits, secs, color="#2a78d6", marker="o", markersize=4, linewidth=2)
    right.set_yscale("log", base=2)
    right.set_xlabel("Bit length of A")
    right.set_ylabel("Median time, s (log2 scale)")
    right.set_title("(b) vs bits: doubles per bit", fontsize=10)

    fig.suptitle(f"Bottom-up DP, D = {{{', '.join(map(str, D))}}} (k = {len(D)})", fontsize=11)
    fig.tight_layout()
    out = RESULTS_DIR / "exp2_pseudo_polynomial.png"
    fig.savefig(out, dpi=200)
    print("saved", out)


if __name__ == "__main__":
    main()
