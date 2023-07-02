from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Location, Trip
import os

database_path = os.path.abspath("db/trippy.db")

engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

class_lookup = {'users': User, 'locations': Location, 'trips': Trip}

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