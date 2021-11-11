from django.urls import path
from schools import views
app_name='schools'

urlpatterns = [
	# path('scrap_schools/', views.scrap_schools, name='scrap'),
    path('<int:code>/', views.show_school, name='show'),
    path('', views.HomeView.as_view(), name='home'),
    path('sync_school2/', views.save_to_schools2, name='sync_school2'),
]