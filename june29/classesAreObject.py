def factory(aClass, *args, **kwargs):           # Varargs tuple, dict
    return aClass(*args, **kwargs)              # Call aClass (or apply in 2.X only)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job = None):
        self.name = name
        self.job  = job


if __name__ == '__main__':
    object1 = factory(Spam)                                 # make a spam object
    object2 = factory(Person, "Arthur", "King")             # make a person object
    object3 = factory(Person, name = "Brian")               # ditto(the same thing again), with keywords and default
    print(object1.doit(99))
    print(object2.name, object2.job)
    print(object3.name)