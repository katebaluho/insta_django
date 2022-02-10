from rest_framework import routers
from .views.likes import LikesPostView, LikesCommentView

api_router = routers.DefaultRouter()

api_router.register('post', LikesPostView)
api_router.register('comment', LikesCommentView)