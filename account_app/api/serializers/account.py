from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from account_app.models import Profile
from media_app.api.serializers.media import MediaSerializer
from media_app.models import Media


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'user', )


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'user', )


class UserSerializer(serializers.ModelSerializer):
    # for main view insta profile
    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'groups', 'user_permissions', 'date_joined']
        read_only_fields = ['last_login', 'is_active']
        extra_kwargs = {
            'profile': {'required' : True, 'write_only': True, 'help_text': 'Info about user'}
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


class UserPreviewSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'is_active','profile')

    #TODO ERROR
    profile = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='avatar'
    )





