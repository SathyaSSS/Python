# raise

'''raise Exception
raise IndexError
raise IndexError('out of range')
raise NameError('name M is not defined')'''


num=11
try:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                raise Exception('not prime')
        

    else:
        raise Exception('not prime')

except Exception as msg:
    print(msg)

else:
    print('prime')

finally:
    print('finished')



num=153
try:
    dup=num
    res=0
    power=len(str(num))
    while num!=0:
        res+=(num%10)**power
        num//=10
    if res==dup:
        raise Exception('Armstrong')

except Exception as msg:
    print(msg)

else:
    print('not Armstrong')

finally:
    print('executed')
    
