"""
File mapattrs.py (3.x + 2.x)

main tool: mapattrs() maps all attributes on or inherited by an instance to the instance or class
from which they are inherited.

Assumes dir() gives all attributes of an instance. To simulate inheritance, uses either the class's MRO tuple, which
gives the search order for new-style classes (and all in 3.x), or a recursive traversal to infer the DFLR order of
classic classes in 2.X.

Also here: inheritance() gives version-neutral class ordering; assorted dictionary tools using 3.X/2.7 comprehensions.

"""

import pprint       # pretty printer

def trace(X, label = '', end = '\n'):
    print(label + pprint.pformat(X) + end)


def filterdictvals(D,V):
    """
    Dict D with entries for value V removed
    :param D:
    :param V:
    :return:
    """
    # return {K: V2 for (K,V2) in D.items if V2 != V}
    return {K: V2 for (K, V2) in D.items() if V2 != V}


def invertdict(D):
    """
    dict D with values changed to keys (grouped by values)
    Values must all be hashable to work as dict/set keys
    :param D: dict(a=1, b=2, c=1)
    :return: {1:['a','c'], 2:['b']}
    """
    def keyof(value):
        return sorted(key for key in D.keys() if D[key] == value)
    return {value: keyof(value) for value in set(D.values())}


def dflr(cls):
    """
    classic depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes
    :param cls:
    :return:
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    """
    Inheritance order sequence: new-style(MRO) or classic (DFLR)
    :param instance:
    :return:
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


if __name__ == '__main__':
    # L = [i**2 for i in range(100)]
    # trace(L)
    trace('123')

    dict_example1 = {'Xintao Lin': 27, 'Jiahao Wu': 28, 'Tianyuan Xu': 26}
    print(filterdictvals(dict_example1,26))
    trace(dict_example1)
    pprint.pprint(dict_example1)

    # set random dict
    def set_random_dict(set_loopNum = 20):
    # set_loopNum = 100
        import random, string, names
        # list1 = [x for x in range(set_loopNum)]
        # list2 = [y**2 for y in range(100)]
        list1 = [names.get_full_name() for i in range(set_loopNum)]
        list2 = [random.randint(1,10) for i in range(set_loopNum)]
        # print(list2)
        res_dict = dict(zip(list1, list2))
        return res_dict

    # trace(set_random_dict())
    import mapattrs
    print(mapattrs.__doc__)

    D = set_random_dict()
    def keyof(value):
        return sorted(key for key in D.keys() if D[key] == value)



    print(keyof(5))
    print(D)

    trace({value: keyof(value) for value in set(D.values())})
    pprint.pprint({value: keyof(value) for value in set(D.values())})
    print(type(pprint))
    print(pprint.__class__)
    print(type(pprint.pprint))
    print(pprint.pprint.__class__)

    class A:            attr1 = 1
    class B(A):         attr2 = 2
    class C(A):         attr1 = 3
    class D(B,C):       pass

    I = D()
    print(dir(I.__class__))
    print(dir(D.__class__))
    print(dir())
    print(dflr(I.__class__))
    print(I.__class__)
    print(type(I))
    print(I.__class__ is type(I) )
    print(type(I) is I.__class__)
    print(type(I) == I.__class__)
    # print(dflr(I))

    print('-' * 60 )
    print(inheritance(I))
    print(D.__mro__)
    # (<__main__.D object at 0x7f3b584d3fd0>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    # print(hasattr(I.__class__, '__mro__'))
    # [<__main__.D object at 0x7fb78fb27f98>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]