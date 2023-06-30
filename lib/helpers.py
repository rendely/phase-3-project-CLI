from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location

engine = create_engine('sqlite:///db/trippy.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_user_to_db(name):
    session.add(User(name=name))
    session.commit()
    print(f"Created new user {name}")

def get_all_users_from_db():
    [print(u) for u in session.query(User).all()]

def update_user_in_db(id, new_name):
    session.query(User).filter(User.id==id).update({User.name: new_name})
    session.commit()
    print(f"Updated User.id={id} to new name: {name}")

def delete_all_users_from_db():
    session.query(User).delete()   
    session.commit()
    print('Deleted all users')

def get_all_locations_from_db():
    [print(l) for l in session.query(Location).all()]

def add_location_to_db(city, country):
    session.add(Location(city=city, country=country))
    session.commit()
    print(f"Added new location {city}, {country}")