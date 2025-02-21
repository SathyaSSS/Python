''' 1 -----num=5'''

'''for loop'''
'''for val in range(1,num+1):
    print('*',end=' ')'''
   

'''while loop'''
'''while num!=0:
    print('*')
    num-=1'''
''''''''''''''''''''''''''''''''''''''''''

'''2---------num=4'''

'''for row in range(1,num+1):
    for col in range(1,num+1):
        print('*',end=' ')
    print()'''

'''for val in range(1,num+1):
    print('* ' * num)'''

'''row = num
while row != 0:
    col=num
    while col!=0:
        print('*',end=' ')
        col-=1
    print( )
    row-=1'''
''''''''''''''''''''''''''''''''''''''''''
'''3------num=5'''

'''for row in range(1,num+1):
    for col in range(row):
        print('*',end=' ')
    print()
    row+=1'''

'''row = 1
while row <= num:
    col = row
    while col!=0:
        print('*',end=' ')
        col-=1
    print()
    row+=1'''
''''''''''''''''''''''''''''''''''''''''''
'''4--------num=5
for row in range(num,0,-1):
    for col in range(row):
        print('*',end=' ')
    print()
    row-=1'''

'''for row in range(1,num+1):
    for col in range((num+1)-row):
        print('*',end=' ')
    print()'''
    
'''row=num
while row!=0:
    col=row
    while col!=0:
        print('*',end=' ')
        col-=1
    print()
    row-=1'''

''''''''''''''''''''''''''''''''''''''''''
'''5-----num =5
for line in range(1,num+1):
    for sp in range(line-1):
        print(' ',end=' ')
    for st in range((num+1)-line):
        print('*',end=' ')
    print()'''

'''num=5
spaces=0
stars=5
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1'''
        

''''''''''''''''''''''''''''''''''''''''''

'''6----num=5
for line in range(1,num+1):
    for sp in range(num-line):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()'''

'''num=5
spaces=num
stars=1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1'''
''''''''''''''''''''''''''''''''''''''''''

'''7-----------num =5
for line in range(1,num+1):
    for sp in range(num-line):
        print(' ',end=' ')
    for st in range(line*2-1):
        print('*',end=' ')
    print()'''

'''num = 5
spaces=num-1
stars=1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1'''

''''''''''''''''''''''''''''''''''''''''''

#8-------

num=5
for line in range(num,0,-1):
    for sp in range(num-line):
        print(' ',end=' ')
    for st in range(line*2-1):
        print('*',end=' ')
    print()

num = 5
spaces=0
stars=2*num-1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    stars-=2
    spaces+=1

''''''''''''''''''''''''''''''''''''''''''
'''9------'''

'''num = 7
spaces=num//2
stars=1
for line in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if line < num//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1'''

''''''''''''''''''''''''''''''''''''''''''
'''10--------'''

'''num=5
stars=1
for line in range(num):
    for st in range(stars):
        print('*',end=' ')
    print()
    if line < num // 2:
        stars+=1
    else:
        stars-=1'''

'''num=5
spaces=num//2
stars=1
for line in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if line < num//2:
        spaces-=1
        stars+=1
    else:
        spaces+=1
        stars-=1'''

''''''''''''''''''''''''''''''''''''''''''''
#11

'''num=5
for row in range(num):
    for col in range(num):
        if row == 0 or col==0 or row==num-1 or col==num-1:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''

#12
'''num=5
for row in range(num):
    for col in range(num):
        if row == num-1 or col == 0 or row==col:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''

'''num=5
for row in range(num):
    for col in range(num):
        if row == 0 or col == 0 or row+col == num-1:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''

#13

'''num=5
spaces=0
stars=num
for row in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        if st == num-1 or row == 0 or row==st:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    stars+=1


for row in range(num):
    for col in range(num):
        if row == 0 or col == num-1 or row==col:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''

#14
'''num=5
spaces=num-1
stars=1
for row in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        if st == 0 or row == num-1 or row*2==st:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    stars+=2

num=5
spaces=0
stars=num*2-1
for row in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        if st == 0 or row == 0 or st==(num*2)-2 - row*2:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()
    spaces+=1
    stars-=2'''

#15

'''num=5
for row in range(num):
    for col in range(num):
        if col==row or row+col==num-1:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''

#16
'''num=5
for row in range(num):
    for col in range(num):
        if col==row or row+col==num-1 or row==0 or col==0 or col==num-1 or row == num-1:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()'''


            
    


         
        
        
        

        

