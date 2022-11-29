"""
Tests for the user API
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """create and return a new user"""
    return get_user_model.objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """test the public features of the user API"""
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """test creating user is successful"""
        payload = {
            'email': "test@example.com",
            'password': 'tst123',
            'name': 'tester',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        create_user(password='test123', email='test@example.com', name='exa')
        res = self.client.post(
            CREATE_USER_URL,
            {'password':'test1234', 'email':'test@example.com', 'name':'pro'}
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test error returned for password to short"""
        payload = {
            'email': 'test@example.com',
            'password': 't',
            'name': 'Cool Dude',
        }


        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
