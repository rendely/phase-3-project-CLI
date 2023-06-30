from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'User(id={self.id}, name={self.name})'

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer(), primary_key=True)
    country = Column(String())
    city = Column(String())

    def __repr__(self):
        return f'Location(id={self.id}, city={self.city}, country={self.country})'        

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    year = Column(Integer())

    def __repr__(self):
        return f'Trip(id={self.id}, name={self.name}, year={self.year})'                