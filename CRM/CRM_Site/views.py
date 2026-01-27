from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request, "home.html", {"records" : records})

def login_user(request):
    pass

def logout_user(request):
    pass

def customer_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "customer_record.html", {"record" : record})
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        customer.delete()
        messages.success(request, "{customer.first_name} deleted")
        return redirect("home")
    else:
        messages.success(request, "Only admin can access this")
        return redirect("home")

def add_customer(request):
    form = AddRecordForm()
    return render(request, "add_customer.html", {"form" : form})

def update_customer():
    pass