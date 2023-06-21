#!/bin/bash

rm db.sqlite3
rm -rf ./soapdishapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations soapdishapi
python3 manage.py migrate soapdishapi
python3 manage.py loaddata soapers
python3 manage.py loaddata recipes
python3 manage.py loaddata oils
python3 manage.py loaddata recipe_oils
python3 manage.py loaddata comments
