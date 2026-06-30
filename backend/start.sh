#!/bin/bash
echo "=== DEBUT ===" 1>&2
python manage.py migrate --settings=config.settings.production 1>&2
echo "=== MIGRATE OK ===" 1>&2
PORT=${PORT:-8000}
echo "=== PORT EST: $PORT ===" 1>&2
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --log-level debug