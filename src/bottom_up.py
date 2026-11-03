"""Bottom-up DP (Part 2A-D).  Owner: P3

Also serves as the "exact DP" ground truth for P4's greedy counterexample search
and is the solver measured in Exp 2 (pseudo-polynomial scaling).
"""

from __future__ import annotations

from collections.abc import Iterable

from coin_common import IMPOSSIBLE, CoinResult, bump, check_target, normalize_denominations


def bottom_up(D: Iterable[int], A: int, stats: dict[str, int] | None = None) -> CoinResult:
    """Exact minimum-coin solution by filling a table for amounts 0, 1, ..., A in order.

    Suggested approach:
        - best[a]   = fewest coins to make amount a (or "infinity" if impossible)
        - choice[a] = a coin used in one optimal solution for a
        - rebuild the coin list by following choice[] from A down to 0

    Instrumentation (when stats is not None), see `coin_common.py`:
        states_processed += 1 per table entry computed (A + 1 total, amounts 0..A)

    Returns:
        (coin_count, chosen_coins) or IMPOSSIBLE.
    """
    denoms = normalize_denominations(D)
    check_target(A)
    # TODO(P3)
    raise NotImplementedError("P3: bottom_up")
