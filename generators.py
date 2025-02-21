'''def sample():
    a=10
    yield a,100,1000
    a+=5
    yield a

gobj=sample()
while True:
    print(next(gobj))'''


def factorial(num,fact=1):
    yield 1
    for ele in range(1,num+1):
        fact*=ele
        yield fact
    raise StopIteration('no element')

gobj=factorial(5)
while True:
    print(next(gobj))
