# py -3

from mapattrs import trace, dflr, inheritance, mapattrs
from testmixin0 import Sub

if __name__ == '__main__':
    I = Sub()
    trace(dflr(I.__class__))
    trace(dflr(Sub))
    trace(inheritance(I))
    trace(mapattrs(I))
    trace(mapattrs(I, bysource =  True))
    trace(mapattrs(I, withobject = True))
    trace(mapattrs(I, withobject=True, bysource=True))