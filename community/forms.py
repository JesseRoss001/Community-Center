from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import UserProfile , GOVERNMENT_OFFICIAL , INSTRUCTOR , GENERAL_PUBLIC 

class GovernmentOfficialForm(UserCreationForm):
    badge_number = forms.CharField(max_length=5)

    class Meta:
        model=User
        fields = ('username', 'email', 'password1','password2')

class InstructorForm(UserCreationForm):
    card_number = forms.CharField(max_length=4)

    class Meta:
        model = User 
        fields = ('username','email','password1','password2')

class GeneralPublicForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')