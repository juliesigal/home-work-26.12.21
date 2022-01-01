from sqlalchemy import Column, Integer, String
from db_config import Base


class Attractions(Base):
    __tablename__ = 'attraction'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer(), nullable=False)


    def __repr__(self):
        return f'\n<Attraction id={self.id} name={self.fname} price={self.price} >'

    def __str__(self):
        return f'\n<Attraction id={self.id} name={self.fname} price={self.price} >'