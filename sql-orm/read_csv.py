import Model
import csv
from pprint import pprint

db = Model.DB()

with open('daten1.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter = ';'))

years = data[1][1:]

for line in data[2:]:
    energy_name = line[0].strip()
    energy = Model.Energy(name = energy_name)
    db.session.add(energy)
    db.session.commit()  
    
    for i, v in enumerate(line[1:]):
        price = Model.Price(year   = years[i], 
                            price  = float(v.replace(',','.')), 
                            energy = energy)
        db.session.add(price)            
    db.session.commit()
    
    