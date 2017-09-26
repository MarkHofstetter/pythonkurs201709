text = 'Python ist toll'

print(text + text)

print((text + ' ') * 4 )

print(text)
print('=' * len(text))

print(text.lower())
print(text.upper())

# for b in text:
#    print(b)

''' 
der benutzer soll eine scuhstring eingeben
und es soll ueberprueft werden ob der in in text enthalten ist
===
+ gross/kleinschreibung ignorieren

'''

searchstring = input("Suchtext eingeben bitte: ")
if searchstring.strip().lower() in text.lower():
    print(searchstring, "enthalten")
else:
    print(searchstring, "nicht gefunden")

print(text.count('ll'))
print(text.replace('Python', 'perl'))    


