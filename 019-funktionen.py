def addiere(a, b, c):
    summe = a + b + c    
    b += 1
    print('aus fkt', b)
    return summe

def beliebigearg(**kwargs):
    print(kwargs)
    
def_b = 12
    
def default_werte(a, b=def_b):
    print(a,b)
    return a,b 
    
def kreisumfang(radius)    
'''    
def f_array(feld):
    print('aus fkt', feld)
    feld.append(4)    
    
feld_main = [1,2,3]
f_array(feld_main)    
print(feld_main)
'''

c, d = default_werte(b=8, a=13)

kreditrate(laufzeit=8,zinsatz=0.1,12,5)

kreisumfang(radius=5)
'''
beliebigearg(a=1, b=2, c=7)

a = 3
b = 4    
d = addiere(a, b, 7)
print(d)
'''

