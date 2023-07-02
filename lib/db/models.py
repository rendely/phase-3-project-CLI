from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

user_trip = Table(
    'user_trips',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('trip_id', ForeignKey('trips.id'), primary_key=True),
    extend_existing=True,
)

trip_location = Table(
    'trip_locations',
    Base.metadata,
    Column('trip_id', ForeignKey('trips.id'), primary_key=True),
    Column('location_id', ForeignKey('locations.id'), primary_key=True),
    extend_existing=True,
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    trips = relationship('Trip', secondary=user_trip, back_populates='users')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, trips={self.trips})'

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer(), primary_key=True)
    country = Column(String())
    city = Column(String())
    trips = relationship('Trip', secondary=trip_location, back_populates='locations')

    def __repr__(self):
        return f'Location(id={self.id}, city={self.city}, country={self.country}, trips={self.trips})'        

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    year = Column(Integer())
    users = relationship('User', secondary=user_trip, back_populates='trips')
    locations = relationship('Location', secondary=trip_location, back_populates='trips')

    def __repr__(self):
        return f'Trip(id={self.id}, name={self.name}, year={self.year}, locations={self.locations})'                