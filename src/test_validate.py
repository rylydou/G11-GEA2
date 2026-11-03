# Validator, exact-solver cross-check, and counterexample search tests.  Owner: P4
#
#   pytest src/test_validate.py
#
# The cross-check and search tests need P2's and P3's solvers, so they fail until those exist.

from bottom_up import bottom_up
from coin_cases import HAND_CASES, random_instances
from counterexamples import find_counterexamples
from helpers import IMPOSSIBLE
from recursive import memo, naive
from validate import is_valid

EXACT = [naive, memo, bottom_up]


def test_is_valid():
    assert is_valid([1, 3, 4], 6, (2, [3, 3]))
    assert is_valid([2], 3, IMPOSSIBLE)
    assert not is_valid([1, 3, 4], 6, (2, [4, 1]))     # wrong sum
    assert not is_valid([1, 3, 4], 6, (2, [3, 3, 0]))  # count != len(coins)
    assert not is_valid([1, 3, 4], 6, (2, [2, 4]))     # 2 isn't a coin


def test_exact_solvers_on_hand_cases():
    for D, A, expected in HAND_CASES:
        for solver in EXACT:
            result = solver(D, A)
            assert is_valid(D, A, result), (solver.__name__, D, A, result)
            assert (result if result is IMPOSSIBLE else result[0]) == expected


def test_exact_solvers_agree_on_100_random_instances():
    for D, A in random_instances(100, 20):
        results = [solver(D, A) for solver in EXACT]
        counts = {r if r is IMPOSSIBLE else r[0] for r in results}
        assert len(counts) == 1, (D, A, results)
        assert all(is_valid(D, A, r) for r in results)


def test_counterexample_search():
    found = find_counterexamples([[1, 3, 4]], max_target=10)
    assert any(r["A"] == 6 and r["greedy_count"] == 3 and r["optimal_count"] == 2 for r in found)
    assert all(r["greedy_count"] > r["optimal_count"] for r in found)
    assert find_counterexamples([[1, 5, 10, 25]], max_target=200) == []  # US coins: greedy works
