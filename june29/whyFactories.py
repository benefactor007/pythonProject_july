# from classesAreObject import Person
# import classesAreObject

class Person:
    def __init__(self, name, job = None):
        self.name = name
        self.job  = job
    def __repr__(self):
        return str(self.name)


if __name__ == '__main__':
   x = Person("Arthur")
   c = getattr(Person("Arthur"), '__init__')
   print(x)
   print(c)