from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from account.models import User


class TestEmployeeModelUseCase(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('moti', 'moti@gmail.com', 'password123!@', is_staff=False)
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'moti@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",
                          email='moti@gmail.com', password='password123!@')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username='', email='moti@gmail.com', password='password123!@')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The email must be set'):
            User.objects.create_user(username='moti', email='', password='password123!@')
