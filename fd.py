'''class MyClass(object):
    def __init__(self, a):
        self.__a=a
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, val):
        if val < 0:
            self.__a = 0
        elif val >1000:
            self.__a = 1000
        else:
            self.__a = val

x = MyClass(10)
x.a=-121
print(x.a)'''
'''N = 3
a = [range(N*N)[i::N]for i in range(N)]
print (a[1][1])'''
def f(x):
    return 42
def f(*args):
    return type(args)
print(f(1))