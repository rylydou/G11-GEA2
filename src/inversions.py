# Part I: counting inversions.  Owner: P1
#
# An inversion is a pair i < j with arr[i] > arr[j]. Inputs are lists of
# distinct ints. Don't modify the input list.


def brute_force(arr):
    # Check every pair i < j and count the ones out of order.
    # This is the oracle used to test sort_and_count.
    # TODO(P1)
    raise NotImplementedError("P1: brute_force")


def sort_and_count(arr):
    # Divide and conquer (modified mergesort). Returns (sorted copy of arr, inversion count).
    # Split in half, recurse on each half, then merge_and_count the two sorted halves.
    # Total = left inversions + right inversions + cross inversions.
    # TODO(P1)
    raise NotImplementedError("P1: sort_and_count")


def merge_and_count(left, right):
    # Merge two sorted lists in O(n) and count cross inversions (x in left > y in right).
    # Returns (merged list, cross inversion count).
    # Key idea: when right[j] < left[i], right[j] is inverted with every element
    # still remaining in left, so add len(left) - i all at once.
    # TODO(P1)
    raise NotImplementedError("P1: merge_and_count")
