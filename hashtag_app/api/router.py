from rest_framework import routers

from .views.hashtags import HashtagsView

api_router = routers.DefaultRouter()

api_router.register('', HashtagsView)