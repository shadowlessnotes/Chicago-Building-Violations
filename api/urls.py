from django.urls import path
from . import views

urlpatterns = [
    path('property/scofflaws/violations/', views.get_scofflaw_violations),
    path('property/<str:address>/', views.get_data),
    path('property/<str:address>/comments/', views.add_comment)
]