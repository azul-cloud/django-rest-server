from rest_framework.test import APITestCase

from core.tests import APITestMixin
from accounts.factories import NormalUserFactory


class ArticleAPITests(APITestCase, APITestMixin):
    def setUp(self):
        self.user = NormalUserFactory.create()

        self.model_url = 'articles/'
        self.data = {
            'title': 'Article Title',
            'headline': 'This is the test headline',
            'body': '<h1>PURE AWESOMENESS</h1>',
            'author': self.user.id,
            'create_date': '2015-02-17',
        }