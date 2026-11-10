# Bottom-up DP tests.  Owner: P3
#
#   pytest src/test_bottom_up.py

import pytest

from bottom_up import bottom_up
from coin_cases import HAND_CASES, random_instances, reference_count
from helpers import IMPOSSIBLE, new_stats


def check(D, A, result, expected):
    if expected is IMPOSSIBLE:
        assert result is IMPOSSIBLE
    else:
        count, coins = result
        assert count == expected == len(coins)
        assert sum(coins) == A and set(coins) <= set(D)


@pytest.mark.parametrize("D, A, expected", HAND_CASES)
def test_hand_cases(D, A, expected):
    check(D, A, bottom_up(D, A), expected)


def test_100_random_instances():
    for D, A in random_instances(100, 200):
        check(D, A, bottom_up(D, A), reference_count(D, A))


def test_stats():
    for A in [0, 1, 64, 500]:
        stats = new_stats()
        bottom_up([1, 3, 4], A, stats)
        assert stats["states_processed"] == A + 1


def test_no_one_coin_with_gaps():
    # D = {4, 7} with no 1-coin: many amounts in the table are unreachable,
    # and the rebuild must only step through reachable ones.
    for A in range(0, 60):
        check([4, 7], A, bottom_up([4, 7], A), reference_count([4, 7], A))


def test_large_A():
    # No recursion, so a large A works without touching Python's recursion limit.
    A = 2**16
    check([1, 5, 12, 19], A, bottom_up([1, 5, 12, 19], A), reference_count([1, 5, 12, 19], A))
