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

    def clean(self):
        #validation for card + badge 
        if self.role == GOVERNMENT_OFFICIAL and not self.badge_number:
            raise ValidationError({'badge_number': 'This field is required for government officials '})
        if self.role == INSTRUCTOR and not self.card_number:
            raise ValidationError({'card_number': 'This field is required for instructors '})
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    