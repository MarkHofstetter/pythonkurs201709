'''
+ aus dem Wertbereich 1-45 sollen 6 Zahlen gezogen werden
+ ACHTUNG: es darf keine doppelt vorkommen

===

+ mit einem einzeiler (siehe doku random)
+ testbarkeit?!
+ die richtigen Zahlen vom nächsten Sonntag
'''

import random

all = list(range(1,46))
winning_numbers = []
# print(all)
'''
count = 0 
while count < 6:
    random_ = random.randint(1, 45)
    if random_ in winning_numbers:
        print("bumm")
        continue
    winning_numbers.append(random_)    
    count += 1
    
print(winning_numbers)    

exit()

for i in range(7):
    print(random.sample(all, 6))
    print(len(all))
exit()
'''


for i in range(0,6):
    random_index = random.randint(0,len(all)-1)   ##   44-i)
    winning_numbers.append(all[random_index])
    del(all[random_index])

winning_numbers.sort()

print("Deine Zahlen:", winning_numbers)


