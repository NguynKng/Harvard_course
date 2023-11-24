from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger
import json
# Create your views here.

def home(request):
    return HttpResponse("Welcome to our website!")

def index(request):
    # load dữ liệu từ database, sau đó bind vào html template rồi render ra 
    return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })

def index1(request):
    f = open('flights/data.json')
    data = json.load(f)
    return render(request,"flights/index1.html",{
        "data": data
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        "flight": flight,
        "passengers": flight.passenger.all(),
        "non_passenger": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight_id)))