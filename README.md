# Phase 3 CLI Project - Trip Planner

## Overview

A CLI to help users keep track of places they have visited or want to vist.

## Command line options

These are the actions a user should be able to accomplish:

Action | Command
---|---
Create a user | `trippy add user`
Get all users | `trippy show users`
Create a location | `trippy add location`
Update a location | `trippy update location`
Get all locations | `trippy show locations`
Create a trip | `trippy add trip`
Update a trip | `trippy update trip`
Get all trips | `trippy show trips`
Get completed trips | `trippy show trips --status=completed`
Get planned trips | `trippy show trips --status=planned`

## Database structure

User Table: This table stores details about each user.

- id (Primary Key)
- name

---

Location Table: This table stores all the locations

- id (Primary Key)
- name (Name of the location, e.g., 'Paris')
- country

---

Trips Table: This table stores information about the trips a user has planned or completed.

- id (Primary Key)
- user_id (Foreign Key referencing User Table)
- location_id (Foreign Key referencing Location Table)
- month
- year
- status ('planned' or 'completed')
