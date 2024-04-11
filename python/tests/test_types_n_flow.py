#!../env/bin/python3
import pytest
from types_n_flow import *


def test_convert_to_float():
    assert 3.0 == convert_to_float(3)
    assert 110.0 == convert_to_float("110.0")
    assert 4.5 == convert_to_float("4.5")


def test_is_odd_or_mul_of_ten():
    assert is_odd_or_mul_of_ten(0)
    assert is_odd_or_mul_of_ten(1)
    assert is_odd_or_mul_of_ten(5)
    assert is_odd_or_mul_of_ten(10)
    assert is_odd_or_mul_of_ten(40)
    assert is_odd_or_mul_of_ten(-710)
    assert is_odd_or_mul_of_ten(-711)
    assert is_odd_or_mul_of_ten(33)
    assert not is_odd_or_mul_of_ten(22)
    assert not is_odd_or_mul_of_ten(2)
    assert not is_odd_or_mul_of_ten(-8)
    assert not is_odd_or_mul_of_ten(64)
    assert not is_odd_or_mul_of_ten(2002)


def test_convert_to_binary():
    assert "11" == convert_to_binary(3)
    assert "100" == convert_to_binary(8)
    assert "101" == convert_to_binary(9)


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


def test_one_operation_string_calculator():
    # [+, -, *, %, /, //, <, !=]
    assert 15 == one_operation_string_calculator("10 + 5")
    assert one_operation_string_calculator("10 - 5") == one_operation_string_calculator(
        "10 + -5"
    )
    assert -77 > one_operation_string_calculator(
        "2.22 - 80.1"
    ) and -78 < one_operation_string_calculator("2.22 - 80.1")
    assert 0.0 == one_operation_string_calculator("0 * 1.0")
    assert 22 == one_operation_string_calculator("11 * 2")
    assert 1 == one_operation_string_calculator("13 % 2")
    assert 0 == one_operation_string_calculator("66 % 2")
    assert 21 == one_operation_string_calculator("42 / 2")
    assert 111.0 == one_operation_string_calculator("333.3333 // 3")
    assert one_operation_string_calculator("23.68 < 23.7")
    assert not one_operation_string_calculator("23.68 < 23")
    assert one_operation_string_calculator("30 != -30")
    assert not one_operation_string_calculator("34 != 34")
