from django.shortcuts import render
from django.http import HttpResponse
import requests
from .tasks import task_scrap_schools 
from .models import School

# Create your views here.
def home(request):
    return render(request,'schools/home.html',{'schools':School.objects.all()})

def show_school(request,code):
    return render(request,'schools/show.html',{'school':School.objects.get(code=code)})

def scrap_schools(request):
    task_scrap_schools.delay(21) # first 21 items

    return HttpResponse('<a href="/">back</a> Task Added Success')