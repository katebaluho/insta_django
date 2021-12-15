from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from hashtag_app.api.serializers.hashtags import HashtagSerializer
from hashtag_app.models import Hashtag


class HashtagsView(GenericViewSet,ListModelMixin, CreateModelMixin):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()