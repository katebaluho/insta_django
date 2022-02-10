from django.contrib.auth.models import User
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account_app.api.serializers.account import UserSerializer
from comments_app.api.serializers.comments import CommentDetailSerializer
from comments_app.models import Comment
from hashtag_app.api.serializers.hashtags import TagDetailSerializer
from publication_app.api.serializers.publications import PostSerializer
from publication_app.models import Post

# class AuthPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True
#         return False
#
#     #проверяем права на конкретный объект, например редактирование
#     def has_object_permission(self, request, view, obj):
#         pass

class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', ]


    @action(methods=['get', ], detail = False, url_path=r'(?P<label>\w+)')
    def filter_by_tag(self, request, *args, **kwargs):
        # 'Filtering posts by hashtag_label'
        label = self.kwargs['label']
        if label is not None:
            posts = self.queryset.filter(hashtags__hashtag_label=label)
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data)


    @action(methods=['get', ], detail=True, serializer_class = CommentDetailSerializer)
    def comments(self, request, pk = None, *args, **kwargs):
        # Get comments by post id
        if pk is not None:
            comm = Comment.objects.filter(post = pk)
            serializer = self.serializer_class(comm, many=True)
            return Response(serializer.data)


    @action(methods=['get', ], detail=True, serializer_class = UserSerializer)
    def likes(self, request, pk = None, *args, **kwargs):
        # Get liked post user by post id
        if pk is not None:
            liked_user = User.objects.filter(likes__post = pk)
            serializer = self.serializer_class(liked_user, many=True)
            return Response(serializer.data)










