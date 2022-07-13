#! /usr/bin/python3.5

from listtree import ListTree

class A(ListTree):
    attr = 1


class B(A):
    pass


class C(A):
    attr = 2


class D(B,C):
    # pass
    # attr = B.attr
    attr = C.attr

if __name__ == '__main__':
    X = D()
    print(X)
    print(X.attr)

    class A:
        def meth(s):
            print('A.meth')


    class C(A):
        def meth(s):
            print('C.meth')


    class B(A):
        pass


    class D(B,C):
        # pass
        # meth = C.meth
        # meth = B.meth
        def meth(self):
            C.meth(self)

    x = D()
    x.meth()
    print(D.__mro__)

    from classtree import instancetree
    instancetree(D())