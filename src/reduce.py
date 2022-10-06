"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')
# Hvad gør TypeVar og Callable?

def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    """
    assert len(x) >= 2
    
    # Version where the intermediate results are not stored in memory.
    number = x[0]
    for i in range(1, len(x)):
        number = f(number, x[i])
    return number

    # Version where memory to store intermediate results are used.
    # n = len(x)
    # y = [0]*n
    # y[0] = x[0]
    # for i in range(1, len(x)):
    #    y[i] = f(y[i-1], x[i])
    # return y[n-1]

print(reduce(lambda x,y: x+y, [1, 2, 3]))
print(reduce(lambda x,y: x*y, [1,2,3]))

def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    """
    n = len(x)
    y = [0] * n
    y[0] = x[0]
    for i in range(1,len(x)):
        y[i] = f(y[i-1], x[i])
    return y

print(accumulate(lambda x,y: x+y, [1,2,3]))
print(accumulate(lambda x,y: x*y, [1,2,3]))
