from rest_framework.mixins import ListModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from ..serializers.media import MediaSerializer
from ...models import Media


class MediaView(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    parser_classes = [MultiPartParser]
