from abc import ABC,abstractmethod

class Tv(ABC):
    @abstractmethod
    def channel(self):
        pass
    def power(self):
        print('on/off')

class ch1(Tv):
    def channel(self):
        print('ch1 is playing')

class ch2(Tv):
    def channel(self):
        print('ch2 is playing')

class ch3(Tv):
    def channel(self):
        print('ch3 is playing')

        

obj=ch1()
obj.channel()
obj.power()



from abc import ABC,abstractmethod

#abstract method

class car(ABC):
    @abstractmethod
    def startengine(self):
        pass

    @abstractmethod
    def offengine(self):
        pass

    def honk(self):
        print('beemmm beemmm')



#concrete method

class electriccar(car):
    def startengine(self):
        print('EV started')

    def offengine(self):
        print('EV offed')

class petrolcar(car):
    def startengine(self):
        print('car started')

    def offengine(self):
        print('car offed')

ev=electriccar()
GTR=petrolcar()

ev.startengine()
ev.offengine()
ev.honk()

print('-----------------------------------')

GTR.startengine()
GTR.offengine()
GTR.honk()















    
