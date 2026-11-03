# Part 2A-A: greedy, largest coin first.  Owner: P2
#
# A heuristic only, not a correct solver for every coin system.
# Result format: see the top of helpers.py.

from helpers import IMPOSSIBLE


def greedy(D, A):
    # Repeatedly take the largest coin that fits in what's left.
    # Return IMPOSSIBLE if it gets stuck (D=[3,5], A=9: takes 5, then 3, and 1 is left).
    # Example of a bad answer: greedy([1,3,4], 6) gives 4+1+1, but 3+3 is better.
    # TODO(P2)
    raise NotImplementedError("P2: greedy")
