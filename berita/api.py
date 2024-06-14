import os
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from sidamas import pagination

from . import serializers
from . import models
from . import filters


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
    queryset = models.Berita.objects.all()
    serializer_class = serializers.BeritaSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.BeritaFilter
    
    def perform_create(self, serializer):
        if not serializer.validated_data.get('slug'):
            serializer.validated_data['slug'] = slugify(serializer.validated_data['judul'])
        serializer.save(created_by=self.request.user, kategori_id=self.request.data.get('kategori'))

    def perform_update(self, serializer):
        instance = serializer.instance
        request_file = self.request.data.get('gambar_utama', None)
        
        if request_file and instance.gambar_utama:
            if os.path.isfile(instance.gambar_utama.path):
                os.remove(instance.gambar_utama.path)

        if not serializer.validated_data.get('slug'):
            serializer.validated_data['slug'] = slugify(serializer.validated_data['judul'])
        
        serializer.save(updated_by=self.request.user)
        
    def perform_destroy(self, instance):
        if instance.gambar_utama:
            if os.path.isfile(instance.gambar_utama.path):
                os.remove(instance.gambar_utama.path)
        instance.delete()