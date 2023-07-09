#!/usr/bin/env python3

import pytest
from click.testing import CliRunner
from cli import cli

runner = CliRunner()

class TestBasic:
    '''[CLI basics]'''
    def test_cli(self):
        '''cli'''
        
        result = runner.invoke(cli)
        assert result.exit_code == 0
        assert 'Usage: cli' in result.output

class TestUser:
    '''[CLI user commands]'''
    def test_cli_user(self):
        '''cli user'''
        result = runner.invoke(cli, ['user'])
        assert result.exit_code == 0
        assert 'Usage: cli user [OPTIONS]' in result.output

    def test_cli_user_add(self):
        '''cli user add'''
        result = runner.invoke(cli, ['user', 'add', '--name', 'TestName'])
        assert result.exit_code == 0
        assert "User(id=11, name=TestName, trips=[0])\n" in result.output

    def test_cli_user_update(self):
        '''cli user update'''
        result = runner.invoke(cli, ['user', 'update', '--id=10', '--name=NewTestName'])
        assert result.exit_code == 0
        assert "User(id=10, name=NewTestName, trips=[0])\n" in result.output    
    
    def test_cli_user_get_all(self):
        '''cli user get-all'''
        result = runner.invoke(cli, ['user', 'get-all'])
        assert result.exit_code == 0
        assert 'User(id=' in result.output
    
    def test_user_add_trip(self):
        '''cli user add-trip'''
        result = runner.invoke(cli, ['user', 'add-trip', '--user_id=3', '--trip_id=1'])
        assert result.exit_code == 0
        assert "User(id=3" in result.output
        assert "trips=[1])\n" in result.output
    
    def test_user_remove_trip(self):
        '''cli user remove-trip'''
        result = runner.invoke(cli, ['user', 'remove-trip', '--user_id=3', '--trip_id=1'])
        assert result.exit_code == 0
        assert "trips=[0])\n" in result.output

    def test_user_get_trips(self):
        '''cli user get-trips'''
        result = runner.invoke(cli, ['user', 'get-trips', '--user_id=1'])
        assert result.exit_code == 0
        assert "Trip(id=1, name=Japan trip, year=2016, locations=[2])" in result.output
        pass
        

class TestLocation:
    '''[CLI location commmands]'''
    def test_cli_location(self):
        '''cli location'''
        result = runner.invoke(cli, ['location'])
        assert result.exit_code == 0
        assert 'Usage: cli location [OPTIONS]' in result.output

    def test_cli_location_add(self):
        '''cli location add'''
        result = runner.invoke(cli, ['location', 'add', '--city=TestCity', '--country=TestCountry'])
        assert result.exit_code == 0
        assert "Location(id=7, city=TestCity, country=TestCountry)\n" in result.output

    def test_cli_location_get_all(self):
        '''cli location get-all'''
        result = runner.invoke(cli, ['location', 'get-all'])
        assert result.exit_code == 0
        assert 'Location(id=' in result.output

    def test_cli_location_remove(self):
        '''cli location remove'''
        result = runner.invoke(cli, ['location', 'remove', '--location_id=10'])
        assert result.exit_code == 0
        assert 'None' in result.output

class TestTrip:
    '''[CLI trip commands]''' 
    def test_cli_trip_add(self):
        '''cli trip add'''
        result = runner.invoke(cli, ['trip', 'add', '--name=TestTripName', '--year=1234'])
        assert result.exit_code == 0
        assert "Trip(id=3, name=TestTripName, year=1234, locations=[0])\n" in result.output
    
    def test_cli_trip_add_location(self):
        '''cli trip add-location'''
        result = runner.invoke(cli, ['trip', 'add-location', '--trip_id=2', '--location_id=6'])
        assert result.exit_code == 0
        assert "Trip(id=2, name=Europe trip, year=2022, locations=[4])\n" in result.output

    def test_cli_trip_remove_location(self):
        '''cli trip remove-location'''
        result = runner.invoke(cli, ['trip', 'remove-location', '--trip_id=2', '--location_id=6'])
        assert result.exit_code == 0
        assert "Trip(id=2, name=Europe trip, year=2022, locations=[3])\n" in result.output

    def test_cli_trip_remove(self):
        '''cli trip remove'''
        result = runner.invoke(cli, ['trip', 'remove', '--trip_id=1'])
        assert result.exit_code == 0
        assert 'None' in result.output