#!/bin/bash

echo DATABASE_USER: "$DATABASE_USER"
echo DATABASE_HOST: "$DATABASE_HOST"
pipenv run gunicorn -b :8000 bookstore_project.wsgi
