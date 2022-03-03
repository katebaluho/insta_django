from rest_framework import serializers

from comments_app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.likes.count()



class CommentDetailSerializer(CommentSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentUpdateSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ('text', )

