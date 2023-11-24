from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home, name="home"),
    path("index/",views.index, name="index"),
    path("index1/",views.index1, name="index1"),
    path("<int:flight_id>/",views.flight, name="flight"),
    path("<int:flight_id>/book",views.book, name="book")
]