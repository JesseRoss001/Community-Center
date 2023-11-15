# community urls 
from django.urls import path 
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home , name='home'),
    path('events/',views.events,name ='events'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('booking/',views.booking,name='booking'),
    #django template login logout 
    path('login/', auth_views.LoginView.as_view(template_name='community/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register_public/', views.general_public, name='register_public'),
    path('register_instructor/', views.register_instructor, name='register_instructor'),
    path('register_government/', views.register_government, name='register_government'),
    path('create_event/', views.create_event, name="create_event")
]