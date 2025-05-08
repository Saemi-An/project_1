#!/usr/bin/env bash

# If errors then stop
set -e

RUN_MANAGE_PY='poetry run python -m core.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run -m core.project.wsgi:application -p 8080 -b 0.0.0.0
exec $RUN_MANAGE_PY runserver
