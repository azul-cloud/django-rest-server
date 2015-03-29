from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title