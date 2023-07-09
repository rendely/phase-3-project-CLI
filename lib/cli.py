#!/usr/bin/env python3

from helpers import add_to_db, get_all_from_db, update_in_db 
from helpers import add_join_to_db, remove_join_from_db, reset_db
from helpers import get_attribute_from_db
import click

@click.group()
def cli():
    '''Command line for trip management'''
    pass

@click.command(name='reset')
def reset():
    """resets the db with seed.py"""
    reset_db()

cli.add_command(reset)

""" * 
    * user command group
    * all commands applied to the User class
    *
"""
@click.group(name='user')
def user_group():
    '''Group of user commands'''
    pass 

@click.command(name='add')
@click.option('--name', prompt='User\'s name',type=str)
def add_user(name):
    '''Creates a new user with {name}'''
    add_to_db('users', {'name': name})

@click.command(name='update')
@click.option('--id', prompt='User\'s id', type=str)
@click.option('--name', prompt='Updated name', type=str)
def update_user(id, name):
    '''Updates the user's name with name'''
    update_in_db('users', id, {'new_name': name})

@click.command(name='get-all')
def get_all_users():
    '''Gets all users'''
    get_all_from_db('users')

@click.command(name='add-trip')
@click.option('--user_id', prompt='User\'s id', type=str)
@click.option('--trip_id', prompt='Trips\'s id', type=str)
def add_user_trip(user_id, trip_id):
    """Adds a trip to a user's trips"""
    add_join_to_db('user_trips', user_id, trip_id)


@click.command(name='remove-trip')
@click.option('--user_id', prompt='User\'s id', type=str)
@click.option('--trip_id', prompt='Trips\'s id', type=str)
def remove_user_trip(user_id, trip_id):
    """Removes a trip from a user's trips"""
    remove_join_from_db('user_trips', user_id, trip_id)

@click.command(name='get-trips')
@click.option('--user_id', prompt="User's id", type=str)
def get_user_trips(user_id):
    """Gets the trips belonging to a user"""
    get_attribute_from_db('users', user_id, 'trips')

user_group.add_command(add_user)        
user_group.add_command(update_user)
user_group.add_command(get_all_users)
user_group.add_command(add_user_trip)
user_group.add_command(remove_user_trip)
user_group.add_command(get_user_trips)


""" *
    * location command group
    * all commands applied to the Location class
    *
"""
@click.group(name='location')
def location_group():
    '''Group of location commands'''
    pass 

@click.command(name='add')
@click.option('--city', prompt='City', type=str)
@click.option('--country', prompt='Country',type=str)
def add_location(city, country):
    '''Creates a new location with {city} and {country}'''
    add_to_db('locations', {'city': city, 'country': country})

@click.command(name='get-all')
def get_all_locations():
    '''Gets all locations'''
    get_all_from_db('locations')

location_group.add_command(add_location)
location_group.add_command(get_all_locations)            



""" *
    * trips command group
    * all commands applied to the Trip class
    *
"""
@click.group(name='trip')
def trip_group():
    '''Group of trip commands'''
    pass

@click.command(name='add')
@click.option('--name', prompt='Trip Name', type=str)
@click.option('--year', prompt='Year', type=int)
def add_trip(name, year):
    '''Creates a new trip with {name} and {year}'''
    add_to_db('trips', {'name': name, 'year': year})

@click.command(name='get-all')
def get_all_trips():
    '''Gets all trips'''
    get_all_from_db('trips')

@click.command(name='add-location')
@click.option('--trip_id', prompt='Trip\'s id', type=str)
@click.option('--location_id', prompt='Location\'s id', type=str)
def add_trip_location(trip_id, location_id):
    """Ads a location to a trip"""
    add_join_to_db('trip_locations', trip_id, location_id)

@click.command(name='remove-location')
@click.option('--trip_id', prompt='Trip\'s id', type=str)
@click.option('--location_id', prompt='Location\'s id', type=str)
def remove_trip_location(trip_id, location_id):
    """Removes a location from a trip"""
    remove_join_from_db('trip_locations', trip_id, location_id)    

trip_group.add_command(add_trip)
trip_group.add_command(get_all_trips)
trip_group.add_command(add_trip_location)
trip_group.add_command(remove_trip_location)

cli.add_command(user_group)
cli.add_command(location_group)
cli.add_command(trip_group)


if __name__ == "__main__":
    cli()