# Price Comparison Extension Application

This is the simple app created with Flask.

## Motivation

This is a simple application called `Price Comparison Extension`.
The purpose of this application is to present the outstanding features of Flask, learn how to use information architecture to create a workable folder structure.

## Code style

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://pypi.org/project/flake8/)

## Backend languages/frameworks used

### Python

Python is a programming language that lets you work quickly and integrate systems more effectively.

[Homepage](https://www.python.org/)

### Flask

Flask is a lightweight WSGI web application framework.
It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

[Homepage](https://flask.palletsprojects.com/)

## Features

* User can login/logout

* Guest can search the place sell with best price by product name

## Installation

Note: make sure you have `pip3` and `virtualenvwrapper` installed.

Create environment: `mkvirtualenv flask-env`

Initial installation: `pip install -r requirements.txt`

To run test: `bin/test-run.sh`

To run application: `bin/run.sh`

Make sure to run the initial migration commands to update the database.

* `bin/init_db.sh`

* `bin/migrate.sh`

* `bin/upgrade.sh`

## Viewing the app

    Open the following url on your browser to view swagger documentation
    http://localhost:5000/apidocs/
