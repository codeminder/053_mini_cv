from django.core.management import call_command
from .celery import app

@app.task
def backup_db():
  try:
      call_command('dbbackup')
  except:
      pass