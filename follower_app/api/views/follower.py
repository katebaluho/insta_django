from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account_app.api.serializers.account import UserSerializer
from follower_app.api.serializers.follower import FollowerSerializer, FollowerHashtagSerializer
from follower_app.models import Follower, FollowingHashtag
from hashtag_app.api.serializers.hashtags import HashtagSerializer
from hashtag_app.models import Hashtag


class FollowView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    @action(methods=['get', ], detail=False, serializer_class=UserSerializer, url_path=r'(?P<user_id>[^/.]+)/followers')
    def user_followers(self, request, *args, **kwargs):
        # Подписчики пользователя

        user_id = self.kwargs['user_id']
        if user_id is not None:
            user_followers = User.objects.filter(followings__following__id=user_id).all()
            serializer = self.get_serializer(user_followers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get', ], detail=False, serializer_class=UserSerializer,
            url_path=r'(?P<user_id>[^/.]+)/followings')
    def user_followings(self, request, *args, **kwargs):
        # Подписки пользователя

        user_id = self.kwargs['user_id']
        if user_id is not None:
            user_followings = User.objects.filter(followers__follower__id=user_id).all()
            serializer = self.get_serializer(user_followings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class FollowHashtagView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerHashtagSerializer
    queryset = FollowingHashtag.objects.all()

    @action(methods=['get', ], detail=False, serializer_class=HashtagSerializer,
            url_path=r'(?P<user_id>[^/.]+)/following_tags')
    def user_followings(self, request, *args, **kwargs):
        # Список тегов, на которые подписан пользователь

        user_id = self.kwargs['user_id']
        if user_id is not None:
            user_followings = Hashtag.objects.filter(followers__follower__id=user_id).all()
            serializer = self.get_serializer(user_followings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
