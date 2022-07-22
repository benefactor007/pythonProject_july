from listtree import ListTree

class C(ListTree):
    pass


if __name__ == '__main__':
    X = C()                     # ok, no __slots__ used
    print(X)

    class C(ListTree):
        __slots__ = ['a', 'b']          # OK: superclass produces __dict__
    X = C()
    X.c = 3
    print(X)                    # Displays at X,a and b at C
    print(getattr(X, 'c'))


    class A:
        __slots__ = ['a']
    class B(A,ListTree):
        pass

    print('=='*60)
    X = B()
    print(X)

    print('**' * 60)
    class A:
        __slots__ = ['a']

    class B(A, ListTree):
        __slots__ = ['b']

    X = B()
    print(X)