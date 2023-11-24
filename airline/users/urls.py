from django.urls import path
from . import views

urlpatterns = [
    path("",views.user_data,name="user_data"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
]