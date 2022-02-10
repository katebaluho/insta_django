from rest_framework import serializers

from like_app.models import Like


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user', )

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )


class LikesPostSerializer(LikesSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'comment',)


class LikesCommentSerializer(LikesSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'post',)