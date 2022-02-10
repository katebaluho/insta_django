from rest_framework import routers

from .views.account import AccountView, ProfileView

api_router = routers.DefaultRouter()

api_router.register('account', AccountView)
api_router.register('profile', ProfileView)