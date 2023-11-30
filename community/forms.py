from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import UserProfile , GOVERNMENT_OFFICIAL , INSTRUCTOR , GENERAL_PUBLIC , Event , TIME_SLOTS
from django.core.exceptions import ValidationError
from django.utils import timezone



class GovernmentOfficialForm(UserCreationForm):
    badge_number = forms.CharField(max_length=5)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    class Meta:
        model=User
        fields = ('username', 'email', 'password1','password2')

class InstructorForm(UserCreationForm):
    card_number = forms.CharField(max_length=4)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    class Meta:
        model = User 
        fields = ('username','email','password1','password2')

class GeneralPublicForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


#Event Form 
class EventForm(forms.ModelForm):
    time = forms.ChoiceField(choices=TIME_SLOTS)
    
    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        if event_date is None:
            raise forms.ValidationError("This field is required.")
        if event_date < timezone.now().date():
            raise forms.ValidationError("Event date cannot be in the past.")
        return event_date 
    def clean_capacity(self):
        capacity = self.cleaned_data.get('capacity')
        if capacity > 60:
            raise ValidationError("The capacity cannot exceed 60.")
        return capacity

    class Meta:
        model = Event
        fields = ['title','description','date','time', 'capacity', 'image' ]
        widgets = {'date':DateInput(attrs={'type':'date'}),}

class EventUpdateForm(forms.ModelForm):
    def clean_capacity(self):
        capacity = self.cleaned_data.get('capacity')
        if capacity > 60:
            raise ValidationError("The capacity cannot exceed 60.")
        return capacity
    class Meta:
        model = Event
        exclude = ['author','date','time']
