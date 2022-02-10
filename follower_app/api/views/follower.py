from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from follower_app.api.serializers.follower import FollowerSerializer, FollowerHashtagSerializer
from follower_app.models import Follower, FollowingHashtag


class FollowView(GenericViewSet,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

class UnfollowView(GenericViewSet,DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

class FollowHashtagView(GenericViewSet,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerHashtagSerializer
    queryset = FollowingHashtag.objects.all()

class UnfollowHashtagView(GenericViewSet,DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerHashtagSerializer
    queryset = FollowingHashtag.objects.all()
