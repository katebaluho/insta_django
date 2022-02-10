from rest_framework import routers

from .views.follower import FollowView, UnfollowView, FollowHashtagView, UnfollowHashtagView

api_router = routers.DefaultRouter()

api_router.register('follow', FollowView)
api_router.register('unfollow', UnfollowView)
api_router.register('follow_hashtag', FollowHashtagView)
api_router.register('unfollow_hashtag', UnfollowHashtagView)