"""Tests for models."""

from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email='user@exaple.com', password='testpass123'):
    """Create and return user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_model_with_email_successful(self):
        """Creating a user with an email is successful"""
        email = "test@example.com"
        password = "password123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test if email is normalized for new user"""
        sample_emails = [
            ['test@EXAMPLE.com', "test@example.com"],
            ['TEST@example.com', 'TEST@example.com'],
        ]

        for email, expected in sample_emails:

            user = get_user_model().objects.create_user(email, 'sample543')
            self.assertAlmostEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass12')

    def test_create_superuser(self):
        """testing proper creation of the superuser"""
        superuser = get_user_model().objects.create_superuser('d@e.c', 't1')

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'pass123'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)