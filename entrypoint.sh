#!/bin/bash

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Load initial data"
python manage.py loaddata config/fixtures/initial_user.json || true

echo "Run Server"
exec gunicorn config.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 4 \
  --timeout 300