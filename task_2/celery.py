import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_2.settings')

app = Celery('task_2')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'load-the-data-structure-every-day': {
        'task': 'main.tasks.load_data_structure_task',
        'schedule': crontab(minute=0, hour=0),
    }
}
