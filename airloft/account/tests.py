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
