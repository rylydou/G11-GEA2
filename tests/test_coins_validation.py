"""Exact-solver cross-validation, validator, and counterexample search.  Owner: P4

These depend on P2's and P3's solvers. They skip until those solvers are implemented.
"""

import pytest
from cases import COIN_CASES
from conftest import SEED

from coins import (
    EXACT_SOLVERS,
    IMPOSSIBLE,
    bottom_up,
    find_greedy_counterexamples,
    greedy,
    validate_solution,
)
from generators import make_rng, random_coin_system

RANDOM_TRIALS = 100


# --- validator ---------------------------------------------------------------


def test_validator_accepts_correct_answers():
    validate_solution([1, 3, 4], 6, (2, [3, 3]), expected_count=2)
    validate_solution([1, 2, 5], 0, (0, []), expected_count=0)
    validate_solution([2], 3, IMPOSSIBLE, expected_count=IMPOSSIBLE)
    validate_solution([1, 3, 4], 6, (3, [4, 1, 1]))  # no expected count: structure only


@pytest.mark.parametrize(
    "D, A, result, expected_count",
    [
        ([1, 3, 4], 6, (2, [4, 1]), 2),       # wrong sum
        ([1, 3, 4], 6, (2, [3, 3, 0]), 2),    # count != len(coins)
        ([1, 3, 4], 6, (2, [2, 4]), 2),       # 2 is not a denomination
        ([1, 3, 4], 6, (3, [4, 1, 1]), 2),    # valid but not optimal
        ([1, 3, 4], 6, IMPOSSIBLE, 2),        # missed a solution
        ([2], 3, (1, [3]), IMPOSSIBLE),       # invented a solution
    ],
    ids=["wrong_sum", "count_mismatch", "bad_coin", "not_optimal", "missed_solution", "invented_solution"],
)
def test_validator_rejects_bad_answers(D, A, result, expected_count):
    with pytest.raises(ValueError):
        validate_solution(D, A, result, expected_count=expected_count)


# --- exact-solver cross-validation -------------------------------------------


@pytest.mark.parametrize("name, D, A, expected", COIN_CASES, ids=[c[0] for c in COIN_CASES])
def test_all_exact_solvers_pass_hand_cases(name, D, A, expected):
    for solver in EXACT_SOLVERS.values():
        validate_solution(D, A, solver(D, A), expected_count=expected)


def test_exact_solvers_agree_on_random_instances():
    """100+ random small instances: naive, memo, and bottom_up must agree on the count."""
    rng = make_rng(SEED)
    for trial in range(RANDOM_TRIALS):
        D = random_coin_system(rng.randint(1, 4), 10, rng, include_one=rng.random() < 0.8)
        A = rng.randint(0, 20)
        results = {name: solver(D, A) for name, solver in EXACT_SOLVERS.items()}
        counts = {name: (r if r is IMPOSSIBLE else r[0]) for name, r in results.items()}
        assert len(set(counts.values())) == 1, f"seed={SEED} trial={trial} D={D} A={A}: {counts}"
        expected = next(iter(counts.values()))
        for result in results.values():
            validate_solution(D, A, result, expected_count=expected)


# --- greedy counterexample search --------------------------------------------


def test_search_finds_required_counterexample():
    found = find_greedy_counterexamples([(1, 3, 4)], max_target=10)
    hits = [r for r in found if tuple(r["denominations"]) == (1, 3, 4) and r["A"] == 6]
    assert hits, "search must detect D={1,3,4}, A=6"
    assert hits[0]["greedy_count"] == 3 and hits[0]["optimal_count"] == 2


def test_search_results_are_real_counterexamples():
    rng = make_rng(SEED)
    systems = [random_coin_system(3, 15, rng) for _ in range(20)]
    for r in find_greedy_counterexamples(systems, max_target=50):
        D, A = r["denominations"], r["A"]
        assert greedy(D, A)[0] == r["greedy_count"]
        assert bottom_up(D, A)[0] == r["optimal_count"]
        assert r["greedy_count"] > r["optimal_count"]


def test_search_finds_nothing_for_canonical_us_coins():
    assert find_greedy_counterexamples([(1, 5, 10, 25)], max_target=200) == []
