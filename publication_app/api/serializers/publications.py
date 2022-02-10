from rest_framework import serializers, filters

from hashtag_app.api.serializers.hashtags import HashtagSerializer
from hashtag_app.models import Hashtag
from media_app.api.serializers.media import MediaSerializer
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['id', 'user', 'file__file']
        exclude = ['is_public']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    file = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='file'
    )

    tags = HashtagSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.likes.count()

    def get_comments_count(self, instance) -> int:
        return instance.comments.count()
