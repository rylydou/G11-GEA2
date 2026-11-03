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


def find_counterexamples(coin_systems, max_target):
    # Check every coin system against every target 0..max_target, comparing greedy
    # to bottom_up. Skip targets where greedy returns IMPOSSIBLE.
    # Return one dict per counterexample:
    #   D, A, greedy_count, greedy_coins, optimal_count, optimal_coins
    # TODO(P4)
    raise NotImplementedError("P4: find_counterexamples")


def main():
    # TODO(P4): build a list of coin systems ([1, 3, 4] plus random_coins(...) ones),
    #   run find_counterexamples, save_csv(rows, "counterexamples.csv"), print a summary.
    raise NotImplementedError("P4: counterexamples")


if __name__ == "__main__":
    main()
