#!env/bin/python3
"""
This file contains some weird examples that you need to debug

"""
import pytest
from totally_normal_module import totally_normal_decorator

# TODO: without removing or edditing the above import, clean up this module's output


@totally_normal_decorator
def sum_of_previous_ints(value: int):
    """Recursively calculates the sum of N_i + N_i-1 + ... N_0"""
    # TODO
    if value == 0:
        return 0
    else:
        return value + sum_of_previous_ints(value - 1)


@totally_normal_decorator
def handy_adder(base, add):
    print(f"\n\tI am going to add {base} to {add} for you")
    base += add
    print(f"\thandy adder result:", base)


@totally_normal_decorator
@totally_normal_decorator
@totally_normal_decorator
def what_is_my_return():
    pass


def min_max(arg):
    return min(arg), max(arg)


def get_lambda(power):
    """Returns a lambda that returns the count of a given character in text to a given power"""
    # TODO: edit the lambda to satisfy the contition
    return lambda character, text: character + text


@totally_normal_decorator
def main():
    # fix the implementation of this function so that it's correct
    print(sum_of_previous_ints(5))

    mylist = ["a", "b", "c", "d"]
    print("mylist:", mylist)
    handy_adder(mylist, ["e"])
    print("mylist after handy_adder:", mylist)
    myage = 30
    print("myage:", myage)
    handy_adder(myage, -4)
    print("myage after handy_adder", myage)

    # expansions
    handy_adder(*(-10, -20))
    handy_adder(*[5, 2])
    handy_adder(*{"add": [4], "base": [1, 2, 3]})
    handy_adder(**{"add": [4], "base": [1, 2, 3]})

    # returns
    print("The function name has a value:", what_is_my_return)
    print("The function can return a value", what_is_my_return())
    print("Returns are flexable in python", min_max([1, 21, 5, 6, 10]))

    # Lambdas
    # nameless functions, good for simple operations
    # Format:
    #    lambda arguments: singleline_expression
    lambda x, y: x**2 + y**2

    print(lambda x, y: x**2 + y**2)


if __name__ == "__main__":
    main()
