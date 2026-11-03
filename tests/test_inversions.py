"""Part I tests.  Owner: P1"""

import pytest
from cases import INVERSION_CASES
from conftest import SEED

from generators import make_rng, random_distinct_array
from inversions import count_inversions_brute, merge_and_count, sort_and_count

RANDOM_TRIALS = 200
MAX_N = 60


@pytest.mark.parametrize("name, arr, expected", INVERSION_CASES, ids=[c[0] for c in INVERSION_CASES])
def test_brute_hand_cases(name, arr, expected):
    assert count_inversions_brute(arr) == expected


@pytest.mark.parametrize("name, arr, expected", INVERSION_CASES, ids=[c[0] for c in INVERSION_CASES])
def test_sort_and_count_hand_cases(name, arr, expected):
    sorted_arr, count = sort_and_count(arr)
    assert sorted_arr == sorted(arr)
    assert count == expected


def test_merge_and_count_counts_cross_inversions():
    assert merge_and_count([1, 3, 5], [2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)


def test_inputs_not_modified():
    arr = [3, 1, 4, 5, 2]
    original = list(arr)
    count_inversions_brute(arr)
    sort_and_count(arr)
    assert arr == original


def test_random_cross_check_against_brute_force():
    """200+ random arrays: divide and conquer must match brute force exactly."""
    rng = make_rng(SEED)
    for trial in range(RANDOM_TRIALS):
        arr = random_distinct_array(rng.randint(0, MAX_N), rng)
        sorted_arr, count = sort_and_count(arr)
        assert sorted_arr == sorted(arr), f"seed={SEED} trial={trial} arr={arr}"
        assert count == count_inversions_brute(arr), f"seed={SEED} trial={trial} arr={arr}"
