'''
+ usereingabe eines Satzes
+ und den Anfangsbuchstaben des Satzes soll ein passwort 
  generiert werden
+ "Ich ess gerne Schnitzel" =< IegS
+ der Satz soll einer Funktion übergeben werden, das Pwd retourniert

===

+ zufällige Zahlen/sonderzeichen zwischen den Buchstaben
+ mindestlänge des Satze kontrollieren

'''

import random
import sys

from wifi_password import generate_password

# sentence = input('bitte satz eingeben: ')
sentence = sys.argv[1]
password = generate_password(sentence)
print(password)
