'''
dict, dictionary
hash, assoziativer array
'''

import pprint

#    key          value
#    schlüssel    werte
teilnehmer = {
    'Martin':     {'year': 1976, 'height': 180, 'education': ['VS', 'Gym', 'Uni']},
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':     1998,
    'Christoph':  1981,
    'RolandS':     1974,
}

teilnehmer['Mark'] = 1975
# print(teilnehmer['Martin'])
pprint.pprint(teilnehmer)


for tn_name in teilnehmer:
    print(tn_name, teilnehmer[tn_name])
    
# print(teilnehmer.keys(), teilnehmer.values())    

print(list(teilnehmer.keys())[0])

'''
+ Namen abfragen und Geburtsjahr ausgeben

===

+ wenn es bei einem Teilnehmer eine "education" gibt, dann die "letzte" Ausgeben
'''


name = input("Name: ")
if name in teilnehmer:
    if type(teilnehmer[name]) == dict and \
       'education' in teilnehmer[name]:
        print(teilnehmer[name]['education'][-1])
    else:
        print(teilnehmer[name])    
    '''
        try:
            if 'education' in teilnehmer[name]:
                print(teilnehmer[name]['education'][-1])
        except TypeError:            
            print(teilnehmer[name])
    '''        
else:
    print("nichts gefunden")
