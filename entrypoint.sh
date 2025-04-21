#!/bin/bash

echo "Apply database migrations"
python manage.py migrate

echo "Run Server"
exec python manage.py runserver 0.0.0.0:8000
