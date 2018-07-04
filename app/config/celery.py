import json
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
app = Celery('config')
# namespace 지정 CELERY_시작할때만 Settings에서 가져서와서 사용하도록 지정
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    # Calls repr() on the argument first
    print('Request: {0!r}'.format(self.request))
