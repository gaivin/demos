from __future__ import absolute_import
import os
from celery import Celery, shared_task
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_service_demo.settings')

app = Celery('async_service_demo')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.config_from_object('async_service_demo.celery_settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@shared_task(name="async_service_demo.debug")
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# app.conf.update(CELERY_RESULT_BACKEND='djcelery.backends.database.DatabaseBackend')
