import Model
import os
import pytest

db_name = 'energytest.db'
db = Model.DB('sqlite:///' + db_name)

def test_db_create():    
    try:
        os.remove(db_name)
    except:
        pass
    
    db.create()
    c = db.sq(Model.Energy).count()
    assert c == 0

def test_insert():
    en = 'FluxCompensator'
    new_energy = Model.Energy()
    new_energy.name = en
    db.session.add(new_energy)
    db.session.commit()    
    
    energy = db.sq(Model.Energy).filter_by(name=en).first()
    assert energy.name == en

    

'''    

print(new_energy.id)
 
new_price = Model.Price(year=1997, energy=new_energy)
new_price.price = 12.12
db.session.add(new_price)
db.session.commit()
'''