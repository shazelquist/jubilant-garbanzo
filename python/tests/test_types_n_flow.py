#!../env/bin/python3
import pytest
from types_n_flow import *


def test_convert_to_binary():
    assert 11 == convert_to_binary(3)
    assert 100 == convert_to_binary(8)
    assert 101 == convert_to_binary(9)


def test_convert_to_decimal():
    assert 3 == convert_to_decimals(11)
    assert 8 == convert_to_decimals(100)
    assert 9 == convert_to_decimals(101)


def test_get_even_max():
    assert get_even_max([-12, 55, 11]) == -12
    assert get_even_max([2, 6, 8, 12, 15, 16, 17]) == 17
    assert get_even_max([]) == None


def test_get_pn_sum():
    p, n = get_pn_sum([-15, 5.5, 600, 10])
    assert p == 615.5 and n == -15
    p, n = get_pn_sum([-15, -1, -1, -4])
    assert p == 0 and n == -21
