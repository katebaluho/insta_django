from rest_framework import routers

from .views.publications import PostsView, PostCreateView, PostUpdateView

api_router = routers.DefaultRouter()

api_router.register('', PostsView)
api_router.register('create', PostCreateView)
api_router.register('post', PostUpdateView)