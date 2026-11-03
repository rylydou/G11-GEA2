"""Independent solution validator (Part 2B).  Owner: P4

Checks a solver's answer without trusting the solver.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from coin_common import IMPOSSIBLE, CoinResult

NOT_GIVEN: Any = object()  # default for expected_count: "don't check the count"


def validate_solution(
    D: Iterable[int],
    A: int,
    result: CoinResult,
    expected_count: int | None = NOT_GIVEN,
) -> None:
    """Raise ValueError (with a clear message) if `result` is not a valid answer.

    Always check:
        - result is IMPOSSIBLE or a (coin_count, chosen_coins) pair
        - coin_count == len(chosen_coins)
        - sum(chosen_coins) == A
        - every coin is one of the denominations in D

    If expected_count is given:
        - expected_count=IMPOSSIBLE -> result must be IMPOSSIBLE
        - expected_count=<int>      -> result must exist and use exactly that many coins

    Returns None when the result is valid.
    """
    # TODO(P4)
    raise NotImplementedError("P4: validate_solution")
