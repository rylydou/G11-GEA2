"""Part I: counting inversions.  Owner: P1

An inversion is a pair of indices i < j with arr[i] > arr[j].
Inputs are sequences of distinct integers. Functions must NOT modify their input.
"""

from __future__ import annotations

from collections.abc import Sequence


def count_inversions_brute(arr: Sequence[int]) -> int:
    """Count inversions by checking every pair (i, j) with i < j.

    This is the small-instance oracle used to validate `sort_and_count`.

    Example:
        >>> count_inversions_brute([2, 4, 1, 3, 5])
        3
    """
    # TODO(P1): loop over every pair i < j and count arr[i] > arr[j].
    raise NotImplementedError("P1: count_inversions_brute")


def sort_and_count(arr: Sequence[int]) -> tuple[list[int], int]:
    """Divide-and-conquer sort-and-count (modified mergesort).

    Returns:
        (sorted copy of arr, number of inversions in arr)

    Steps:
        1. Base case: length 0 or 1 -> (list(arr), 0).
        2. Split at the middle; recursively sort-and-count each half.
        3. Merge the halves with `merge_and_count` to get cross inversions.
        4. Total = left inversions + right inversions + cross inversions.

    Example:
        >>> sort_and_count([2, 4, 1, 3, 5])
        ([1, 2, 3, 4, 5], 3)
    """
    # TODO(P1)
    raise NotImplementedError("P1: sort_and_count")


def merge_and_count(left: Sequence[int], right: Sequence[int]) -> tuple[list[int], int]:
    """Merge two sorted lists and count cross inversions in linear time.

    A cross inversion is a pair (x in left, y in right) with x > y.

    Central idea (keep this visible in the code): when the next element from
    `right` is smaller than the next element from `left`, it forms an inversion
    with EVERY remaining element in `left`, so add that many at once.

    Example:
        >>> merge_and_count([1, 3, 5], [2, 4, 6])
        ([1, 2, 3, 4, 5, 6], 3)
    """
    # TODO(P1)
    raise NotImplementedError("P1: merge_and_count")
