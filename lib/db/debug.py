#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models import User, Location, Trip, user_trip, trip_location

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_dir, "trippy.db")
    engine = create_engine(f'sqlite:///{database_path}')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
