'''def outer(arg):
    def inner(val1,val2):
        if val1<0 and val2<0:
            arg(val1*(-1) ,val2*(-1))
        elif val1<0:
            arg(val1*(-1),val2)
        elif val2<0:
            arg(val1,val2*(-1))
        else:
            arg(val1,val2)
    return inner


@outer
def add(val1,val2):
    print(val1+val2)


add(3,1)
add(-4,3)
add(5,-4)
add(-4,-4)'''



def outer(arg):
    def inner(num1,num2):
        if num1>0 and num2>0:
            arg(num1,num2)
        elif num1==0 and num2>0:
            arg(num1,num2)
        elif num1>0 and num2==0:
            arg(num2,num1)
        else:
            print('not possible')
    return inner

@outer
def divide(num1,num2):
    print(num1/num2)

divide(5,2)
divide(0,4)
divide(4,0)
divide(0,0)




#singleton


def outer(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner

@outer
class single:
    def __init__(self):
        print('init is called')

obj=single()
obj1=single()
obj2=single()
print(obj,obj1,obj2)
































