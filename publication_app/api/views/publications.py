from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.publications import PostSerializer
from publication_app.models import Post


class PostsView(GenericViewSet,ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['hashtags__hashtag_label']

