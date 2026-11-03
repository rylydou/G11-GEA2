# Part 2C Exp 1: repeated subproblems, naive recursion vs. memoization.  Owner: P2
#
#   python src/exp1_repeated_subproblems.py
#
# Outputs: results/exp1_repeated_subproblems.csv   calls, distinct states, cache hits per A
#          results/exp1_repeated_subproblems.png   calls vs A for both solvers

import matplotlib.pyplot as plt

from helpers import RESULTS_DIR, new_stats, save_csv
from recursive import memo, naive

D = [1, 3, 4]               # TODO(P2): pick and justify a coin system
TARGETS = range(0, 41, 2)   # TODO(P2): increase until naive becomes impractical
NAIVE_CALL_CUTOFF = 10**7   # safety cutoff: stop running naive once a run passes this many calls


def main():
    # TODO(P2): for each A, run naive and memo, each with its own new_stats().
    #   One row per (solver, A): solver, A, coin_count, calls, distinct_states, cache_hits.
    #   Stop running naive after a run passes NAIVE_CALL_CUTOFF.
    # TODO(P2): save_csv(rows, "exp1_repeated_subproblems.csv"), then plot calls vs A
    #   (log y) for both solvers -> RESULTS_DIR / "exp1_repeated_subproblems.png"
    raise NotImplementedError("P2: exp1")


if __name__ == "__main__":
    main()
