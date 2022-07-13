#! /usr/bin/python3.5

if __name__ == '__main__':
    import listinstance
    class C(listinstance.ListInstance):
        pass
        # def __str__(self):
        #     return 'yes'

    x = C()
    x.a, x.b, x.c = 1, 2, 3
    print(x)