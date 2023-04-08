import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_cv.settings')

app = Celery('simple_cv')

# Set the default Django settings module for the 'celery' program.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs. 
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'make-backups-cv': {
        'task': 'cv.tasks.run_bc',
        'schedule': crontab(minute='*/10'),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight 
    },
}

app.conf.timezone = 'Europe/Kyiv'