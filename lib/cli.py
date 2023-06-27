#!/usr/bin/env python3

from helpers import add_user_to_db, get_all_users_from_db, delete_all_users_from_db
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
@click.argument('name', type=str)
def add_user(name):
    '''Creates a new user with {name}'''
    add_user_to_db(name)
    click.echo(f"Created new user {name}...")

@click.command(name='get-all')
def get_all_users():
    '''Gets all users'''
    users = get_all_users_from_db()
    [print(u) for u in users]

@click.command(name='delete-all')
def delete_all_users():
    '''Deletes all users'''
    ans = input('Are you sure? (Y/N)')
    if ans == 'Y':
        delete_all_users_from_db()
        print('Deleted all users')

user_group.add_command(get_all_users)
user_group.add_command(add_user)        
user_group.add_command(delete_all_users)

"""location command group
   all commands applied to the Location class
"""
# TODO

"""trips command group
   all commands applied to the Trip class
"""
# TODO

cli.add_command(user_group)

if __name__ == "__main__":
    cli()