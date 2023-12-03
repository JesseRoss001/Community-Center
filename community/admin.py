from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile, Event , Booking , BalanceChange
# Register your models here.
class BookingInline(admin.TabularInline):
    """
    Inline admin for bookings, allowing for management of bookings directly within the Event admin.
    """
    model = Booking
    extra = 0
    readonly_fields = ('booking_time',)

class BalanceChangeInline(admin.TabularInline):
    """
    Inline admin for balance changes, enabling management of user balance changes directly within the UserProfile admin.
    """
    model = BalanceChange
    extra = 0
    readonly_fields = ('change_date', 'transaction_type', 'change_amount', 'staff_member')
class EventAdmin(SummernoteModelAdmin):
    """
    Admin class for the Event model. 
    Includes configurations for list display, search capabilities, filters, and integration of Summernote for rich text editing.
    """
    list_display = ('title','author','date','time','capacity')
    search_fields = ['title','description','author__user__username']
    list_filter = ('date','author__role')
    summernote_fields = ('description',)

class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin class for the UserProfile model.
    Configured to display user, role, and balance fields, with search and filter capabilities.
    """
    list_display = ('user','role','balance')
    search_fields = ['user__username','role']
    list_filter = ('role',)
    readonly_fields = ('balance',)

class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the Booking model.
    Includes settings for displaying event, user profile, and booking time, along with search and filtering options.
    """
    list_display = ('event','user_profile','booking_time')
    search_fields = ['event__title', 'user_profile__user__username']
    list_filter = ('event',)
    readonly_fields = ('booking_time',)
class BalanceChangeAdmin(admin.ModelAdmin):
    """
    Admin class for the BalanceChange model.
    Provides an interface to view details of balance changes including the user profile, transaction type, amount, and related staff member.
    """
    list_display = ('user_profile', 'change_date', 'transaction_type', 'change_amount', 'event', 'staff_member')
    search_fields = ['user_profile__user__username', 'transaction_type', 'event__title']
    list_filter = ('transaction_type', 'change_date')
    readonly_fields = ('change_date', 'staff_member')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BalanceChange, BalanceChangeAdmin)