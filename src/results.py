"""Results I/O (shared): CSV/JSON files under results/ plus run metadata.

Every experiment should write:
    results/<name>.csv         the data behind a table or plot
    results/<name>.meta.json   seed, parameters, Python version, machine info
"""

from __future__ import annotations

import csv
import datetime as _dt
import json
import platform
import sys
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"
PLOTS_DIR = RESULTS_DIR / "plots"


def results_path(filename: str) -> Path:
    """Path inside results/ (creates the folder if needed)."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return RESULTS_DIR / filename


def _cell(value: Any) -> Any:
    """Store lists/tuples as JSON text (e.g. "[1, 3, 4]") so a CSV cell stays readable."""
    if isinstance(value, (list, tuple)):
        return json.dumps(list(value))
    return value


def write_csv(rows: Iterable[dict], path: Path | str, columns: Sequence[str] | None = None) -> Path:
    """Write a list of dicts to CSV. Columns default to the first row's keys."""
    rows = list(rows)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if columns is None:
        columns = list(rows[0].keys()) if rows else []
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(columns))
        writer.writeheader()
        for row in rows:
            writer.writerow({col: _cell(row.get(col)) for col in columns})
    return path


def read_csv(path: Path | str) -> list[dict[str, str]]:
    """Read a CSV into a list of dicts (all values are strings)."""
    with Path(path).open(newline="") as f:
        return list(csv.DictReader(f))


def write_json(obj: Any, path: Path | str) -> Path:
    """Write obj as pretty-printed JSON."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=list) + "\n")
    return path


def run_metadata(**params: Any) -> dict[str, Any]:
    """Environment info plus any experiment parameters (seed, sizes, repeats, ...)."""
    return {
        "timestamp_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "python_version": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "params": params,
    }


def write_metadata(results_file: Path | str, **params: Any) -> Path:
    """Write <results_file stem>.meta.json next to a results file."""
    results_file = Path(results_file)
    meta_path = results_file.with_name(results_file.stem + ".meta.json")
    return write_json(run_metadata(**params), meta_path)
