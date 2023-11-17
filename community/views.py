from django.shortcuts import render, get_object_or_404
from .forms import GovernmentOfficialForm, InstructorForm, GeneralPublicForm ,EventForm
from .models import UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR, GENERAL_PUBLIC , Event , Booking , TIME_SLOTS
from django.contrib.auth import login as auth_login
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden
import logging 
from django.utils import timezone
from django.utils.dateparse import parse_date
from decimal import Decimal

# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    created_events = None 
    if request.user.is_authenticated:
        created_events = Event.objects.filter(author=request.user.profile)
    return render(request, 'community/home.html', {'created_events':created_events})


def events(request):
    return render(request, 'community/events.html')

def about(request):
    total_users=User.objects.count()
    total_bookings=Booking.objects.count()

    context = {
        'total_users':total_users,
        'total_bookings':total_bookings,
    }
    return render(request,'community/about.html',context)


# gallery view 
def gallery(request):
    events_with_images = Event.objects.exclude(image='').order_by('-date')
    return render(request, 'community/gallery.html', {'events_with_images': events_with_images})


# booking view 
def booking(request):
    start_date= timezone.now().date()
    end_date = start_date + timedelta(days=13)
    all_events = Event.objects.filter(date__range=[start_date,end_date])

    
    schedule = {}
    for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days +1)):
        day_events = all_events.filter(date=single_date)
        day_schedule={slot[0]:None for slot in TIME_SLOTS}
        for event in day_events:
            day_schedule[event.start_time] = event
        schedule[single_date] = day_schedule

    return render(request, 'community/booking.html',{'schedule':schedule, 'time_slots':TIME_SLOTS})


   


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

# Creating +update the event view


logger = logging.getLogger(__name__)
@login_required
def create_or_update_event(request,event_id=None):
     
    user_profile = request.user.profile
    three_months_ahead = timezone.now().date() + timedelta(days=90)
    instance = None 
    if event_id:
        instance = Event.objects.get(id=event_id)
    # Only government officials and instructors can create events  
    if user_profile.role not in [INSTRUCTOR,GOVERNMENT_OFFICIAL]:
        messages.error(request, "You are not authorised to create events or update them ")
        return redirect('home')
       
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES, instance =instance)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = user_profile
            # events can only be booked 3 months in advance
            if event.date > three_months_ahead or event.date < timezone.now().date():
                message.error(request,'Event date must be within 3 months and not in the past ')
                return render (request, 'community/events/create_update_event.html',{'form':form})

            critical_profiles = UserProfile.objects.filter(
                role__in =[INSTRUCTOR, GOVERNMENT_OFFICIAL]
            )
            #Ensures events are unique and not double booked 
            overlapping_events = Event.objects.filter(
                author__in = critical_profiles,
                date = event.date ,
                start_time =event.start_time  
            ).exclude(id=event.id)

            if overlapping_events.exists():
                message.error(request, 'This time slot is already booked ')
                return render (request, 'community/events/create_update_event.html',{'form':form})
            # instructors are charged 200 to create an event however they are allowed a negative balance up to a point to book an event 
            if not event_id and user_profile.role == INSTRUCTOR:
                if user_profile.balance >= -400:
                    user_profile.balnace -=200
                    user_profile.save 

                else:
                    messages.error(request, "Insufficient fund balance to book an event ")
                    (request, 'community/events/create_update_event.html',{'form':form})
            
            elif not event_id and user.profile.role == GOVERNMENT_OFFICIAL:
                user_profile.balance = 0
                user_profile.save 

            event.save()
            user_profile.created_events.add(event)
            messages.success(request,'Event created successfully ')
            return redirect('home')

        else:
            messages.error(request,'Invalid form submission ')    
    else:
        form = EventForm(instance=instance)
    return render(request,'community/events/create_update_event.html',{'form': form})
# Delete event
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id , author=request.user.profile)
    if request.method == 'POST':
        event.delete()
        messages.success(request, ' Event deleted successfully ')
        return redirect('home')
    return render(request, 'community/events/confirm_delete.html')            

def event_detail(request,event_id):
    event = get_object_or_404 (Event,pk = event_id)
    return render(request,'community/events/event_detail.html',{'event':event})
# Image Deletion from gallery 
@login_required
def delete_event_image(request,event_id):
    event =get_object_or_404(Event,pk=event_id , author=request.user.profile)

    if request.user != event.author.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
     event.image.delete()
     event.save()
     messages.success(request,'image deleted')
     return redirect('gallery')
    return render(request,'community/events/delete_event_image.html', {'event': event})

# Users purchasing events 
@login_required
def join_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user_profile = request.user.profile
    #ensuring venue is not overfilled 
    if request.method == 'POST':
        if event.capacity > 0:
            event.capacity -= 1
            event.save()
            # balance transfer
            if event.author.role != GOVERNMENT_OFFICIAL:
                instructor_profile = event.author
                instructor_profile.balance += Decimal('7.00')
                instructor_profile.save()
                user_profile.balance -= Decimal('7.00')
                user_profile.save()
            messages.success(request, "You have successfully joined the event ")
            return redirect('home')
        else:
            messages.error(request, "Event is full ")
    return render(request, 'community/join_event.html', {'event': event})
