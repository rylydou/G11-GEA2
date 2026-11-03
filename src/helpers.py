# Shared helpers: the coin-change result format, seeded random inputs, timing, and saving results.
# Finished. Ask the team before changing anything here.
#
# Always use rng = random.Random(SEED), never the global random module,
# so every run can be repeated from its seed.

import csv
import statistics
import time
from pathlib import Path

SEED = 4050  # base seed for every experiment
RESULTS_DIR = Path(__file__).parent.parent / "results"

# --- Coin-change result format (used by every coin file) ----------------------
#
# Every coin solver takes (D, A): D is a list of positive coin values, A >= 0 is the
# target, and coins can be reused. It returns (coin_count, coins), where coins is a
# list that sums to A, or IMPOSSIBLE if no combination of coins works.
#
# naive, memo, and bottom_up take an optional stats dict (from new_stats()) and add to it:
#   calls             naive, memo: +1 per recursive call
#   distinct_states   naive, memo: number of different amounts reached
#   cache_hits        memo: +1 when the amount is already cached (naive: always 0)
#   states_processed  bottom_up: +1 per table entry (A + 1 in total)
# Only recurse on coins d <= amount. Then for memo, calls == distinct_states + cache_hits.

IMPOSSIBLE = None


def new_stats():
    return {"calls": 0, "distinct_states": 0, "cache_hits": 0, "states_processed": 0}


# --- Random inputs -------------------------------------------------------------


def random_array(n, rng):
    # n distinct ints in random order.
    return rng.sample(range(10 * n + 1), n)


def nearly_sorted_array(n, swaps, rng):
    # [0..n-1] with a few random neighbor swaps (each swap adds at most 1 inversion).
    arr = list(range(n))
    for _ in range(swaps if n > 1 else 0):
        i = rng.randrange(n - 1)
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def random_coins(k, max_coin, rng, include_one=True):
    # k distinct coin values from 1..max_coin, sorted. With include_one=True, 1 is
    # always included, so every target can be made.
    if include_one:
        return sorted([1] + rng.sample(range(2, max_coin + 1), k - 1))
    return sorted(rng.sample(range(2, max_coin + 1), k))


# --- Timing and results --------------------------------------------------------


def time_median(fn, *args, repeats=5):
    # Run fn(*args) `repeats` times and return the median time in seconds.
    # Only the call itself is timed, so build inputs before calling this.
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        fn(*args)
        times.append(time.perf_counter() - start)
    return statistics.median(times)


def save_csv(rows, filename):
    # Save a list of dicts to results/<filename>. Returns the path.
    RESULTS_DIR.mkdir(exist_ok=True)
    path = RESULTS_DIR / filename
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return path
