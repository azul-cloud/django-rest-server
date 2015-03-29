from django.conf.urls import patterns, include, url
from django.contrib import admin
from .routers import v1_router

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/docs/', include('rest_framework_swagger.urls')),
    url(r'^v1/', include(v1_router.urls)),
)
