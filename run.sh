#!/bin/bash

pipenv run gunicorn -b :8000 bookstore_project.wsgi

