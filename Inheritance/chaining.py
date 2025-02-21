#Method chaining

'''class A:
    var1=10
    var2=20
    def M2(self):
        print('M1 of class A')

class B(A):
    var1=100
    var2=200
    def M2(self):
        print('M2 of class B')
        super().M2()
        A.M2(self)
       

obj = B()
obj.M2()'''


#constructor chaining

class A1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def M2(self):
        print(self.name)
        print(self.age)

class B1(A1):
    def __init__(self,name,age,mob,gender):
        super().__init__(name,age)
        self.mob=mob
        self.gender=gender
    def M2(self):
        super().M2()
        print(self.mob)
        print(self.gender)

class C1(B1):
    def __init__(self,name,age,mob,gender,status,vdo):
        super().__init__(name,age,mob,gender)
        self.status=status
        self.vdo=vdo
    def M2(self):
        super().M2()
        print(self.status)
        print(self.vdo)

obj=C1('sathya',22,11111,'male','possible','possible')
obj.M2()
        
        
