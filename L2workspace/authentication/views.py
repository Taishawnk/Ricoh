from django.shortcuts import render
from django.contrib.auth import login , logout, authenticate


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    return render(request, 'authenticate/login.html', {})
# Create your views here.
