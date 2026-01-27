from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request, "home.html", {"records" : records})

def login_user(request):
    pass

def logout_user(request):
    pass