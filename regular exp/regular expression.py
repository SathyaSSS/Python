#match
import re
s='software developer'

print(re.match('s',s))
print(re.match('t',s))


#search

print(re.search('de',s))
print(re.match('g',s))


#findall

print(re.findall('s',s))
print(re.findall('e',s))
print(re.findall('h',s))


#split

print(re.split('s',s))
print(re.split('e',s,2))
print(re.split('h',s))


#sub
print(re.sub('e','E',s))
print(re.sub('e','E',s,2))
print(re.sub('h','E',s))


#subn
print(re.subn('e','E',s))
print(re.subn('e','E',s,2))
print(re.subn('h','E',s))


#finditer
print(re.finditer('e',s))
print(re.finditer('h',s))
print(list(re.finditer('h',s)))
print(list(re.finditer('e',s)))



#compile

obj=re.compile('e')
print(obj.findall(s))

obj=re.compile('h')
print(obj.findall(s))

obj=re.compile('d')
print(obj.findall(s))
