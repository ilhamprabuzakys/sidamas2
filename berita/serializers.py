from rest_framework import serializers

from . import models


class BeritaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Berita
        fields = '__all__'
        datatables_always_serialize = ['slug', 'judul']
        depth = 1

class KategoriSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Kategori
        fields = [
            "created_at",
            "updated_at",
            "nama",
        ]

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = [
            "created_at",
            "updated_at",
            "nama",
        ]

