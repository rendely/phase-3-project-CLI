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
        assert "Added record to users: {'name': 'TestName'}" in result.output

    def test_cli_user_update(self):
        '''cli user update'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'update', '--id=10', '--name=NewTestName'])
        assert result.exit_code == 0
        assert "Updated record in users id=10 to {'new_name': 'NewTestName'}\n" in result.output    
    
    def test_cli_user_get_all(self):
        '''cli user get-all'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'get-all'])
        assert result.exit_code == 0
        assert 'User(id=' in result.output
    
    def test_user_add_trip(self):
        '''cli user add-trip'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'add-trip', '--user_id=3', '--trip_id=1'])
        assert result.exit_code == 0
        assert "Added trip to user" in result.output
    
    def test_user_remove_trip(self):
        '''cli user remove-trip'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user', 'remove-trip', '--user_id=3', '--trip_id=1'])
        assert result.exit_code == 0
        assert "Removed trip from user" in result.output
        

class TestLocation:
    '''[CLI location commmands]'''
    def test_cli_location(self):
        '''cli location'''
        runner = CliRunner()
        result = runner.invoke(cli, ['location'])
        assert result.exit_code == 0
        assert 'Usage: cli location [OPTIONS]' in result.output

    def test_cli_location_add(self):
        '''cli location add'''
        runner = CliRunner()
        result = runner.invoke(cli, ['location', 'add', '--city=TestCity', '--country=TestCountry'])
        assert result.exit_code == 0
        assert "Added record to locations: {'city': 'TestCity', 'country': 'TestCountry'}\n" in result.output

    def test_cli_user_get_all(self):
        '''cli location get-all'''
        runner = CliRunner()
        result = runner.invoke(cli, ['location', 'get-all'])
        assert result.exit_code == 0
        assert 'Location(id=' in result.output

class TestTrip:
    '''[CLI trip commands]''' 
    def test_cli_trip_add(self):
        '''cli trip add'''
        runner = CliRunner()
        result = runner.invoke(cli, ['trip', 'add', '--name=TestTripName', '--year=1234'])
        assert result.exit_code == 0
        assert "Added record to trips: {'name': 'TestTripName', 'year': 1234}\n" in result.output
    
    def test_trip_add_location(self):
        '''cli trip add-location'''
        runner = CliRunner()
        result = runner.invoke(cli, ['trip', 'add-location', '--trip_id=1', '--location_id=8'])
        assert result.exit_code == 0
        assert "Added location to trip" in result.output

    def test_trip_remove_location(self):
        '''cli trip remove-location'''
        runner = CliRunner()
        result = runner.invoke(cli, ['trip', 'remove-location', '--trip_id=1', '--location_id=8'])
        assert result.exit_code == 0
        assert "Removed location from trip" in result.output