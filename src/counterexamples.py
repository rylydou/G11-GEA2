# Part 2B: automatically find cases where greedy is feasible but not optimal.  Owner: P4
#
#   python src/counterexamples.py
#
# Must find D = [1, 3, 4], A = 6 (greedy 4+1+1 = 3 coins, optimum 3+3 = 2 coins).
# The report needs 3+ distinct counterexamples, with one explained.
#
# Output: results/counterexamples.csv

import random

from bottom_up import bottom_up
from greedy import greedy
from helpers import IMPOSSIBLE, SEED, random_coins, save_csv
from validate import is_valid

# [1, 3, 4] is the required case. US coins are a control: greedy is optimal there.
FIXED_SYSTEMS = [[1, 3, 4], [1, 5, 10, 25]]
N_RANDOM = 30    # extra seeded random systems, all distinct
K_RANGE = (3, 4)  # coins per random system (1 is always one of them)
MAX_COIN = 20     # largest coin value a random system can have
MAX_TARGET = 50   # check every A = 0..50 (more than the two biggest coins add up to)


def find_counterexamples(coin_systems, max_target):
    # Check every coin system against every target 0..max_target, comparing greedy
    # to bottom_up. Skip targets where greedy returns IMPOSSIBLE.
    # Return one dict per counterexample:
    #   D, A, greedy_count, greedy_coins, optimal_count, optimal_coins
    found = []
    for D in coin_systems:
        for A in range(max_target + 1):
            g = greedy(D, A)
            if g is IMPOSSIBLE:
                continue  # greedy got stuck: not a "feasible but worse" case
            best = bottom_up(D, A)  # never IMPOSSIBLE here, since greedy found coins
            # Check both coin lists before trusting their counts.
            assert is_valid(D, A, g) and is_valid(D, A, best), (D, A, g, best)
            if g[0] > best[0]:
                found.append({
                    "D": D,
                    "A": A,
                    "greedy_count": g[0],
                    "greedy_coins": g[1],
                    "optimal_count": best[0],
                    "optimal_coins": best[1],
                })
    return found


def coin_systems():
    # The fixed systems, then N_RANDOM distinct seeded random ones (each includes 1).
    rng = random.Random(SEED)
    systems = [list(D) for D in FIXED_SYSTEMS]
    while len(systems) < len(FIXED_SYSTEMS) + N_RANDOM:
        D = random_coins(rng.randint(*K_RANGE), MAX_COIN, rng)
        if D not in systems:
            systems.append(D)
    return systems


def show(coins):
    # [1, 4, 1] -> "4+1+1"
    return "+".join(map(str, sorted(coins, reverse=True)))


def main():
    systems = coin_systems()
    found = find_counterexamples(systems, MAX_TARGET)
    rows = [{
        "D": "{" + ", ".join(map(str, r["D"])) + "}",
        "A": r["A"],
        "greedy_count": r["greedy_count"],
        "greedy_coins": show(r["greedy_coins"]),
        "optimal_count": r["optimal_count"],
        "optimal_coins": show(r["optimal_coins"]),
        "extra_coins": r["greedy_count"] - r["optimal_count"],
    } for r in found]
    path = save_csv(rows, "counterexamples.csv")

    first = {}  # D -> its smallest counterexample (rows are in increasing A for each D)
    for row in rows:
        first.setdefault(row["D"], row)
    print(f"checked {len(systems)} coin systems x A = 0..{MAX_TARGET} "
          f"({len(systems) * (MAX_TARGET + 1)} cases)")
    print(f"found {len(rows)} counterexamples in {len(first)} of {len(systems)} systems")
    print("smallest counterexample per system:")
    for row in first.values():
        print(f"  D = {row['D']}, A = {row['A']}: greedy {row['greedy_coins']} "
              f"({row['greedy_count']}), optimal {row['optimal_coins']} ({row['optimal_count']})")
    worst = max(rows, key=lambda row: row["extra_coins"])
    print(f"largest gap: D = {worst['D']}, A = {worst['A']}, greedy uses "
          f"{worst['extra_coins']} more coins")
    print("saved", path)


if __name__ == "__main__":
    main()
