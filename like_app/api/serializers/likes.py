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

    def validate(self, data):
        if data["user"] == data["post"].user:
            raise serializers.ValidationError("No like permission")
        return data


class LikesCommentSerializer(LikesSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'post',)

    def validate(self, data):
        print(data)
        if data["user"] == data["comment"].user:
            raise serializers.ValidationError("No like permission")
        return data