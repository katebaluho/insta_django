from django.contrib.auth.models import User
from rest_framework import serializers

from account_app.models import Profile
from media_app.api.serializers.media import MediaSerializer


class ProfileSerializator(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields  = '__all__'
        read_only_fields = ('id', 'user')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    media = MediaSerializer(source='avatar', allow_null=True, read_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'groups', 'user_permissions']
        read_only_fields = ['id','last_login', 'date_joined', 'is_active', 'profile']
        extra_kwargs = {
            'profile': {'required' : True, 'write_only': True, 'help_text': 'Info about user'}
        }

    profile_user = ProfileSerializator(source='profile', read_only=True)

    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()

    def get_followers_count(self, instance):
        return instance.followers.count()

    def get_followings_count(self, instance):
        return instance.followings.count()



