'''
+ "kleines 1x1" abpruefen
+ dh 2 zufallszahlen aus [0..9] ermitteln
+ den User antworten lassen => richtig/falsch + ergebnis ausgeben

===

+ x Rechnungen machen lassen und ermitteln wieviele richtig und falsch waren
+ zb ausgabe 70% richtig etc
+ Gedanken über konfigurierbarkeit machen, zb nur bis zur 5er Reihe etc usw

'''

import random
from integer_input import user_input_integer

end = False
correct_answers = 0
wrong_answers   = 0
count = 0

while True:
    factor1 = random.randint(0,9)
    factor2 = random.randint(0,9)
    product = factor1 * factor2
    
    print("Zerlege %s?" % (product))    
    error = False
    u1, error = user_input_integer()
    u2, error = user_input_integer()
    if error:
        continue
    if u1 == 'x':
        break
    if u1 * u2 == product:
        print("\033[32mRichtig\033[0m")
        correct_answers += 1
    else: 
        print("Falsch, %s * %s ist richtig" % (factor1, factor2))
        wrong_answers += 1
    
if count > 0:        
    print("du hast %d von %d richtig beantwortet,\n dass sind %d%%" % 
             (correct_answers,
              count,
              round(correct_answers/count * 100)))