# Coin-change test data, shared by every coin test file.  Owner: P4
# P2 and P3 only import from this file. Ask P4 before changing it.

import random
from collections import deque

from helpers import IMPOSSIBLE, SEED, random_coins

# (D, A, optimal coin count or IMPOSSIBLE). TODO(P4): add more to reach 10+ hand-checked cases.
HAND_CASES = [
    ([1, 2, 5], 0, 0),               # target 0
    ([1, 5, 10, 25], 30, 2),         # 25+5
    ([1, 2, 5], 11, 3),              # 5+5+1
    ([2], 3, IMPOSSIBLE),
    ([5, 10], 3, IMPOSSIBLE),
    ([1, 2, 3], 4, 2),               # multiple optimal: 1+3 or 2+2
    ([1, 3, 4], 6, 2),               # 3+3 (greedy: 4+1+1)
    ([3, 5], 9, 3),                  # 3+3+3 (greedy gets stuck)
]


def reference_count(D, A):
    # Test-only answer key: breadth-first search over amounts. Written differently
    # from every team solver, so the solver tests don't depend on each other.
    seen = {0: 0}
    queue = deque([0])
    while queue:
        amount = queue.popleft()
        if amount == A:
            return seen[amount]
        for d in D:
            if amount + d <= A and amount + d not in seen:
                seen[amount + d] = seen[amount] + 1
                queue.append(amount + d)
    return IMPOSSIBLE


def random_instances(n, max_A):
    # n seeded random (D, A) pairs. About 20% of the coin systems have no 1, so some are impossible.
    rng = random.Random(SEED)
    for _ in range(n):
        D = random_coins(rng.randint(1, 4), 10, rng, include_one=rng.random() < 0.8)
        yield D, rng.randint(0, max_A)
