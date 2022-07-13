class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3

    def doit(self, message):
        print(message)


def square(arg):
    return arg ** 2  # Simple functions (def or lambda)


class Sum:  # callable instances
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:  # Bound methods
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


class Negate(object):
    # a single action is better coded as a simple function than a class with a constructor,
    # but the class here serves to illustrate its callable nature:
    def __init__(self, val):  # classes are callables too
        self.val = -val  # but called for object, not work
    def __repr__(self):  # instance print format
        return str(self.val)


if __name__ == '__main__':
    x = Number(2)  # class instance objects
    y = Number(3)  # State + methods
    z = Number(4)
    print(x.double())  # Normal immediate calls
    acts = [x.double, y.double, y.triple, z.double]  # list of bound methods
    for act in acts:  # calls are deferred
        print(act())  # call as though functions

    temp = Number.double
    print(temp(Number(2)))

    print(Number.triple(Number(3)))
    # object1 = Spam()
    # t = Spam.doit        # unbound method object (a function in 3.X: see ahead)
    # t(object1, 'howdy')     # pass in instance ( if the method expects one in 3.X)
    x = Number(10)
    bound = x.double
    print(bound.__self__)
    print(bound.__func__)
    print(bound.__self__.base)
    print(bound())  # calls bound.__func__(bound.__self__,...)
    print(bound.__func__(bound.__self__))
    ## Add in 7/1/2022
    print('-' * 60)

    print('-' * 60)

    print('*' * 60)
    sobject = Sum(2)
    project = Product(3)
    actions = [square, sobject, project.method]  # function, instance, method
    for act in actions:
        print(act(5))
    print(actions[-1](5))

    print(Sum(2)(3))

    actions = [square, sobject, project.method, Negate]
    # actions = [square, sobject, project.method]
    for act in actions:
        print(act(5))

    print([act(5) for act in actions])

    table = {act(5): act for act in actions}  # 3.X/2.7 dict comprehension
    print(Negate)
    # print(type(Negate))
    # print(type(str(Negate)))
    print(table)
    for (key, value) in table.items():
        print(type(key),type(value))
    print(Negate(5))
    print(type(Negate(5)))
    for (key, value) in table.items():
        # print("{0:2} => {1}".format(key, str(value)))
        print("%2s => %2s" % (key, value))
    # print(table)
    # print("%s => %s" %(sobject(5), sobject))
    # print("%2s => %s" % (Negate(5), Negate))
