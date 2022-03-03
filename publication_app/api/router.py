from django.template.defaulttags import url
from rest_framework import routers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views.publications import PostsView, PostCreateView

api_router = routers.DefaultRouter()

api_router.register('', PostsView)
api_router.register('post', PostCreateView)
