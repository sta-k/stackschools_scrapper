from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

import schools

from .tasks import task_scrap_schools 
from .models import School, CeleryTasks
from schools import tasks


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
    
    context = {
        'code': school.code,
        'html':school.html,
        'school_profile':{
            'school_name':'Hamidia Public School Rampore',
            'udise_code':'01020503406',
            'state':'Jammu & Kashmir',
            'district':'BARAMULA',
            'block':'dangerpora',
            'cluster':'c1_bms_watlab',
            'village':'rampora',
            'pincode':'193201',
            'school_category':'1-primary',
            'school_type':'3-co-educational',
            'class_from':'1',
            'class_to':'5',
            'state_management':'5-private_unaided_(recognized)',
            'national_management':'5-private_unaided_(recognized)',
            'status':'0-operational',
            'location':'1-rural',
        },
        'basic_details': {
            'aff_board_sec':'',
            'aff_board_hsec':'',
            'year_of_establishment':'2015',
            'pre_primary':'1-Yes'
        },
        'facilities': {
            'building_status':'1-private',
            'boundary_wall':'6-others',
            'no_of_boys_toilets':'1',
            'no_of_girls_toilets':'0',
            'no_of_cwsn_toilets':'0',
            'drinking_water_availability':'yes',
            'hand_wash_facility':'yes',
            'functional_generator':'0',
            'library':'1-yes',
            'reading_corner':'1-yes',
            'book_bank':'1-yes',
            'functional_laptop':'1',
            'functional_desktop':'0',
            'functional_tablet':'0',
            'functional_scanner':'0',
            'functional_printer':'0',
            'functional_led':'0',
            'functional_digiboard':'0',
            'internet':'2-no',
            'dth':'2-no',
            'functional_web_cam':'0',
        },
        'room_details':{
            'class_rooms':'8',
            'other_rooms':'1'
        },
        'enrolment_of_the_students':['37','12','37','12','37','12','37','12','37','12','37','12','last'],
        'total_teachers':'4'
    }
    return render(request,'schools/show_new.html',context)
