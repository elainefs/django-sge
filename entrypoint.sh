#!/bin/bash

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Load initial data"
python manage.py loaddata config/fixtures/initial_user.json

echo "Run Server"
exec python manage.py runserver 0.0.0.0:8000
