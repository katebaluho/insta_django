from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser

from account_app.api.serializers.account import UserSerializer, ProfileSerializer, UserCreateSerializer, \
    UserUpdateSerializer, ProfileUpdateSerializer, UserPreviewSerializer
from account_app.models import Profile


class AccountView(GenericViewSet, ListModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id',]
    actions_serializers = {'update': UserUpdateSerializer,
                           'partial_update': UserUpdateSerializer,
                           }

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)


    @action(methods=['get', ], detail=False, url_path=r'(?P<username>[^/.]+)')
    def by_username(self, request, pk=None, *args, **kwargs):
        # Get user by username
        name = self.kwargs['username']
        if name is not None:
            user = self.get_queryset().filter(username=name).first()
            serializer = self.serializer_class(user, many=False)
            return Response(serializer.data)


class AccountCreateView(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class ProfileView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    parser_classes = [MultiPartParser, JSONParser]
    actions_serializers = {'update': ProfileUpdateSerializer,
                           'partial_update': ProfileUpdateSerializer,}

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)


class UserPreviewView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPreviewSerializer
    queryset = User.objects.all()







