#!/bin/bash
echo "=== DEBUT ===" 1>&2
python manage.py migrate --settings=config.settings.production 1>&2
echo "=== MIGRATE OK ===" 1>&2
echo "=== PORT EST: $PORT ===" 1>&2
python -m http.server $PORT 1>&2