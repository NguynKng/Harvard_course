from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home, name="home"),
    path("info/",views.index, name="index"),
]