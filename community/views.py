# Standard library imports
from collections import defaultdict
from datetime import datetime, timedelta
from decimal import Decimal
from itertools import accumulate
import json
import logging
# Related third party imports
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Avg, Count, Sum, Case, When, IntegerField, Q
from django.db.models.functions import Coalesce
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseForbidden,Http404 ,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date
# Local application/library specific imports
from .forms import (GovernmentOfficialForm, InstructorForm, GeneralPublicForm, StaffForm,
                    EventForm, EventUpdateForm, RatingForm, CreditIssueForm , EventSearchForm)
from .models import (UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR, GENERAL_PUBLIC, STAFF, Event,
                     Booking, TIME_SLOTS, BalanceChange, Rating, Like)
# Create your views here.
#Creating views for home , events , about , gallery and booking pages 
def home(request):
    """
    The view function for the home page of the community.
    Fetches and displays created and joined events, user balance transactions, and other relevant data for authenticated users.
    """
    context = {}  # Define context dictionary if not already defined

    if request.user.is_authenticated:
        # Fetch events created and joined by the user
        created_events = Event.objects.filter(author=request.user.profile, date__gte=timezone.now().date())
        joined_bookings = Booking.objects.filter(user_profile=request.user.profile, event__date__gte=timezone.now().date())
        joined_events = [booking.event for booking in joined_bookings]
        # Fetch balance transactions for the user
        balance_transactions = BalanceChange.objects.filter(
            user_profile=request.user.profile
        ).order_by('-change_date')
        transaction_dates = [transaction.change_date.strftime("%Y-%m-%d") for transaction in balance_transactions]
        transaction_amounts = [float(transaction.change_amount) for transaction in balance_transactions]
        # Fetch the created events with booking counts
        user_events_with_booking_counts = created_events.annotate(
            total_bookings=Count('booking')
        )
        event_titles = [event.title for event in user_events_with_booking_counts]
        booking_counts = [event.total_bookings for event in user_events_with_booking_counts]
        # Update context
        context.update({
            'created_events': created_events,
            'joined_events': joined_events,
            'balance_transactions': balance_transactions,
            'transaction_dates': json.dumps(transaction_dates),
            'transaction_amounts': json.dumps(transaction_amounts),
            'user_balance': request.user.profile.balance,
            'event_titles': json.dumps(event_titles),
            'booking_counts': json.dumps(booking_counts)
        })
        if request.user.profile.role == STAFF:
            public_users = UserProfile.objects.filter(role=GENERAL_PUBLIC).order_by('balance')
            context['public_users'] = public_users
        else:
            context['public_users'] = None
  

    return render(request, 'community/home.html', context)
def events(request):
    """
    The view function for displaying events.
    """
    return render(request, 'community/events.html')
def about(request):
    """
    The view function for the about page.
    Displays statistics like total number of users and bookings.
    """
    total_users=User.objects.count()
    total_bookings=Booking.objects.count()
    context = {
        'total_users':total_users,
        'total_bookings':total_bookings,
    }
    return render(request,'community/about.html',context)
# gallery view 
def gallery(request):
    """
    The view function for the gallery page.
    Displays events with images, ordered by date in descending order.
    """
    events_with_images = Event.objects.exclude(image='').order_by('-date')
    return render(request, 'community/gallery.html', {'events_with_images': events_with_images})
# booking view 
def booking(request):
    """
    The view function for handling event bookings.
    Displays a paginated schedule of events and handles user bookings.
    """
    total_days = 90
    days_per_page = 14
    # start and end dates for the whole period
    start_date = timezone.now().date()
    date_list = [start_date + timedelta(days=x) for x in range(total_days)]
    
    # Paginating the events 
    paginator = Paginator(date_list, days_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    schedule = {}
    for single_date in page_obj:
        day_schedule = {slot[0]: {'events': [], 'available': True} for slot in TIME_SLOTS}
        events_on_date = Event.objects.filter(date=single_date)
        for event in events_on_date:
            day_schedule[event.time]['events'].append(event)
            day_schedule[event.time]['available'] = False
        schedule[single_date] = day_schedule
    
    user_bookings = []
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user_profile=request.user.profile).values_list('event_id', flat=True)
    rating_form = RatingForm()
    context = {
        'schedule': schedule,
        'page_obj': page_obj,
        'user_bookings': user_bookings,
        'rating_form': rating_form,  
    }
    return render(request, 'community/booking.html', context) 
def register_staff(request):
    """
    The view function for registering a new staff member.
    Handles the submission of the StaffForm and user creation.
    """
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            user = form.save()
            staff_id = form.cleaned_data.get('staff_id')
            UserProfile.objects.create(user=user, role=STAFF, staff_id=staff_id)
            auth_login(request, user)
            return redirect('home')
    else:
        form = StaffForm()
    return render(request, 'community/register_staff.html',{'form':form})
