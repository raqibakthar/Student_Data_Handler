from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('details/<int:id>/',views.details,name='details'),
    path('search/',views.search,name='search'),
    path('edit/<int:id>/',views.edit,name='edit'),
    
]
