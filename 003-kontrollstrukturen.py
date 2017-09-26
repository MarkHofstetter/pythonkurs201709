zahl = int(input('bitte eine Zahl eingeben: '))

if zahl == 3:
    print("super drei!")
    print("gut das du 3 geschrieben hast")
elif zahl > 3 and zahl <= 6:
    print("mehr als 3")
    if zahl != 5:
        print("zahl muss 4 oder 6 sein")
elif zahl > 6:
    print("mehr als 6")    
else:
    pass

print("Ende")    

