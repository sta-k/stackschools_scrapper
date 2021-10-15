from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import School

# Create your views here.
def home(request):
    return render(request,'schools/home.html',{'schools':School.objects.all()})

def show_school(request,code):
    return render(request,'schools/show.html',{'school':School.objects.get(code=code)})

def scrap_schools(request):
    get_text = lambda code: requests.post('https://src.udiseplus.gov.in/searchSchool/getSchoolDetail', data={'schoolIdforDashSearch': code})
    # for i in range(1,10):
    #     t = get_text(1000000*i+1)
    #     if t.text:print(1000000*i)
    # return HttpResponse('success')
    
    for sid in range(1000001,6000000):
        if School.objects.filter(code = sid): 
            # if school date already exists then skip
            continue

        r = get_text(sid)
        if r.text:
            # if some text in response create school
            School.objects.create(code = sid,html = r.text)
    return HttpResponse('<a href="/">back</a> Success')