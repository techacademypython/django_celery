# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task
def toplama(a, b):
    time.sleep(20)
    return a + b