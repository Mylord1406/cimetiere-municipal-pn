#!/bin/bash
echo "=== DEBUT DU SCRIPT ===" 1>&2
python manage.py migrate --settings=config.settings.production 1>&2
echo "=== FIN MIGRATE ===" 1>&2
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --log-level debug 1>&2