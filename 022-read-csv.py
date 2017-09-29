'''
+ csv datei einlesen

Preise in EUR;;;;;;;;;;;;;
Nettopreis;2003;2004;2005;2006;2007;2008;2009;2010;2011;2012;2013;2014;2015
 Heiz�l schwer (Industrie)/t ;162,38;154;224,92;267,54;278,98;392,05;283,68;386,12;504,2;573,75;511,77;472,79;33
 
+ "in richtige zahlen konvertieren"
+ Durchschnittpreis pro Energieträger
+ Grafik Preisverlauf
+ "sauberes" csv abspeichern

'''

import csv
import numpy
from matplotlib import pyplot as plt
from pprint import pprint

with open('daten.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter=';'))
    
## pprint(data[2])

prices = dict()

for row in data[2:]:
    # [' Heiz�l schwer (Industrie)/t ', '162,38', '154', '224,92', 
    # print(row)
    prices[row[0].strip()] = [ float(e.replace(',', '.')) for e in row[1:] ]

with open('daten_clean.csv', 'w', newline='') as writecsv:
   writer = csv.writer(writecsv, delimiter=',')
   
   writer.writerow([None] + data[1][1:])   
   for energy, price_list in prices.items():
       writer.writerow([energy] + price_list)
    
    
plt.subplot(121)
plt.xticks([int(y) for y in data[1][1:]])
# print(data[1][1:])
for energy, price_list in prices.items():
    print("%-35s Durchschnittspreis %.2f" % (energy, numpy.average(price_list)))
    plt.plot(price_list, label=energy)
    
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig('foo.png')
# plt.show()
    
    
'''
+ für jeden energieträger eine grafik (oder alle in einem) oder beides 
  mit dem Preisverlauf
+ x Achsen beschriftung
+ legende
+ etc
'''
    
