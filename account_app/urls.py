from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration_page, name="registration"),
    path('sigin/', auth_page, name="sigin"),
    path("edit_profile/", profile_edit_page, name="edit_profile"),
    path("profile/", profile_page, name="profile"),
    path("logout/", logout_view, name="logout"),
]