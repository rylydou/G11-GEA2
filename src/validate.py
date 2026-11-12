# Part 2B: independent check of a coin solver's answer.  Owner: P4
#
# Result format: see the top of helpers.py.

from helpers import IMPOSSIBLE


def is_valid(D, A, result):
    # True if result is IMPOSSIBLE, or if count == len(coins), sum(coins) == A,
    # and every coin is in D. This does NOT check optimality (compare counts for that).
    # It also can't tell if IMPOSSIBLE was the right answer (compare with an exact solver).
    if result is IMPOSSIBLE:
        return True
    count, coins = result
    return count == len(coins) and sum(coins) == A and all(c in D for c in coins)
