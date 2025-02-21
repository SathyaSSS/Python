#reverse a string

'''using for loops'''

'''s='sathya'
res=''
for ch in s:
    res=ch+res
print(res)


s='sathya'
res=''
for ch in range(len(s)-1,-1,-1):
    res=res+s[ch]
print(res)


s='sathya'
res=''
for ch in range(-1,-len(s)-1,-1):
    res=res+s[ch]
print(res)'''



#using while loop

'''s='sathya'
res=''
ind=len(s)-1
while ind!=-1:
    res=res+s[ind]
    ind-=1
print(res)


s='sathya'
res=''
ind=-1
while ind!=-len(s)-1:
    res=res+s[ind]
    ind-=1
print(res)

s='sathya'
res=''
ind=0
while ind!=len(s):
    res=s[ind]+res
    ind+=1
print(res)'''


#print digit from the string

'''s='ab3n4m5'
res=''
for ch in s:
    if ch.isdigit():
        res=res+ch
print(res)'''
        

#palindrome string

'''s='madam'
res=''
for ch in s:
    res=ch+res
if res==s:
    print('palindrome')
else:
    print('not')'''
    
    
#all substring

'''s='sathya'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        print(s[sv:ev])'''

s='sathya'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res=''
        for ind in range(sv,ev):
            res+=s[ind]
        print(res)

#substring palindrome

'''s='madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res=''
        rev=''
        for ind in range(sv,ev):
            res+=s[ind]
            rev=s[ind]+rev
        if res == rev:
            print(rev)'''

'''s='madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        word = s[sv:ev]
        if word == word[::-1]:
            print(word)'''

#even/odd lenght substring

'''s='sathya'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res=''
        for ind in range(sv,ev):
            res+=s[ind]
        if len(res)%2==0:
            print(res)'''

'''s='sathya'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res=''
        for ind in range(sv,ev):
            res+=s[ind]
        if len(res)%2!=0:
            print(res)'''

#longest/lowest lenght substring palindrome

'''s='madam'
l=[]
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        word = s[sv:ev]
        if word == word[::-1]:
            l.append(word)
print(max(l,key=len))

s='madam'
l=[]
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        word = s[sv:ev]
        if word == word[::-1]:
            l.append(word)
print(min(l,key=len))'''

#small/uppercase and upper/smallcase and s-u ==>u-s

'''s='asDEYq'
res=''
for ch in s:
    if 'A'<=ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=ch
print(res)


s='asDEYq'
res=''
for ch in s:
    if 'a'<=ch<='z':
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)


s='asDEYq'
res=''
for ch in s:
    if 'A'<=ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=chr(ord(ch)-32)
print(res)'''

#remove duplicates/unique char

'''s = 'raining'
unq=''
for ch in s:
    if ch not in unq:
        unq+=ch
print(unq)


s = 'raining'
unq=''
ind=0
while ind !=len(s):
    if s[ind] not in unq:
        unq+=s[ind]
    ind+=1
print(unq)'''

#counting the occurance of every char

'''s = 'raining'
unq=''
count=0
for ch in s:
    if ch not in unq:
        unq+=ch
        count+=1
print(count)


s = 'raining'
count=0
for ch in s:
    count+=1
print(count)'''


''''''''''''''''''''''''''''''''''''''''''''''''        

'''s = 'raining'
unq=''
for ch in s:
    if ch not in unq:
        unq+=ch
for ch in unq:
    print(f'{ch} - {s.count(ch)}')

s='raining'
unq=''
ind=0
while ind != len(s):
    if s[ind] not in unq:
        unq+=s[ind]
    ind+=1
for ch in unq:
    print(f'{ch} - {s.count(ch)}')'''
    

#using replace method

'''s='raining'
while s != '':
    print(f'{s[0]} - {s.count(s[0])}')
    s=s.replace(s[0],'')'''

'''s='raining'
while s != '':
    print(f'{s[0]} - {s.count(s[0])}')
    s=s.replace(s[0],'')'''


