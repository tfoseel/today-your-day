#!/bin/bash

python manage.py migrate --noinput
python manage.py create_admin
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
