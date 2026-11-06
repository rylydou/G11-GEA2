# Part I: counting inversions.  Owner: P1
#
# An inversion is a pair i < j with arr[i] > arr[j]. Inputs are lists of
# distinct ints. Don't modify the input list.


def brute_force(arr):
    # Check every pair i < j and count the ones out of order.
    # This is the oracle used to test sort_and_count.
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


def merge_and_count(left, right):
    # Merge two sorted lists in O(n) and count cross inversions (x in left > y in right).
    # Returns (merged list, cross inversion count).
    # Key idea: when right[j] < left[i], right[j] is inverted with every element
    # still remaining in left, so add len(left) - i all at once.
    merged = []
    i = 0
    j = 0
    count = 0
    len_left = len(left)
    len_right = len(right)

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len_left - i
            j += 1

    if i < len_left:
        merged.extend(left[i:])
    if j < len_right:
        merged.extend(right[j:])

    return merged, count


def sort_and_count(arr):
    # Divide and conquer (modified mergesort). Returns (sorted copy of arr, inversion count).
    # Split in half, recurse on each half, then merge_and_count the two sorted halves.
    # Total = left inversions + right inversions + cross inversions.
    if len(arr) <= 1:
        return list(arr), 0

    mid = len(arr) // 2
    left_sorted, left_inv = sort_and_count(arr[:mid])
    right_sorted, right_inv = sort_and_count(arr[mid:])
    merged, cross_inv = merge_and_count(left_sorted, right_sorted)

    return merged, left_inv + right_inv + cross_inv
