from rest_framework import routers

from blog.views import ArticleViewSet
from accounts.views import UserViewSet


v1_router = routers.DefaultRouter()
v1_router.register('articles', ArticleViewSet)
v1_router.register('users', UserViewSet)
