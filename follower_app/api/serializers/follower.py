from rest_framework import serializers

from follower_app.models import Follower, FollowingHashtag


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'
        read_only_fields = ('follower', 'create_date')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="follower"
    )

class FollowerHashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowingHashtag
        fields = '__all__'
        read_only_fields = ('follower', 'create_date')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="follower"
    )