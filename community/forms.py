from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import UserProfile , GOVERNMENT_OFFICIAL , INSTRUCTOR , GENERAL_PUBLIC , Event 

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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','start_time', 'end_time', 'capacity', 'cost' , 'image' ]

def create_event(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid() and user_profile.role in [UserProfile.INSTRUCTOR, UserProfile.GOVERNMENT_OFFICIAL]:
            event = form.save(commit=False)
            event.author = user_profile
            event.save()
            return redirect('event_detail',event_id=event.id)
    else:
        form =EventForm()
    return render(request, 'events/create_event.html',{'form':form})