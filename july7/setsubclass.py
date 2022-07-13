from __future__ import print_function       # 2.X compatibility

class Set(list):
    def __init__(self, value = []):             # Constructor
        list.__init__([])                       # Customizes list
        self.concat(value)                      # copies mutable defaults
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):                    # other is any sequence
        for x in value:
            if not x in self:
                self.append(x)


    def __and__(self,other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x,y,len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)