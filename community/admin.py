from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile, Event , Booking
# Register your models here.

class EventAdmin(SummernoteModelAdmin):
    list_display = ('title','author','date','start_time','end_time','capacity','cost')
    search_fields = ['title','description','author__user__username']
    list_filter = ('date','author__role')
    summernote_fields = ('description',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','role','balance')
    search_fields = ['user__username','role']
    list_filter = ('role',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event','user_profile','booking_time')
    search_fields = ['event__title', 'user_profile__user__username']
    list_filter = ('event',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)