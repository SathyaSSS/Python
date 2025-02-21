'''def sample():
    print('hello')
    print('bye')
    return 5
sample()
sample()
print(sample())'''

''''''''''''''''''''''''''''''''''''

'''functional arguments'''

'''POSITIONAL ARGUMENTS'''


'''def details(name,age,gender):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'gender = {gender}')
    
details("sathya",21,"male")
details("subaa",21,"female")'''

''''''''''''''''''''''''''''''''''''


'''KEYWORD ARGUMENTS'''

'''def keyword(num1,num2,num3):
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')
    print(f'num3 = {num3}')

keyword(num2=10,num3=15,num1=5)
keyword(num1=10,num2=15,num3=5)'''

''''''''''''''''''''''''''''''''''''

'''BOTH POSITIONAL AND KEYWORD ARGS'''

'''def sample(num1,num2,num3):
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')
    print(f'num3 = {num3}')

sample(10,num3=15,num2=20)'''

''''''''''''''''''''''''''''''''''''


'''DEFAULT ARGUMENTS'''

'''def default(num1=1,num2=2,num3=3):
    return num1+num2+num3
print(default())
print(default(5,6))
print(default(5))'''

''''''''''''''''''''''''''''''''''''

'''VARIABLE LENGTH NON KEYWORD ARGUMENT'''

def vlnka(*args):
    print(args)
vlnka()
vlnka(8,2)
vlnka(2,3,4)


'''def vlnka(*args,res=0):
    for val in args:
        res+=val
    return res
print(vlnka())
print(vlnka(8,2))
print(vlnka(2,3,4))'''

''''''''''''''''''''''''''''''''''''

'''VARIABLE LENGTH KEYWORD ARGUMENT'''

def vlka(**kwargs):
    print(kwargs)
vlka()
vlka(a=4,b=3,c=7)
vlka(c=3,b=5)

'''BOTH VLNKA AND VLKA'''

'''def sample(*args,**kwargs):
    print(args,kwargs)
sample(10,20,30,a=3,b=4,c=5)
sample()
sample(a=6,c=5)
sample(10,30,50)'''











    


