#
from listtree import ListTree
from mapattrs import mapattrs,trace


class C(ListTree):
    pass



if __name__ == '__main__':
    X = C()                 # ok: no __slots__ used
    print(X)

    class C(ListTree):
        __slots__ = ['a', 'b']      # ok: superclass produces __dict__

    X = C()
    X.c = 3
    X.a = 5
    print(X)                        # Display c at X, a and b at C

    # Try to test mapattrs
    print("#" * 60)
    class C:
        __slots__ = ['a']
    X = C()

    print(getattr(X,'c',{}))
    print(getattr(X, '__dict__',{}))
    print(hasattr(X, '__dict__'))
    # mapattrs(X, withobject= True, bysource= False)
    trace(mapattrs(X))

    # while slots primarily optimize memory use