#print duplicate values

'''s='engineering'
unq=''
for ch in s:
    if ch not in unq:
         unq+=ch
         if s.count(ch)>1:
            print(ch)'''


#count only the digits

'''s='acb3f2b4#@^(5'
count=0
for ch in s:
    if ch.isdigit():
        count+=1
print(count)
            

s='acb3f2b4#@^(5'
count=0
for ch in s:
    if ch in '1234567890':
        count+=1
print(count)


s='acb3f2b4#@^(5'
count=0
for ch in s:
    if '0'<=ch<='9':
        count+=1
print(count)'''


#count only the alphabets

'''s='acb3f2b4#@^(5'
count=0
for ch in s:
    if ch.isalpha():
        count+=1
print(count)


s='acb3f2b4#@^(5'
count=0
for ch in s:
    if 'a'<=ch<='z' or 'A'<=ch<='Z':
        count+=1
print(count)'''



#print only vowels

'''s='acbeu3f2b4#@^(5'
res=''
count=0
for ch in s:
    if ch in 'AEIOUaeiou':
        res+=ch
        count+=1
print(res)
print(count)'''


#print only consonants or not vowels

'''s='acbeu3f2b45'
res=''
count=0
for ch in s:
    if ch not in 'AEIOUaeiou':
        res+=ch
        count+=1
print(res)
print(count)


s='acbeu3f2b45'
res=''
count=0
for ch in s:
    if ch not in 'AEIOUaeiou' and ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
        res+=ch
        count+=1
print(res)
print(count)'''


#print both alphabets and digits

'''s='acbeu3f2b45'
res=''
count=0
for ch in s:
    if 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9':
        res+=ch
        count+=1
print(res)
print(count)

s='acbeu3f2b45'
res=''
count=0
for ch in s:
    if ch.isalnum():
        res+=ch
        count+=1
print(res)
print(count)'''

#print special char


'''s='acbeu3f2b4@#$5'
spcl=''
count=0
for ch in s:
    if ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
        pass
    else:
        spcl+=ch
        count+=1
print(spcl)
print(count)


s='acbeu3f2b4@#$5'
spcl=''
count=0
for ch in s:
    if not ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
        spcl+=ch
        count+=1
print(spcl)
print(count)'''

#reverse the position of words

s='we have class on sunday'
l=[]
l=s.split()
l.reverse()
print(' '.join(l))
    
#without using builtin methods

'''s='we have class on sunday'
l=[]
revs=''
word=''
for ch in s:
    if ch == ' ':
        l=[word]+l
        word=''
    else:
        word+=ch
l=[word]+l
ind =0
while ind!=len(l):
    if ind != len(l)-1:
        revs+=l[ind]+' '
    else:
        revs+=l[ind]
    ind+=1
print(revs)'''


#reverse the every word in gn string

'''s='we have class on sunday'
l=[]
revs=''
word=''
for ch in s:
    if ch == ' ':
        l+=[word]
        word=''
    else:
        word=ch+word
l+=[word]
print(l)
ind =0
while ind!=len(l):
    if ind != len(l)-1:
        revs+=l[ind]+' '
    else:
        revs+=l[ind]
    ind+=1
print(revs)'''



s='we have class on sunday'
l=[]
res=[]
l=s.split()
for ele in l:
    res.append(ele[::-1])
print(' '.join(res))



#aaabbccddd = 3a2b2c3d

s='aaabbccddd'
res=''
count=1
for ind in range(0,len(s)-1):
    if s[ind] == s[ind+1]:
        count+=1
    else:
        res+=str(count)+s[ind]
        count=1
res+=str(count)+s[ind]
print(res)
        
                 
s='3a2b2c3d'
res=''
num=''
for ch in s:
    if '0'<=ch<='9':
        num+=ch
    else:
        res+=int(num)*ch
        num=''
print(res)
        
                 







