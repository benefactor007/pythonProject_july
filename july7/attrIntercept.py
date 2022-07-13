#! /usr/bin/python3.5
#
# class C(object):
#     data = 'spam'
#     def __getattr__(self, name):                # classic in 2.x: catches built-ins
#         print(name)
#         return getattr(self.data, name)

# class C(object):
    # pass
    # def __getattr__(self, name):
        # print(name)


class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)
    def __getitem__(self, i):
        print('getitem: ' +  str(i))
        return self.data[i]
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)



if __name__ == '__main__':
    X = C()
    try:
        print(X.__getitem__(1))                # traditional mapping works but new-style's does not
        # X[1]
        # type(X).__getitem__(X, 1)               # >> type object 'C' has no attribute '__getitem__'
        print(X.__add__('eggs'))
        #print(X + 'eggs')                       # >> unsupported operand type(s) for +: 'C' and 'str'
        print(type(X).__add__(X, 'eggs'))           # >> type object 'C' has no attribute '__add__'
        print(X.upper())
        print(X[1])
        print(X.upper)
        print(X + 'eggs')
    except Exception as e:
        print(e)



    # X = C()
    # try:
    #     X[0]            #TypeError: 'C' object does not support indexing
    # except TypeError as e:
    #     print(e)
    # print(X)

    #
    # X = C()
    # X.normal = lambda: 99
    # X.normal()
    # X.__add__ = lambda y: 88 + y
    # print(X.__add__(1))
    # try:
    #     print(X + 1)
    # except TypeError as e:
    #     print(e)

    # X = C()
    # X.normal
    # X.__add__
    # try:
    #     X + 1
    # except TypeError as e:
    #     print(e)
