class limiter(object):
    __slots__ = ['age','name','job']


class C:                            # Requires "(object)" in 2.X only. cuz new-style classes derived from object
    __slots__ = ['a', 'b']          # __slots__ means no __dict__ by default


class D:                            # use D(object) for same result in 2.X
    __slots__ = ['a','b']
    def __init__(self):             # cannot add new names if no __dict__
        self.d = 4


class D_v2:
    __slots__ = ['a','b','__dict__']    # Name
    c = 3                               # class attrs work normally
    def __init__(self):
        self.d = 4                      # d stored in __dict__, a is a slot


if __name__ == '__main__':
    x = limiter()
    try:
        x.age
    except AttributeError as e:
        print(e, '# Must assign before use')
    x.age = 18              # looks like nstance data
    print(x.age)
    try:
        x.ape = 1000
    except AttributeError as e:
        print(e, '# Illegal: not in __slots__')

    """This feature is envisioned as both a way to catch typo errors like this (assignments to illegal attribute names
    not in __slots__ are detected) as well as an optimization mechanism."""


    X = C()
    print('a' in dir(X))            # True
    X.a = 1

    print(X.a)
    try:
        print(X.__dict__)
    except AttributeError as e:
        print(e)            # >> 'C' object has no attribute '__dict__'

    print(getattr(X, 'a'))
    try:
        print(X.b)
    except AttributeError as e:
        print(e, '# Must assign before use')
    setattr(X, 'b', 2)          # but getattr() and setattr() still work
    print(X.b)
    print('a' in dir(X))         # True
    print('b' in dir(X))         # True
    try:
        X = D()
        print(X.d)
    except AttributeError as e:
        print(e, "# AttributeError: 'D' object has no attribute 'd'")

    X = D_v2()
    print(X.d)
    print(X.c)
    try:
        print(X.a)
    except AttributeError as e:
        print(e)
    X.a, X.b  = 1 , 2
    print(X.a)
    print(X.b)
    print(X.__dict__)       # Some objects have both __dict__ and slot names; getattr() can fetch either type of attr
    print(X.__slots__)
    print(getattr(X,'a'),getattr(X, 'c'), getattr(X, 'd'))      # Fetches all 3 forms
    for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
        print(attr, '=>', getattr(X, attr))