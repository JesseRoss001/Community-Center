from django import forms
from django.contrib.auth.models import user 
from .models import UserProfile , GOVERNMENT_OFFICIAL , INSTRUCTOR , GENERAL_PUBLIC 

class GovernmentOfficialForm(forms.ModelForm):
    badge_number = forms.CharField(max_length=5)

    class Meta:
        model=User
        fields = ('username', 'email ', 'password')

class InstructorForm(forms.ModelForm):
    card_number = forms.CharField(max_length=4)

    class Meta:
        model = User 
        fields = ('username','email','password')

class GeneralPublicForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password')