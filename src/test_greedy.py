# Greedy tests.  Owner: P2
#
#   pytest src/test_greedy.py

from coin_cases import random_instances, reference_count
from greedy import greedy
from helpers import IMPOSSIBLE


def test_greedy_hand_cases():
    assert greedy([1, 2, 5], 0) == (0, [])
    assert greedy([1, 5, 10, 25], 41)[0] == 4           # 25+10+5+1
    assert sorted(greedy([1, 3, 4], 6)[1]) == [1, 1, 4]  # not optimal
    assert greedy([3, 5], 9) is IMPOSSIBLE               # stuck


def test_greedy_valid_and_never_better_than_optimal():
    for D, A in random_instances(100, 40):
        result = greedy(D, A)
        if result is not IMPOSSIBLE:
            count, coins = result
            assert count == len(coins) and sum(coins) == A and set(coins) <= set(D)
            assert count >= reference_count(D, A)
