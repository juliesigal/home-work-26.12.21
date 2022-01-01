from sqlalchemy import Table, Column, Integer,  ForeignKey
from db_config import Base
from sqlalchemy.orm import relationship, backref


association_table = Table('tourist_attraction', Base.metadata,
                          Column('tourist_id', ForeignKey('tourist.id'), primary_key = True),
                          Column('attraction_id', ForeignKey('attraction.id'), primary_key = True)
                          )


class Visits(Base):
    __tablename__ = 'visit'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    tourist_id = Column(Integer(), ForeignKey('tourist.id'), nullable=False)
    attraction_id = Column(Integer(), ForeignKey('visit.id'), nullable=False)
    year_of_visit = Column(Integer(), nullable=False)

    def __repr__(self):
        return f'\n<Visits id={self.id} tourist id ={self.tourist_id} attraction id = {self.attraction_id}, year of visit = {self.year_of_visit} >'

    def __str__(self):
        return f'\n<Visits id={self.id} tourist id ={self.tourist_id} attraction id = {self.attraction_id}, year of visit = {self.year_of_visit} >'





