from django.shortcuts import render, get_object_or_404
from .forms import GovernmentOfficialForm, InstructorForm, GeneralPublicForm ,EventForm , EventUpdateForm
from .models import UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR, GENERAL_PUBLIC , Event , Booking , TIME_SLOTS , BalanceChange
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
from django.db import transaction
from django.core.paginator import Paginator
import json
import logging
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    context = {
    'created_events' : None,
    'joined_events' : None,
    'balance_transactions' : None,
    'transaction_dates':'[]',
    'transaction_amounts':'[]',
    'user_balance':0,
    'event_titles': '[]',  
    'booking_counts': '[]'  

    }
    if request.user.is_authenticated:
        created_events = Event.objects.filter(author=request.user.profile)
        joined_bookings = Booking.objects.filter(user_profile=request.user.profile)
        joined_events = [booking.event for booking in joined_bookings]
        balance_transactions = BalanceChange.objects.filter(
            user_profile=request.user.profile 
        ).order_by('-change_date')
        transaction_dates =[transaction.change_date.strftime("%Y-%m-%d") for transaction in balance_transactions]
        transaction_amounts =[float(transaction.change_amount) for transaction in balance_transactions]
        user_events = Event.objects.filter(author=request.user.profile).annotate(
            total_bookings=Count('booking')
        )
        event_titles = [event.title for event in user_events]
        booking_counts = [event.total_bookings for event in user_events]
        context['created_events'] = created_events
        context['joined_events'] = joined_events
        context['balance_transactions'] = balance_transactions
        context['transaction_dates'] = json.dumps(transaction_dates)
        context['transaction_amounts'] = json.dumps(transaction_amounts)
        context.update({
            'event_titles': json.dumps(event_titles),
            'booking_counts': json.dumps(booking_counts)
        })
        context['user_balance'] = request.user.profile.balance

    if request.user.is_authenticated:
        user_events = Event.objects.filter(author=request.user.profile)
        event_participation_data = user_events.annotate(
            total_participants=Count('booking')
        ).values('title', 'total_participants')

        event_titles = [event['title'] for event in event_participation_data]
        participation_counts = [event['total_participants'] for event in event_participation_data]

        context.update({
            'event_titles': json.dumps(event_titles),
            'participation_counts': json.dumps(participation_counts)
        })

    return render(request, 'community/home.html', context)

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
    total_days = 90
    days_per_page = 14
    #start and end dates for the whole period
    start_date= timezone.now().date()
    date_list = [start_date +timedelta(days=x) for x in range(total_days)]
    



    # Paginating the events 
    paginator = Paginator(date_list, days_per_page)
    page_number = request.GET.get('page', 1) 
    page_obj = paginator.get_page(page_number)
    schedule = {}
    for single_date in page_obj:
        day_schedule ={slot[0]: {'events': [] ,'available':True} for slot in TIME_SLOTS}
        events_on_date =Event.objects.filter(date=single_date)
        for event in events_on_date:
            day_schedule[event.time]['events'].append(event)
            day_schedule[event.time]['available'] = False
        schedule[single_date] = day_schedule
    
       
    user_bookings = []
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user_profile=request.user.profile).values_list('event_id',flat=True)


    return render(request, 'community/booking.html',{'schedule':schedule,'page_obj':page_obj , 'user_bookings': user_bookings})


   


