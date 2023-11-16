from django.shortcuts import render, get_object_or_404
from .forms import GovernmentOfficialForm, InstructorForm, GeneralPublicForm ,EventForm
from .models import UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR, GENERAL_PUBLIC , Event
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    user_profile = request.user.profile if request.user.is_authenticated else None

    if user_profile and user_profile.created_events.exists():
        created_events = user_profile.created_events.all()
        return render(request, 'community/home.html',{'created_events': created_events})
    else:
        return render(request, 'community/home.html')

def events(request):
    return render(request, 'community/events.html')

def about(request):
    total_users=User.objects.count()
    total_bookings=Booking.objects.count()

    context = {
        'total_users':total_users,
        'total_bookings':total_bookings,
    }
    return render(request,'community/about.html')



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

# Creating the event view
@login_required
def create_event(request):
    user_profile = request.user.profile
    two_months_ahead = datetime.now() + timedelta(days=90)


    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid() and user_profile.role in [INSTRUCTOR,GOVERNMENT_OFFICIAL]:
            event = form.save(commit=False)
            event.author = user_profile
            event.save()
            user_profile.created_events.add(event)
            return redirect('home' )
    else:
        form = EventForm()
    
    return render(request , 'community/events/create_event.html',{'form':form})

def event_detail(request,event_id):
    event = get_object_or_404 (Event,pk = event_id)
    return render(request,'community/events/event_detail.html',{'event':event})
