"""Naive exact recursive solver, no memoization (Part 2A-B).  Owner: P2

Only practical for small A. Its call count grows exponentially.
"""

from __future__ import annotations

from collections.abc import Iterable

from coin_common import IMPOSSIBLE, CoinResult, bump, check_target, normalize_denominations


def naive(D: Iterable[int], A: int, stats: dict[str, int] | None = None) -> CoinResult:
    """Exact minimum-coin solution by trying every possible final coin.

    Recurrence:
        best(0) = 0 coins
        best(a) = 1 + min(best(a - d)) over coins d <= a that lead to a solution
        best(a) = IMPOSSIBLE if no coin d <= a leads to a solution

    Instrumentation (when stats is not None), see `coin_common.py`:
        calls            += 1 on every recursive call
        distinct_states  = number of different amounts reached (track them in a set;
                           tracking is fine, but do NOT reuse answers, since that is memoization)
        cache_hits       stays 0

    Returns:
        (coin_count, chosen_coins) or IMPOSSIBLE.
    """
    denoms = normalize_denominations(D)
    check_target(A)
    # TODO(P2): write a recursive helper that returns (count, coins) or IMPOSSIBLE.
    # Recurse only on coins d <= amount. Call bump(stats, "calls") on each call.
    raise NotImplementedError("P2: naive")
