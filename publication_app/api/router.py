from django.template.defaulttags import url
from rest_framework import routers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views.publications import PostsView

api_router = routers.DefaultRouter()

api_router.register('post', PostsView)
#api_router.register(r'^publication/post_tags/<str:label>$', PostsView, basename='post_tags')


#api_router.register('publication/post_tags/<str:label>', PostHashtagView )
