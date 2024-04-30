# import numpy as np
# import matplotlib.pyplot as plt
from numpy import pi, linspace, sin
from matplotlib.pyplot import plot, show
import os


def f(x):
    return sin(x)


def info():
    curr = os.getcwd()
    fileloc = os.path.dirname(os.path.realpath(__file__))
    print('We are currently in \n'
          '\t{}\n'
          'According to "os.path.dirname(os.path.realpath(__file__))" the file is in\n'
          '\t{}\n'
          '\n'.format(curr, fileloc))


def menu():
    choices = f'\n\nmake a choice bitch\n' \
        '1\tdo nothing\n' \
        '2\tShow beautiful plot\n' \
        '3\tinfo\n' \
        '0\tExit\n>>>'

    v = 100
    x = linspace(0, 2*pi, 100)
    y = f(x)
    while v != 0:
        v = input(choices)
        if v == "1":
            continue
        elif v == "2":
            plot(x, y)
            show()
        elif v =="3":
            info()
        elif v =="0":
            break
        else:
            print(f'wrong voice command "{v}". Need to be either 1, 2 or 3.\n'
                  'Please try again')


menu()
