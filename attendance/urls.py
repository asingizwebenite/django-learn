from django.urls import path
from . import views

urlpatterns = [
    path('farmers/', views.mark_attendance, name='farmer_list'),
    path('farmers/attendance', views.mark_attendance, name='mark_attendance'),
    path('farmers/add/', views.add_farmer, name='add_farmer'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('farmers/json', views.farmer_list, name='farmer_list_json'),

]
