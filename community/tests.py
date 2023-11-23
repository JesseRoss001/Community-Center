from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event, UserProfile ,Booking,BalanceChange
from django.utils import timezone
import datetime
# Developed with assistance from ChatGPT, Stack Overflow to test various functionalities in a Django web application
#Django's official documentation on testing: https://docs.djangoproject.com/en/4.0/topics/testing/
class EventTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.user_profile = UserProfile.objects.create(user=self.user, role='INSTRUCTOR')
        self.date = datetime.date.today() + datetime.timedelta(days=1)
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=self.date,
            time='08:00',
            capacity=60,
            author=self.user_profile,
        )
    def test_event_creation_page(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('create_event'))
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('update_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_event(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_join_event(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('join_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_event_creation_fee(self):
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('create_event'), {
            'title': 'New Event',
            'description': 'New Event Description',
            'date': self.date,
            'time': '10:00',
            'capacity': 50,
            'cost': 0,
        })
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.balance, -200)

class UserRegistrationTests(TestCase):

    def test_instructor_registration(self):
        response = self.client.post(reverse('register_instructor'), {
            'username': 'instructor',
            'email': 'instructor@example.com',
            'password1': 'complex_password',
            'password2': 'complex_password',
            'card_number': '6789',
        })
        self.assertEqual(response.status_code, 302)

    def test_government_official_registration(self):
        response = self.client.post(reverse('register_government'), {
            'username': 'govuser',
            'email': 'govuser@example.com',
            'password1': 'complex_password',
            'password2': 'complex_password',
            'badge_number': '12345',
        })
        self.assertEqual(response.status_code, 302)
from decimal import Decimal
class EventBookingTests(TestCase):
    
    def setUp(self):
        # Set up data for the whole TestCase
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.user_profile = UserProfile.objects.create(user=self.user, role='INSTRUCTOR', balance=Decimal('500.00'))
        self.event = Event.objects.create(
            title='Test Event',
            description='A test event',
            date=timezone.now().date(),
            time='08:00',
            capacity=60,
            author=self.user_profile,
        )

    def test_double_booking_prevention(self):
        # Ensure a user can't book the same event twice
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('join_event', args=[self.event.id]))
        response = self.client.post(reverse('join_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_balance_changes_on_event_creation(self):
        # Test balance changes when an event is created
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('create_event'), {
            'title': 'New Event',
            'description': 'Another test event',
            'date': timezone.now().date(),
            'time': '10:00',
            'capacity': 50
        })
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.balance, Decimal('300.00'))  # Assuming 200 is deducted

    def test_balance_changes_on_event_deletion(self):
        # Test balance changes when an event is deleted
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('delete_event', args=[self.event.id]))
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.balance, Decimal('700.00'))  # Assuming 200 is refunded

    def test_image_deletion_from_gallery(self):
        # Test image deletion functionality
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('delete_event_image', args=[self.event.id]))
        self.event.refresh_from_db()
        self.assertFalse(self.event.image)  # Assuming image field is empty after deletion

class UserAccountTests(TestCase):

    def setUp(self):
        # Set up data for the whole TestCase
        self.client = Client()
        self.user = User.objects.create_user('testuser2', 'test2@example.com', 'password')
        self.user_profile = UserProfile.objects.create(user=self.user, role='INSTRUCTOR', balance=Decimal('500.00'))

    def test_user_balance(self):
        # Test the user's balance
        self.client.login(username='testuser2', password='password')
        response = self.client.get(reverse('home'))
        self.assertContains(response, '500.00', status_code=200)

