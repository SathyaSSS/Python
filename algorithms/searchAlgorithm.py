#lineary search

l=[22,3,7,1,-1,11,960]
user = -1
for ind in range(len(l)):
    if l[ind]==user:
        print(ind)
        break
else:
    print(-1)


#binary search

l=[-1,0,4,7,11,19,24]

user = 11
low = 0
high = len(l)-1
while low <= high:
    mid = (low + high) // 2
    if l[mid] > user:
        high = mid - 1
    elif l[mid] < user:
        low = mid + 1
    elif l[mid] == user:
        print(mid)
        break
else:
    print(-1)

#interpolation search

'''l[low] = m*low + c
l[high] = m*high + c
user = m*ind + c

l[high] - l[low] = m(high-low)
m = l[high] - l[low] / high-low --------------- 4


user - l[low] = m(ind - low)
m = user - l[low] / ind - low ------------------5


l[high] - l[low] / (high-low)  =  user - l[low] / (ind - low)

(ind - low) (l[high] - l[low])  =  (user - l[low]) (high-low)

ind - low = (user - l[low]) (high-low) / (l[high] - l[low])

ind = low + (user - l[low]) (high-low) / (l[high] - l[low]) -------answer '''



l = [-2,0,4,8,12,13,47] 

user = 0
low = 0
high = len(l) - 1

while low <= high and l[low] <= user <= l[high]:
    mid =  low + (user - l[low]) * (high-low) // (l[high] - l[low])
    
    if l[mid] > user:
        high = mid - 1
    elif l[mid] < user:
        low = mid + 1
    elif l[mid] == user:
        print(mid)
        break
else:
    print(-1)

















