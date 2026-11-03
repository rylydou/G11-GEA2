# Naive recursion and memoized DP tests.  Owner: P2
#
#   pytest src/test_recursive.py
#   pytest src/test_recursive.py -k memo     just one solver

import pytest

from coin_cases import HAND_CASES, random_instances, reference_count
from helpers import IMPOSSIBLE, new_stats
from recursive import memo, naive


def check(D, A, result, expected):
    if expected is IMPOSSIBLE:
        assert result is IMPOSSIBLE
    else:
        count, coins = result
        assert count == expected == len(coins)
        assert sum(coins) == A and set(coins) <= set(D)


@pytest.mark.parametrize("solver", [naive, memo])
@pytest.mark.parametrize("D, A, expected", HAND_CASES)
def test_hand_cases(solver, D, A, expected):
    check(D, A, solver(D, A), expected)


@pytest.mark.parametrize("solver", [naive, memo])
def test_100_random_instances(solver):
    for D, A in random_instances(100, 20):  # small A: naive is exponential
        check(D, A, solver(D, A), reference_count(D, A))


def test_memo_stats():
    stats = new_stats()
    memo([1, 3, 4], 30, stats)
    assert stats["distinct_states"] <= 31 and stats["cache_hits"] > 0
    assert stats["calls"] == stats["distinct_states"] + stats["cache_hits"]


def test_naive_stats():
    naive_stats, memo_stats = new_stats(), new_stats()
    naive([1, 3, 4], 18, naive_stats)
    memo([1, 3, 4], 18, memo_stats)
    assert naive_stats["cache_hits"] == 0
    assert naive_stats["calls"] > naive_stats["distinct_states"]  # repeats work
    assert naive_stats["calls"] > memo_stats["calls"]
