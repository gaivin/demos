#!/usr/bin/env bash

# Ensure the celery can be start up by root user.
export C_FORCE_ROOT="true"

echo "Start up the Event monitor..."
nohup python manage.py celerycam > celerycam.log 2>&1 &
echo $!
echo "Start up the Celery worker monitor..."
nohup python manage.py celery worker -l info -E > celeryworker.log 2>&1 &
echo $!