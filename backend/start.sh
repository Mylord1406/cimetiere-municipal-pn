#!/bin/bash
set -e
echo "=== STARTING MIGRATIONS ==="
python manage.py migrate --settings=config.settings.production
echo "=== MIGRATIONS DONE ==="
echo "=== STARTING GUNICORN ON PORT $PORT ==="
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --log-level debug