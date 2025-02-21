#1...

'''l=[2,3,4,5,6,7,8,9]
l1=[]
for num in l:
    if num>1:
        for val in range(2,num//2+1):
            if num%val == 0:
                break
        else:
            l1.append(num)
print(l1)'''
            

#2 reverse a list
'''l=[1,2,3,4,5]
print(l[::-1])'''

'''l.reverse()
print(l)'''

p=[22,2,3,4,5]
'''res=[]
for ind in range(len(p)-1,-1,-1):
    res.append(p[ind])
print(res)'''

#without using buildin methods

'''rev=[]
for ele in p:
    rev=[ele]+rev
print(rev)'''

#while loop

'''rev=[]
ind=len(p)-1
while ind !=-1:
    rev.append(p[ind])
    ind-=1
print(rev)'''


#with less no of iterations
l=[1,2,3,2,1,4]
'''for ind in range(0,len(l)//2):
    l[ind],l[-ind-1] = l[-ind-1],l[ind]
print(l)

ind=len(l)-1
while ind != -1:
    l[ind],l[-ind-1] = l[-ind-1],l[ind]
    ind-=1
print(l)'''


# pair of numbers whose num equal to target

'''l=[1,2,3,4,5]
target = 6
for ind1 in range(0,len(l)-1):
    for ind2 in range(ind1+1,len(l)):
        if l[ind1]+l[ind2]==target:
            print(l[ind1],l[ind2])

l=[1,2,3,4,5]
target = 6
for ind1 in range(len(l)):
    for ind2 in range(len(l)):
        if l[ind1]+l[ind2]==target:
            print(l[ind1],l[ind2])'''

#remove()
'''l=[1,2,3,4,5]
for ele in l:
    l.remove(ele)
print(l)'''



#list comprehension

'''print([val for val in range(int(input("enter the starting value:")),int(input("enter the ending value:")))])'''


'''print([int(input("enter the value:")) for val in range(int(input("enter the length:")))])'''

'''l=[10,11,12,13]
print([ele*ele for ele in l])'''

'''print([val for val in range(1,11) if val%2 == 0])'''

'''print([val for val in range(1,20) if val%2 == 0 and val %3==0])'''

print([[ind1,ind2] for ind1 in range(1,4) for ind2 in range(3,5)])


#add two lists using list comprehensions
'''l1=[1,2,3,4]
l2=[1,2,3,4]
print([l1[ind]+l2[ind] for ind in range(len(l1))])'''


#l='abcde' ==> a bb ccc dddd eeeee

l='abcde'

print('\n'.join(l[ind]*(ind+1) for ind in range(len(l))))

for ind in range(len(l)):
    print(l[ind] * (ind+1))


# Ternary operator

print(['even' if val%2==0 else 'odd' for val in range(1,11)])

s='hello'
print([s[ind] if ind%2==0 else 0 for ind in range(len(s))])

# dictionary comprehension
s='abcd'
print({s[ind]:s[ind]*(ind+1) for ind in range(len(s))})



s='world'
print({s[ind]:s[ind]*(ind) for ind in range(len(s)) if ind%2==0})

print({val:'even' if val%2==0 else 'odd' for val in range(1,11)})























