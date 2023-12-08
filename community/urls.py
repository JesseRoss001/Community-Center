"""Comunity urls"""
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import (like_event, submit_rating, issue_credit,
                    search_events, issue_credit)


urlpatterns = [
    path('', views.home, name='home'),  # noqa: E203
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register_public/', views.general_public, name='register_public'),
    path('register_instructor/',
    views.register_instructor, name='register_instructor'),
    path('register_government/',
    views.register_government, name='register_government'),
    path('register_staff/', views.register_staff, name='register_staff'),
    path('event/create/', views.create_event, name="create_event"),
    path('event/update/<int:event_id>/',
    views.update_event, name='update_event'),
    path('event/delete/<int:event_id>/',
    views.delete_event, name='delete_event'),
    path('event/join/<int:event_id>/', views.join_event, name='join_event'),
    path('event/<int:event_id>/', views.event_detail, name="event_detail"),
    path('event/delete_image/<int:event_id>/',
    views.delete_event_image, name='delete_event_image'),
    path('summernote/', include('django_summernote.urls')),
    path('like_event/<int:event_id>/', views.like_event, name='like_event'),
    path('submit_rating/<int:instructor_id>/',
    submit_rating, name='submit_rating'),
    path('issue-credit/', issue_credit, name='issue_credit'),
    path('search-events/', search_events, name='search_events'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
