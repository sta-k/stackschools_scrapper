from celery import shared_task
import requests
from django.utils import timezone
from django.db.models import Max
from schools.models import School, CeleryTasks


@shared_task
def task_scrap_schools(limit=5000000):
    tasklog = CeleryTasks.objects.create(name="task_scrap_schools", started= timezone.now())
    get_text = lambda code: requests.post('https://src.udiseplus.gov.in/searchSchool/getSchoolDetail', data={'schoolIdforDashSearch': code})
    start = School.objects.aggregate(c=Max('code'))['c'] or 1000001
    for sid in range(start,start+limit):
        # if School.objects.filter(code = sid): 
        #     # if school data already exists then skip
        #     continue

        r = get_text(sid)
        if r.text:
            # if some text in response create school
            School.objects.create(code = sid,html = r.text)
    tasklog.finished = timezone.now()
    tasklog.save()