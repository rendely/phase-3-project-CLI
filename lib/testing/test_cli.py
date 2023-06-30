#!/usr/bin/env python3

import pytest
from click.testing import CliRunner
from cli import cli

class TestBasic:
    '''[CLI basics]'''
    def test_cli(self):
        '''cli'''
        runner = CliRunner()
        result = runner.invoke(cli)
        assert result.exit_code == 0
        assert 'Usage: cli' in result.output

class TestUser:
    '''[CLI user commands]'''
    def test_cli_user(self):
        '''cli user'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user'])
        assert result.exit_code == 0
        assert 'Usage: cli user [OPTIONS]' in result.output

    def test_cli_user_add(self):
        '''cli user add'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'add', '--name', 'TestName'])
        assert result.exit_code == 0
        assert 'Created new user TestName' in result.output

    def test_cli_user_update(self):
        '''cli user update'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'update', '--id=10', '--name=NewTestName'])
        assert result.exit_code == 0
        assert 'Updated User.id=10 to new name: NewTestName' in result.output    
    
    def test_cli_user_get_all(self):
        '''cli user get-all'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'get-all'])
        assert result.exit_code == 0
        assert 'User(id=' in result.output