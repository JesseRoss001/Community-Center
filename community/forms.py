from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (UserProfile, GOVERNMENT_OFFICIAL, INSTRUCTOR,
                     GENERAL_PUBLIC, STAFF, Event,
                     Booking, TIME_SLOTS, BalanceChange, Rating, Like)
from django.core.exceptions import ValidationError
from django.utils import timezone


class GovernmentOfficialForm(UserCreationForm):
    """
    A form for creating government official users.
    Includes a field for the government official's badge number.
    """
    badge_number = forms.CharField(max_length=5)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    class Meta:
        """
        Meta class for GovernmentOfficialForm.
        Specifies the model to use and the fields to be included in the form.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class InstructorForm(UserCreationForm):
    """
    A form for creating instructor users.
    Includes a field for the instructor's card number.
    """
    card_number = forms.CharField(max_length=4)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    class Meta:
        """
        Meta class for InstructorForm.
        Specifies the model to use and the fields to be included in the form.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class GeneralPublicForm(UserCreationForm):
    """
    A form for creating public users.
    """
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    class Meta:
        """
        Meta class for GeneralPublicForm.
        Specifies the model to use and the fields to be included in the form.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class StaffForm(UserCreationForm):
    """
    A form for creating staff users.
    """
    staff_id = forms.CharField(max_length=6)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    class Meta:
        """
        Meta class for StaffForm.
        Specifies the model to use and the fields to be included in the form.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Event Form
class EventForm(forms.ModelForm):
    """
    A form for creating or updating events.
    Includes custom validation for event date and capacity.
    """
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = Event.TAG_CHOICES

    def clean_date(self):
        """
        Validates the 'date' field of the form.
        Ensures that the event date is not left blank
        and is not set in the past.
        """
        event_date = self.cleaned_data.get('date')
        if event_date is None:
            raise forms.ValidationError("This field is required.")
        if event_date < timezone.now().date():
            raise forms.ValidationError("Event date cannot be in the past.")
        return event_date

    def clean_capacity(self):
        """
        Validates the 'capacity' field of the form.
        Ensures that the event capacity does not exceed
        a predefined maximum limit (e.g., 60).
        """
        capacity = self.cleaned_data.get('capacity')
        if capacity > 60:
            raise ValidationError("The capacity cannot exceed 60.")
        return capacity

    class Meta:
        """
        Meta class for EventForm.
        Specifies the model to use and the fields,
        widgets to be included in the form.
        """
        model = Event
        fields = ['title', 'description', 'date', 'time', 'capacity', 'image', 'tags']
        widgets = {'date': DateInput(attrs={'type': 'date'})}


class EventUpdateForm(forms.ModelForm):
    """
    A form for updating existing events.
    Excludes certain fields like 'author', 'date', 'time',
    and 'capacity' from updates.
    """
    class Meta:
        """
        Meta class for EventUpdateForm.
        Specifies the model and fields to exclude from the form.
        """
        model = Event
        exclude = ['author', 'date', 'time', 'capacity', 'course_type', 'tags']


class RatingForm(forms.ModelForm):
    """
    A form for rating instructors.
    """
    class Meta:
    """
    rating form fields 
    """
        model = Rating
        fields = ['score']
        labels = {'score': 'Rate this instructor:'}
        widgets = {
            'score': forms.Select
            (choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        }


class CreditIssueForm(forms.Form):
    """
    A form for issuing credits to a user's account.
    Includes custom validation for credit amount and user existence.
    """
    user_id = forms.IntegerField(label='User ID', widget=forms.HiddenInput())
    credit_amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Credit Amount')

    def __init__(self, *args, **kwargs):
        super(CreditIssueForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'user_id' in kwargs['initial']:
            self.fields['user_id'].initial = kwargs['initial'].get('user_id')
            self.user_id = kwargs['initial'].get('user_id')

    def clean_credit_amount(self):
        """
        Validates the 'credit_amount' field of the form.
        Ensures that the credit amount entered has exactly two decimal places.
        """
        credit_amount = self.cleaned_data['credit_amount']
        # Check for two decimal places
        if credit_amount and credit_amount.as_tuple().exponent != -2:
            raise ValidationError ("Please enter a credit amount with two decimal places.")
        return credit_amount

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        credit_amount = cleaned_data.get('credit_amount')

        if user_id and credit_amount:
            # Fetch the user's profile
            try:
                user_profile = UserProfile.objects.get(user__id=user_id)
                if user_profile.balance < 0 and credit_amount > abs (user_profile.balance):
                    self.add_error
                    ('credit_amount',
                     "Credit amount cannot bring the balance to"
                     "positive for users in debt.")
            except UserProfile.DoesNotExist:
                raise ValidationError("User not found.")


TIME_SLOTS_CHOICES = [('', 'Any Time of Day')] + list(TIME_SLOTS)
LIKES_CHOICES = (
    ('', 'Any Order'),
    ('asc', 'Ascending'),
    ('desc', 'Descending'),
)


class EventSearchForm(forms.Form):
    tags = forms.ChoiceField(
        choices=[('', 'Any Tag')] + Event.TAG_CHOICES,
        required=False,
        widget=forms.Select
    )
    instructor_ranking = forms.DecimalField(
        required=False, min_value=0, decimal_places=2, widget=forms.NumberInput
        (attrs={'type': 'number', 'step': "0.01"}))
    likes_order = forms.ChoiceField(
        choices=LIKES_CHOICES, required=False, label='Likes Order')
    day_of_week = forms.ChoiceField(
        choices=[('', 'Any Day')] + [('1', 'Monday'), ('2', 'Tuesday'),
                ('3', 'Wednesday'), ('4', 'Thursday'),  # noqa: W291
                ('5', 'Friday'), ('6', 'Saturday'),
                ('7', 'Sunday')], required=False)
    time_of_day = forms.ChoiceField(choices=TIME_SLOTS_CHOICES, required=False)

    def search(self):
        events = Event.objects.all()

        if self.cleaned_data.get('course_type'):
            course_type = self.cleaned_data['course_type']
            if course_type == 'Free':
                events = events.filter(
                    author__role=UserProfile.GOVERNMENT_OFFICIAL)
            elif course_type == 'Paid':
                events = events.filter(author__role=UserProfile.INSTRUCTOR)

        if self.cleaned_data.get('instructor_ranking'):
            min_ranking = self.cleaned_data['instructor_ranking']
            events = events.filter(
                author__role=UserProfile.INSTRUCTOR,
                author__ranking__gte=min_ranking)

        likes_order = self.cleaned_data.get('likes_order')
        if likes_order:
            order = '' if likes_order == 'asc' else '-'
            events = events.annotate(
                likes_count=Count('likes')).order_by(f'{order}likes_count')

        if self.cleaned_data.get('time_of_day'):
            time_of_day = self.cleaned_data['time_of_day']
            events = events.filter(time=time_of_day)

        if self.cleaned_data.get('day_of_week'):
            day_of_week = self.cleaned_data['day_of_week']
            events = events.filter(date__week_day=day_of_week)

        if self.cleaned_data.get('tags'):
            tags = self.cleaned_data['tags']
            events = events.filter(tags__in=tags).distinct()

        return events
