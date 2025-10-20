from django.urls import path
from . import views

urlpatterns = [
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('farmers/add/', views.add_farmer, name='add_farmer'),
]
