from django.urls import path
from . import views

urlpatterns = [

    path('',views.loginfnc,name="login"),
    path('logout/',views.logoutfnc,name="logout")

]