from rest_framework import routers

from .views.follower import FollowView, FollowHashtagView

api_router = routers.DefaultRouter()

api_router.register('user', FollowView)
api_router.register('hashtag', FollowHashtagView)