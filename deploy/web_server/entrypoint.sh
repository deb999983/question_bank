#!/bin/sh

echo "== Starting Django app: $WORKDIR: $DJANGO_SETTINGS_MODULE"
echo "Waiting for postgres..."
while ! nc -z ${MY_DB_HOST:-question_bank} ${MY_DB_PORT:-5432}; do
  sleep 0.1
done
echo "DB Ready ..."
python ${WORKDIR}/web_server/manage.py migrate

echo "Starting Gunicorn ......."
gunicorn -v
gunicorn web_server.wsgi:application --bind=0.0.0.0:8000 --log-level='debug' --capture-output
