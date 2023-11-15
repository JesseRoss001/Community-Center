"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

application = get_wsgi_application()

#BASE_DIR
BASE_DIR = settings.BASE_DIR

#enabling white noise 
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
