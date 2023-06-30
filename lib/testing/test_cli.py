#!/usr/bin/env python3

import pytest
from click.testing import CliRunner
from cli import cli

class TestBasic:
    '''[CLI basics]'''
    def test_cli(self):
        '''Does the CLI run when called'''
        runner = CliRunner()
        result = runner.invoke(cli)
        assert result.exit_code == 0
        assert 'Usage: cli' in result.output

class TestUser:
    '''[CLI user commands]'''
    def test_cli_user(self):
        '''Does the CLI user command work'''
        runner = CliRunner()
        result = runner.invoke(cli, ['user'])
        assert result.exit_code == 0
        assert 'Usage: cli user [OPTIONS]' in result.output