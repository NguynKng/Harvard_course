from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello Khang! Welcome back.")

def form(request):
    return render(request, "hello/index.html")