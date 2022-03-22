from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from account_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'user',)

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'user',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'groups', 'user_permissions', 'date_joined']
        read_only_fields = ['last_login', 'is_active']
        extra_kwargs = {
            'profile': {'required': True, 'write_only': True, 'help_text': 'Info about user'}
        }

    profile_user = ProfileSerializer(source='profile', read_only=True)

    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()

    @extend_schema_field(str)
    def get_followers_count(self, instance):
        return instance.followers.count()

    @extend_schema_field(str)
    def get_followings_count(self, instance):
        return instance.followings.count()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
