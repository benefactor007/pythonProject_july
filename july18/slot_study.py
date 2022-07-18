class limiter(object):
    __slots__ = ['age','name','job']


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