from rest_framework import routers

from .views.comments import CommentView

api_router = routers.DefaultRouter()

api_router.register('comment', CommentView)