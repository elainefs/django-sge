#!/bin/bash

echo "Waiting for PostgreSQL..."
until python -c "import psycopg2; psycopg2.connect(host='sge_db', port=5432, user='${POSTGRES_USER}', password='${POSTGRES_PASSWORD}', dbname='${POSTGRES_DB}')" 2>/dev/null; do
  sleep 2
done

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Load initial data"
python manage.py loaddata config/fixtures/initial_user.json

echo "Run Server"
exec python manage.py runserver 0.0.0.0:8000
