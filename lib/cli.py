#!/usr/bin/env python3

from helpers import add_user

if __name__ == '__main__':
    print('Welcome to my CLI! What\'s your name?')
    name = input()
    add_user(name)
