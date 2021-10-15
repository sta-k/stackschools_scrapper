# djangoceleryscrapper

Django Celery Scheduled Scrapper

### Install Redis](https://stackoverflow.com/a/67293964/2351696)::

    $ sudo add-apt-repository ppa:redislabs/redis
    $ sudo apt-get update
    $ sudo apt-get install redis

### [Celery setup for django](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)

`mysite/celery.py`::

    import os

    from celery import Celery

    # Set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

    app = Celery('proj')

    # Using a string here means the worker doesn't have to serialize
    # the configuration object to child processes.
    # - namespace='CELERY' means all celery-related configuration keys
    #   should have a `CELERY_` prefix.
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django apps.
    app.autodiscover_tasks()

`mysite/__init__.py`::

    # This will make sure the app is always imported when
    # Django starts so that shared_task will use this app.
    from .celery import app as celery_app

    __all__ = ('celery_app',)

`schools/tasks.py`::

    from celery import shared_task
    from schools.models import School, CeleryTasks

    @shared_task
    def task_scrap_schools():
        tasklog = CeleryTasks.objects.create(name="task_scrap_schools")

`schools/views.py`::

    from django.http import HttpResponse
    from .tasks import task_scrap_schools 
    def scrap_schools(request):
        task_scrap_schools.delay()
        return HttpResponse('<a href="/">back</a> Task Added Success')

add broker url in `settings.py`::

    ...
    CELERY_BROKER_URL = 'redis://localhost/0'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC'



run celery::

    celery -A mysite worker -l INFO



### Daemonization here is a nice tutorial

add celery to supervisor::

    $ apt-get install supervisor

Then, add `/etc/supervisor/conf.d/celery_proj_worker.conf` file:

    [program:projworker]
    command=/var/www/djangoceleryscrapper/env/bin/celery -A mysite worker -l info
    directory=/var/www/djangoceleryscrapper

update it:

    $ supervisorctl reread
    $ supervisorctl update
    $ supervisorctl start projworker

now when anychanges in `tasks.py` you need to restart supervisor:

    $ supervisorctl restart projworker

    
checkout log in: `$ /var/log/supervisor`