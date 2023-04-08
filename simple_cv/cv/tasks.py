from simple_cv.celery import app
from simple_cv.utils import backup_db

@app.task
def run_bc():
    backup_db()