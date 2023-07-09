# Phase 3 CLI Project - Trip Planner

## Overview

A CLI to help users keep track of trips. Users can create trips and associate them with a list of locations.

## Command line options

### Overview

```markdown
trippy [OPTIONS] COMMAND [ARGS]...
Options:
  --help  Show this message and exit.

Commands:
  location  Group of location commands
  reset     resets the db with seed.py
  trip      Group of trip commands
  user      Group of user commands
```

### user commands

```markdown
trippy user [OPTIONS] COMMAND [ARGS]...
Commands:
  add          Creates a new user
  add-trip     Adds a trip to a user's trips
  get-all      Gets all users
  get-trips    Gets the trips belonging to a user
  remove-trip  Removes a trip from a user's trips
  update       Updates the user's name with name
```

### location commands

```markdown
trippy location [OPTIONS] COMMAND [ARGS]...
Commands:
  add      Creates a new location
  get-all  Gets all locations
  remove   Remove a location
```

### trip commands

```markdown
trippy trip [OPTIONS] COMMAND [ARGS]...
Commands:
  add              Creates a new trip
  add-location     Ads a location to a trip
  get-all          Gets all trips
  remove           Remove a trip
  remove-location  Removes a location from a trip
```

## Useful commandline arguments for development

```shell
alembic revision --autogenerate -m '<comment here>'
```

```shell
alembic upgrade head
```

```shell
alias trippy='python ~/Flatiron/code/phase-3/phase-3-project-CLI/lib/cli.py'
```
