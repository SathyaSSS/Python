#[any numbers,alphabets,characters]

import re
s='i 2a5@m ^49bat3man1+'
print(re.findall('[arn]',s))
print(re.findall('[a12345]',s))
print(re.findall('[^a-zA-z0-9]',s))


print(re.findall('[a-zA-Z0-9]',s))
print(re.findall('[a-z]',s))
print(re.findall('[A-Z]',s))

print(re.findall('[0-9]',s))
print(re.findall('[0-5][0-9]',s))
print(re.findall('[0-9][a-zA-z]',s))

print(re.findall('[^a-z]',s))
print(re.findall('\^',s))
print(re.findall('[+]',s))
