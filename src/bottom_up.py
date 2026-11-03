# Part 2A-D: bottom-up DP.  Owner: P3
#
# Also the "exact DP" that P4's counterexample search compares greedy against.
# Result format and stats counters: see the top of helpers.py.

from helpers import IMPOSSIBLE


def bottom_up(D, A, stats=None):
    # Fill best[0..A] in increasing order, plus choice[a] = a coin used for amount a.
    # Rebuild the coin list by following choice[] back from A to 0.
    # TODO(P3)
    raise NotImplementedError("P3: bottom_up")
