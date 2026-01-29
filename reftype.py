
a=[10,20,30]
b=iter(a)
print(next(b))
print(next(b))
print(next(b))


def method():
    yield 10
    yield 20
    yield 30

a=method()
print(next(a))
print(next(a))
print(next(a))

#outer function
def method1(a):
    #inner function
    def method2():
        return a
    return method2

b=method1(10)
print(b())
b=method1(20)
print(b())
b=method1(30)
print(b())

