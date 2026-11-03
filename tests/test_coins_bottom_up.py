"""Tests for bottom-up DP.  Owner: P3

These compare against the test-only BFS oracle in conftest.py,
so they don't depend on anyone else's code.
"""

import pytest
from cases import COIN_CASES
from conftest import SEED, assert_coin_result, reference_min_coins

from coins import bottom_up, new_stats
from generators import make_rng, random_coin_system

RANDOM_TRIALS = 100


@pytest.mark.parametrize("name, D, A, expected", COIN_CASES, ids=[c[0] for c in COIN_CASES])
def test_bottom_up_hand_cases(name, D, A, expected):
    assert_coin_result(D, A, bottom_up(D, A), expected)


def test_bottom_up_random_against_reference():
    rng = make_rng(SEED)
    for _ in range(RANDOM_TRIALS):
        D = random_coin_system(rng.randint(1, 5), 30, rng, include_one=rng.random() < 0.8)
        A = rng.randint(0, 200)
        assert_coin_result(D, A, bottom_up(D, A), reference_min_coins(D, A))


@pytest.mark.parametrize("A", [0, 1, 64, 500])
def test_states_processed_is_A_plus_one(A):
    stats = new_stats()
    bottom_up([1, 3, 4], A, stats=stats)
    assert stats["states_processed"] == A + 1


def test_stats_are_optional():
    assert bottom_up([1, 3, 4], 6) == bottom_up([1, 3, 4], 6, stats=None)
