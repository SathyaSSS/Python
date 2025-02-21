#exceptional handling using block

#Try block

l=[2,3,4,5]
try:
    res=0
    for ele in l:
        res+=ele
    print(res)
finally:
    print('finally block executing all time')


print('--------------------------------------------------')


#except block

l=[2,3,4,5]
try:
    res=0
    for ele in l:
        res+=l[ele]
    print(res)
    
except Exception as msg:
    print(f'Error:{msg}')
    
finally:
    print('finally block executing all time')



l=[2,3,4,5]
try:
    res=0
    for ele in l:
        res+=M[ele]
    print(res)

except TypeError as msg:
    print(f'Error:{msg}')

except NameError as msg:
    print(f'Error:{msg}')

except IndexError as msg:
    print(f'Error:{msg}')

    
finally:
    print('finally block executing all time')


print('--------------------------------------------------')

    
#else block

l=[2,3,4,5]
try:
    res=0
    for ele in l:
        res+=ele
    print(res)

except Exception as msg:
    print(f'Error:{msg}')

else:
    print('no error')

finally:
    print('finally block executing all time')


print('--------------------------------------------------')


#finally block

try:
    pass
finally:
    print('finally block executing all time')
    
