from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
 
class DB():
    engine = None
    db_name = None
    session = None
    sq = None    
    
    def __init__(self, db_name = 'sqlite:///sqlalchemy_energy.db'):
        self.db_name = db_name
        self.engine = create_engine(self.db_name)  
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        self.sq = self.session.query
        
    def create(self):
        Base.metadata.create_all(self.engine)
 
class Energy(Base):
    __tablename__ = 'energy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    prices = relationship('Price')
 
class Price(Base):
    __tablename__ = 'price'
    __public__ = ('price')    
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    _price = Column('price', Float, nullable=False)
    energy_id = Column(Integer, ForeignKey('energy.id'))
    energy = relationship(Energy)
    
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, price):        
        if price < 0:
            raise ValueError('price may not be negative')
        self._price = price
 
def main():
    print("creating database")
    db = DB()
    db.create()
    
if __name__ == '__main__':
    main()
