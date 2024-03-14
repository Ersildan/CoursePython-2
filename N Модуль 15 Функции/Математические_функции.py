# put your python code here
from math import *


def f1():
    return n**2


def f2():
    return n**3


def f3():
    return n**0.5


def f4():
    return abs(n)


def f5():
    return sin(n)


commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}

n = int(input())
command = input()

print(commands[command](n))
