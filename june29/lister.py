# File lister.py
# Collect all three lister in one module for convenience

from listinstance import ListInstance
from listinherited import ListInherited
from listtree import ListTree

Lister = ListTree # Choose a default lister

import lister
if __name__ == '__main__':
    print(lister.ListInstance)
    print(lister.Lister)
    from lister import Lister
    print(Lister)
    from lister import ListInstance as Lister     # use Lister alias
    print(Lister)