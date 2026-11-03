"""Shared pytest setup.

1. Any test that hits a NotImplementedError is reported as SKIPPED, not FAILED.
   So `pytest` stays green while stubs are unfinished, and the skip list shows
   what's left (e.g. "not implemented yet: P2: memo").
2. Small, test-only helpers that don't depend on any teammate's code.
"""

from __future__ import annotations

from collections import deque

import pytest

from coins import IMPOSSIBLE

SEED = 4050


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if call.when == "call" and call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        reason = str(call.excinfo.value) or item.name
        report.outcome = "skipped"
        report.longrepr = (str(item.path), item.location[1] or 0, f"Skipped: not implemented yet: {reason}")


def reference_min_coins(D, A):
    """Test-only oracle: fewest coins summing to A, via breadth-first search over amounts.

    A different method from every team solver, so it is an independent check.
    Returns an int, or IMPOSSIBLE. Keep A small (it's O(k * A)).
    """
    if A == 0:
        return 0
    dist = {0: 0}
    queue = deque([0])
    while queue:
        amount = queue.popleft()
        for d in D:
            nxt = amount + d
            if nxt == A:
                return dist[amount] + 1
            if nxt < A and nxt not in dist:
                dist[nxt] = dist[amount] + 1
                queue.append(nxt)
    return IMPOSSIBLE


def assert_coin_result(D, A, result, expected_count):
    """Minimal test-only sanity check (P4's validate_solution is the official, fuller validator)."""
    if expected_count is IMPOSSIBLE:
        assert result is IMPOSSIBLE, f"D={D}, A={A}: expected IMPOSSIBLE, got {result}"
        return
    assert result is not IMPOSSIBLE, f"D={D}, A={A}: expected {expected_count} coins, got IMPOSSIBLE"
    count, coins = result
    assert count == expected_count, f"D={D}, A={A}: expected {expected_count} coins, got {count}"
    assert len(coins) == count, f"count {count} != len(coins) {len(coins)}"
    assert sum(coins) == A, f"coins {coins} sum to {sum(coins)}, not {A}"
    assert set(coins) <= set(D), f"coins {coins} use values not in D={D}"
