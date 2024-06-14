from rest_framework import viewsets, permissions

from . import serializers
from . import models


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for the Tag class"""

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class KategoriViewSet(viewsets.ModelViewSet):
    """ViewSet for the Kategori class"""

    queryset = models.Kategori.objects.all()
    serializer_class = serializers.KategoriSerializer
    permission_classes = [permissions.IsAuthenticated]


class BeritaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Berita class"""

    queryset = models.Berita.objects.all()
    serializer_class = serializers.BeritaSerializer
    permission_classes = [permissions.IsAuthenticated]