# Part I tests.  Owner: P1
#
#   pytest src/test_inversions.py

import random

import pytest

from helpers import SEED, random_array
from inversions import brute_force, merge_and_count, sort_and_count

# (array, expected inversions). 12 hand-checked cases covering base cases,
# sorted, reverse, nearly sorted, cross-only, and negative numbers.
HAND_CASES = [
    ([], 0),
    ([42], 0),
    ([1, 2], 0),
    ([2, 1], 1),
    ([1, 2, 3, 4, 5], 0),
    ([5, 4, 3, 2, 1], 10),
    ([1, 2, 4, 3, 5], 1),
    ([2, 4, 1, 3, 5], 3),
    ([3, 1, 4, 5, 2], 4),
    ([6, 5, 4, 3, 2, 1], 15),
    ([1, 3, 5, 2, 4, 6], 3),
    ([10, -5, 0, 7, 3], 5),
]


@pytest.mark.parametrize("arr, expected", HAND_CASES)
def test_brute_force_hand_cases(arr, expected):
    assert brute_force(arr) == expected


@pytest.mark.parametrize("arr, expected", HAND_CASES)
def test_sort_and_count_hand_cases(arr, expected):
    assert sort_and_count(arr) == (sorted(arr), expected)


def test_merge_and_count():
    assert merge_and_count([1, 3, 5], [2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)


def test_input_not_modified():
    arr = [3, 1, 4, 5, 2]
    brute_force(arr)
    sort_and_count(arr)
    assert arr == [3, 1, 4, 5, 2]


def test_200_random_arrays_match_brute_force():
    rng = random.Random(SEED)
    for _ in range(200):
        arr = random_array(rng.randint(0, 60), rng)
        assert sort_and_count(arr) == (sorted(arr), brute_force(arr)), arr
