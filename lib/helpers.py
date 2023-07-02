from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Location, Trip
from db.seed import run_seed
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_dir, "db/trippy.db")
print(database_path)
engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

class_lookup = {'users': User, 'locations': Location, 'trips': Trip}

def reset_db():
    run_seed()
    print('db has been reset')

def add_to_db(table, data):
    db_class = class_lookup[table]
    session.add(db_class(**data))
    session.commit()
    print(f'Added record to {table}: {data}')

def update_in_db(table, id, data):
    if table == 'user':
        user = session.get(User, id)
        user.name = data.new_name    
        session.commit()
    print(f"Updated record in {table} id={id} to {data}")

def get_all_from_db(table):
    db_class = class_lookup[table]
    [print(r) for r in session.query(db_class).all()]

def add_join_to_db(table, id1, id2):
    if table == 'user_trip':
        user = session.get(User, id1)
        trip = session.get(Trip, id2)
        if not trip in user.trips:
            user.trips.append(trip)
            session.commit()
            print('Added trip to user')
        else:
            print('Already exists')
    
    if table == 'trip_location':
        trip = session.get(Trip, id1)
        location = session.get(Location, id2)
        if not location in trip.locations:
            trip.locations.append(location)
            session.commit()
            print('Added location to trip')
        else:
            print('Already exists')

def remove_join_from_db(table, id1, id2):
    if table == 'user_trip':
        user = session.get(User, id1)
        trip = session.get(Trip, id2)
        if trip in user.trips:
            user.trips.remove(trip)
            session.commit()
            print('Removed trip from user')
        else:
            print('Did not exist')    

    if table == 'trip_location':
        trip = session.get(Trip, id1)
        location = session.get(Location, id2)
        if location in trip.locations:
            trip.locations.remove(location)
            session.commit()
            print('Removed location from trip')
        else:
            print('Did not exist')            