"""Tests for greedy, naive recursion, and memoized DP.  Owner: P2

These compare against the test-only BFS oracle in conftest.py,
so they don't depend on anyone else's code.
"""

import pytest
from cases import COIN_CASES
from conftest import SEED, assert_coin_result, reference_min_coins

from coins import IMPOSSIBLE, greedy, memo, naive, new_stats
from generators import make_rng, random_coin_system

EXACT = {"naive": naive, "memo": memo}
RANDOM_TRIALS = 100
CASE_IDS = [c[0] for c in COIN_CASES]


# --- greedy ------------------------------------------------------------------


def test_greedy_target_zero():
    assert greedy([1, 2, 5], 0) == (0, [])


def test_greedy_matches_optimum_on_canonical_system():
    count, coins = greedy([1, 5, 10, 25], 41)
    assert count == 4 and sorted(coins) == [1, 5, 10, 25]


def test_greedy_is_suboptimal_on_required_counterexample():
    count, coins = greedy([1, 3, 4], 6)
    assert count == 3 and sorted(coins) == [1, 1, 4]


def test_greedy_reports_impossible_when_stuck():
    assert greedy([3, 5], 9) is IMPOSSIBLE


def test_greedy_returns_valid_coins_and_never_beats_optimum():
    rng = make_rng(SEED)
    for _ in range(RANDOM_TRIALS):
        D = random_coin_system(rng.randint(1, 4), 12, rng)
        A = rng.randint(0, 40)
        result = greedy(D, A)
        optimum = reference_min_coins(D, A)
        if result is not IMPOSSIBLE:
            count, coins = result
            assert len(coins) == count and sum(coins) == A and set(coins) <= set(D)
            assert count >= optimum


# --- naive + memo (exact) ----------------------------------------------------


@pytest.mark.parametrize("solver", EXACT.values(), ids=EXACT.keys())
@pytest.mark.parametrize("name, D, A, expected", COIN_CASES, ids=CASE_IDS)
def test_exact_hand_cases(solver, name, D, A, expected):
    assert_coin_result(D, A, solver(D, A), expected)


@pytest.mark.parametrize("solver", EXACT.values(), ids=EXACT.keys())
def test_exact_random_against_reference(solver):
    rng = make_rng(SEED)
    for trial in range(RANDOM_TRIALS):
        D = random_coin_system(rng.randint(1, 4), 10, rng, include_one=rng.random() < 0.8)
        A = rng.randint(0, 20)  # small: naive is exponential
        assert_coin_result(D, A, solver(D, A), reference_min_coins(D, A))


@pytest.mark.parametrize("solver", EXACT.values(), ids=EXACT.keys())
def test_stats_are_optional(solver):
    assert solver([1, 3, 4], 6) == solver([1, 3, 4], 6, stats=None)


# --- instrumentation ---------------------------------------------------------


def test_memo_stats_are_consistent():
    stats = new_stats()
    memo([1, 3, 4], 30, stats=stats)
    assert stats["distinct_states"] <= 31           # at most amounts 0..30
    assert stats["cache_hits"] > 0
    assert stats["calls"] == stats["distinct_states"] + stats["cache_hits"]


def test_naive_has_no_cache_hits_and_repeats_work():
    stats = new_stats()
    naive([1, 3, 4], 15, stats=stats)
    assert stats["cache_hits"] == 0
    assert stats["calls"] > stats["distinct_states"]  # same amounts solved repeatedly


def test_memo_makes_far_fewer_calls_than_naive():
    naive_stats, memo_stats = new_stats(), new_stats()
    naive([1, 3, 4], 18, stats=naive_stats)
    memo([1, 3, 4], 18, stats=memo_stats)
    assert memo_stats["calls"] < naive_stats["calls"]
