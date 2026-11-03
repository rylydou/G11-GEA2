# Part 2C Exp 2: pseudo-polynomial scaling of bottom-up DP.  Owner: P3
#
#   python src/exp2_pseudo_polynomial.py
#
# Keep the coin system fixed and small, and double A each step: 2^8, 2^9, ...
#
# Outputs: results/exp2_pseudo_polynomial.csv   A, bit length, states, runtime
#          results/exp2_pseudo_polynomial.png   runtime vs bit length

import matplotlib.pyplot as plt

from bottom_up import bottom_up
from helpers import RESULTS_DIR, new_stats, save_csv, time_median

D = [1, 5, 12, 19]        # TODO(P3): pick and justify (k fixed and small)
EXPONENTS = range(8, 21)  # A = 2^8 ... 2^20. TODO(P3): extend as far as practical
REPEATS = 5


def main():
    # TODO(P3): for each A = 2**e, record one row:
    #   A, bit_length (A.bit_length()), states_processed (one run with new_stats()),
    #   median_seconds (time_median).
    # TODO(P3): save_csv(rows, "exp2_pseudo_polynomial.csv"), then plot median_seconds
    #   vs bit_length (log y) -> RESULTS_DIR / "exp2_pseudo_polynomial.png"
    raise NotImplementedError("P3: exp2")


if __name__ == "__main__":
    main()
