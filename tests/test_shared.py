"""Tests for shared glue (generators, input checks, results I/O, plotting). Should pass now."""

import json

import pytest

from coins import new_stats, normalize_denominations
from generators import (
    make_rng,
    nearly_sorted_array,
    random_coin_system,
    random_distinct_array,
    reverse_sorted_array,
    sorted_array,
)
from plotting import plot_csv
from results import read_csv, write_csv, write_metadata


def test_rng_is_reproducible():
    a = random_distinct_array(50, make_rng(7))
    b = random_distinct_array(50, make_rng(7))
    assert a == b


def test_array_generators():
    rng = make_rng(1)
    arr = random_distinct_array(100, rng)
    assert len(arr) == 100 and len(set(arr)) == 100
    assert sorted_array(4) == [0, 1, 2, 3]
    assert reverse_sorted_array(4) == [3, 2, 1, 0]
    nearly = nearly_sorted_array(20, 3, rng)
    assert sorted(nearly) == sorted_array(20)


def test_random_coin_system():
    rng = make_rng(2)
    for _ in range(50):
        D = random_coin_system(4, 20, rng)
        assert D[0] == 1 and len(set(D)) == 4 and list(D) == sorted(D)
        D2 = random_coin_system(3, 20, rng, include_one=False)
        assert 1 not in D2 and len(D2) == 3


def test_normalize_denominations():
    assert normalize_denominations([5, 1, 5, 3]) == (1, 3, 5)
    for bad in ([], [0, 1], [-2], [1.5]):
        with pytest.raises(ValueError):
            normalize_denominations(bad)


def test_new_stats_keys():
    assert new_stats() == {"calls": 0, "distinct_states": 0, "cache_hits": 0, "states_processed": 0}


def test_csv_round_trip_and_metadata(tmp_path):
    path = write_csv([{"D": (1, 3, 4), "A": 6}], tmp_path / "out.csv")
    assert read_csv(path) == [{"D": "[1, 3, 4]", "A": "6"}]
    meta = json.loads(write_metadata(path, seed=4050).read_text())
    assert meta["params"]["seed"] == 4050 and meta["python_version"]


def test_plot_csv(tmp_path):
    rows = [{"algorithm": alg, "n": n, "seconds": n * (2 if alg == "brute" else 1)}
            for alg in ("brute", "dc") for n in (1, 2, 4)]
    csv_path = write_csv(rows, tmp_path / "bench.csv")
    out = plot_csv(csv_path, x="n", y="seconds", group_by="algorithm", out_path=tmp_path / "p.png")
    assert out.exists() and out.stat().st_size > 0
