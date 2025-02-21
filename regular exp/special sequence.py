#\A
import re
s='hel1 2nms5 world @7'
print(re.findall('\Ah',s))
print(re.findall('\Ae',s))
print(re.findall('h\A',s))


#\Z
s='hel1 2nms5 world @7'
print(re.findall('7\Z',s))
print(re.findall('e\Z',s))
print(re.findall('\Z7',s))



#\b
s='hel1 2nms5 world @7'
print(re.findall(r'\bh',s))
print(re.findall(r'\b7',s))
print(re.findall(r'\b2',s))

print(re.findall(r'\bm',s))

print(re.findall(r'1\b',s))
print(re.findall(r'5\b',s))
print(re.findall(r'd\b',s))



#\B
s='hel1 2nms5 world @7'
print(re.findall(r'\Be',s))
print(re.findall(r'\Bn',s))
print(re.findall(r'\Bm',s))

print(re.findall(r'7\B',s))
print(re.findall(r'r\B',s))
print(re.findall(r'h\B',s))


#\dD
s='hel1 2nms5 world @7'
print(re.findall('\d',s))
print(re.findall('\D',s))



#\sS
s='hel1 2nms5 world @7'
print(re.findall('\s',s))
print(re.findall('\S',s))


#\wW
s='hel1 2nms5 w_orld @7'
print(re.findall('\w',s))
print(re.findall('\W',s))
