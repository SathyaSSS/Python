class A:
    def M1(self):
        print('M1 of class A')

class B(A):
    def M1(self):
        print('M1 of class B')

obj = B()
obj.M1()
