class A:
    course='pfsd'
    location = 'bangalore'

obj1=A()
obj2=A()

print(A)
print(obj1,obj2)


#accessing using obj and cls reference

print(obj1.location)
print(A.location,A.course)

#modifying using obj and cls reference

obj1.location = 'marathahalli'
obj2.location = 'chennai'
print(obj1.location,obj1.course)
print(obj2.location,obj2.course)

A.location = 'coimbatore'
print(obj1.location,obj2.location)


''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''class attributes //// object attributes or members'''

#constructor ---- def __init__(self):


class A:
    course='pfsd'
    location = 'bangalore'
    def __init__(self):
        print('constructor')
        print(self)

obj1=A()
print(obj1)
obj2=A()
print(obj2)


#OBJECT METHOD..............


class A:
    course='pfsd'
    location = 'bangalore'
    def __init__(self,name,age,mob):
        self.name=name
        self.age=age
        self.mob=mob
        
    def Details(self):
        print(self.name)
        print(self.age)
        print(self.mob)
        print(self.course)
        
    def modify(self):
        self.name='subbuuu'
        self.age=21
        self.course = 'jfsd'
        

obj1 = A('sathya',22,11111)
obj2 = A('subaa',21,22222)
obj3 = A('shree',21,33333)

#accessing by obj reference

'''print(obj1.name,obj1.location,obj1.age)
print(obj2.name,obj2.location,obj2.age)
print(obj3.name,obj3.location,obj3.age)'''

obj1.Details()
obj2.Details()
obj3.Details()

#accessing by cls reference

A.Details(obj1)
A.Details(obj2)


#modifying using obj reference

obj1.modify()
obj1.Details()

#modifying using cls reference

A.modify(obj2)
A.modify(obj3)
obj2.Details()
obj3.Details()








#CLASS METHOD........


class B:
    a=10
    b=20

    @classmethod
    def M1(cls):
        cls.a=100

obj = B()
print(B)
print(B.a)
obj.M1()
print(B.a)



#static method

class C:
    @staticmethod
    def M1():
        print('subaa')
       
obj=C()

obj.M1()
C.M1()










