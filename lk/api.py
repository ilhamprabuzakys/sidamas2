from rest_framework import viewsets, permissions

from . import serializers
from . import models


class tbl_eformViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_eform class"""

    queryset = models.tbl_eform.objects.all()
    serializer_class = serializers.tbl_eformSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_responden_eformViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_responden_eform class"""

    queryset = models.tbl_responden_eform.objects.all()
    serializer_class = serializers.tbl_responden_eformSerializer
    permission_classes = [permissions.IsAuthenticated]