"""Greedy largest-denomination-first heuristic (Part 2A-A).  Owner: P2

This is a comparison heuristic, NOT a correct solver for arbitrary coin systems.
"""

from __future__ import annotations

from collections.abc import Iterable

from coin_common import IMPOSSIBLE, CoinResult, check_target, normalize_denominations


def greedy(D: Iterable[int], A: int) -> CoinResult:
    """Repeatedly take the largest denomination that does not exceed the remaining amount.

    Returns:
        (coin_count, chosen_coins), or IMPOSSIBLE if the rule gets stuck
        (amount left over but no coin fits). Greedy can get stuck even when a
        solution exists, e.g. D = {3, 5}, A = 9: greedy takes 5, then 3, and has 1 left.

    Example:
        >>> greedy([1, 3, 4], 6)   # not optimal; 3 + 3 uses 2 coins
        (3, [4, 1, 1])
    """
    denoms = normalize_denominations(D)
    check_target(A)
    # TODO(P2): walk denominations from largest to smallest.
    raise NotImplementedError("P2: greedy")
