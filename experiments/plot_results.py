"""Make a PNG plot from any results CSV (shared).

Example:
    python experiments/plot_results.py results/inversion_benchmark.csv \
        --x n --y median_seconds --group-by algorithm --logx --logy
"""

import argparse

from plotting import plot_csv


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", help="path to a results CSV")
    p.add_argument("--x", required=True, help="column for the x-axis")
    p.add_argument("--y", required=True, help="column for the y-axis")
    p.add_argument("--group-by", help="column whose values become separate lines")
    p.add_argument("--out", help="output PNG (default: results/plots/<csv>_<y>.png)")
    p.add_argument("--title")
    p.add_argument("--xlabel")
    p.add_argument("--ylabel")
    p.add_argument("--logx", action="store_true")
    p.add_argument("--logy", action="store_true")
    a = p.parse_args()

    out = plot_csv(a.csv, a.x, a.y, out_path=a.out, group_by=a.group_by, title=a.title,
                   xlabel=a.xlabel, ylabel=a.ylabel, logx=a.logx, logy=a.logy)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
