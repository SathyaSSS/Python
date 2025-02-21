
'''ARMSTRONG NUMBER'''

'''def armstrong(num,power,res=0):
    while num !=0:
        rem = num%10
        res=res+rem**power
        num//=10
    return res
num=153
power=len(str(num))
if num == armstrong(num,power):
    print('armstrong')
else:
    print(' not armstrong')'''

'''def armstrong(num,dup,power,res=0):
    while num !=0:
        rem = num%10
        res=res+rem**power
        num//=10
    if res==dup:
        return 'armstrong'
    return 'not armstrong'
num=153
power=len(str(num))
print(armstrong(num,num,power))'''

''''''''''''''''''''''''''''''''''''''''''

'''REVERSE NUMBER'''

'''def reverse(num,rev=0):
    while num!=0:
        rem = num% 10
        rev = rev*10+rem
        num//=10
    return rev
num=123
print(reverse(num))'''

'''def reverse(num,power,rev=0):
    while num!=0:
        rem = num%10
        rev=rev+rem*power
        power//=10
        num//=10
    return rev
num=123
power=10**(len(str(num))-1)
print(reverse(num,power))'''
        

''''''''''''''''''''''''''''''''''''''''''

'''PALINDROME NUMBER'''


'''def palindrome(num,rev=0):
    while num!=0:
        rem = num % 10
        rev=rev*10+rem
        num//=10
    return rev
num=121
if num == palindrome(num):
    print('palindrome')
else:
    print('not palindrome')'''

''''''''''''''''''''''''''''''''''''''''''

'''PALYPRIME NUMBER'''

def prime(num):
    if num > 1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'not prime'
        return 'prime'
    return 'not prime'

def palindrome(num,dup,rev=0):
    while num!=0:
        rem = num % 10
        rev=rev*10+rem
        num//=10
    return rev

def palyprime(num):
    if prime(num) and palindrome(num,num):
        return 'palyprime'
    return 'not palyprime'

num=12
print(palyprime(num))

''''''''''''''''''''''''''''''''''''''''''

'''INTEGER TO BINARY'''

'''def integer(num,power,res=0):
    while num!=0:
        rem = num%2
        res=res+rem*power
        power*=10
        num//=2
    return res
num=13
power=1
print(integer(num,power))'''

''''''''''''''''''''''''''''''''''''''''''

'''BINARY TO INTEGER'''

'''def binary(num,power,res=0):
    while num!=0:
        rem = num%10
        res=res+rem*power
        power*=2
        num//=10
    return res
num=1101
power=1
print(binary(num,power))'''

''''''''''''''''''''''''''''''''''''''''''

'''STRONG NUMBER'''

'''def fact(num,fac=1):
    while num!=0:
        fac*=num
        num-=1
    return fac

def adddigit(num,res=0):
    while num!=0:
        rem=num%10
        res=res+fact(rem)
        num//=10
    return res

def strong(num):
    if num == adddigit(num):
        return 'strong'
    return 'not strong'

num=145
print(strong(num))'''

''''''''''''''''''''''''''''''''''''''''''
    
'''HAPPY NUMBER'''

'''def result(num,res=0):
    while num!=0:
        rem = num%10
        res=res+rem**2
        num//=10
    return res

def happy(num):
    while num>9:
        num=result(num)
    if num==1 or num==7:
        return 'happy'
    return 'not happy'

num=19
print(happy(num))'''

''''''''''''''''''''''''''''''''''''''''''

'''COMPOSITE NUMBER'''

def composite(num):
    if num > 3:
        for val in range(1,num//2+1):
            if num%val==0:
                return 'composite'
        return 'not composite'
    return 'not composite'

num=14
print(composite(num))

''''''''''''''''''''''''''''''''''''''''''

'''DISARUM NUMBER'''

'''def result(num,dup,power,res=0):
    while num!=0:
        rem = num%10
        res=res+rem**power
        power-=1
        num//=10
    return res

def disarum(num):
    if num == result(num,num,power):
        return 'disarum'
    return 'not disarum'

num=135
power=len(str(num))
dup=num
print(disarum(num))'''

''''''''''''''''''''''''''''''''''''''''''

'''EMIRP NUMBER'''

'''def palindrome(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev

def prime(num):
    if num > 1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'not prime'
        return 'prime'
    return 'not prime'

def emirp(num):
    var = palindrome(num)
    if var!=num and prime(num) and prime(var):
        return 'emirp'
    return 'not emirp'

num=17
print(emirp(num))'''

''''''''''''''''''''''''''''''''''''''''''

'''SPECIAL NUMBER'''

'''def result(num,res=0):
    for val in range(1,num//2+1):
        if num%val==0:
            res+=val
    return res

def special(num):
    if num == result(num):
        return 'special'
    return 'not special'

num=28
print(special(num))'''

''''''''''''''''''''''''''''''''''''''''''

'''TECH NUMBER'''

'''def add(num):
    if len(s)%2==0:
        adds=int(s[len(s)//2:]) + int(s[:len(s)//2])
    return adds
def tech(num):
    if num == add(num)**2:
        return 'tech'
    return 'not tech'

num=2025
s=str(num)
print(tech(num))'''

''''''''''''''''''''''''''''''''''''''''''

'''LCM'''

'''def lcm(num1,num2):
    if num1>num2:
        lcm=num1
    else:
        lcm=num2
    while True:
        if lcm%num1==0 and lcm%num2==0:
            return lcm
        lcm+=1

num1,num2=10,15
print(lcm(num1,num2))'''

''''''''''''''''''''''''''''''''''''''''''

'''GCD'''

'''def gcd(num1,num2):
    if num1<num2:
        gcd=num1
    else:
        gcd=num2
    while True:
        if num1%gcd==0 and num2%gcd==0:
            return gcd
        gcd-=1

num1,num2=4,6
print(gcd(num1,num2))'''

''''''''''''''''''''''''''''''''''''''''''

'''PERFECT SQUARE'''

def persq(num,val=0):
    for val in range(num+1):
        if val*val==num:
            return 'persq'
    return 'not persq'
            
num=14
print(persq(num))

''''''''''''''''''''''''''''''''''''''''''

'''spy NUMBER'''

def spy(num,sum=0,mul=1):
    while num!=0:
        rem=num%10
        sum=sum+rem
        mul=mul*rem
        num//=10
    if sum==mul:
        return 'spy'
    return 'not spy'

num=123
print(spy(num))

        

    
    
    

def palindrome(num,dup,rev=0):
    while num!=0:
        rev=rev*10+(num%10)
        num//=10
    return rev==dup

def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'not prime'
        return 'prime'
    return 'not'

def pp(num):
    if palindrome(num,num) and prime(num):
        return 'pp'
    return 'not'

num=131
print(pp(num))

            
        
    

def palindrome(num,rev=0):
    while num!=0:
        rev=rev*10+(num%10)
        num//=10
    return rev

def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'not prime'
        return 'prime'
    return 'not'

def emirp(num):
    var=palindrome(num)
    if var!=num and prime(var) and prime(num):
        return 'emirp'
    return 'not'

num=16
print(emirp(num))


def palindrome(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev

def prime(num):
    if num > 1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'False'
        return 'True'
    return 'not prime'

def emirp(num):
    var = palindrome(num)
    if var!=num and prime(num) and prime(var):
        return 'emirp'
    return 'not emirp'

num=12
print(emirp(num))















