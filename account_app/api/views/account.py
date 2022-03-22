from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser

from account_app.api.serializers.account import UserSerializer, ProfileSerializer, UserCreateSerializer, \
    ProfileUpdateSerializer, UserUpdateSerializer
from account_app.models import Profile
from insta_dj.permissions import IsOwner


class AccountView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


    @action(methods=['get', ], detail=False, url_path=r'filter/(?P<username>[^/.]+)')
    def by_username(self, request, pk=None, *args, **kwargs):
        # Get user by username
        name = self.kwargs['username']
        if name is not None:
            user = self.get_queryset().filter(username=name).first()
            serializer = self.serializer_class(user, many=False)
            return Response(serializer.data)


class AccountCreateView(GenericViewSet, CreateModelMixin):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class AccountUpdateView(GenericViewSet, UpdateModelMixin):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class ProfileView(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    parser_classes = [MultiPartParser, JSONParser]


class ProfileUpdateView(GenericViewSet, UpdateModelMixin):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()
    parser_classes = [MultiPartParser, JSONParser]






