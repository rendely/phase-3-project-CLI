from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from db.models import User, Location, Trip, user_trip, trip_location
from db.seed import run_seed

current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_dir, "db/trippy.db")
engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

class_lookup = {'users': User, 'locations': Location, 
                'trips': Trip, 'user_trips': (User, Trip, 'trips', user_trip), 
                'trip_locations': (Trip, Location, 'locations', trip_location)}

def reset_db():
    run_seed()
    print('db has been reset')

def add_to_db(table, data):
    db_class = class_lookup[table]
    session.add(db_class(**data))
    session.commit()
    added = session.query(db_class).filter_by(**data).first()
    print('\nAdded:\n')
    print(added)
    print('\n')

def get_joined_and_unjoined_from_db(table, id):
    db_class = class_lookup[table]
    all_data = session.query(db_class[1]).all()
    joined_data = session.query(db_class[1]).join(db_class[3]).join(db_class[0]).filter(db_class[0].id==id).all()
    unjoined_data = [d for d in all_data if d not in joined_data] 
    print('\nExisting:')
    if not joined_data:
        print('None')
    else:
        [print(r) for r in joined_data]
    print('\nAll available:')
    if not unjoined_data:
        print('None')
    else:
        [print(r) for r in unjoined_data]
    print('')
    return unjoined_data

def update_in_db(table, id, data):
    db_class = class_lookup[table]
    record = session.get(db_class, id)
    for key, value in data.items():
        setattr(record, key, value)
    session.commit()
    updated = session.get(db_class, id)
    print('\nUpdated:\n')
    print(updated)
    print('\n')

def get_all_from_db(table):
    db_class = class_lookup[table]
    print(f'\nAll {table}:')
    print('-------------')
    [print(r) for r in session.query(db_class).all()]
    print('\n')

def get_all_from_db_as_string(table):
    db_class = class_lookup[table]
    records = session.query(db_class).all()
    records_strings = [str(r) for r in records]
    return '\n'.join(records_strings)

def get_attribute_from_db(table, id, attr):
    db_class = class_lookup[table]
    attribute = getattr(session.get(db_class, id), attr)
    print(f'\nAll {attr}')
    print('-------------')
    for i in attribute:
        print(i)
    print('\n')

def remove_from_db(table, id):
    db_class = class_lookup[table]
    session.query(db_class).filter(getattr(db_class,'id')==id).delete()
    session.commit()
    print(f'\nRemoved id={id}, updated list:\n')
    [print(r) for r in session.query(db_class).all()]
    print('\n')

def add_join_to_db(table, id1, id2):
    print(id1, id2)
    db_class = class_lookup[table]
    record1 = session.get(db_class[0], id1)
    record2 = session.get(db_class[1], id2)
    attribute = getattr(record1, db_class[2])
    if not record2 in attribute:
        attribute.append(record2)
        session.commit()
        print(f'\nAdded to {table}')
        print(record1)
        [print(a) for a in attribute]
        print('\n')
    else:
        print('\nAlready exists\n')

def remove_join_from_db(table, id1, id2):
    db_class = class_lookup[table]
    record1 = session.get(db_class[0], id1)
    record2 = session.get(db_class[1], id2)
    attribute = getattr(record1, db_class[2])
    if record2 in attribute:
        attribute.remove(record2)
        session.commit()
        print(f'\nRemoved from {table}')
        print(record1)
        [print(a) for a in attribute]
        print('\n')
    else:
        print('\nDid not exist\n')