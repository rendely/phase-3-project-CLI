#!/usr/bin/env python3
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Location, Trip, user_trip, trip_location

def run_seed():

    engine = create_engine('sqlite:///trippy.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Location).delete()
    session.query(Trip).delete()
    session.query(user_trip).delete()
    session.query(trip_location).delete()

    fake = Faker()

    locations = []
    for i in range(0,10):
      locations.append(Location(city=fake.city(), country=fake.country()))

    session.add_all(locations)

    trips = []
    trips.append(Trip(name='Japan trip', year=2016))
    trips.append(Trip(name='Europe trip', year=2022))

    session.add_all(trips)

    users = []
    for i in range(0,10):
      users.append(User(name=fake.first_name()))
    
    session.add_all(users)

    users[0].trips.append(trips[0])
    trips[0].locations.extend(locations[0:4])
    trips[1].locations.extend(locations[5:10])

    session.commit()
    session.close()

if __name__ == '__main__':
    run_seed()