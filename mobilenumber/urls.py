from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="Search"),
    path('reportnumber/', views.reportnumber, name="reportnumber"),
    path('allnumbers/', views.allnumbers, name="reportnumber"),
    
]