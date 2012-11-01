"""
Build a ArithmeticSequence class that have the following attributes and methods
1. __init__(self, arguv1, argv2)
2. __getitem__
3. setittem__
"""


def checkIndex(key):

    if not isinstance(key, (int, long)): raise TypeError
    if key<0: raise IndexError


class ArithmeticsSequence:

    def __init__(self, start=0, step=0):
        self.start = start  # Store the start value
        self.step = step   #Store the step value
        self.changed = {} # No items have been modified


    def __getitem__(self, key):

        checkIndex(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):

        checkIndex(key)
        self.changed[key] = value


class Fibs:

    def __init__(self):
        self.a =0
        self.b =1

    def next(self):
        self.a,  self.b = self.b, self.a + slef.b
        return self.a
    def __iter__(self):
        return self




