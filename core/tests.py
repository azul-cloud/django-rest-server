from django.conf import settings
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase


class APITestMixin(object):
    """
    mixin to perform the default API Test functionality
    """
    api_root = settings.REST_FRAMEWORK.get("API_ROOT")
    model_url = ''
    data = {}
    
    def get_endpoint(self):
        """
        return the API endpoint
        """
        endpoint = self.api_root + self.model_url
        return endpoint

    def test_create_object(self):
        """
        create a new object
        """
        response = self.client.post(self.get_endpoint(), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data, [])

    def test_get_objects(self):
        """
        get a list of objects
        """
        response = self.client.get(self.get_endpoint())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertNotEqual(response.data, [])


class NavigationTests(TestCase):
    def test_api_v1_docs(self):
        url = '/v1/docs/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django REST Swagger')

    def test_api_auth_login_page(self):
        url = '/auth/login/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_api_auth_logout_page(self):
        url = '/auth/logout/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


