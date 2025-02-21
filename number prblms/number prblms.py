'''DISARUM NUMBER'''

'''num=135
dup=num
res=0
power=len(str(num))
while num!=0:
    rem=num%10
    res=rem**power+res
    power-=1
    num//=10
if dup==res:
    print('disarum number')
else:
    print('not disarum number')'''
    

''''''''''''''''''''''''''''''''''''''

'''SPECIAL NUMBER'''

'''num=28
res=0
for val in range(1,num//2+1):
    if num%val==0:
        res=res+val
if res==num:
    print('special number')
else:
    print('not special number')'''
    

''''''''''''''''''''''''''''''''''''''

'''STRONG NUMBER'''

'''num=145
dup=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact=fact*val
    res=res+fact
    num=num//10
if res==dup:
    print('strong number')
else:
    print('not strong number')'''
        

''''''''''''''''''''''''''''''''''''''

'''REVERSE NUMBER'''

'''num=456
rev=0
pos=10**(len(str(num))-1)
while num!=0:
    rem=num%10
    rev=rev+rem*pos
    pos//=10
    num//=10
print(rev)'''

'''num=246
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print(rev)'''

''''''''''''''''''''''''''''''''''''''

'''palindrome'''

'''num=12321
res=0
dup=num
while num!=0:
    rem=num%10
    res=res*10+rem
    num//=10
if(dup==res):
    print('palindrome')
else:
    print('not palindrome')'''

''''''''''''''''''''''''''''''''''''

'''number to binary'''

'''num=13
res=0
pos=1
while num!=0:
    rem=num%2
    res=res+rem*pos
    pos=pos*10
    num//=2
print(res)'''

''''''''''''''''''''''''''''''''''''

'''binary to number'''

'''num=1001
res=0
pos=1
while num!=0:
    rem=num%10
    res=res+(rem*pos)
    pos*=2
    num//=10
print(res)'''

''''''''''''''''''''''''''''''''''''

'''TECH NUMBER'''

'''num=2025
s=str(num)
sum=int(s[:len(s)//2])+int(s[len(s)//2:])
ans=sum**2
if(ans==num):
    print('tech')
else:
    print('not tech')'''

'''num =2025
s=str(num)
if len(s)% 2==0:
    ft=int(s[:len(s)//2:])
    sc=int(s[len(s)//2:])
    if(ft+sc)**2==num:
        print('tech')
    else:
        print('not tech')
else:
    print('not tech')'''

''''''''''''''''''''''''''''''''''''''

'''palyprime'''

'''num=11
rev=0
dup=num
while num!=0:
    rem = num%2
    rev=rev*10+rem
    num//=10
if(rev==dup):
    if dup>1:
        for val in range(2,dup//2+1):
            if dup%val==0:
                print('not palyprime')
                break
        else:
            print('palyprime')
    else:
        print('not palyprime')
else:
    print('not palyprime')'''

''''''''''''''''''''''''''''''''''''''
'''EMIRP NUMBER'''

num = 13
rev=0
dup = num
while num!=0:
    rem = num%10
    rev=rev*10+rem
    num//=10
if dup!=rev:
    if dup>1:
        for val in range(2,dup//2+1):
            if dup%val==0:
                print('not emirp')
                break
        else:
            if rev>1:
                for val in range(2,rev//2+1):
                    if rev%val==0:
                        print('not emirp')
                else:
                    print('emirp')
            else:
                print('not emirp')
    else:
        print('not emirp')
else:
    print('not emirp')
''''''''''''''''''''''''''''''''''''''''''

'''HAPPY NUMBER'''

'''num = 19
while num > 9:
    res=0
    while num !=0:
        rem = num%10
        res=res+rem**2
        num//=10
    num=res
if (num==1 or num==7):
    print('happy number')
else:
    print('not happy')'''

''''''''''''''''''''''''''''''''''''''''''
        
'''LCM'''

'''num1=10
num2=15
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if(lcm%num1==0 and lcm%num2==0):
        print(lcm)
        break
    lcm=lcm+1'''

'''num1=10
num2=15
num3=20
if num1>num2 and num2>num3:
    lcm=num1
elif num2>num3:
    lcm=num2
else:
    lcm=num3
while True:
    if(lcm%num1==0 and lcm%num2==0 and lcm%num3==0):
        print(lcm)
        break
    lcm=lcm+1'''

''''''''''''''''''''''''''''''''''''''''''

'''GCD'''

'''num1=4
num2=6
num3=8
if num1<num2 and num1<num3:
    gcd=num1
elif num2<num3:
    gcd=num2
else:
    gcd=num3
while True:
    if(num1%gcd==0 and num2%gcd==0 and num3%gcd==0):
        print(gcd)
        break
    gcd=gcd-1'''

'''num1=4
num2=6
if num1<num2 :
    gcd=num1
else:
    gcd=num2
while True:
    if(num1%gcd==0 and num2%gcd==0):
        print(gcd)
        break
    gcd=gcd-1'''
''''''''''''''''''''''''''''''''''''''''''

'''PERFECT SQUARE'''

'''num=16
val=0
while val*val<=num:
    if val*val==num:
        print('per sq')
        break
    else:
        val+=1
else:
    print('not per sq')'''

''''''''''''''''''''''''''''''''''''''''''

'''spy number'''

'''num=123
a=0
m=1
while num>0:
    rem=num%10
    a=a+rem
    m=m*rem
    num//=10
if a==m:
    print('spy num')
else:
    print('not spy')'''

'''''''''''''''''''''''''''''''''''''''''''''

''''''''''''''''''''''''''''''''''''''''''

'composite number'''

'''num = 12
if num>3:
    for val in range(1,num//2+1):
        if num%val==0:
            print('composite')
            break
    else:
        ('not composite')
else:
    ('not composite')'''

''''''''''''''''''''''''''''''''''''''''''

'''COUNT'''

'''num=1234
count=0
while num!=0:
    num//=10
    count+=1
print(count)'''

''''''''''''''''''''''''''''''''''''''''''

'''ARMSTRONG NUMBER'''

'''num=153
dup=num
res=0
pos=len(str(num))
while num>0:
    rem=num%10
    res=res+rem**pos
    num//=10
if(res==dup):
    print('armstrong')
else:
    print('not armstrong')'''
  










    
