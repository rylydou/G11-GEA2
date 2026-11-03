"""Part II: coin change. One import point for everything coin-related:

    from coins import greedy, naive, memo, bottom_up, IMPOSSIBLE, new_stats, ...

Every solver shares one interface:

    solver(D, A)              -> (coin_count, chosen_coins) | IMPOSSIBLE
    solver(D, A, stats=dict)  -> same, and fills in instrumentation counters

Ownership:
    greedy, naive, memo         P2
    bottom_up                   P3
    validate_solution           P4
    find_greedy_counterexamples P4
"""

from bottom_up import bottom_up
from coin_common import (
    IMPOSSIBLE,
    STAT_KEYS,
    CoinResult,
    bump,
    check_target,
    new_stats,
    normalize_denominations,
)
from counterexamples import find_greedy_counterexamples
from greedy import greedy
from memo import memo
from naive import naive
from validate import validate_solution

EXACT_SOLVERS = {"naive": naive, "memo": memo, "bottom_up": bottom_up}
SOLVERS = {"greedy": greedy, **EXACT_SOLVERS}

__all__ = [
    "IMPOSSIBLE",
    "STAT_KEYS",
    "CoinResult",
    "EXACT_SOLVERS",
    "SOLVERS",
    "bottom_up",
    "bump",
    "check_target",
    "find_greedy_counterexamples",
    "greedy",
    "memo",
    "naive",
    "new_stats",
    "normalize_denominations",
    "validate_solution",
]
