import Model
 
db = Model.DB()


gimme_enery(name, db)


'''
new_energy = Model.Energy()
new_energy.name = 'FluxCompensator'
db.session.add(new_energy)
db.session.commit()
print(new_energy.id)
 
new_price = Model.Price(year=1997, energy=new_energy)
new_price.price = 12.12
db.session.add(new_price)
db.session.commit()
'''

def gimme_enery(name, db):
    return db.get_energy()