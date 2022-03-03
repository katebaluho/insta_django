from rest_framework import serializers, filters

from hashtag_app.api.serializers.hashtags import HashtagSerializer
from hashtag_app.models import Hashtag
from media_app.api.serializers.media import MediaSerializer
from media_app.models import Media
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['id', 'user']
        exclude = ['is_public']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    file = MediaSerializer()

    hashtags = serializers.StringRelatedField(many=True)
    comments = serializers.StringRelatedField(many=True)
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()


    def get_likes_count(self, instance) -> int:
        return instance.likes.count()

    def get_comments_count(self, instance) -> int:
        return instance.comments.count()


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('user','is_public','create_date')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )

    file = serializers.ImageField()

    def create(self, validated_data):
        media = Media.objects.create(file=validated_data.pop('file'), user=validated_data['user'])
        post = Post.objects.create(file=media, **validated_data)
        return post