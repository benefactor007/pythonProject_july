# Subclass built-in list type/class
# Map 1..N to 0..N-1; call back to built-in verison

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)
        # return list.__getitem__(self, offset)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')                   # __init__ inherited from list
    print(x)                            # __repr__ inherited from list

    print(x[1])
    # (indexing['a', 'b', 'c'] at 1)
    # a
    print(x[3])
    # (indexing['a', 'b', 'c'] at 3)
    # c
    x.append('spam');                   # Attributes from list superclass
    print(x)
    x.reverse();
    print(x)