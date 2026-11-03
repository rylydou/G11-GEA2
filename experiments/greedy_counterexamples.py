"""Part 2B: automated search for greedy counterexamples.  Owner: P4

Run:     python experiments/greedy_counterexamples.py
Output:  results/greedy_counterexamples.csv (+ .meta.json)
"""

from coins import find_greedy_counterexamples  # noqa: F401
from generators import make_rng, random_coin_system  # noqa: F401
from results import results_path, write_csv, write_metadata

SEED = 4050
MAX_TARGET = 100
# Always include the required sanity-check system; TODO(P4): add more (random and/or enumerated).
COIN_SYSTEMS = [(1, 3, 4)]

COLUMNS = ["denominations", "A", "greedy_count", "greedy_coins", "optimal_count", "optimal_coins"]


def run() -> list[dict]:
    # TODO(P4): build the list of systems, call find_greedy_counterexamples, return rows
    raise NotImplementedError("P4: greedy_counterexamples.run")


def main() -> None:
    rows = run()
    out = write_csv(rows, results_path("greedy_counterexamples.csv"), COLUMNS)
    write_metadata(out, seed=SEED, max_target=MAX_TARGET, coin_systems=COIN_SYSTEMS)
    print(f"wrote {len(rows)} counterexamples to {out}")


if __name__ == "__main__":
    main()
