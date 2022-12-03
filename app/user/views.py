"""
Views for user Api
"""

from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create for new user in the system"""
    serializer_class = UserSerializer