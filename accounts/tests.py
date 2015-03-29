from rest_framework.test import APITestCase

from .factories import NormalUserFactory
from core.tests import APITestMixin


class UserAPITests(APITestCase, APITestMixin):
    def setUp(self):
        self.user = NormalUserFactory.create()

        self.model_url = 'users/'
        self.data = {
            'username': 'newtestuser',
            'password': 'password',
            'email': 'newuser@email.com',
            'first_name': 'first',
            'last_name': 'last',
        }