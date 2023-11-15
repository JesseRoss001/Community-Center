from django.shortcuts import render
# Create your views here.
#Creating views for home , events , about , gallery and booking pages 

def home(request):
    return render(request, 'community/home.html')

def events(request):
    return render(request, 'community/events.html')

def about(request):
    return render(request,'community/about.html')

def login(request):
    return render(request,'community/login.html')

def gallery(request):
    return render(request, 'community/gallery.html')

def booking(request):
    return render(request, 'community/booking.html')

def register_government(request):
    if request.method == 'POST':
        user_form = GovernmentOfficialForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            badge_number = user_form.cleaned_data['badge_number']
            UserProfile.objects.create(user=user , role=GOVERNMENT_OFFICIAL, badge_number= badge_number)
            return redirect('login')
    else: 
        user_form = GovernmentOfficialForm()
    return render(request,'community/register_government', {'form':user_form})

def register_instructor(request):
    if request.method == 'POST':
        user_form = InstructorForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            card_number = user_form.cleaned_data['card_number']
            UserProfile.objects.create(user=user , role=INSTRUCTOR, card_number=card_number)
            return redirect('login')
    else: 
        user_form = InstructorForm()
    return render(request,'community/register_instructor.html', {'form':user_form})

def general_public(request):
    if request.method == 'POST':
        user_form = GeneralPublicForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserProfile.objects.create(user=user,role=GENERAL_PUBLIC)
            return redirect('login')
    else:
        user_form =GeneralPublicForm()
    return render(request,'community/register_public',{'form':user_form})