from rest_framework import routers

from .views.comments import CommentView
from .. import views

api_router = routers.DefaultRouter()

api_router.register('', CommentView)