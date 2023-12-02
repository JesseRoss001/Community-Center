from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import UserProfile , GOVERNMENT_OFFICIAL , INSTRUCTOR , GENERAL_PUBLIC , STAFF, Event , TIME_SLOTS
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
class StaffForm(UserCreationForm):
    staff_id = forms.CharField(max_length=6)
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

    class Meta:
        model = Event
        exclude = ['author','date','time','capacity']
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        labels = {'score': 'Rate this instructor:'}
        widgets = {
            'score': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        }
class CreditIssueForm(forms.Form):
    user_id = forms.IntegerField(label='User ID', widget=forms.HiddenInput())
    credit_amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Credit Amount')

    def __init__(self, *args, **kwargs):
        super(CreditIssueForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'user_id' in kwargs['initial']:
            self.fields['user_id'].initial = kwargs['initial'].get('user_id')
            self.user_id = kwargs['initial'].get('user_id')

    def clean_credit_amount(self):
        credit_amount = self.cleaned_data['credit_amount']
        # Check for two decimal places
        if credit_amount and credit_amount.as_tuple().exponent != -2:
            raise ValidationError("Please enter a credit amount with two decimal places.")
        return credit_amount

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        credit_amount = cleaned_data.get('credit_amount')

        if user_id and credit_amount:
            # Fetch the user's profile
            try:
                user_profile = UserProfile.objects.get(user__id=user_id)
                if credit_amount > user_profile.balance:
                    self.add_error('credit_amount', "Credit amount cannot exceed the user's current balance.")
            except UserProfile.DoesNotExist:
                raise ValidationError("User not found.")