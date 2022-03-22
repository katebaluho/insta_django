from rest_framework import routers

from .views.comments import CommentUpdateView, CommentCreateView
from .. import views

api_router = routers.DefaultRouter()

api_router.register('', CommentCreateView)
api_router.register('', CommentUpdateView)