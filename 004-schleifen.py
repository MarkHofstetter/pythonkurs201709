for i in range(0,10,2):
    print(i)
    
print(i)

j = 0
while j < 10:
    print(j)
    # j = j + 1
    j += 1
    
    
k = 0
print("repeat until")
while True:    
    k += 1
    if k == 4:
        continue
    print(k)    
    if k > 10:
        break        