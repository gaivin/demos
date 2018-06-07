# Celery settings

CELERY_BROKER_URL = 'amqp://celery:changeme@10.98.77.200:15672//'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_BACKEND = 'db+sqlite:///db_celery_task_results.sqlite'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'