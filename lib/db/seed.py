#!/usr/bin/env python3
from faker import Faker
import random
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . models import User, Location, Trip, user_trip, trip_location

def run_seed():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_dir, "trippy.db")
    engine = create_engine(f'sqlite:///{database_path}')
    # engine = create_engine('sqlite:///trippy.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Location).delete()
    session.query(Trip).delete()
    session.query(user_trip).delete()
    session.query(trip_location).delete()

    fake = Faker()

    locations = []
    locations.append(Location(city='Tokyo', country='Japan'))
    locations.append(Location(city='Kyoto', country='Japan'))
    locations.append(Location(city='Paris', country='France'))
    locations.append(Location(city='London', country='England'))
    locations.append(Location(city='Barcelona', country='Spain'))
    locations.append(Location(city='Milan', country='Italy'))
    
    session.add_all(locations)

    trips = []
    trips.append(Trip(name='Japan trip', year=2016))
    trips.append(Trip(name='Europe trip', year=2022))

    session.add_all(trips)

    users = []
    for i in range(0,10):
      users.append(User(name=fake.first_name()))
    
    session.add_all(users)

    users[0].trips.extend(trips)
    trips[0].locations.extend(locations[0:1])
    trips[1].locations.extend(locations[2:4])

    session.commit()
    session.close()

if __name__ == '__main__':
    run_seed()