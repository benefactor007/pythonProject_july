#! /usr/bin/python3.5

class Wrapper:
    def __init__(self, object):
        self.wrapped = object           # save object
    def __getattr__(self, attrname):
        print('Trace:' + attrname)                      # trace fetch
        return getattr(self.wrapped, attrname)          # delegate fetch


from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass


class Sub(Super):
    def action(self):
        print('spam')



if __name__ == '__main__':
    C = Wrapper([1,2,3])
    C.append(4)                 #Trace:append
    print(C.wrapped)

    x  = Wrapper({'a':1, 'b':2})
    print(x.keys())             # Trace:keys; dict_keys(['b', 'a'])


    X  = Sub()
    X.delegate()
