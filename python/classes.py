#!env/bin/python3
"""
This file contains some weird examples that you need to debug

"""
import pytest

# Some terminal color values
Y_TXT = "\033[93m"
R_TXT = "\033[91m"
RST_TXT = "\033[0m"


# CLASSES
class Weird_number:
    def __init__(self, value):
        assert str(value).replace(".", "").replace("-", "").isnumeric()
        data = None
        if type(value) == type(self):
            data = value.data
        else:
            # TODO: there's something that you can improve on the next line (what type is 'value'?)
            data = value

        self.data = data

    def get_square(self):
        """Returns Wn^2"""
        return Weird_number(self.data**2)

    def __repr__(self):
        """repr ie: representation, used as a default for print if not otherwised defined"""
        return f"{self.data}"

    def __add__(self, other):
        """Returns Wn + other Wn"""
        # TODO
        return Weird_number(self.data - other.data)

    def __sub__(self, other):
        """Returns Wn - other Wn"""
        # TODO
        return Weird_number(self.data + other.data)

    def __mul__(self, other):
        """Returns Wn * other Wn"""
        return Weird_number(self.data * other.data)

    def __truediv__(self, other):
        """Returns Wn / other Wn"""
        # TODO
        return Weird_number(other.data / self.data)

    def __eq__(self, other):
        """Returns Wn == other Wn"""
        return self.data == other.data

    # TODO: Add a method called `shift` that takes an integer argument
    # This method mutates Weird number by 10 times that integer and has no return value


def main():
    # CLASSES
    # help(Weird_number)
    print("CLASS PRACTICE")
    wn_a = Weird_number(30.30)
    wn_b = Weird_number(-600)
    wn_c = Weird_number(0)
    wn_d = Weird_number("1.0")
    wn_e = Weird_number(3)

    print(
        f"Initialized set:\n\t{Y_TXT}wn_a: {wn_a}\n\twn_b: {wn_b}\n\twn_c: {wn_c}\n\twn_d: {wn_d}\n\twn_e: {wn_e}{RST_TXT}\n"
    )
    print(f"  wn_a {Y_TXT}+{RST_TXT} wn_b = {R_TXT}{wn_a + wn_b}{RST_TXT}")
    print(f"  wn_c {Y_TXT}-{RST_TXT} wn_a = {R_TXT}{wn_c + wn_a}{RST_TXT}")
    print(f"  wn_c {Y_TXT}*{RST_TXT} wn_b = {R_TXT}{wn_c * wn_b}{RST_TXT}")
    print(f"  wn_b {Y_TXT}/{RST_TXT} wn_c = {R_TXT}{wn_b / wn_c}{RST_TXT}")
    print(
        f"  (wn_b {Y_TXT}/{RST_TXT} wn_c == wn_c) = {R_TXT}{(wn_b / wn_c == wn_c)}{RST_TXT}"
    )
    print(f"  wn_d {Y_TXT}*{RST_TXT} wn_e {R_TXT}{wn_d * wn_e}{RST_TXT}")
    print(f"  {Y_TXT}wn_d.get_square(){RST_TXT} = {wn_d.get_square()}")
    wn_a += wn_b
    print(f"  wn_a {Y_TXT}+={RST_TXT} wn_b = {R_TXT}{wn_a}{RST_TXT}")


if __name__ == "__main__":
    main()
