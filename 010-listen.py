'''
list, array, field

liste, Feld
'''
#    0 1 2 3 4 5 6  7
f = [1,1,2,3,5,8,13,21]

print(f)
# der index einer liste beginnt bei 0
print(f[3])
# liefert das letzte Element
print(f[-1])
# list slices
print(f[3:6])
print(f[:3])
print(f[3:])
print(f[-2:])

print("zahl der Elemente", len(f))
print("letztes Element", f[len(f)-1])

f[7] = 23
f.append(45)
print(f)

r = f # kopiert nicht! sondern erstellt nur ein neue Variable auf die bestehende referenz
r = list(f) # erstellt eine neue Liste mit den Werten der Bestehenden
f.reverse() # oder sort etc

for element in r:
    print(element)    

f.insert(0,'bla')    
print(f)
f.insert(3, 23)    
print(f)

i = f.remove(23) # geht auf Werte, bei nichtexistenz => fehler
print(i, f)

del(f[0])
print(f)

l = [0] * 45
print(l)



