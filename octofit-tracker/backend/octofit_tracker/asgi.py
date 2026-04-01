<<<<<<< HEAD
"""
ASGI config for octofit_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')

=======
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
>>>>>>> a20f5c2 (OctoFit Tracker: Django backend, MongoDB, CORS, and API endpoints for users, teams, activities, leaderboard, and workouts)
application = get_asgi_application()
