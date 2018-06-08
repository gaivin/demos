# Celery settings
import djcelery

djcelery.setup_loader()

# You must create a RabbitMQ server at first, and create a user, virtual host for the celery broker
RABBITMQ_USER = "celery"
RABBITMQ_PASSWORD = "changeme"
RABBITMQ_HOST = "10.98.77.200"
RABBITMQ_PORT = 5672
RABBITMQ_VIRTUAL_HOST = "async_service_demo"
BROKER_URL = 'amqp://%s:%s@%s:%s/%s' % (RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VIRTUAL_HOST)


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
