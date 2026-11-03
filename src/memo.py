"""Top-down DP with memoization (Part 2A-C).  Owner: P2

Same recurrence as `naive.py`, but each amount is solved once and cached.
"""

from __future__ import annotations

from collections.abc import Iterable

from coin_common import IMPOSSIBLE, CoinResult, bump, check_target, normalize_denominations


def memo(D: Iterable[int], A: int, stats: dict[str, int] | None = None) -> CoinResult:
    """Exact minimum-coin solution using the naive recurrence plus a cache.

    Suggested approach:
        - cache[amount] = (best_count, coin_chosen_last), or IMPOSSIBLE
        - after solving A, rebuild one optimal coin list by following
          coin_chosen_last from A down to 0

    Instrumentation (when stats is not None), see `coin_common.py`:
        calls            += 1 on every recursive call
        cache_hits       += 1 when the amount is already in the cache
        distinct_states  += 1 when an amount is solved for the first time
        (so calls == distinct_states + cache_hits)

    Note: recursion depth can reach A / min(D). Python's default limit is about
    1000 frames, so large A may need sys.setrecursionlimit(...) or a smaller A.

    Returns:
        (coin_count, chosen_coins) or IMPOSSIBLE.
    """
    denoms = normalize_denominations(D)
    check_target(A)
    # TODO(P2)
    raise NotImplementedError("P2: memo")
