#!/usr/bin/python3.5
# File listtree.py (2.x + 3.x)

class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class tree and all its object's attrs at and above self; run by
    print(), str() returns constructed string; use __X attr names to avoid impacting clients; recureses to
    superclasses explicitly, uses str.format for clarity;
    """
    def __attrnames(self, obj, indent):
        # print('indent is', indent)
        spaces = ' ' * (indent + 1 )
        result = ''
        for attr in sorted(obj.__dict__):
            # # print("obj.__dict__", obj.__dict__)
            if attr.startswith('__') and attr.endswith('__'):
                # result += spaces + '{0}\n'.format(attr)
                pass
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            # print(">>>>>>yes, ", aClass ," is in self.__visited is true", self.__visited)
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                                dots,
                                aClass.__name__,
                                id(aClass)
            )
        else:
            self.__visited[aClass] = True
            # here = self.__attrnames(aClass, indent)
            above = ''
            # for super in aClass.__bases__:
            #     above += self.__listclass(super,indent+4)
            ## above = ' '.join(self.__listclass(super, indent + 4) for super in aClass.__bases__)
            # return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
            #     dots,
            #     aClass.__name__,
            #     id(aClass),
            #     here,
            #     above,
            #     dots
            # )
            genabove = (self.__listclass(c, indent + 4 ) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ' '.join(genabove),
                # genabove,
                dots
            )

    def __str__(self):

        # return self.__class__.__name__
        # temp = ''
        # # for i in self.__class__.__bases__:
        # for i in self.__dict__:
        #     temp += '\t'+ str(i)
        # return temp

        self.__visited = {}
        # self.__abc = "abc"
        here = self.__attrnames(self,0)
        # print('________', self.__class__)
        # print('+++++++++++++++', self.__class__.__bases__)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of %s, address %s:\n%s%s' % (                 # Expression
        # return '<Instance of {0}, address {1}:\n{2}{3}>'.format(        # Method
                            self.__class__.__name__,
                            id(self),
                            here,above
        )

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)