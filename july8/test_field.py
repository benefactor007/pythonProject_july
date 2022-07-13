#! /usr/bin/python3.5

# all classes derive from "object"

class C(object):        # new-style classes inherit object defaults
    pass


if __name__ == '__main__':
    X = C()
    print(type(X),type(C))
    print(X.__class__, C.__class__)

    print(isinstance(X, object))
    print(isinstance(C,object))             # classes always inherit from object

    print(C.__bases__)

    print(type('spam'), type(str))
    print(isinstance('spam', object))       # same for built-in types (classes)
    print(isinstance(str, object))

    print(type(type))
    print(type(object))
    print(isinstance(type,object))          # all classes derive from object, even type
    print(isinstance(object,type))          # types makes classes, and type is a class
    print(type is object)
    print(str is object)

    print(X.__repr__)