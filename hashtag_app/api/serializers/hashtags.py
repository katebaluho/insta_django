from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from publication_app.models import Post
from ...models import Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        exclude = ['posts', ]

    posts_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    @extend_schema_field(int)
    def get_posts_count(self, instance) -> int:
        return instance.posts.count()

    def get_followers_count(self, instance) -> int:
        return instance.followers.count()


class TagDetailSerializer(HashtagSerializer):

    class Meta:
        model = Hashtag
        fields = ('id', 'hashtag_label', 'posts_count', 'followers_count' ,'posts')




