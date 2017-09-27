'''
+ usereingabe englisches Wort => ausgabe deutsches Wort
+ fehler abfangen

===
+ "dict umkehren", dh ein 2tes dict erstellen wo key und values 
  vertauscht werden 
+ wenn das wort von eng2ger nicht gefunden wird schauen ob ein ger2eng 
  uebersetzung moeglich ist 
  
'''


import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read('woerterbuch.ini')
config.sections()

wb = config['english_to_german']
pprint(dict(wb))
# game = config['game']
# pprint(dict(game))

## dict umkehren 
# version 1
wb_ger2eng = {}
for word in wb:
    wb_ger2eng[wb[word]] = word

# version 2 
wb_ger2eng = dict((v,k) for k,v in wb.items())
# version 3
# wb_ger2eng = dict(zip(wb.values(), wb.keys()))
pprint(wb_ger2eng)    
    
user_input = input('Bitte Wort eingeben: ')
if user_input in wb:
    print("Englisch [%s] => Deutsch [%s]" % (user_input, wb[user_input]))
elif user_input in wb_ger2eng:   
    print("Deutsch [%s] => Englisch [%s]" % (user_input, wb_ger2eng[user_input]))
else:
    print("unbekannt")
  