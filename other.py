import math


def funct_sum(x):
    if x == 0:
        return x
    elif x == 1:
        return x
    else:
        return x + funct_sum(x - 1)


a = funct_sum(10)


def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)


a = factorial(3)

some_dict = {'first': 1, 'second': 2}


def add(*args):
    print(args)



a = (1,5,6,7)

print(sum())

