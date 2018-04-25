'''
Energiepreise
+ eingabe eines Energieträgers "Diesel (komm. Einsatz)/l" + Jahr

"Diesel (komm. Einsatz)/l" + 2015 => 0.52
'''

import csv
from pprint import pprint


with open('daten1.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter = ';'))

for line in data:
    print(line)
    