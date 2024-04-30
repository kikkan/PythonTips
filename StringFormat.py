import random
from time import perf_counter as pf
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape


def timeit():
    # start = pf()
    # print('*-'*10, 'Started', '-*'*10)
    # yield
    # print(f'Runtime: {round(pf() - start, 4)}')
    # yield
    while 1:
        start = pf()
        yield
        dt = pf() - start
        print(f'Runtime: {round(dt, 4)}')
        yield dt


def dotFormat(v, m):
    print('#'*50)
    print('Testing .format() method:\n')
    print('This is a test with some values lined up')
    s = ['value one,', ' should appear at\n', 'the same spot as value two,', '.']
    print('{:<30}{}{}'
          '{:<30}{}{}'
          ''.format(s[0], v[0], s[1], s[2], v[1], s[3]))

    print('\nThis is a custom table with .format:')
    for i in m:
        print('|', end='')
        for j in i:
            print('{:>4}'.format(j), end='')
        print('|')


def fstring(v, m):
    print('#'*50)
    print('Testing the f string method:\n')
    s = ['value one,', ' should\n', 'appear at the same spot as value two,', '.']
    print(f'{s[0]:<40}{v[0]}{s[1]}'
          f'{s[2]:<40}{v[1]}{s[3]}'
          )

    print('\nThis is a custom table with f string:')
    for i in m:
        print('|', end='')
        for j in i:
            print(f'{j:>4}', end='')
        print('|')


def main():
    values = [1, 2, 3, 4, 5]
    np.random.seed(1)
    matrix = np.random.randint(0, 1e3, size=(10, 10))
    t = timeit()
    # next(timeit())
    # timeit()
    next(t)
    dotFormat(values, matrix)
    timeFormat = next(t)
    # next(timeit)
    # next(timeit())
    next(t)
    fstring(values, matrix)
    timeFstring = next(t)

    print('\n\nTime comparison\n'
          f'.format:  {round(timeFormat,5)}\n'
          f'f string: {round(timeFstring, 5)}'
          )


main()


random.seed()


# def do_action1():
#     print("Hello")
#     yield
#     print("HELLO!")
#     yield
#     print("hello?")


# def do_action2():
#     print("Are you there?")
#     yield
#     print("ARE YOU THERE!")
#     yield
#     print("I'm scared.")


# def do_action3():
#     print("Is somebody out there?")
#     yield
#     print("SOMEBODY IS OUT THERE!")
#     yield
#     print("I'm dead.")


# def bot(*actions):
#     actions = [action() for action in actions]
#     while actions:
#         action = random.choice(actions)
#         try:
#             next(action)
#         except StopIteration:
#             actions.remove(action)
#     return


# bot(do_action1, do_action2, do_action3)
