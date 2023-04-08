## How to install it

    pip install celery
    pip install django-celery-results

    INSTALLED_APPS = (
    ...,
    'django_celery_results',
    )

    python manage.py migrate django_celery_results

    CELERY_RESULT_BACKEND = 'django-db'

### How to run it

    docker run -d -p 6379:6379 redis
    celery -A simple_cv worker --loglevel=INFO
    celery -A simple_cv beat