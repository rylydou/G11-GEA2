"""Hand-checkable test cases shared by the test files.

Starter sets only. The assignment requires 10+ hand cases for each part;
owners should add their own and explain them in the report.
"""

from coins import IMPOSSIBLE

# (name, array of distinct values, expected inversion count)
# Owner: P1. TODO(P1): add cases to reach 10+.
INVERSION_CASES = [
    ("empty", [], 0),
    ("single", [42], 0),
    ("sorted", [1, 2, 3, 4, 5], 0),
    ("reverse_sorted", [5, 4, 3, 2, 1], 10),              # n(n-1)/2
    ("nearly_sorted_one_swap", [1, 2, 4, 3, 5], 1),       # (4,3)
    ("random_small", [2, 4, 1, 3, 5], 3),                 # (2,1) (4,1) (4,3)
    ("random_mixed", [3, 1, 4, 5, 2], 4),                 # (3,1) (3,2) (4,2) (5,2)
]

# (name, denominations, target A, expected optimal coin count or IMPOSSIBLE)
# Owner: P4. TODO(P4): add cases to reach 10+.
COIN_CASES = [
    ("target_zero", (1, 2, 5), 0, 0),
    ("canonical_us", (1, 5, 10, 25), 30, 2),              # 25+5
    ("classic", (1, 2, 5), 11, 3),                        # 5+5+1
    ("impossible_single_denom", (2,), 3, IMPOSSIBLE),
    ("impossible_all_too_big", (5, 10), 3, IMPOSSIBLE),
    ("multiple_optimal", (1, 2, 3), 4, 2),                # 1+3 or 2+2
    ("greedy_counterexample", (1, 3, 4), 6, 2),           # 3+3 (greedy: 4+1+1)
    ("greedy_gets_stuck", (3, 5), 9, 3),                  # 3+3+3 (greedy: 5+3, stuck at 1)
]
