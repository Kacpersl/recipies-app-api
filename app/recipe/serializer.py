"""Serializer for recipe api"""
from rest_framework import serializers

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializers):
    """Serializer for recipe api"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']