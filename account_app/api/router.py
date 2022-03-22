from rest_framework import routers

from .views.account import AccountView, ProfileView, AccountCreateView, ProfileUpdateView, AccountUpdateView

api_router = routers.DefaultRouter()

api_router.register('user', AccountView)
api_router.register('update', AccountUpdateView)
api_router.register('registration', AccountCreateView)
api_router.register('profile', ProfileView)
api_router.register('profile/update', ProfileUpdateView)
