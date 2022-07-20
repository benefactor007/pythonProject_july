# This module includes class as below,
#   - Slotful


class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self,data):
        self.c = data


class C:
    pass

class D(C):
    __slots__ = ['a']


if __name__ == '__main__':
    I = Slotful(3)
    I.a, I.b = 1, 2
    print(I.a, I.b, I.c)
    print(I.__dict__)
    print([x for x in dir(I) if not x.startswith('__')])
    print(I.__dict__['c'])
    print(getattr(I,'c'), getattr(I, 'a'))
    for a in (x for x in dir(I) if not x.startswith('__')):
        print(a, getattr(I,a))

    X = D()                             # Bullet 1: slots in sub but not super
    X.a,X.b = 1, 2                      # makes instance dict for nonslots
    print(X.__dict__)                   # but slot name still managed in class
    print(D.__dict__.keys())


    class C:                            # Bullet2: slots in super but not sub
        __slots__ = ['a']               # makes instance dict for nonslots
                                        # but slot name still managed in class
    class D(C):
        pass


    X = D()
    X.a, X.b = 1,2
    print(X.__dict__)
    print(X.__dict__.keys())
    from mapattrs import trace,mapattrs
    trace(mapattrs(X))

    class C:                            # Bullet 3: only lowest slot accessible
        __slots__ = ['a']

    class D(C):
        __slots__ = ['a']


    X = D()

    from mapattrs import trace,mapattrs
    trace(mapattrs(X))



    try:
        class C:
            __slots__ = ['a']
            a = 99
    except ValueError as e:
        print(e, '# Bullet 4: no class-level defaults')


    class C:
        __slots__ = ['a']

    class D(C):
        __slots__ = ['b']

    X = D()
    X.a, X.b = 1,2
    try:
        print(X.__dict__)
    except AttributeError as e:
        print(e, "# 'D' object has no attribute '__dict__'")
    print(C.__dict__.keys(), D.__dict__.keys())