def register_government(request):
    if request.method == 'POST':
        form = GovernmentOfficialForm(request.POST)
        if form.is_valid():
            user = form.save()
            badge_number = form.cleaned_data.get('badge_number')
            UserProfile.objects.create(user=user, role=GOVERNMENT_OFFICIAL, badge_number=badge_number)
            auth_login(request, user)
            return redirect('home')
    else:
        form = GovernmentOfficialForm()
    return render(request, 'community/register_government.html', {'form':form})

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
def create_event(request, event_id=None):
    user_profile = request.user.profile
    three_months_ahead = timezone.now().date() + timedelta(days=90)
    instance = None

    if event_id:
        instance = Event.objects.get(id=event_id)

    if user_profile.role not in [INSTRUCTOR, GOVERNMENT_OFFICIAL]:
        messages.error(request, "You are not authorised to create events or update them.")
        return redirect('home')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = user_profile

            if event.date > three_months_ahead or event.date < timezone.now().date():
                messages.error(request, 'Event date must be within 3 months and not in the past.')
                return render(request, 'community/events/create_event.html', {'form': form})

            critical_profiles = UserProfile.objects.filter(role__in=[INSTRUCTOR, GOVERNMENT_OFFICIAL])
            overlapping_events = Event.objects.filter(author__in=critical_profiles, date=event.date, time=event.time).exclude(id=event.id)

            if overlapping_events.exists():
                messages.error(request, 'This time slot is already booked.')
                return render(request, 'community/events/create_event.html', {'form': form})

            # Save the event before creating BalanceChange
            event.save()

            if not event_id and user_profile.role == INSTRUCTOR:
                if user_profile.balance >= -400:
                    user_profile.balance -= 200
                    user_profile.save()
                    BalanceChange.objects.create(
                        user_profile=user_profile,
                        event=event,
                        change_amount=-200,
                        transaction_type="Event Creation Fee"
                    )
                else:
                    messages.error(request, "Insufficient fund balance to book an event.")
                    return render(request, 'community/events/create_event.html', {'form': form})

            elif not event_id and user_profile.role == GOVERNMENT_OFFICIAL:
                user_profile.balance = 0
                user_profile.save()

            user_profile.created_events.add(event)
            messages.success(request, 'Event created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = EventForm()

    return render(request, 'community/events/create_event.html', {'form': form})
#update event 
@login_required
def update_event(request, event_id):
    user_profile = request.user.profile
    event = get_object_or_404(Event, id=event_id, author=user_profile)

    if user_profile.role not in [INSTRUCTOR, GOVERNMENT_OFFICIAL]:
        messages.error(request, "You are not authorised to update this event.")
        return redirect('home')
    if event.author != request.user.profile:
        return HttpResponseForbidden("You are not authorized to update this event.")

    if request.method == 'POST':
        form = EventUpdateForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()

            # BalanceChange logic removed for brevity.

            messages.success(request, 'Event updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = EventUpdateForm(instance=event)

    return render(request, 'community/events/update_event.html', {'form': form, 'event_id': event_id})

# Delete event
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id , author=request.user.profile)
    if event.author != request.user.profile:
        return HttpResponseForbidden("You are not authorized to delete this event.")
    
    if request.method == 'POST':
        with transaction.atomic():
            if event.author.role == INSTRUCTOR:
                event.author.balance += 200
                event.author.save()
                BalanceChange.objects.create(
                    user_profile=event.author,
                    change_amount=200,
                    transaction_type="Event Deletion Refund"
                )
            elif event.author.role == GOVERNMENT_OFFICIAL:
                pass
        event.delete()
        messages.success(request, ' Event deleted successfully ')
        return redirect('home')
    

    
    return render(request, 'community/events/confirm_delete.html',{'event': event})            

def event_detail(request,event_id):
    event = get_object_or_404 (Event,pk = event_id)
    return render(request,'community/events/event_detail.html',{'event':event})
# Image Deletion from gallery 
@login_required
def delete_event_image(request,event_id):
    event =get_object_or_404(Event,pk=event_id , author=request.user.profile)

    if event.author != request.user.profile:
        return HttpResponseForbidden("You are not authorized to delete this event.")

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
    if user_profile.role == GENERAL_PUBLIC and user_profile.balance < Decimal('28.00'):
        messages.error(request, "Your balance is too low to join this event.")
        return redirect('event_detail', event_id=event_id)
    if user_profile.role in [INSTRUCTOR,GOVERNMENT_OFFICIAL]:
        messages.error(request,'Instructors and officials are not allowed to join booking classes')
    existing_booking=Booking.objects.filter(event=event,user_profile=user_profile).exists()

    if existing_booking:
        messages.info(request,"You have already joined this event.")
    #ensuring venue is not overfilled 
    if request.method == 'POST':
        if event.capacity > 0:
            event.capacity -= 1
            event.save()
            # balance transfer
            if event.author.role != GOVERNMENT_OFFICIAL:
                event.author.balance += Decimal('7.00')
                event.author.save()
                BalanceChange.objects.create(
                    user_profile=event.author,
                    event=event,
                    change_amount=Decimal('7.00'),
                    transaction_type="Event Joining Fee Recieved"
                )
            request.user.profile.balance -= Decimal('7.00')
            request.user.profile.save()
            BalanceChange.objects.create(
                user_profile=request.user.profile,
                event=event,
                change_amount=Decimal('7.00'),
                transaction_type='Event Joing Fee Paid'
            )
        else:
            messages.error(request, "Event is full ")
        Booking.objects.create(event=event,user_profile=user_profile)
        messages.success(request, "You have successfully joined the event ")
        return redirect('home')
    return render(request, 'community/join_event.html', {'event': event})

