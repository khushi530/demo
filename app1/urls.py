
from django.urls import path
from .views import *
urlpatterns = [
  
    path('',nav ),
    path('login/',login),
    path('data/',data),
    path('about/',about),
]
