from celery import shared_task
import requests
from requests.exceptions import ConnectionError
from django.utils import timezone
from django.db.models import Max
from schools.models import School, CeleryTasks
from bs4 import BeautifulSoup

@shared_task
def task_scrap_schools(limit=5000000):
    errors={}
    tasklog = CeleryTasks.objects.create(name="task_scrap_schools", started= timezone.now())
    get_text = lambda code: requests.post('https://src.udiseplus.gov.in/searchSchool/getSchoolDetail', data={'schoolIdforDashSearch': code})
    start = School.objects.aggregate(c=Max('code'))['c'] or 1000000
    for sid in range(start+1,start+limit):
        # if School.objects.filter(code = sid): 
        #     # if school data already exists then skip
        #     continue
        try:
            r = get_text(sid)
        except ConnectionError:
            if sid in errors:
                # if tried this once
                tasklog.name=f'error: {sid}'
                break
                
            else:
                r = get_text(sid)
                errors[sid]='error'

        
        if r.text:
            # if some text in response create school
            soup = BeautifulSoup(r.text, 'html.parser')
            resp = '<ul>'
            for item in soup.find_all("span", "pFont14"):
                resp+=f'<li>{item.get_text()}</li>'
            resp+=f'<li>{soup.find_all("table", "mt-3")[0].get_text()}</li>'
            resp+='</ul>'
            School.objects.create(code = sid,html = resp)
        else:
            School.objects.create(code = sid,html = 'no data')
    tasklog.finished = timezone.now()
    tasklog.save()