# Part 2A-A: greedy, largest coin first.  Owner: P2
#
# A heuristic only, not a correct solver for every coin system.
# Result format: see the top of helpers.py.

from helpers import IMPOSSIBLE


def greedy(D, A):
    # Repeatedly take the largest coin that fits in what's left.
    # Return IMPOSSIBLE if it gets stuck (D=[3,5], A=9: takes 5, then 3, and 1 is left).
    # Example of a bad answer: greedy([1,3,4], 6) gives 4+1+1, but 3+3 is better.
    coins = []
    left = A
    for d in sorted(D, reverse=True):
        # Taking d while it fits is the same as taking left // d copies at once.
        take = left // d
        coins += [d] * take
        left -= take * d
    if left > 0:
        return IMPOSSIBLE  # stuck: no coin fits the remainder
    return len(coins), coins
