#.
s='a ab abc abbc abbbc abbbbc c'
import re
print(re.findall('.',s))



#^
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('^a',s))
print(re.findall('^b',s))
print(re.findall('c^',s))



#$
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('c$',s))
print(re.findall('a$',s))
print(re.findall('$c',s))



#*
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('a*b',s))
print(re.findall('ab*c',s))
print(re.findall('abc*',s))


#+
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('a+b',s))
print(re.findall('ab+c',s))
print(re.findall('abc+',s))


#?
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('a?b',s))
print(re.findall('ab?c',s))
print(re.findall('abc?',s))



#{}
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('a{3}b',s))
print(re.findall('ab{4}c',s))
print(re.findall('abc{3}',s))

print(re.findall('a{0,3}b',s))
print(re.findall('ab{0,3}c',s))
print(re.findall('abc{0,3}',s))



#|
s='a ab abc abbc abbbc abbbbc c'
print(re.findall('a|b',s))
print(re.findall('ab|c',s))
print(re.findall('abc|',s))



#()
s='a ab abc abbc abbbc abbbbc c'
print(re.findall(('a|b'),s))
print(re.findall(('ab|c'),s))
print(re.findall(('abc|'),s))




#\

s='^a dcf.|thhj fjry'
print(re.findall('\^',s))
print(re.findall('\.',s))
print(re.findall('\|',s))



#[]

s='a dcf^.|thhj fjry'
print(re.findall('[.]',s))
print(re.findall('[|]',s))


































