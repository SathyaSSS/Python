#BUBBLE SORT

l = [33,2,4,77,10,-2,1,0]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2] > l[ind2 + 1]:
            l[ind2],l[ind2 + 1] = l[ind2 + 1],l[ind2]
print(l)


# SELECTION SORT

l = [33,2,4,777,10,-2,1,0]
for ind1 in range(len(l) -1):
    select = ind1
    for ind2 in range(ind1+1,len(l)):
        if l[ind2] < l[select]:
            select = ind2
    l[ind1],l[select] = l[select],l[ind1]
print(l)


# QUICK SORT

def quick(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    left = [num for num in l[1:] if num < pivot]
    right = [num for num in l[1:] if num >= pivot]
    return quick(left) + [pivot] + quick(right)

l = [33,2,4,7777,10,-2,1,0]
print(quick(l))


#MERGE SORT

def half(l):
    if len(l) > 1:
        mid = len(l)//2
        left,right = l[:mid],l[mid:]
        half(left),half(right)
        merge(l,left,right)
        
def merge(l,left,right):
    lind,rind,mind = 0,0,0
    
    while lind < len(left) and rind < len(right):
        if left[lind] < right[rind]:
            l[mind]=left[lind]
            lind += 1
        else:
            l[mind] = right[rind]
            rind += 1
        mind += 1
        
    while lind < len(left):
        l[mind] = left[lind]
        lind += 1
        mind += 1
        
    while rind < len(right):
        l[mind] = right[rind]
        rind += 1
        mind += 1

l = [33,2,4,77777,10,-2,1,0]
half(l)
print(l)



#INSERTION SORT

l = [33,2,4,777777,10,-2,1,0]

for ind1 in range(1,len(l)):
    a = ind1
    val = l[a]
    while a > 0 and val < l[a-1]:
        l[a] = l[a-1]
        a-=1
    l[a] = val
print(l)
        
            



































