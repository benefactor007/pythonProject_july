# file testmixin0.py

from listinstance import ListInstance

class Super(ListInstance):
    def __init__(self):       # superclass __init__
        self.data1 = 'spam'     # create instance attrs
    def ham(self):
        pass


# class Sub(Super, ListInstance):     # Mix in ham and a __str__
class Sub(Super):  # Mix in ham and a __str__
    def __init__(self):             # Listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'         # More instance attrs
        self.data3 = 42

    def spam(self):                 # Define another method here
        pass


if __name__ == '__main__':
    X = Sub()
    print(X)                        # Run mixed-in __str__
    S = Super()
    print(S)
