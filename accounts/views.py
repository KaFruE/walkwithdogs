from django.contrib.auth import get_user_model
from rest_framework.response import Response

from serializers import UserSerializer

User = get_user_model()
