#!/usr/bin/env python3

from helpers import add_to_db, get_all_from_db
from helpers import update_user_in_db
import click

@click.group()
def cli():
    '''Command line for trip management'''
    pass

"""user command group
   all commands applied to the User class
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
    # add_user_to_db(name)

@click.command(name='update')
@click.option('--id', prompt='User\'s id', type=str)
@click.option('--name', prompt='Updated name', type=str)
def update_user(id, name):
    '''Updates the user's name with name`'''
    update_user_in_db(id, name)

@click.command(name='get-all')
def get_all_users():
    '''Gets all users'''
    # get_all_users_from_db()
    get_all_from_db('users')

user_group.add_command(add_user)        
user_group.add_command(update_user)
user_group.add_command(get_all_users)

"""location command group
   all commands applied to the Location class
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

"""trips command group
   all commands applied to the Trip class
"""
# TODO

cli.add_command(user_group)
cli.add_command(location_group)

if __name__ == "__main__":
    cli()