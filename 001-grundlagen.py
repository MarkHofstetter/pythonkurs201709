print("Hallo Welt")

a = 2
print(a)

# b bekommt den Wert 5 als String
# zur demonstration von kompatiblen Typen
b = "5" 
print(b)

pi = 3.1415

umsatzsteuer_oesterreich = 0.2


c = a + float(b) + 1.23
print(c)

# variablen typen muessen zusammenpassen
print(str(a) + b)
print(a + int(b))
 
print(a, b)

eingabe = input('Gib mir eine Zahl: ')
print(type(eingabe))
eingabe = int(eingabe)
print(type(eingabe))
print(eingabe + 1)