from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User

engine = create_engine('sqlite:///db/trippy.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_user(name):
    session.add(User(name=name))
    session.commit()