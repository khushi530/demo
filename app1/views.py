from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data(request):
    return HttpResponse("this is my first page")

def nav(request):
    return render(request,'nav.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')