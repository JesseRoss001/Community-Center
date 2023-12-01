from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from django.db.models import Avg
# Create your models here.
ADMIN = 'ADMIN'
INSTRUCTOR = 'INSTRUCTOR'
GOVERNMENT_OFFICIAL = 'GOVERNMENT'
GENERAL_PUBLIC = 'PUBLIC'
USER_ROLES = [
    (ADMIN,'Admin'),
    (INSTRUCTOR,'Instructor'),
    (GOVERNMENT_OFFICIAL,'Government Official'),
    (GENERAL_PUBLIC,'General Public User'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=30,choices=USER_ROLES,default=GENERAL_PUBLIC)
    badge_number = models.CharField(max_length=5,blank=True) #required badgeg number for government offic
    card_number = models.CharField(max_length=4,blank=True) # card number required for instructors 
    created_events = models.ManyToManyField('Event', related_name='creators', blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def clean(self):
        #validation for card + badge 
        if self.role == GOVERNMENT_OFFICIAL and not self.badge_number:
            raise ValidationError({'badge_number': 'This field is required for government officials '})
        if self.role == INSTRUCTOR and not self.card_number:
            raise ValidationError({'card_number': 'This field is required for instructors '})
        if self.role != GOVERNMENT_OFFICIAL:
            self.badge_number = ''
        if self.role != INSTRUCTOR:
            self.card_number = ''
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    def save(self, *args, **kwargs):
        self.average_rating = self.ratings.aggregate(Avg('score'))['score__avg'] or 0
        super().save(*args, **kwargs)

#globally define time slot constant
TIME_SLOTS = (
    ('08:00', '08:00 - 10:00'),
    ('10:00','10:00-12:00'),
    ('12:30','12:30-14:30'),
    ('14:30','14:30-16:30'),
    ('17:00','17:00-19:00'),
    ('19:00','19:00-21:00'),
)
#event model 
class Event(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_SLOTS)
    capacity =models.IntegerField(default=60)
    image = models.ImageField(upload_to='event_images/',blank=True , null=True)
    def clean(self):
        if self.date is None:
            raise ValidationError("Event date is required.")
        if self.date < timezone.now().date():
            raise ValidationError("Event date cannot be in the past.")
    class Meta:
        unique_together = ('date','time')
    def __str__(self):
        return self.title

#booking class 
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.event.date < timezone.now().date():
            raise ValidationError("Cannot book a past event.")
        if Booking.objects.filter(event=self.event).count() >= self.event.capacity:
            raise ValidationError("This event is fully booked.")
        super(Booking, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.user_profile.user.username} booking for {self.event.title}'


class BalanceChange(models.Model):
    TRANSACTION_TYPES = [
        ('CREATE_EVENT',' Created Event'),
        ('JOIN_EVENT',' Joined Event'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='balance_changes')
    change_amount = models.DecimalField(max_digits=10,decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=90, choices=TRANSACTION_TYPES)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f"{self.change_amount} on {self.change_date} ({self.get_transaction_type_display()})"
class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        superuser = super().create_superuser(username, email, password, **extra_fields)
        UserProfile.objects.create(user=superuser, role=ADMIN)
        return superuser
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, 'profile'):
            user=instance, 
            defaults={'role': ADMIN if instance.is_superuser else GENERAL_PUBLIC}
    
    else:
        if not UserProfile.objects.filter(user=instance).exists():
            UserProfile.objects.create(
                user=instance, 
                role=ADMIN if instance.is_superuser else GENERAL_PUBLIC
            )

User.add_to_class('objects', CustomUserManager())


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

class Rating(models.Model):
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # For reference to the rated event
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')