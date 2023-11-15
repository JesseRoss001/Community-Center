from django.shortcuts import render
# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    return render(request, 'community/home.html')

def events(request):
    return render(request, 'community/events.html')

def about(request):
    return render(request,'community/about.html')

def about(request):
    return render(request,'community/login.html')

def gallery(request):
    return render(request, 'community/gallery.html')

def booking(request):
    return render(request, 'community/booking.html')


