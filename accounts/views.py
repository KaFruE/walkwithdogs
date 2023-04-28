import requests
from json.decoder import JSONDecodeError

from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.http import JsonResponse

from .serializers import UserSerializer

from .models import User

from dj_rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

User = get_user_model()

MAIN_DOMAIN = settings.MAIN_DOMAIN
GOOGLE_CALLBACK_URI = MAIN_DOMAIN + 'api/users/google/callback/'

def google_login(request):
    """
    Code Request
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

def google_callback(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    print('request : ', request)

    return
