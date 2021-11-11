from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

import schools

from .tasks import task_scrap_schools, error_handler
from .models import School, CeleryTasks, School2 #, Village
from .helpers import html_to_json


class HomeView(View):
    template_name = 'schools/home.html'
    def get(self, request):
        schools = School.objects.order_by('-id')[:5]
        last_task = CeleryTasks.objects.order_by('-started').first()
        
        return render(request,self.template_name,{'schools':schools,'task':last_task})

    def post(self, request):
        messages.success(request, 'Task Added Successfully!')
        n_items = int(request.POST['number_of_items'])
        print(n_items)
        # Celery provides two function call options, delay() and apply_async(), to invoke Celery tasks.
        # task_scrap_schools.delay(n_items) # first 21 items
        task_scrap_schools.apply_async(link_error=error_handler.s(), args=(n_items,))
        return redirect('schools:home')
"""
def todel():
    # block: 1134 cluster: 9638 name: 47462
    items= []
    
    for i,school in enumerate(School.objects.exclude(html__exact='').exclude(html='error')):
        if i%2000==0:print(i)
        try:
            data = html_to_json(school.html)
        except:
            print(school.code)
            continue
        p=data['school_profile']
        Village.objects.get_or_create(state=p['state'],district=p['district'],block=p['block'],cluster=p['cluster'],name=i)
        # if Village.objects.filter(state=p['state'],district=p['district'],block=p['block'],cluster=p['cluster'],name=p['village']):
        #     continue
        items.append(Village(state=p['state'],district=p['district'],block=p['block'],cluster=p['cluster'],name=p['village']))

        if i>2000:
            return 0

    print('finished. going to bulk create')
    for i in range(10):
        print(10000*i, 10000*(i+1))
        Village.objects.bulk_create(items[10000*i:10000*(i+1)])
    print(100000)
    Village.objects.bulk_create(items[100000:])
""" 
    
def save_to_schools2(request):
    # todel()
    # messages.success(request, 'Villages synced Successfully!')
    # return redirect('schools:home')

    items= []
    for school in School.objects.exclude(html__exact='').exclude(html='error'):
        try:
            data = html_to_json(school.html)
        except:
            print(school.code)
            continue
        s = School2(**dict(data['school_profile'],**data['address'], **data['basic_details'],**data['facilities'],**data['room_details']))
        s.enrolment_of_the_students = ','.join(data['enrolment_of_the_students'])
        s.total_teachers = data['total_teachers']
        s.code = school.code
        # s.address = Address.objects.get_or_create(**data['address'])[0]
        items.append(s)
    print('finished. going to bulk create')
    for i in range(10):
        print(10000*i, 10000*(i+1))
        School2.objects.bulk_create(items[10000*i:10000*(i+1)])
    print(100000)
    School2.objects.bulk_create(items[100000:])
    messages.success(request, 'Schools2 synced Successfully!')
    return redirect('schools:home')

def show_school(request,code):
    school= School.objects.get(code=code)
    if not school.html.startswith('<ul>'):
        return render(request,'schools/show.html',{'school':school})
    data = html_to_json(school.html)
    
    return render(request,'schools/show_new.html',data)
