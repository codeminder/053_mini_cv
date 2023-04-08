from .celery import app
from .utils import backup_db

@app.task
def run_bc():
    backup_db()