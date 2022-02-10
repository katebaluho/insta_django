from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin


from account_app.api.serializers.account import UserSerializer, ProfileSerializator
from account_app.models import Profile


class AccountView(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'username']


class ProfileView(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializator
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']