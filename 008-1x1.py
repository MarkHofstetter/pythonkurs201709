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

end = False
correct_answers = 0
wrong_answers   = 0
count = 0

while True:
    factor1 = random.randint(0,9)
    factor2 = random.randint(0,9)
    print("Wieviel ist %s mal %s?" % (factor1, factor2))
    while True:
        try:
            user_input = input("Bitte Ergebnis eingeben: ")
            if user_input == 'x':
                end = True
                break
            user_input = int(user_input)
            count += 1
            break
        except ValueError:
            print(user_input, "ist keine Zahl")
    if end:
        break
        
    product = factor1 * factor2
    if user_input == product:
        print("\033[32mRichtig\033[0m")
        correct_answers += 1
    else: 
        print("Falsch, %s ist richtig" % (product))
        wrong_answers += 1
        
if count > 0:        
    print("du hast %d von %d richtig beantwortet,\n dass sind %d%%" % 
             (correct_answers,
              count,
              round(correct_answers/count * 100)))