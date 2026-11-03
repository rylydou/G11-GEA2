"""Automated search for greedy counterexamples (Part 2B).  Owner: P4

A counterexample is a (D, A) where greedy finds a solution, but uses MORE coins
than the exact optimum from bottom-up DP.

Required sanity check: the search must find D = {1, 3, 4}, A = 6
(greedy 4+1+1 = 3 coins, optimum 3+3 = 2 coins).

Import the solvers from their own modules (`from greedy import greedy`,
`from bottom_up import bottom_up`, `from validate import validate_solution`),
NOT from `coins`. coins.py imports this file, so that would be a circular import.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence


def find_greedy_counterexamples(
    coin_systems: Iterable[Sequence[int]],
    max_target: int,
) -> list[dict]:
    """Check every coin system against every target 0..max_target.

    Returns one dict per counterexample (CSV-friendly, see results.write_csv):
        {
            "denominations": tuple[int, ...],   # sorted
            "A": int,
            "greedy_count": int,
            "greedy_coins": list[int],
            "optimal_count": int,
            "optimal_coins": list[int],
        }

    Skip targets where greedy returns IMPOSSIBLE. Those are greedy failures too,
    but not the "feasible but worse" kind the assignment asks for.
    Compare against bottom_up (exact DP) and validate both answers with validate_solution.
    """
    # TODO(P4)
    raise NotImplementedError("P4: find_greedy_counterexamples")
