"""Seeded input generators (shared).

Always pass a `random.Random` from `make_rng(seed)`, never the global `random`
module. That way every run can be reproduced from its recorded seed.
"""

from __future__ import annotations

import random

DEFAULT_SEED = 4050


def make_rng(seed: int = DEFAULT_SEED) -> random.Random:
    """Return an independent, seeded random number generator."""
    return random.Random(seed)


# --- Part I: arrays of distinct values -----------------------------------------


def sorted_array(n: int) -> list[int]:
    """[0, 1, ..., n-1]: zero inversions."""
    return list(range(n))


def reverse_sorted_array(n: int) -> list[int]:
    """[n-1, ..., 1, 0]: the maximum n(n-1)/2 inversions."""
    return list(range(n - 1, -1, -1))


def random_distinct_array(n: int, rng: random.Random, max_value: int | None = None) -> list[int]:
    """n distinct ints drawn from range(max_value), in random order.

    max_value defaults to 10 * n so values aren't just a shuffle of 0..n-1.
    """
    if max_value is None:
        max_value = max(10 * n, 1)
    if max_value < n:
        raise ValueError("max_value must be >= n to get n distinct values")
    return rng.sample(range(max_value), n)


def nearly_sorted_array(n: int, swaps: int, rng: random.Random) -> list[int]:
    """Sorted array with `swaps` random adjacent swaps (each adds at most 1 inversion)."""
    arr = sorted_array(n)
    if n < 2:
        return arr
    for _ in range(swaps):
        i = rng.randrange(n - 1)
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# --- Part II: coin systems -----------------------------------------------------


def random_coin_system(
    k: int,
    max_coin: int,
    rng: random.Random,
    include_one: bool = True,
) -> tuple[int, ...]:
    """k distinct denominations from 1..max_coin, sorted ascending.

    include_one=True (the default for generated systems) guarantees 1 is present,
    so every target A >= 0 is feasible. Use include_one=False to produce impossible cases.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    if include_one:
        if k > max_coin:
            raise ValueError("k must be <= max_coin")
        others = rng.sample(range(2, max_coin + 1), k - 1)
        return tuple(sorted([1, *others]))
    if k > max_coin - 1:
        raise ValueError("k must be <= max_coin - 1 when include_one is False")
    return tuple(sorted(rng.sample(range(2, max_coin + 1), k)))
