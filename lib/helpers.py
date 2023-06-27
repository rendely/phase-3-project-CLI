from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User

engine = create_engine('sqlite:///db/trippy.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_user_to_db(name):
    session.add(User(name=name))
    session.commit()

def get_all_users_from_db():
    return session.query(User).all()

def delete_all_users_from_db():
    session.query(User).delete()   
    session.commit()