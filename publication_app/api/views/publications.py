from django.contrib.auth.models import User
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account_app.api.serializers.account import UserSerializer
from comments_app.api.serializers.comments import CommentDetailSerializer
from comments_app.models import Comment
from insta_dj.permissions import IsOwner
from publication_app.api.serializers.publications import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from publication_app.models import Post


class PostsView(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()
                                        .filter(user__followers__follower=request.user)
                                        .order_by('-create_date').all())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get', ], detail=False, url_path=r'tag/(?P<label>[^/.]+)')
    def filter_by_tag(self, request, *args, **kwargs):
        # 'Filtering posts by hashtag_label'
        label = self.kwargs['label']
        if label is not None:
            posts = self.get_queryset().filter(hashtags__hashtag_label=label)
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data)

    @action(methods=['get', ], detail=True, serializer_class=CommentDetailSerializer)
    def comments(self, request, pk=None, *args, **kwargs):
        # Get comments by post id
        if pk is not None:
            comment = Comment.objects.filter(post=pk)
            serializer = self.serializer_class(comment, many=True)
            return Response(serializer.data)

    @action(methods=['get', ], detail=True, serializer_class=UserSerializer, url_path=r'liked')
    def likes(self, request, pk=None, *args, **kwargs):
        # Get users who liked post by post id
        if pk is not None:
            liked_user = User.objects.filter(likes__post=pk)
            serializer = self.serializer_class(liked_user, many=True)
            return Response(serializer.data)


class PostCreateView(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser]


class PostUpdateView(GenericViewSet, UpdateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser]
