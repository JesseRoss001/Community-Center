# community urls 
from django.urls import path 
from django.urls import include
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('events/',views.events,name ='events'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('booking/',views.booking,name='booking'),
]