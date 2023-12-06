from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
ADMIN = 'ADMIN'
INSTRUCTOR = 'INSTRUCTOR'
GOVERNMENT_OFFICIAL = 'GOVERNMENT'
GENERAL_PUBLIC = 'PUBLIC'
STAFF = 'STAFF'
USER_ROLES = [
    (ADMIN, 'Admin'),
    (INSTRUCTOR, 'Instructor'),
    (GOVERNMENT_OFFICIAL, 'Government Official'),
    (GENERAL_PUBLIC, 'General Public User'),
    (STAFF, 'Staff'),
]


class UserProfile(models.Model):
    """
    A class representing a user profile,
    extending the basic User model in Django.
    This includes additional fields like role,
    badge number, and associated events.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(
        max_length=30, choices=USER_ROLES, default=GENERAL_PUBLIC)
    badge_number = models.CharField(max_length=5, blank=True)
    card_number = models.CharField(max_length=4, blank=True)
    staff_id = models.CharField(max_length=6, blank=True)
    created_events = models.ManyToManyField(
        'Event', related_name='creators', blank=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    average_rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)

    def clean(self):
        if self.role == GOVERNMENT_OFFICIAL and not self.badge_number:
            raise ValidationError(
                {'badge_number': 'This field is required for officials '})
        if self.role == INSTRUCTOR and not self.card_number:
            raise ValidationError(
                {'card_number': 'This field is required for instructors '})
        if self.role == STAFF and not self.staff_id:
            raise ValidationError(
                {'staff_id': 'This field is required for staff members'})
        if self.role != STAFF:
            self.staff_id = ''
        if self.role != GOVERNMENT_OFFICIAL:
            self.badge_number = ''
        if self.role != INSTRUCTOR:
            self.card_number = ''

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    def update_average_rating(self):
        """
        Updates the average rating of an instructor.
        This method calculates the average score from
        all ratings related to the instructor
        and updates the 'average_rating' field.
        Only applicable if the user is an instructor.
        """
        if self.role == INSTRUCTOR:
            aggregate_rating = self.ratings.aggregate(
                Avg('score'))['score__avg'] or 0
            self.average_rating = round(aggregate_rating, 2)
            self.save()

    def update_balance_by_staff(self, staff_member, change_amount):
        """
        Updates the balance of a user profile by a specified amount.
        This method is only permitted to be executed by staff members.
        It creates a record in the BalanceChange model to log the transaction.
        """
        if staff_member.role != STAFF:
            raise ValidationError("Only staff members can update balances")
        self.balance += change_amount
        self.save()
        BalanceChange.objects.create(
            user_profile=self,
            change_amount=change_amount,
            transaction_type='CREDIT_ISSUED',
            staff_member=staff_member
        )


TIME_SLOTS = (
    ('08:00', '08:00 - 10:00'),
    ('10:00', '10:00-12:00'),
    ('12:30', '12:30-14:30'),
    ('14:30', '14:30-16:30'),
    ('17:00', '17:00-19:00'),
    ('19:00', '19:00-21:00'),
)


class Event(models.Model):
    """
    Represents an event, with details such as author, title,
    description, date, and time.
    Also includes features like capacity and optional image for the event.
    """
    TAG_CHOICES = [
        ('education', 'Education'),
        ('physical_fitness', 'Physical Fitness'),
        ('wellbeing', 'Wellbeing'),
        ('technology', 'Technology'),
        ('art_culture', 'Art & Culture'),
        ('science_innovation', 'Science & Innovation'),
        ('environment', 'Environment'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('community_service', 'Community Service'),
        ('personal_development', 'Personal Development'),
        ('health_nutrition', 'Health & Nutrition'),
        # ... other tags as needed
    ]

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_SLOTS)
    capacity = models.IntegerField(default=60)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    tags = models.CharField(max_length=50, choices=TAG_CHOICES, blank=True)

    @property
    def instructor_ranking(self):
        """ Calculate ranking only for events held by instructors """
        if self.author.role == INSTRUCTOR:
            return self.author.get_instructor_ranking()
        return None

    @property
    def number_of_likes(self):
        """ Count the number of likes for this event """
        return self.like_set.count()

    def clean(self):
        if self.date is None:
            raise ValidationError("Event date is required.")
        if self.date < timezone.now().date():
            raise ValidationError("Event date cannot be in the past.")

    def has_bookings(self):
        """
        Checks if the event has any bookings.
        Returns True if bookings exist, False otherwise.
        """
        return self.booking_set.exists()

    def __str__(self):
        tag_display = dict(Event.TAG_CHOICES).get(self.tags, "No Tag")
        return f"{self.title} - {tag_display}"

    class Meta:
        """
        Meta class for the Event model.
        Defines a unique constraint for each combination
        of event date and time,
        ensuring no two events occur at the same date and time.
        """
        unique_together = ('date', 'time')

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Manages the bookings for events. Each booking is
    linked to a specific event and user profile.
    Includes validations to ensure bookings are
    for future events and within the event capacity.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user_profile')

    def save(self, *args, **kwargs):
        if self.event.date < timezone.now().date():
            raise ValidationError("Cannot book a past event.")
        if Booking.objects.filter(
                event=self.event).count() >= self.event.capacity:
            raise ValidationError("This event is fully booked.")
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user_profile.user.username} booking  {self.event.title}'


class BalanceChange(models.Model):
    """
    Tracks changes in user balances, including the type of
    transaction and related event or staff member.
    Useful for maintaining a record of all
    financial transactions in the system.
    """
    TRANSACTION_TYPES = [
        ('CREATE_EVENT', ' Created Event'),
        ('JOIN_EVENT', ' Joined Event'),
        ('CREDIT_ISSUED', 'Credit Issued'),
    ]

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='balance_changes')
    change_amount = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=90, choices=TRANSACTION_TYPES)
    event = models.ForeignKey(
        Event, on_delete=models.SET_NULL, null=True, blank=True)
    staff_member = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='initiated_balance_changes')

    def __str__(self):
        return f"{self.change_amount} on {self.change_date} ({self.get_transaction_type_display()})"  # noqa: W291


class CustomUserManager(UserManager):
    """
    Custom user manager for creating superuser with a linked UserProfile.
    Overrides the default create_superuser method to include a user profile.
    """
    def create_superuser(
            self, username, email=None, password=None, **extra_fields):
        superuser = super().create_superuser(
            username, email, password, **extra_fields)
        UserProfile.objects.create(user=superuser, role=ADMIN)
        return superuser


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver for post-save on User model
    to create or update UserProfile.
    Ensures a UserProfile is created for each new user, with default roles set.
    """
    if created or not hasattr(instance, 'profile'):
        user = instance,
        defaults = {'role': ADMIN if instance.is_superuser else GENERAL_PUBLIC}
    else:
        if not UserProfile.objects.filter(user=instance).exists():
            UserProfile.objects.create(
                user=instance,
                role=ADMIN if instance.is_superuser else GENERAL_PUBLIC
            )


User.add_to_class('objects', CustomUserManager())


class Like(models.Model):
    """
    Represents a 'like' given by a user to an event.
    Includes a unique constraint to ensure a user can only like an event once.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for the Like model.
        Ensures a unique constraint between a user and an event,
        preventing a user from liking the same event more than once.
        """
        unique_together = ('user', 'event')


class Rating(models.Model):
    """
    Manages ratings given by users to instructors.
    Ratings are constrained between 1 and 5
    and are unique between a user and an instructor.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='given_ratings')
    instructor = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for the Rating model.
        Specifies a unique constraint between a user and an instructor,
        ensuring a user can only rate an instructor once.
        """
        unique_together = ('user', 'instructor')

    def __str__(self):
        return f"Rating for {self.instructor.user.username} by {self.user.username}: {self.score}"  # noqa: W291

