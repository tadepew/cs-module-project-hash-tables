import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


"""
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
sol = dict()


def compute_sol():
    for x in range(2, 14):

        for y in range(3, 6):

            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653

            sol[(x, y)] = v


compute_sol()


def slowfun(x, y):

    return sol[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
