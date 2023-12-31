"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^$', RedirectView.as_view(url='community/', permanent=False)),
]
handler404 = 'community.views.custom_404'
handler500 = 'community.views.custom_500'
handler403 = 'community.views.custom_403'
