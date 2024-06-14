import os
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from sidamas import pagination

from . import serializers
from . import filters
from . import models

class LiterasiViewSet(viewsets.ModelViewSet):
    queryset = models.Literasi.objects.all()
    serializer_class = serializers.LiterasiSerializer
    # permission_classes = [permissions.IsAuthenticated]    
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.LiterasiFilter
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        request_file = self.request.data.get('dokumen', None)
        
        if request_file and instance.dokumen:
            if os.path.isfile(instance.dokumen.path):
                os.remove(instance.dokumen.path)

        serializer.save(updated_by=self.request.user)
        
    def perform_destroy(self, instance):
        if instance.dokumen:
            if os.path.isfile(instance.dokumen.path):
                os.remove(instance.dokumen.path)
        instance.delete()
        
    @action(methods=['get'], detail=True)
    def increment_unduhan(self, request, pk):
        try:
            literasi = models.Literasi.objects.get(pk=pk)
            literasi.jumlah_diunduh += 1
            literasi.save()
            return Response({"message": "Jumlah unduhan berhasil diperbarui."}, status=status.HTTP_200_OK)
        except models.Literasi.DoesNotExist:
            return Response({"message": "Literasi tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
