"""Plotting helper (shared). Reads result CSVs, so plotting never runs inside timed code."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from results import PLOTS_DIR, read_csv


def plot_csv(
    csv_path: Path | str,
    x: str,
    y: str,
    out_path: Path | str | None = None,
    group_by: str | None = None,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    logx: bool = False,
    logy: bool = False,
) -> Path:
    """Line plot of column `y` against column `x`, one line per value of `group_by`.

    Example (one line per algorithm, log-log axes):
        plot_csv("results/inversion_benchmark.csv", x="n", y="median_seconds",
                 group_by="algorithm", logx=True, logy=True)

    Saves a PNG (default: results/plots/<csv stem>_<y>.png) and returns its path.
    """
    import matplotlib

    matplotlib.use("Agg")  # no GUI window; works on any machine
    import matplotlib.pyplot as plt

    csv_path = Path(csv_path)
    rows = read_csv(csv_path)
    if not rows:
        raise ValueError(f"{csv_path} has no rows")

    series: dict[str, list[tuple[float, float]]] = defaultdict(list)
    for row in rows:
        key = row[group_by] if group_by else y
        series[key].append((float(row[x]), float(row[y])))

    fig, ax = plt.subplots(figsize=(7, 4.5))
    for label, points in series.items():
        points.sort()
        xs, ys = zip(*points)
        ax.plot(xs, ys, marker="o", label=label)

    if logx:
        ax.set_xscale("log")
    if logy:
        ax.set_yscale("log")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    ax.set_title(title or f"{y} vs {x}")
    ax.grid(True, which="both", alpha=0.3)
    if group_by:
        ax.legend()
    fig.tight_layout()

    if out_path is None:
        out_path = PLOTS_DIR / f"{csv_path.stem}_{y}.png"
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path
