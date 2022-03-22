from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from hashtag_app.api.serializers.hashtags import HashtagSerializer
from hashtag_app.models import Hashtag



class HashtagsView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()


    @action(methods=['get', ], detail = False, url_path=r'hashtag/(?P<label>[^/.]+)')
    def info_about_label(self, request, *args, **kwargs):
        label = self.kwargs['label']
        if label is not None:
            tag = self.get_queryset().filter(hashtag_label=label).first()
            serializer = self.get_serializer(tag, many=False)
            return Response(serializer.data)


