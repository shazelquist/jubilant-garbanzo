import random

insults = [
    "WOW this function smells",
    "This function needs to take a bath",
    "BTW not even using arch btw",
    "When is the last time you read a book?",
    "BEEP" * 300,
    "I bet your computer is slow",
    "What even is a decorator",
    "I bet you can't guess my memory address",
]


def totally_normal_decorator(func):
    return Insult(func)


class Insult:
    def __init__(self, func):
        self.text = random.choice(insults)
        self.func = func
        self.__name__ = "angy insulter"

    def __call__(self, *param, **kparams):
        print(self.func.__name__, "SUCKS,", random.choice(insults))
        if random.randint(0, 15) == 5:
            print("This is my function now, hope it didn't do anything important!")
        else:
            return self.func(*param, **kparams)
