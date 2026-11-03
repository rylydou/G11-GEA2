# Part 2A-B and 2A-C: naive recursion and top-down memoized DP.  Owner: P2
#
# Both use the same recurrence:
#   best(0) = 0
#   best(a) = 1 + min(best(a - d) for each coin d <= a), or IMPOSSIBLE if none work
# Result format and stats counters: see the top of helpers.py.

from helpers import IMPOSSIBLE


def naive(D, A, stats=None):
    # Exact, no memoization, so only use small A.
    # For distinct_states, track the amounts seen in a set (but never reuse their answers).
    # TODO(P2)
    raise NotImplementedError("P2: naive")


def memo(D, A, stats=None):
    # Same recurrence, but cache each amount's answer the first time it's solved.
    # Rebuild one optimal coin list from the cache at the end.
    # Recursion depth can reach A, and Python's default limit is about 1000.
    # TODO(P2)
    raise NotImplementedError("P2: memo")
