import re

pwd = 'C4$'

matches = re.search(r'^[A-Z](\d)[\$%&]$', pwd)
print(matches[1])
print(len(matches.groups()))
if matches:
    print('OK')
else:
    print('not OK')
    

pwd = '%4C'

if re.search(r'[A-Z]', pwd) and  \
   re.search(r'\d', pwd) and \
   re.search(r'[\$%&]', pwd):     
    print('OK')
else:
    print('not OK')

