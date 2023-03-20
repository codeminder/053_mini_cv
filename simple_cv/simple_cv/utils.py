from django.core.management import call_command

def backup_db():
  try:
      call_command('dbbackup')
  except:
      pass