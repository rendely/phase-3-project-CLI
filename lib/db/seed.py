#!/usr/bin/env python3
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User

if __name__ == '__main__':
    engine = create_engine('sqlite:///trippy.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()

    fake = Faker()
    users = []
    for i in range(0,10):
      users.append(User(name=fake.first_name()))
    
    session.add_all(users)

    session.commit()
    session.close()
