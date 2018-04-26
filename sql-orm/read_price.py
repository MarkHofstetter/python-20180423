from Model import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_energy.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

'''
energies = session.query(Energy).all()

for energy in energies:
    print(energy.name)
    
'''


energy = session.query(Energy).filter_by(name='FluxCompensator').first()
print(energy.name)
for price in energy.prices:
    print(price.year, price.price)
    

'''
prices = session.query(Price).filter(Price.energy == energy).all()

for p in prices:
    print(p.year, p.price)
'''
