# Part 2A-B and 2A-C: naive recursion and top-down memoized DP.  Owner: P2
#
# Both use the same recurrence:
#   best(0) = 0
#   best(a) = 1 + min(best(a - d) for each coin d <= a), or IMPOSSIBLE if none work
# Result format and stats counters: see the top of helpers.py.

import sys

from helpers import IMPOSSIBLE


def naive(D, A, stats=None):
    # Exact, no memoization, so only use small A.
    # For distinct_states, track the amounts seen in a set (but never reuse their answers).
    seen = set()

    def solve(a):
        # Returns (count, coins) for amount a, or IMPOSSIBLE.
        if stats is not None:
            stats["calls"] += 1
            seen.add(a)
        if a == 0:
            return 0, []
        best = IMPOSSIBLE
        for d in D:
            if d <= a:  # only recurse on coins that fit
                sub = solve(a - d)
                if sub is not IMPOSSIBLE and (best is IMPOSSIBLE or sub[0] + 1 < best[0]):
                    best = (sub[0] + 1, sub[1] + [d])
        return best

    result = solve(A)
    if stats is not None:
        stats["distinct_states"] += len(seen)
    return result


def memo(D, A, stats=None):
    # Same recurrence, but cache each amount's answer the first time it's solved.
    # Rebuild one optimal coin list from the cache at the end.
    # Recursion depth can reach A (e.g. all 1-coins), so raise Python's limit if needed.
    sys.setrecursionlimit(max(sys.getrecursionlimit(), A + 1000))
    cache = {}  # amount -> (count, last coin used), or IMPOSSIBLE

    def solve(a):
        # Returns the best coin count for amount a, or IMPOSSIBLE.
        if stats is not None:
            stats["calls"] += 1
        if a in cache:
            if stats is not None:
                stats["cache_hits"] += 1
            entry = cache[a]
            return IMPOSSIBLE if entry is IMPOSSIBLE else entry[0]
        if stats is not None:
            stats["distinct_states"] += 1
        best = IMPOSSIBLE if a > 0 else (0, None)
        for d in D:
            if d <= a:
                sub = solve(a - d)
                if sub is not IMPOSSIBLE and (best is IMPOSSIBLE or sub + 1 < best[0]):
                    best = (sub + 1, d)
        cache[a] = best
        return IMPOSSIBLE if best is IMPOSSIBLE else best[0]

    count = solve(A)
    if count is IMPOSSIBLE:
        return IMPOSSIBLE
    # Rebuild: follow the stored coin choices from A back down to 0.
    coins = []
    a = A
    while a > 0:
        d = cache[a][1]
        coins.append(d)
        a -= d
    return count, coins
