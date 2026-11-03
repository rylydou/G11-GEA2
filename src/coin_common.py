"""Shared coin-change contract: result type, input checks, instrumentation counters.

This file is shared. Change it only after the whole team agrees.

Result format:
    (coin_count, chosen_coins)  where len(chosen_coins) == coin_count
                                  and sum(chosen_coins) == A
                                  and every coin is in D
    IMPOSSIBLE                  if no combination of coins sums to A

Instrumentation (`stats` dict, see `new_stats`). Solvers only touch the keys that apply:
    calls             naive, memo: one per recursive call, including the top-level call
    distinct_states   naive, memo: number of different target amounts reached
    cache_hits        memo: calls answered straight from the cache (naive always 0)
    states_processed  bottom_up: number of DP table entries computed (amounts 0..A -> A + 1)

Convention so the counts mean the same thing in both recursive solvers:
recurse only on coins d <= amount (never call with a negative amount). For memo,
every call is then either a cache hit or a newly solved state, so
calls == distinct_states + cache_hits.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Optional

IMPOSSIBLE = None

CoinResult = Optional[tuple[int, list[int]]]

STAT_KEYS = ("calls", "distinct_states", "cache_hits", "states_processed")


def new_stats() -> dict[str, int]:
    """Return a fresh counter dict with every key set to 0."""
    return {key: 0 for key in STAT_KEYS}


def bump(stats: dict[str, int] | None, key: str, amount: int = 1) -> None:
    """Add `amount` to stats[key] if stats were requested. Does nothing when stats is None."""
    if stats is not None:
        stats[key] += amount


def normalize_denominations(D: Iterable[int]) -> tuple[int, ...]:
    """Return the denominations as a sorted tuple of unique positive ints.

    Raises:
        ValueError: if D is empty or contains a value that is not a positive int.
    """
    denoms = tuple(sorted(set(D)))
    if not denoms:
        raise ValueError("D must contain at least one denomination")
    for d in denoms:
        if isinstance(d, bool) or not isinstance(d, int) or d <= 0:
            raise ValueError(f"denominations must be positive ints, got {d!r}")
    return denoms


def check_target(A: int) -> None:
    """Raise ValueError unless A is a non-negative int."""
    if isinstance(A, bool) or not isinstance(A, int) or A < 0:
        raise ValueError(f"target A must be a non-negative int, got {A!r}")
