import numpy as np

# %% Pattern matching arraylike


def patMatch(arr):
    print('#'*30+'\n'+f'Input: {arr}\n' + '#'*30)
    match arr:
        case [0, 0]:
            print(F'origin: {arr}\n')
        case [0, y]:
            print(F'Vertical line: {y}\n')
        case [x, 0]:
            print(F'Horisontal line: x={x}\n')
        case [x, y, _]:
            print(F'Three elements starting with: {(x,y)}\n')
        case [x, y, z, *e]:
            l = len(e)
            print(F'Three elements or more starting with: ({x}, {y}, {z},...)\n'
                  F'some of the ending {e[0:int(l/2)]}\n'
                  f'last of the ending {e[-int(l/2):]}\n'
                  )
        case [x, y] if x==y:
            print(f'x=y: {x}={y}\n')
        case _:
            print(F'None were matched for {arr}\n')


arr1 = range(0, 21, 4)  # vary range to test some cases
arr2 = [3, 3]  # case equal guard
# patMatch(arr1)
# patMatch(arr2)


# %% Dict pattern match

def dictMatch(d):
    match d:
        case {'first': str(s)}:
            print(f'It is a dict with a string: {s}')
        case {'second': int(i)}:
            print(f'It is a dict with an int: {i}')
        # case {k: str()}:
        #     print(f'Dict with key {k}')


d1 = {
    'first': 'string',
    'second': 123,
    'third': ('string1', 'string2'),
    'fourth': (123, 321),
    'fifth': {'fifthSub': 'inception'}
}


# dictMatch(d1)

i = 1


def argsKwargsMatch(*args, **kwargs):
    global i
    print(f'\nrun {i}')
    i+=1
    match (args, kwargs):
        # case ((), {}):
        #     print('neither args nor kwargs')
        # case ((), k):
        #     print(f'no args, only kwargs: {k}')
        # case (a, {}):
        #     print(f'No kwargs, only args: {a}')
        # case (a, {**k}):
        #     print(f'both args and kwargs: {a}, {k}')
        case ((), k):
            print('kwargs', k)
        case (a, {}):
            print('args', a)
        case a, k:
            print('args, kwargs', a, k)

        case debug:
            print(debug)
    print()


d2 = {  # unpack for kwargs
    'key': 'value'
}
args = ['stuff', 123, 'more']

# argsKwargsMatch()
# argsKwargsMatch(**d2)
# argsKwargsMatch('stuff', 123, 'more', 'no Kwargs tho.')
argsKwargsMatch('stuff', 123, 'more', **d2)
