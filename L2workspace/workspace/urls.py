from django.urls import path
from . import views #importing the views file from this directory

urlpatterns = [
    path('', views.index, name='index'),
]
