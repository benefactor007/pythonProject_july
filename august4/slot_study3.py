#
from listtree import ListTree

class C(ListTree):
    pass



if __name__ == '__main__':
    X = C()                 # ok: no __slots__ used
    print(X)

    class C(ListTree):
        __slots__ = ['a', 'b']      # ok: superclass produces __dict__

    X = C()
    X.c = 3
    print(X)                        # Display c at X, a and b at C
