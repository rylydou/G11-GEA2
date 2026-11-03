"""Timing harness.  Owner: P3

Keep timing separate from input generation, plotting, file I/O, and formatting.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def time_call(
    fn: Callable[..., Any],
    make_args: Callable[[], tuple],
    repeats: int = 5,
    warmup: int = 1,
) -> dict[str, Any]:
    """Time fn(*make_args()) several times and summarize the results.

    Args:
        fn:        the function to time
        make_args: builds a fresh argument tuple for each run. It is called
                   OUTSIDE the timed region, so input creation and copying aren't timed.
        repeats:   number of timed runs
        warmup:    untimed runs first, to warm caches

    Returns:
        {"median": float, "min": float, "max": float, "times": list[float], "repeats": int}
        (all times in seconds)

    Suggestions: use time.perf_counter() around the call only, and
    statistics.median() for the summary. Consider gc.disable() during the
    timed call (and re-enable after) to cut noise.
    """
    # TODO(P3)
    raise NotImplementedError("P3: time_call")
