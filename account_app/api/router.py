from rest_framework import routers

from .views.account import AccountView, ProfileView, AccountCreateView, UserPreviewView

api_router = routers.DefaultRouter()

api_router.register('', AccountView)
api_router.register('registration', AccountCreateView)
api_router.register('profile', ProfileView)
api_router.register('preview', UserPreviewView)
