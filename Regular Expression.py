import re
list= 'It is a book named Wedensday'
a= re.findall('[a-z]',list)
print(a)

import re
a='1 Hello Shanto'
b=re.findall('^1 ',a)
if b:
    print('Yes, Its start with 1')
else:
    print('No')




