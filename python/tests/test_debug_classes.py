#!../env/bin/python3
import pytest
from debug_classes import *


def test_addition_value():
    wn_a = Weird_number(30.30)
    wn_b = Weird_number(-600)
    assert wn_a + wn_b == Weird_number(-569.7)


def test_addition_is_communitive():
    wn_a = Weird_number(30.30)
    wn_b = Weird_number(-600)
    assert wn_a + wn_b == wn_b + wn_a


def test_subtraction_value():
    wn_a = Weird_number(30.30)
    wn_b = Weird_number(-600)
    assert wn_a - wn_b == Weird_number(630.3)


def test_subtraction_not_communitive():
    wn_a = Weird_number(30.30)
    wn_b = Weird_number(-600)
    assert wn_a - wn_b != wn_b - wn_a


def test_multiplication_value():
    wn_a = Weird_number("1.0")
    wn_b = Weird_number(2)
    wn_c = Weird_number(3.0)
    assert wn_b * wn_a == wn_b
    assert wn_b * wn_c == Weird_number(6.0)


def test_div_by_zero_throws():
    wn_a = Weird_number(5.0)
    wn_b = Weird_number(0)
    with pytest.raises(ZeroDivisionError):
        wn_a / wn_b


def test_eq():
    wn_a = Weird_number(5.0)
    wn_b = Weird_number(0)
    wn_c = Weird_number(5)
    assert wn_a == wn_c
    assert wn_b == wn_b


def test_get_square():
    wn_a = Weird_number(5.0)
    wn_b = Weird_number(0)
    assert wn_a.get_square() == Weird_number(25)
    assert wn_b.get_square() == Weird_number(0.0)


def test_get_squareroot():
    wn_a = Weird_number(4.0)
    wn_b = Weird_number(0)
    assert wn_a.get_squareroot() == Weird_number(2)
    assert wn_b.get_squareroot() == Weird_number(0.0)
