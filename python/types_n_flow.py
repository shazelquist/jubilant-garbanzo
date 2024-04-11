#!env/bin/python3
"""
This file contains some weird examples that you need to debug

"""
import pytest


def convert_to_float(value):
    """Convert some value to a floating point"""
    # TODO
    return


def is_odd_or_mul_of_ten(value: int):
    """Test if the given integer is odd or a multiple of ten, returns a boolean"""
    # TODO
    return


def convert_to_binary(decimal):
    """Convert a number base 10 to base 2 and return it, the return value should be a string"""
    # TODO
    return


def convert_to_decimal(binary):
    """Convert a number base 2 to base 10 and return it"""
    # TODO
    return


def get_even_max(iterable):
    """Returns the maximum even value or None if the iterable is empty"""
    # TODO
    return


def get_pn_sum(iterable):
    """Given a list of numerics, returns both the sum of the positive and negative values"""
    # TODO
    pos_sum, neg_sum = 0, 0

    return pos_sum, neg_sum


def one_operation_string_calculator(command):
    """
    Given a string of the form 'number operation number', calculate and return the result
    Example:
        one_operation_string_calculator('2 + 3') returns the value 6
    Must be able to handle the following operators [+, -, *, %, /, //, <, !=]
    """
    # TODO
    return


def main():
    # Numerics
    # int
    print("\ninteger methods:", dir(int))
    i_a = int(11)
    i_b = 13
    i_c = int("11", base=2)
    i_d = int("11", base=16)
    print(f"int a {i_a}")
    print(f"int b {i_b}")
    print(f"int c {i_c}")
    print(f"int b {i_b}")
    print(f"int b {i_d}")

    # floats
    print("\nfloat methods", dir(float))
    f_a = float(11.1)
    f_b = 13.1
    f_c = 3 / 2
    f_d = 1 / 3
    print(f"float a {f_a}")
    print(f"float b {f_b}")
    print(f"float c {f_c}")
    print(f"float d {f_d}")

    # strings
    print("\nstring methods:", dir(str()))
    s_a = str(111)
    s_b = "eeeee"
    # s_c = input('please enter something: ')
    s_d = "".join(["1", "2", "3", "4"])
    s_e = f"s_d == {s_d}"
    print(f"string a {s_a}")
    print(f"string b {s_b}")
    # print(f'string c {s_c}')
    print(f"string d {s_d}")
    print(f"string e {s_e}")

    # containers
    l_a = [1, 2, 3]  # list()
    t_a = (1, 2, 3)  # tuple()
    d_a = {1: "a", 2: "b", 3: "c"}  # dict()

    for i in range(0, 10):
        l_a.append(max(l_a) + i)

    print(f"l_a {l_a}, l_a[0]:{l_a[0]}")
    print(f"t_a {t_a} l_a[2]:{l_a[3]}")
    print(f"d_a {d_a} d_a[1]:{d_a[1]}")

    # control flow
    int_list = [1, 2, 3, 4, 5, 6]
    print("\nint_list:", int_list)
    for a in int_list:
        if a % 2 == 0:
            is_even = True
        else:
            is_even = False
        print("value of a:{} is even:{}".format(a, is_even))

    print("alternative even values:", [a for a in int_list if a % 2 == 0])
    print("alternative is even:    ", [a % 2 == 0 for a in int_list])

    value = 4  # change me if you want
    if value <= 0:
        print("value is <= 0")
    elif value < 3:
        print(f"value is < 3")
    else:
        print("value is > 2")

    for lvl1 in ["drink", "coffee"]:
        print("\t" + lvl1)
        for lvl2 in lvl1:
            print("\t(" + lvl2 + ")")


if __name__ == "__main__":
    main()
