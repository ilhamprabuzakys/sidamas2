from rest_framework import viewsets, permissions

from . import serializers
from . import models


# class Rakernis_psmViewSet(viewsets.ModelViewSet):
#     """ViewSet for the literasi class"""

#     queryset = models.rakernis_psm.objects.all()
#     serializer_class = serializers.Rakernis_psmSerializer
#     permission_classes = [permissions.IsAuthenticated]
