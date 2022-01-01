from sqlalchemy import Column, Integer, String
from db_config import Base

class Tourists(Base):
    __tablename__ = 'tourist'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    origin_country = Column(String(30), nullable=False)

    def __repr__(self):
        return f'\n<Tourist id={self.id} name ={self.name} origin country = {self.origin_country} >'

    def __str__(self):
        return f'\n<Tourist id={self.id} name ={self.name} origin country = {self.origin_country} >'
