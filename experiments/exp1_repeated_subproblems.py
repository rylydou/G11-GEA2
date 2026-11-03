"""Part 2C Exp 1: repeated subproblems in naive recursion vs. memoization.  Owner: P2

Run:     python experiments/exp1_repeated_subproblems.py
Output:  results/exp1_repeated_subproblems.csv (+ .meta.json)
Plot:    python experiments/plot_results.py results/exp1_repeated_subproblems.csv \
             --x A --y calls --group-by solver --logy
"""

from coins import memo, naive, new_stats  # noqa: F401
from results import results_path, write_csv, write_metadata

DENOMINATIONS = (1, 3, 4)    # TODO(P2): pick and justify a system
TARGETS = range(0, 41, 2)    # TODO(P2): increase until naive becomes impractical
NAIVE_CALL_CUTOFF = 10**7    # safety cutoff: stop running naive once a run exceeds this many calls

COLUMNS = ["solver", "denominations", "A", "coin_count", "calls", "distinct_states", "cache_hits", "cutoff_hit"]


def run() -> list[dict]:
    """One row per (solver, A), using new_stats() for each run."""
    # TODO(P2): run naive and memo for each target; stop naive once NAIVE_CALL_CUTOFF is hit
    raise NotImplementedError("P2: exp1.run")


def main() -> None:
    rows = run()
    out = write_csv(rows, results_path("exp1_repeated_subproblems.csv"), COLUMNS)
    write_metadata(out, denominations=DENOMINATIONS, targets=list(TARGETS), naive_call_cutoff=NAIVE_CALL_CUTOFF)
    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
