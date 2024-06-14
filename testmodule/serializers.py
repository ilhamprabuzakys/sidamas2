from rest_framework import serializers

from . import models


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.user
        fields = [
            "created",
            "last_updated",
            "nilai",
            "nilai2",
            "hasil",
            "pengguna",
        ]
        read_only_fields = ('created', 'last_updated')
    hasil = serializers.CharField(allow_null=True, required=False)

class ImageModelSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.image
        fields = ('id', 'title', 'image')