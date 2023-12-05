from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import UserProfile, Event, Booking, BalanceChange
from django.utils.translation import gettext_lazy as _


class EventImageFilter(admin.SimpleListFilter):
    """
    A custom filter for the Django admin interface to filter
    events based on whether they have an image.
    """
    title = _('Has Image')
    parameter_name = 'has_image'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the
        coded value for the option that will appear in the URL query. The
        second element is the human-readable name for the option
        that will appear in the right sidebar.
        """
        return (
            ('Yes', _('Yes')),
            ('No', _('No')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the
        query string.
        """
        if self.value() == 'Yes':
            return queryset.exclude(image='')
        if self.value() == 'No':
            return queryset.filter(image='')


# Register your models here.
class BookingInline(admin.TabularInline):
    """
    Inline admin for bookings, allowing for management
    of bookings directly within the Event admin.
    """
    model = Booking
    extra = 0
    readonly_fields = ('booking_time',)


class BalanceChangeInline(admin.TabularInline):
    """
    Inline admin for balance changes, enabling management of user balance
    changes directly within the UserProfile admin.
    """
    model = BalanceChange
    extra = 0
    readonly_fields = (
        'change_date', 'transaction_type', 'change_amount', 'staff_member')


class EventAdmin(SummernoteModelAdmin):
    """
    Admin class for the Event model.
    Includes configurations for list display, search capabilities,
    filters, and integration of Summernote for rich text editing.
    """
    list_display = ('title', 'author', 'date', 'time', 'capacity')
    search_fields = ['title', 'description', 'author__user__username']
    list_filter = ('date', 'author__role', EventImageFilter)
    summernote_fields = ('description',)

    def get_urls(self):
        """
        Override get_urls to add custom URL for image deletion.
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                'delete-image/<int:event_id>/',
                self.admin_site.admin_view(self.delete_image),
                name='delete-event-image'),
        ]
        return custom_urls + urls

    def delete_image_link(self, obj):
        """
        Create a link in the admin interface for deleting an event's image.
        This link is only displayed if the event has an image.
        """
        if obj.image:
            return format_html(
                '<a href="{}">Delete Image</a>',
                reverse('admin:delete-event-image', args=[obj.pk]))
        return "No Image"
    delete_image_link.short_description = 'Delete Image'

    def delete_image(self, request, event_id):
        """
        Handle the deletion of an event's image.
        This view is called when the delete link
        is clicked in the admin interface.
        """
        event = Event.objects.get(id=event_id)
        if event.image:
            event.image.delete(save=True)
            self.message_user(request, "Image deleted successfully.")
        return redirect('admin:app_event_changelist')


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin class for the UserProfile model.
    Configured to display user, role, and balance fields,
    with search and filter capabilities.
    """
    list_display = ('user', 'role', 'balance')
    search_fields = ['user__username', 'role']
    list_filter = ('role',)
    readonly_fields = ('balance',)


class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the Booking model.
    Includes settings for displaying event, user profile,
    and booking time, along with search and filtering options.
    """
    list_display = ('event', 'user_profile', 'booking_time')
    search_fields = ['event__title', 'user_profile__user__username']
    list_filter = ('event',)
    readonly_fields = ('booking_time',)


class BalanceChangeAdmin(admin.ModelAdmin):
    """
    Admin class for the BalanceChange model.
    Provides an interface to view details of balance
    changes including the user profile,
    transaction type, amount, and related staff member.
    """
    list_display =
    ('user_profile', 'change_date',
     'transaction_type', 'change_amount', 'event', 'staff_member')
    search_fields =
    ['user_profile__user__username', 'transaction_type', 'event__title']
    list_filter = ('transaction_type', 'change_date')
    readonly_fields = ('change_date', 'staff_member')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BalanceChange, BalanceChangeAdmin)
