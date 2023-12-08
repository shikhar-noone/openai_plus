#!/usr/bin/env bash
# start-server.sh
set -e

# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#     (python manage.py createsuperuser --no-input)
# fi

(gunicorn noone.wsgi --user www-data --reload --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"