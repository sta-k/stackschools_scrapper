from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

import schools

from .tasks import task_scrap_schools 
from .models import School, CeleryTasks
from .helpers import html_to_json


class HomeView(View):
    template_name = 'schools/home.html'
    def get(self, request):
        schools = School.objects.order_by('-id')[:10]
        last_task = CeleryTasks.objects.order_by('-started').first()
        return render(request,self.template_name,{'schools':schools,'task':last_task})

    def post(self, request):
        messages.success(request, 'Task Added Successfully!')
        print(int(request.POST['number_of_items']))
        task_scrap_schools.delay(int(request.POST['number_of_items'])) # first 21 items
        return redirect('schools:home')
        

def show_school(request,code):
    school= School.objects.get(code=code)
    if not school.html.startswith('<ul>'):
        return render(request,'schools/show.html',{'school':school})
    context = html_to_json(school.html)
    return render(request,'schools/show_new.html',context)
