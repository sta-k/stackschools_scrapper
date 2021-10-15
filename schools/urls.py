from django.urls import include, path
from schools import views
app_name='schools'

urlpatterns = [
	path('scrap_schools/', views.scrap_schools, name='scrap'),
    path('<int:code>/', views.show_school, name='show'),
    path('', views.home, name='home'),
]