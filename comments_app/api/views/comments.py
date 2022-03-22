from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comments import CommentSerializer, CommentUpdateSerializer
from comments_app.models import Comment
from insta_dj.permissions import IsOwner


class CommentCreateView(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdateView(GenericViewSet, UpdateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CommentUpdateSerializer
    queryset = Comment.objects.all()




