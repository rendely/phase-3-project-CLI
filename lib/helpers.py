from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location

engine = create_engine('sqlite:///db/trippy.db')
Session = sessionmaker(bind=engine)
session = Session()

class_lookup = {'users': User, 'locations': Location}

def add_to_db(table, data):
    db_class = class_lookup[table]
    session.add(db_class(**data))
    session.commit()
    print(f'Added record to {table}: {data}')

def update_user_in_db(id, new_name):
    session.query(User).filter(User.id==id).update({User.name: new_name})
    session.commit()
    print(f"Updated User.id={id} to new name: {new_name}")

def get_all_from_db(table):
    db_class = class_lookup[table]
    [print(r) for r in session.query(db_class).all()]