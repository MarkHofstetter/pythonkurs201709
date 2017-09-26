'''
+ eingabe einer Zahl
+ beenden wenn die Zahl == 0 ist
+ am Ende die Groesste der eingebenen Zahlen ausgeben

===

+ auch die Summe der Zahlen ausgeben
+ den Durchschnitt der Zahlen (vorsicht!)

- 2
- 1
- 5
- 4
- 3
- 0

ausgabe: hoechste 5, summe 12, 
'''

max_so_far = float("-inf")
sum = 0
count = 0

while True:
    try:
        user_input = input("Bitte Zahl eingeben: ")
        user_input = int(user_input)
    except ValueError:
        print(user_input, " ist keine Zahl")
        continue    
    if user_input == 0:
        break
    sum += user_input    
    if user_input > max_so_far:
        max_so_far = user_input    
    count += 1

if count > 0:
    print("Maximum:", max_so_far)   
    print("Summe:", sum)        
    print("Durchschnitt:", sum/count)
else:
    print("Nicht auszuwerten")
    
    


