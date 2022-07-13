#!python
# file testmixin.py (2.X + 3.X)

"""
Generic lister mixin tester: similar to transitive reloader in chapter25, but passes a class object to tester (not
function), and testByNames adds loading of both module and class by name strings here, in keeping with Chapter 31's
factories pattern)
"""

import importlib

def tester(listerclass, sept=False):

    class Super:
        __slots__ = ['data1']
        def __init__(self):             # Superclass __init__
            self.data1 = 'spam'         # create instance attrs
        def ham(self):
            pass

    class Sub(Super, listerclass):       # Mix in ham and a __str__
        __slots__ = ['data3']
        def __init__(self):             # listers have access to self
            Super.__init__(self)
            self.data2 = 'eggs'         # more instance attrs
            self.data3 = 42
        def spam(self):                 # define another method here
            pass

    instance = Sub()                    # return instance with lister's__str__
    print(instance)                     # Run mixed-in __str__ (or via str(x))
    if sept:
        print('-'*80)


def testByNames(modname, classname, sept= False):
    modobject = importlib.import_module(modname)            # import by namestring
    listerclass = getattr(modobject, classname)             # fetch attr by namestring
    # print('\n----',listerclass)
    tester(listerclass, sept)


if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)           # Test all three here
    # testByNames('listinherited', 'ListInherited', True)
    # testByNames('listtree', 'ListTree', False)