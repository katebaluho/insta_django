from rest_framework import routers

from .views.media import MediaView


api_router = routers.DefaultRouter()

api_router.register('media', MediaView)