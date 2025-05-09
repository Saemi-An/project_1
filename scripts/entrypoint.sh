#!/usr/bin/env bash

# If errors then stop
set -e

RUN_MANAGE_PY='poetry run python -m core.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

echo 'Starting Gunicorn...'
# /gunicorn 디렉토리가 존재하는 상태에서 gunicorn.sock 자동 생성됨
# 컨테이너 내부 경로 기준으로 작성된 path이기 때문에 컴포즈에서 ./shared/gunicorn와 연결됨
exec poetry run gunicorn core.project.wsgi:application \
    --bind unix:/gunicorn/gunicorn.sock \
    --workers 3
