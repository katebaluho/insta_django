from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from like_app.api.serializers.likes import LikesPostSerializer, LikesCommentSerializer
from like_app.models import Like


class LikesPostView(GenericViewSet,CreateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = LikesPostSerializer
    queryset = Like.objects.all()

class LikesCommentView(GenericViewSet,CreateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = LikesCommentSerializer
    queryset = Like.objects.all()




