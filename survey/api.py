from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters

from . import serializers
from . import models

class surveyViewSet(viewsets.ModelViewSet):
    """ViewSet for the kategori class"""

    queryset = models.survey.objects.all()
    serializer_class = serializers.survey
    #permission_classes = [permissions.IsAuthenticated]

class surveycreateViewSet(viewsets.ModelViewSet):
    """ViewSet for the kategori class"""

    queryset = models.survey.objects.all()
    serializer_class = serializers.survey_create
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ('kode',)
    #permission_classes = [permissions.IsAuthenticated]

class surveyshortViewSet(viewsets.ModelViewSet):
    """ViewSet for the berita class"""

    queryset = models.surveyshort.objects.all()
    serializer_class = serializers.surveyshort
    #permission_classes = [permissions.IsAuthenticated]

class survey_resultViewSet(viewsets.ModelViewSet):
    """ViewSet for the berita class"""

    queryset = models.survey_result.objects.all()
    serializer_class = serializers.survey_result
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def get_detail_data(self, request):
        survey_id = request.GET.get('id')
        survey_title = models.survey.objects.values_list('judul', flat=True).get(id=survey_id)
        serialized_data = []
        if(survey_title):
            result = models.survey_result.objects.values('id', 'hasil', 'user_id').filter(survey_id=survey_id)
            serialized_data = {
                'survey_title' : survey_title,
                'result': result
            }
        return Response(serialized_data, status=status.HTTP_200_OK)
