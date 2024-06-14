from rest_framework import viewsets, permissions
from rest_framework.response import Response

from . import serializers
from . import models


class userViewSet(viewsets.ModelViewSet):
    """ViewSet for the user class"""

    queryset = models.user.objects.all()
    serializer_class = serializers.userSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Extract the values of nilai and nilai2 from the serializer
        nilai = serializer.validated_data['nilai']
        nilai2 = serializer.validated_data['nilai2']

        # Calculate the hasil and add it to the serializer data
        hasil = int(nilai) + int(nilai2)
        serializer.validated_data['hasil'] = hasil

        # Call the serializer's save method to save the instance to the database
        serializer.save()

    def perform_update(self, serializer):
        # Extract the values of nilai and nilai2 from the serializer
        nilai = serializer.validated_data['nilai']
        nilai2 = serializer.validated_data['nilai2']

        # Calculate the hasil and update it in the serializer data
        hasil = int(nilai) + int(nilai2)
        serializer.validated_data['hasil'] = hasil

        # Call the serializer's save method to update the instance in the database
        serializer.save()

class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = models.image.objects.all()
    serializer_class = serializers.ImageModelSerializer
    permission_classes = [permissions.IsAuthenticated]

