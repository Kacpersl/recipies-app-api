"""Tests for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model


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
