def checkIndex(key):

    if not isinstance(key, (int, long)): raise TypeError
    if key<0 : raise IndexError

class ArithmeticSequence:

    def __init__(self,start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}


    def __getitem__(self, key):

        checkIndex(key)
        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter +=1
        return super(CounterList, self).__getitem__(index)


class TestIterator:
    value = 0
    def next(self):
        self.value +=1
        if self.value >10 : raise StopIteration
        return self.value
    def __iter__(self):
        return self

def flattern(nested):
    try:
        for sublist in nested:
            for elem in flattern(sublist):
                yield elem
    except TypeError:
        yield nested


def flatternString(nested):
    try:
        try:
            nested + ""
        except TypeError:
            pass
        else: raise TypeError
        for sublist in nested:
            for elem in flatternString(sublist):
                yield elem
    except TypeError:
        yield nested
        
def conflict(state, nextx):
    nexty = len(state)
    for i in range(nexty):
        if abs(state[i]-nextx) in (0, nexty-1):
            return True
    return False

def queens(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
    else :
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos, )+result

def print_params(x,y, z=3, *pospar, **keypar):
    print x, y,z
    print pospar
    print keypar

def story(**kwds):
    return "once upon a time. There was a '\
                '%(job)s called %(name)s" % kwds
                
            
def interval(start, stop=None, step=1):
    """imitates range() for step >0"""
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i<stop:
        result.append(i)
        i += step
    return result
        


def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

def _test():
    import doctest
    doctest.testmod()    

if __name__ == "__main__":
    _test()
