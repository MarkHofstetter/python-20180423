from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from Model import Energy, Base, Price
 
engine = create_engine('sqlite:///sqlalchemy_energy.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
new_energy = Energy()
new_energy.name = 'FluxCompensator'
session.add(new_energy)
session.commit()
print(new_energy.id)
 
new_price = Price(year=1997, energy=new_energy)
new_price.price = -12.12
session.add(new_price)
session.commit()
