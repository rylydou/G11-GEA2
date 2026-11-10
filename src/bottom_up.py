# Part 2A-D: bottom-up DP.  Owner: P3
#
# Also the "exact DP" that P4's counterexample search compares greedy against.
# Result format and stats counters: see the top of helpers.py.
#
# Same recurrence as recursive.py, but filled in a loop instead of by recursion:
#   best[0] = 0
#   best[a] = 1 + min(best[a - d] for each coin d <= a), or IMPOSSIBLE if none work
# Every a - d is smaller than a, so filling a = 0, 1, ..., A means each entry's
# sub-answers are already final when we need them. No recursion, so no depth limit.

from helpers import IMPOSSIBLE

UNREACHABLE = float("inf")  # table marker: no coin combination makes this amount


def bottom_up(D, A, stats=None):
    # Fill best[0..A] in increasing order, plus choice[a] = a coin used for amount a.
    # Rebuild the coin list by following choice[] back from A to 0.
    best = [0] + [UNREACHABLE] * A  # best[a] = fewest coins that sum to a
    choice = [None] * (A + 1)       # choice[a] = last coin in one optimal answer for a
    for a in range(A + 1):
        if stats is not None:
            stats["states_processed"] += 1
        for d in D:
            # inf + 1 is still inf, so an unreachable sub-amount never wins.
            if d <= a and best[a - d] + 1 < best[a]:
                best[a] = best[a - d] + 1
                choice[a] = d

    if best[A] == UNREACHABLE:
        return IMPOSSIBLE
    # Rebuild: take the stored coin for A, move to A - coin, repeat until 0.
    coins = []
    a = A
    while a > 0:
        coins.append(choice[a])
        a -= choice[a]
    return best[A], coins
