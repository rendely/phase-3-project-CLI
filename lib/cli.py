#!/usr/bin/env python3

from helpers import add_user_to_db
import click

@click.group()
def cli():
    pass

# User related commands
@cli.command(name='add-user')
@click.argument('name', type=str)
def add_user(name):
    click.echo(f"Creating new user {name}...")
    add_user_to_db(name)

if __name__ == "__main__":
    cli()