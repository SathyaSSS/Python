#public access modifier

'''class A:

    def __init__(self):
        self.a=100
    def M1(self):
        print(self.a)

obj1=A()
obj1.M1()
print(obj1.a)'''



#protected and private access modifiers

class Mock():
    def __init__(self):
        self.a=100
        self._b=200
        self.__c=300
    def M1(self):
        print(self.a)
        print(self._b)
        print(self.__c)
    

obj = Mock()
obj.M1()
print(obj.a)
print(obj._b)
print(obj._Mock__c)
print(obj.__c)
