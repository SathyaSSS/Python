'''l=[1,2,3,4,5]
obj=iter(l)
while True:
    print(obj)
    print(next(obj))'''
    

class A:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start > self.end:
            raise StopIteration('elements over')
        ele=self.start
        self.start+=5
        return ele

obj=A(10,30)
itobj=iter(obj)
while True:
    print(next(itobj))