def register_government(request):
    """
    The view function for registering a new government official.
    Handles the submission of the GovernmentOfficialForm and user creation.
    """
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
    """
    The view function for registering a new instructor.
    Handles the submission of the InstructorForm and user creation.
    """
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
    """
    The view function for registering a new general public user.
    Handles the submission of the GeneralPublicForm and user creation.
    """
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
    """
    The view function for creating or updating an event.
    Handles form submission for event creation and updates, with validation for event dates and capacity.
    """
    user_profile = request.user.profile
    three_months_ahead = timezone.now().date() + timedelta(days=90)
    instance = get_object_or_404(Event, id=event_id) if event_id else None
    if user_profile.role not in [INSTRUCTOR, GOVERNMENT_OFFICIAL]:
        messages.error(request, "You are not authorised to create events or update them.")
        return redirect('home')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=instance)
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

            event.save()

            if not event_id and user_profile.role == 'INSTRUCTOR':
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

            elif not event_id and user_profile.role == UserProfile.GOVERNMENT_OFFICIAL:
                user_profile.balance = 0
                user_profile.save()

            user_profile.created_events.add(event)
            messages.success(request, 'Event created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = EventForm(instance=instance)

    return render(request, 'community/events/create_event.html', {'form': form})
#update event 
@login_required
def update_event(request, event_id):
    """
    The view function for updating an existing event.
    Handles form submission for updating event details.
    """
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
    """
    The view function for deleting an event.
    Handles the deletion of an event and associated data, ensuring user authorization
    and that no bookings are associated with the event.
    """
    event = get_object_or_404(Event, id=event_id, author=request.user.profile)
    if event.author != request.user.profile:
        return HttpResponseForbidden("You are not authorized to delete this event.")
    if event.has_bookings():
        messages.error(request, "Cannot delete the event as it has bookings.")
        return redirect('event_detail', event_id=event.id)
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
                pass  # Any specific logic for government official can be added here
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('home')
    return render(request, 'community/events/confirm_delete.html', {'event': event})
@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    likes_count = event.like_set.count()

    context = {
        'event': event,
        'likes_count': likes_count,
    }
    if event.author.role == 'INSTRUCTOR':
        context['average_rating'] = event.author.average_rating

    return render(request, 'community/event_detail.html', context)
# Image Deletion from gallery 
@login_required
def delete_event_image(request,event_id):
    """
    The view function for deleting an image associated with an event.
    Handles the deletion of an event's image, ensuring user authorization.
    """
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
    """
    The view function for users to join an event.
    Handles the booking process for an event and updates the user's balance accordingly.
    """
    event = get_object_or_404(Event, id=event_id)
    user_profile = request.user.profile
    if user_profile.role == GENERAL_PUBLIC and user_profile.balance < Decimal('-28.00'):
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
@login_required
def like_event(request, event_id):
    """
    The view function for liking an event.
    Toggles the like status for an event and returns the updated like count and status.
    """
    event = get_object_or_404(Event, id=event_id)
    user_profile = request.user.profile
    # Toggle the like status for the event and user.
    like, created = Like.objects.get_or_create(user=request.user, event=event)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    # Get the updated like count for the event.
    like_count = event.like_set.count()
    # Return the updated like count and like status in the response.
    return JsonResponse({'liked': liked, 'like_count': like_count})
@login_required
def submit_rating(request, instructor_id):
    """
    The view function for submitting a rating for an instructor.
    Handles the submission and validation of the rating form.
    """
    existing_rating = Rating.objects.filter(user=request.user, instructor_id=instructor_id).exists()
    if existing_rating:
        messages.error(request, 'You have already submitted a rating for this instructor.')
        return redirect('booking')
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_instance = form.save(commit=False)
            rating_instance.user = request.user
            instructor_profile = UserProfile.objects.get(pk=instructor_id)
            rating_instance.instructor = instructor_profile
            rating_instance.save()
            instructor = rating_instance.instructor
             # After saving the rating, update the instructor's average rating
            instructor_profile.update_average_rating()
            messages.success(request, 'Thank you for your rating.')
            return redirect('booking')  # Replace 'booking' with the name of your URL pattern for the booking page
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect('booking')  # Replace 'booking' with the name of your URL pattern for the booking page
    else:
        messages.error(request, 'This method is not allowed.')
        return redirect('booking') 
@login_required
def issue_credit(request):
    """
    The view function for issuing credit to a user.
    Handles the credit issuance process, including form submission and balance update.
    """
    # Check if the logged-in user is a staff member
    if request.user.profile.role != 'STAFF':
        messages.error(request, "You are not authorized to issue credits.")
        return redirect('home')
    # Pre-populate the form with the user_id if it's present in the URL
    user_id = request.GET.get('user_id', None)
    initial_data = {'user_id': user_id} if user_id else None
    form = CreditIssueForm(request.POST or None, initial={'user_id': user_id})
    if request.method == 'POST' and form.is_valid():
        user_id = form.cleaned_data['user_id']
        credit_amount = form.cleaned_data['credit_amount']
        try:
            # Use a transaction to ensure atomicity of the balance update
            with transaction.atomic():
                # Lock the user profile row for update and check for the existence
                user_profile = UserProfile.objects.select_for_update().get(user__id=user_id)
                # Update the user's balance
                user_profile.balance += credit_amount
                user_profile.save(update_fields=['balance'])
                # Create a record of this transaction
                BalanceChange.objects.create(
                    user_profile=user_profile,
                    change_amount=credit_amount,
                    transaction_type='CREDIT_ISSUED',
                    staff_member=request.user.profile
                )
                messages.success(request, f"Successfully issued £{credit_amount} credit to {user_profile.user.username}.")
                return redirect('home')
        except UserProfile.DoesNotExist:
            messages.error(request, "User not found.")
        except Exception as e:
            # If any error occurs, show an error message
            messages.error(request, f"An error occurred: {str(e)}")
    # Render the issue credit page with the form
    return render(request, 'community/issue_credit.html', {'form': form, 'user_id': user_id})
def get_cumulative_graph_data(request):
    """
    Fetches and accumulates data for displaying cumulative graphs on events.
    Aggregates data for events created by instructors and government officials.
    """
    instructor_events = Event.objects.filter(
        author__role=INSTRUCTOR
    ).annotate(
        date_only=Cast('date', DateField())
    ).values('date_only').annotate(
        count=Count('id'),
        total=Sum(Case(When(author__role=INSTRUCTOR, then=200), default=0, output_field=IntegerField()))
    ).order_by('date_only')
    # Query events created by government officials
    government_events = Event.objects.filter(
        author__role=GOVERNMENT_OFFICIAL
    ).annotate(
        date_only=Cast('date', DateField())
    ).values('date_only').annotate(
        count=Count('id'),
        total=Sum(Case(When(author__role=GOVERNMENT_OFFICIAL, then=100),
        default=0, output_field=IntegerField()))
    ).order_by('date_only')
    # Combine the queries
    combined_events = instructor_events.union(government_events).order_by('date_only')
    # Accumulate the sums
    instructor_cumulative = list(accumulate(event['total'] for event in instructor_events))
    government_cumulative = list(accumulate(event['total'] for event in government_events))
    combined_cumulative = list(accumulate(event['total'] for event in combined_events))
    # Extract dates
    dates = [event['date_only'].strftime('%Y-%m-%d') for event in combined_events]
    context = {
        'instructor_event_dates': json.dumps(dates),
        'government_event_dates': json.dumps(dates),
        'combined_event_dates': json.dumps(dates),
        'instructor_event_amounts': json.dumps(instructor_cumulative),
        'government_event_amounts': json.dumps(government_cumulative),
        'combined_event_amounts': json.dumps(combined_cumulative),
    }
    return context

@login_required
def search_events(request):
    form = EventSearchForm(request.GET or None)
    events = Event.objects.all()

    if form.is_valid():
        # Filtering logic
        instructor_ranking = form.cleaned_data.get('instructor_ranking')
        likes_order = form.cleaned_data.get('likes_order')
        time_of_day = form.cleaned_data.get('time_of_day')
        day_of_week = form.cleaned_data.get('day_of_week')
        tags = form.cleaned_data.get('tags')

        # Apply filters based on the course type

        # Filter based on instructor ranking, if applicable
        if instructor_ranking is not None:
            events = events.filter(author__average_rating__gte=instructor_ranking, author__role='INSTRUCTOR')

        # Order by likes
        if likes_order:
            order = '' if likes_order == 'asc' else '-'
            events = events.annotate(likes_count=Count('like')).order_by(f'{order}likes_count')

        # Filter by time of day
        if time_of_day:
            events = events.filter(time=time_of_day)

        # Filter by day of the week
        if day_of_week:
            events = events.filter(date__week_day=day_of_week)

        # Filter by tags
        tags = form.cleaned_data.get('tags')
        if tags:
            events = events.filter(tags=tags).distinct()

    # Annotate with likes count
    events = events.annotate(likes_count=Count('like'))

    # Prepare additional details
    event_details_list = [
        {
            'event': event,
            'likes_count': event.likes_count,
            'user_has_liked': event.like_set.filter(user=request.user).exists(),
            'average_rating': event.author.average_rating if event.author.role == 'INSTRUCTOR' else None,
            'cost': 7.00 if event.author.role == 'INSTRUCTOR' else 0.00,
            'tags':  event.tags,
            'user_has_booked': event.booking_set.filter(user_profile=request.user.profile).exists(),
        }
        for event in events
    ]

    context = {
        'form': form,
        'event_details_list': event_details_list,
    }

    return render(request, 'community/search_events.html', context)
# End-of-file (EOF)