var =(lambda ele:ele**2)
print(var(5))


''''''''''''''''''''''''''''''''''''''''''''''''''''''


print(list(map(lambda ele1,ele2 : ele1 + ele2,range(1,6),range(7,11))))

def sum(num1,num2):
    return num1+num2

print(list(map(sum,range(1,6),range(11,16))))

def prime(num):
    if num>1:
        for val in range(2,num//2):
            if(num%val==0):
                return 'not'
        return 'prime'
    return'not'

print(list(map(prime,[5,6,7,8])))

'''print(list(map(lambda l1,l2 : l1+l2 ,list(map(int,input().split())),list(map(int,input().split())))))'''

               
''''''''''''''''''''''''''''''''''''''''''''''''''

print(list(filter(lambda ele : ele%2==0,[1,2,3,4,5,6])))

def prime(num):
    if num>1:
        for val in range(2,num//2):
            if(num%val==0):
                return False
        return True
    return False

print(list(filter(prime,range(11,21))))

print(list(filter(lambda num : num<0,[0,1,-1,2,-3,5,6,-8,0])))


''''''''''''''''''''''''''''''''''''''''''''''''''

from functools import reduce
def sample(num1,num2):
    return num1 + num2

print(reduce(sample,range(1,6),3))



''''''''''''''''''''''''''''''''''''''''''''''''''

print(list(zip(('1','2',3),[1,2,3])))


print(list(zip({'a':1,'b':2},{'c':3,'d':4})))





                                                                                                            
