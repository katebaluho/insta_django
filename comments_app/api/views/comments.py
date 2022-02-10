from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comments import CommentSerializer, CommentDetailSerializer
from comments_app.models import Comment


class CommentView(GenericViewSet,CreateModelMixin,ListModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    actions_serializers = {'retrieve': CommentDetailSerializer, }
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['post', ]
    

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

