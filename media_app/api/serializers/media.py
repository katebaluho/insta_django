from rest_framework import serializers

from ...models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id','file', )


    # publisher_user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(),
    #     source="user"
    # )

    file = serializers.ImageField(required=True, allow_null=False)