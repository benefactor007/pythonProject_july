#! python
"""
classtree.py: Climb inheritance trees using namespace links,
displaying higher superclasses ith indentation for height
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)  #print class name here
    for supercls in cls.__bases__:      # recur to all superclasses
        classtree(supercls, indent + 3) # may visit super > one

def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()
    import specialize
    # instancetree(specialize.Provider())
    func = specialize
    for i in (func.Provider, func.Extender, func.Inheritor,func.Sub,func.Replacer):
        instancetree(i())


