#!../env/bin/python3
import pytest
from functions import *


def test_has_substring():
    assert has_substring(["a", "b", "c", "d"], "a")
    assert has_substring(["a", "b", "c", "d"], "b")
    assert has_substring(["a", "b", "c", "d"], "c")
    assert has_substring(["a", "b", "c", "d"], "d")
    assert not has_substring(["a", "b", "c", "d"], "e")
    assert has_substring(["alpha", "beta", "delta", "gamma"], "mm")
    assert has_substring(["alpha", "beta", "delta", "gamma"], "be")
    assert has_substring(["alpha", "beta", "delta", "gamma"], "ta")
    assert not has_substring(["alpha", "beta", "delta", "gamma"], "gama")


def test_sum_of_previous_ints():
    samples = list(range(1, 10))
    for samp in samples:
        assert sum_of_previous_ints(samp) == sum(samples[:samp])


def test_get_lambda():
    lamb_2 = get_lambda(2)
    assert lamb_2("a", "eeaaee") == 4
    assert lamb_2("_", "__aa__") == 16
    assert lamb_2("a", "aa aa") == 16
    lamb_6p5 = get_lambda(6.5)
    assert lamb_6p5("a", "__aa__") == 2**6.5
    assert lamb_6p5("a", "aa_aa") == 4**6.5
