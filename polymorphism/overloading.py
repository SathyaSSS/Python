'''class A:
    def M1(self,num1,num2,num3,num4):
        print(num1*num2*num3*num4)

    def M1(self,num1,num2,num3):
        print(num1*num2*num3)

    def M1(self,num1,num2):
        print(num1*num2)

obj=A()
obj.M1(2,3)
obj.M1(2,3,4)'''

'''overloading ...it takes last method only'''

#To achieve overloading

'''using defualt parameter'''

class B:
    def M1(self,num1=0,num2=1,num3=1,num4=1):
        print(num1*num2*num3*num4)

obj=B()
obj.M1()
obj.M1(1)
obj.M1(1,2)
obj.M1(1,2,3)
obj.M1(1,2,3,4)

'''using variable length non keyword argument'''

class C:
    def M1(self,*args):
        if len(args)>0:
            res=1
            for ele in args:
                res*=ele
            print(res)
        else:
            print(0)

obj1 = C()
obj1.M1()
obj1.M1(1)
obj1.M1(1,2)
obj1.M1(1,2,3)
obj1.M1(1,2,3,4)


