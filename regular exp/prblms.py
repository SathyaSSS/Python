#mobile num

'''import re
number = input('enter the number :')
s = f'+91 {number}'
print(re.match('^[+]91(-| )[6789][0-9]{9}$',s))
print('valid number' if (re.match('^[+]91(-| )[6789][0-9]{9}$',s)) else 'invalid number')'''

#Email

'''import re
email = input('enter the email :')
s= f'{email}@gmail.com'
print(re.match('^[a-zA-Z0-9.-_]+@gmail.com$',s))
print('valid email' if (re.match('^[a-zA-Z0-9.-_]+@gmail.com$',s)) else 'invalid email')'''




#IP Address

import re

'''s = input('Enter the IP Address :')
print(re.match('^[0-255.]+[0-255.]+[0-255.]+[0-255]$',s))
if re.match('^[0-255.]+[0-255.]+[0-255.]+[0-255]$',s):
    print('valid IP Address')
else:
    print('invalid IP Address')'''



'''s = input('Enter the IP Address :')
print(re.match('^((2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])[.]){3}(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$',s))

if re.match('^((2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])[.]){3}(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$',s):
    print('valid IP Address')
else:
    print('invalid IP Address')'''






'''number=input('enter number :')
s=(f'+91 {number}')
if (re.match('^[+]91(-| )[6789][0-9]{9}$',s)):
    print('valid')
else:
    print('not')'''


email=input('enter mail :')
s= f'{email}@gmail.com'
if (re.match('^[a-zA-Z0-9.-_]+@gmail.com$',s)) and '..' not in s and '--' not in s and '__' not in s:
    print('valid')
else:
    print('not')
