teilnehmer = [
    ['Martin',    1976, ['VS', 'Gym', 'Uni']],
    ['Harald',    1970],
    ['Gerald',    1973],
    ['Roland',    1998],
    ['Christoph', 1981],
    ['Roland',    1974],
]

teilnehmer.append(['Mark', 1975, ['VS', 'Gym', 'Uni']])
teilnehmer.sort()
# print(teilnehmer)

''' 
+ geburtsjahr eines Teilnehmers finden (per kuerzel)
+ in einer for-schleife durchlaufen lassen und ausgeben
'''

name = input("Name: ")

# list comprehension
namen = [ tn[0] for tn in teilnehmer ]

found = False
for tn in teilnehmer:
    # namen.append(tn[0])
    if tn[0] == name:
        # edu = 'n/a' if len(tn) < 3 else tn[2][-1]
        if len(tn) < 3:
            edu = 'n/a'
        else:
            edu = tn[2][-1]
            
        print("%s wurde %d geboren, hoechste Bildung %s" % (name, tn[1], edu))
        found = True

print(namen)
        
if not found:
    print("Nichts gefunden")
        

