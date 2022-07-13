from listinstance import ListInstance

class Spam(ListInstance):               # Inherit a __str__ method
    def __init__(self):
        self.data1 = 'food'


if __name__ == '__main__':
    x = Spam()
    print(x.__class__.__name__)
    print(x.__dict__)
    print(x.__dict__['data1'])
    # dict1 = {'a' : '1', 'b' : 'food'}
    print(list([key for (key, value) in x.__dict__.items() if value == 'food']))
    print()
    print(id(x))
    print(x)
    display = str(x)
    # print(display)
    # print(x)

