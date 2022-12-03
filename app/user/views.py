"""
Views for user Api
"""

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializers
    )

class CreateUserView(generics.CreateAPIView):
    """Create for new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializers_class = AuthTokenSerializers
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES