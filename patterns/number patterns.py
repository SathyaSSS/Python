'''1-----'''

num=5
for row in range(1,num+1):
    for col in range(num):
        print(row,end=' ')
    print()

'''num=5
for row in range(num,0,-1):
    for col in range(num):
        print(row,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''

'''2-------'''

num=5
for row in range(1,num+1):
    for col in range(row):
        print(row,end=' ')
    print()

'''num=5
for row in range(num,0,-1):
    for col in range(row):
        print(row,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''

'''3---------'''

'''num=5
for row in range(num,0,-1):
    for col in range(num+1-row):
        print(row,end=' ')
    print()'''
        
num=5
for row in range(1,num+1):
    for col in range(num+1-row):
        print(row,end=' ')
    print()

''''''''''''''''''''''''''''''''''''

'''4------'''

'''num=5
for row in range(1,num+1):
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(row):
        print(row,end=' ')
    print()'''

'''num=5
for row in range(num,0,-1):
     for sp in range(num-row):
        print(' ',end=' ')
     for col in range(row):
        print(row,end=' ')
     print()'''

''''''''''''''''''''''''''''''''''''''

'''5------'''

'''num=5
for row in range(num,0,-1):
     for sp in range(row-1):
        print(' ',end=' ')
     for col in range(num+1-row):
        print(row,end=' ')
     print()'''


'''num=5
for row in range(1,num+1):
     for sp in range(row-1):
        print(' ',end=' ')
     for col in range(num+1-row):
        print(row,end=' ')
     print()'''

''''''''''''''''''''''''''''''''''''''
'''6---'''

'''num=5
for ev in range(2,num+2):
    for val in range(1,ev):
        print(val,end=' ')
    print()'''

'''num=5
for ev in range(num+1,0,-1):
    for val in range(1,ev):
        print(val,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''''

'''7----'''

'''num=5
for sv in range(num,0,-1):
    for val in range(sv,num+1):
        print(val,end=' ')
    print()'''

'''num=5
for sv in range(1,num+1):
    for val in range(sv,num+1):
        print(val,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''''

'''8------'''

'''num=5
for sv in range(1,num+1):
    for sp in range(sv-1):
        print(' ',end=' ')
    for val in range(sv,num+1):
        print(val,end=' ')
    print()'''

'''num=5
for sv in range(num,0,-1):
    for sp in range(sv-1):
        print(' ',end=' ')
    for val in range(sv,num+1):
        print(val,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''

'''9------'''

'''num=5
for sv in range(1,num+1):
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()'''

'''num=5
for sv in range(num,0,-1):
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''

'''10---------'''

'''num=5
for ev in range(num,0,-1):
    for val in range(num,ev-1,-1):
        print(val,end=' ')
    print()'''

'''num=5
for ev in range(1,num+1):
    for val in range(num,ev-1,-1):
        print(val,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''

'''tables'''

for row in range(1,2):
    for col in range(1,11):
        print(f"{row}x{col}={row*col}",)

''''''''''''''''''''''''''''''''''''




        
