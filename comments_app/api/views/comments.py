from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from comments_app.api.serializers.comments import CommentSerializer, CommentDetailSerializer, CommentUpdateSerializer
from comments_app.models import Comment


class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    actions_serializers = {'retrieve': CommentDetailSerializer,
                           'list': CommentDetailSerializer,
                           'update': CommentUpdateSerializer,
                           'partial_update': CommentUpdateSerializer,}
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['post', ]


    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

