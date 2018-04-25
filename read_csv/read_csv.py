'''
Energiepreise
+ eingabe eines Energieträgers "Diesel (komm. Einsatz)/l" + Jahr

"Diesel (komm. Einsatz)/l" + 2015 => 0.52

Preise in EUR;;;;;;;;;;;;;
Nettopreis;2003;2004;2005;2006;2007;2008;2009;2010;2011;2012;2013;2014;2015
 Heiz�l schwer (Industrie)/t ;162,38;154;224,92;267,54;278,98;392,05;283,68;386,12;504,2;573,75;511,77;472,79;332,34
 Heiz�l schwer (Kraftwerke)/t ;121,88;115,74;138,96;165,27;153,14;226,44;144,04;271,95;320,06;493,1;473,35;340,29;331,06
 Gas�l (Industrie)/1000 l ;228,8;240,48;314,94;363,82;402,61;362,38;318,19;578,91;646,55;689,92;634,83;510,02;477,28

{
    "Diesel (komm. Einsatz)/l": {2003: 3, 2004:3.2},
 
'''

import csv
from pprint import pprint

with open('daten1.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter = ';'))

years = data[1][1:]
print(years)    
p = {}
pprint(data)
for line in data[2:]:    
    p[line[0].strip()] = \
        dict([(years[i], float(v.replace(',','.'))) for i, v in enumerate(line[1:])])
    
pprint(p)    
    