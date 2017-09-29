import re

'''
https://regexr.com/

+ "kann" die usereingabe ein österreichische PLZ sein

A 1234
A-1234
A1234


===

+ regex schreiben
+ pytest machen 5 pos/5 negativ

'''

plz_to_check = {
    'A1234': True,
    'A-1239': True,
    'b1235': False,
    'A  5666': False,
    'A 666': True,
    }

def check_plz(plz):
    matches = re.search(r'^A[ -]{0,1}(\d{4})$', plz)
    # matches = re.search(r'^(A-|A |A){0,1}\d{4}$', plz)
    if matches:
        print("OK AT", matches[0], matches[1])
        return True
    else:
        print("nicht OK", plz)
        return False

test_fail = False        
for plz in plz_to_check:    
    if check_plz(plz) == plz_to_check[plz]:
        # print('Test OK')
        pass
    else:
        test_fail = True
        print('Test NICHT OK !!!!')

if test_fail:
    print('es ist was schiefgegangen')
else:
    print('alles gut')