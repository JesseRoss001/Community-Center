from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models


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

    def clean(self):
        #validation for card + badge 
        if self.role == GOVERNMENT_OFFICIAL and not self.badge_number:
            raise ValidationError({'badge_number': 'This field is required for government officials '})
        if self.role == INSTRUCTOR and not self.card_number:
            raise ValidationError({'card_number': 'This field is required for instructors '})
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

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
    start_time = models.CharField(max_length=10, choices=TIME_SLOTS)
    end_time = models.CharField(max_length=10, choices=TIME_SLOTS)
    capacity =models.IntegerField(default=60)
    cost = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    image = models.ImageField(upload_to='event_images/',blank=True , null=True)

    class Meta:
        unique_together = ('date','start_time')
    def __str__(self):
        return self.title

#booking class 
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_profile.user.username} booking for {self.event.title}'