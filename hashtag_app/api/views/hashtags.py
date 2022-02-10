from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from hashtag_app.api.serializers.hashtags import HashtagSerializer, TagDetailSerializer
from hashtag_app.models import Hashtag

#может ли быть несколько view, как в таком случае подключить роуты
class HashtagsView(GenericViewSet,ListModelMixin, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
    actions_serializers = {'retrieve': TagDetailSerializer, }
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['hashtag_label', ]

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

