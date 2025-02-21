#single inheritance

'''class A:
    var1=10
    var2=20
class B(A):
    var4=20
    var3=30

    
obj=B()
print(obj.var2)
print(obj.var1)'''


#mutilevel inheritance

'''class A:
    var1=10
    var2=20
class B(A):
    var4=20
    var3=30
class C(B):
    var4=10
    var3=45

obj = C()
obj1 = B()
print(obj1.var1)
print(obj.var4)'''


#multiple inheritance

'''class A:
    var1=10
    var2=20
class B:
    var4=20
    var3=30
class C(B,A):
    var4=10
    var2=45

obj = C()
print(obj.var1)
print(obj.var3)'''


#hierarcial inheritance

'''class A:
    var1=10
    var3=25
class B(A):
    var2=20
class C(A):
    var4=45

obj = C()
obj1 = B()
print(obj1.var1)
print(obj.var3)'''


#hybrid inheritance

class A:
    pass
class B(A):
    pass
class C(A,B):
    pass





