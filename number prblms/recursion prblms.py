'''RECURSION'''

'''1---5'''

'''def recursion(num):
    if num == 6:
        return
    print(num)
    recursion(num+1)

recursion(1)'''


'''5---1'''

'''def recursion(num):
    if num == 0:
        return
    print(num)
    recursion(num-1)

recursion(5)'''


'''-1--- -13'''

'''def recursion(num):
    if num ==-14:
        return
    print(num)
    recursion(num-1)

recursion(-1)'''

''''''''''''''''''''''''''''''''''''

'''EVEN NUMBER'''

'''def even(num):
    if num==21:
        return 'hello'
    if num%2==0:
        print(num)
    return even(num+1)

print(even(1))'''


'''def odd(num):
    if num==21:
        return 'hello'
    if num%2==1:
        print(num)
    return odd(num+1)

print(odd(1))'''

''''''''''''''''''''''''''''''''''''

''' FACTORIAL '''

'''def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
num=5
print(factorial(num))'''

'''def factorial(num,val,fact=1):
    if val ==num+1:
        return fact
    return factorial(num,val+1,fact*val)
num=6
val=1
print(factorial(num,val))'''

''''''''''''''''''''''''''''''''''''

'''add digits'''

'''def adddigits(num):
     if num==0:
         return 0
     return (num%10) + adddigits(num//10)
num=123
print(adddigits(num))'''

''''''''''''''''''''''''''''''''''''

'''multiply digits'''

'''def muldigits(num):
     if num==0:
         return 1
     return (num%10) * muldigits(num//10)
num=345
print(muldigits(num))'''

''''''''''''''''''''''''''''''''''''

'''ARMSTRONG'''

'''def armstrong(num,power):
    if num == 0:
        return 0
    return (num%10)**power + armstrong(num//10,power)
num=153
power = len(str(num))
if num == armstrong(num,power):
    print('armstrong number')
else:
    print('not')'''

''''''''''''''''''''''''''''''''''''

'''DISARUM'''

'''def disarum(num,power):
    if num == 0:
        return 0
    return (num%10)**power + disarum(num//10,power-1)
num=135
power = len(str(num))
if num == disarum(num,power):
    print('disarum number')
else:
    print('not')'''


''''''''''''''''''''''''''''''''''''

'''REVERSE '''

'''def reverse(num,pos):
    if num == 0:
        return 0
    return (num%10)*pos + reverse(num//10,pos//10)
num=123
pos=10**(len(str(num))-1)
print(reverse(num,pos))'''

'''def reverse(num,res=0):
    if num==0:
        return res
    return reverse(num//10,res*10+(num%10))
num=123
print(reverse(num))'''

''''''''''''''''''''''''''''''''''''

'''STRONG'''

'''def factorial(num):
    if num == 0 or num==1:
        return 1
    return num * factorial(num-1)

def adddigits(num):
    if num == 0:
        return 0
    return factorial(num%10) + adddigits(num//10)

def strong(num):
    if num == adddigits(num):
        return 'strong number'
    return 'not'
num=145
print(strong(num))'''

''''''''''''''''''''''''''''''''''''

'''HAPPY'''

'''def square(num):
    if num == 0:
        return 0
    return (num%10)**2 + square(num//10)
def happy(num):
    if num>9:
        return happy(square(num))
    if num==1 or num==7:
        return 'happy number'
    return 'not'
num=13
print(happy(num))'''

''''''''''''''''''''''''''''''''''''

'''integer to binary'''

'''def integer(num,power):
    if num==0:
        return 0
    return (num%2)*power + integer(num//2,power*10)
num=13
power=1
print(integer(num,power))'''

''''''''''''''''''''''''''''''''''''

'''integer to binary'''

'''def binary(num,power):
    if num==0:
        return 0
    return (num%10)*power + binary(num//10,power*2)
num=1101
power=1
print(binary(num,power))'''

''''''''''''''''''''''''''''''''''''

'''LCM'''

'''def lcm1(num1,num2,lcm2):
    if lcm2%num1==0 and lcm2%num2==0:
        return lcm2
    return lcm1(num1,num2,lcm2+1)
num1,num2=10,20
print(lcm1(num1,num2,max(num1,num2)))'''

''''''''''''''''''''''''''''''''''''

'''GCD'''

'''def gcd1(num1,num2,gcd2):
    if num1%gcd2==0 and num2%gcd2==0:
        return gcd2
    return gcd1(num1,num2,gcd2-1)
num1,num2=4,8
print(gcd1(num1,num2,min(num1,num2)))'''

''''''''''''''''''''''''''''''''''''

'''SPECIAL NUMBER'''

'''def special(num,val=1,res=0):
    if val>num//2:
        return 0
    if num%val==0:
        res=val
    return res+special(num,val+1)
num=28
if num == special(num):
    print('special')
else:
    print('not')'''

''''''''''''''''''''''''''''''''''''

'''PRIME NUMBER'''

'''def prime(num,val=2):
    if val>num//2:
        return 'prime'
    if num%val==0:
        return 'not prime'
    return prime(num,val+1)
num=7
if num>1:
    print(prime(num))
else:
    print('not prime')'''

''''''''''''''''''''''''''''''''''''

'''TECH NUMBER'''

'''def tech(num):
    if len(s)%2!=0:
        return 0
    fh=int(s[:len(s)//2])
    sh=int(s[len(s)//2:])
    if num == (fh+sh)**2:
        return 'tech'
    return not
       
num=2025
s=str(num)
print(tech(num))'''

'''def tech(num,res=0):
    if num==0:
        return res
    res=num%100
    return res+tech(num//100)
num=2025
if num == tech(num)**2:
    print('tech')
else:
    print('not')'''

''''''''''''''''''''''''''''''''''''

'''palindrome'''

'''def reverse(num,rev=0):
    if num==0:
        return rev
    return reverse(num//10,rev*10+(num%10))
num=1234321
if num == (reverse(num)):
    print('palindrome')
else:
    print('not')'''

''''''''''''''''''''''''''''''''''''

'''palyprime'''

def palindrome(num,rev=0,):
    if num == 0:
        return rev
    return reverse(num//10,rev*10+(num%10))
def prime(rev,val=2):
    if val>rev//2:
        return 'prime'
    if rev%val == 0:
        return ' not prime'
    return (prime(rev,val+1))

num=13
if num >1:
    if reverse(num) and prime(rev):
        print('palyprime')
    else:
        print('not')
        

''''''''''''''''''''''''''''''''''''

'''composite number'''

                         


    

        






    


    
    


































































