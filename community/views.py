from django.shortcuts import render
from .forms import GovernmentOfficialForm, InstructorForm, GeneralPublicForm ,EventForm
from .models import UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR, GENERAL_PUBLIC , Event
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect

# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    return render(request, 'community/home.html')

def events(request):
    return render(request, 'community/events.html')

def about(request):
    return render(request,'community/about.html')

def login(request):
    return render(request,'community/login.html')

def gallery(request):
    return render(request, 'community/gallery.html')

def booking(request):
    return render(request, 'community/booking.html')

def register_government(request):
    if request.method == 'POST':
        form = GovernmentOfficialForm(request.POST)
        if form.is_valid():
            user = form.save()
            badge_number = form.cleaned_data['badge_number']
            UserProfile.objects.create(user=user , role=GOVERNMENT_OFFICIAL, badge_number= badge_number)
            auth_login(request,user)
            return redirect('home')
    else: 
        form = GovernmentOfficialForm()
    return render(request,'community/register_government.html', {'form':form})

def register_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            user = form.save()
            card_number = form.cleaned_data['card_number']
            UserProfile.objects.create(user=user , role=INSTRUCTOR, card_number=card_number)
            auth_login(request,user)
            return redirect('home')
    else: 
        form = InstructorForm()
    return render(request,'community/register_instructor.html', {'form':form})

def general_public(request):
    if request.method == 'POST':
        form = GeneralPublicForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user,role=GENERAL_PUBLIC)
            auth_login(request,user)
            return redirect('home')
    else:
       form =GeneralPublicForm()
    return render(request,'community/register_public.html',{'form':form})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', event_id = event.id )
    else:
        form = EventForm()
    
    return render(request , 'events/create_event.html',{'form':form})
    