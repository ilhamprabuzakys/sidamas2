from django.db.models.functions import ExtractMonth, ExtractYear
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core import exceptions as django_exceptions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework_datatables.pagination import DatatablesPageNumberPagination
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter
from django.core import serializers
from django.db.models import Q, Count
import json
import ast

from survey.models import survey

from . import serializers
from . import models
from . import filters
from sidamas import pagination


# class DAYATIF_KegiatanCountView(APIView):

#     def get(self, request):
#         current_year = timezone.now().year
#         satker_id = request.query_params.get('satker', None)

#         def get_counts(queryset, satker_id):
#             if satker_id:
#                 queryset = queryset.filter(satker_id=satker_id)
#             counts = queryset.annotate(
#                 year=ExtractYear('created_at'),
#                 month=ExtractMonth('created_at')
#             ).values('year', 'month').annotate(
#                 total=Count('id')
#             ).order_by('year', 'month')

#             result = {}
#             for item in counts:
#                 year = item['year']
#                 month = item['month']
#                 if year not in result:
#                     result[year] = {m: 0 for m in range(1, 13)}
#                     result[year]['total'] = 0
#                 result[year][month] = item['total']
#                 result[year]['total'] += item['total']

#             # Ensure all months are present with a value of 0 if no data is found
#             for year in result:
#                 for month in range(1, 13):
#                     if month not in result[year]:
#                         result[year][month] = 0

#             # Ensure the current year is present in the result
#             if current_year not in result:
#                 result[current_year] = {m: 0 for m in range(1, 13)}
#                 result[current_year]['total'] = 0

#             return result

#         tipe_skm_lifeskill = models.TipeSurvei.objects.get(nama="SKM Life Skill")
#         skm_lifeskill = models.DataSurvei.objects.filter(tipe=tipe_skm_lifeskill.id)

#         data = {
#             'formulir_elektronik': get_counts(survey.objects.all(), satker_id),
#             'skm_life_skill': get_counts(skm_lifeskill, satker_id),
#             'pemetaan_stakeholder': get_counts(models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.all(), satker_id),
#             'rapat_sinergi_stakeholder': get_counts(models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER.objects.all(), satker_id),
#             'bimbingan_teknis_stakeholder': get_counts(models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER.objects.all(), satker_id),
#             'bimbingan_teknis_lifeskill': get_counts(models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL.objects.all(), satker_id),
#             'monitoring_dan_evaluasi': get_counts(models.DAYATIF_MONEV_DAYATIF.objects.all(), satker_id),
#             'dukungan_stakeholder': get_counts(models.DAYATIF_DUKUNGAN_STAKEHOLDER.objects.all(), satker_id)
#         }

#         return Response({
#             'status': True,
#             'data': data
#         }, status=status.HTTP_200_OK)


class TipeSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipeSurvei class"""

    queryset = models.TipeSurvei.objects.all()
    serializer_class = serializers.TipeSurveiSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = filters.TipeSurveiFilter
    # filterset_fields = ['direktorat']

class DataSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataSurvei class"""

    queryset = models.DataSurvei.objects.all()
    serializer_class = serializers.DataSurveiSerializer
    filter_backends = [DjangoFilterBackend,]
    # filterset_fields = ('id',)
    pagination_class = pagination.Page100NumberPagination

    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        kode_value = self.request.query_params.get('kode')
        if kode_value:
            return models.DataSurvei.objects.filter(kode=kode_value)

        return models.DataSurvei.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return serializers.DataSurveiDetailSerializer
    #     return serializers.DataSurveiSerializer

    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def triwulan(self, request):
        try:
            triwulan = request.data.get('triwulan')
            tipe = request.data.get('tipe')
            tipe_survei = models.TipeSurvei.objects.get(nama=tipe)

            triwulan_json = json.dumps(triwulan)

            triwulan_lista = json.loads(triwulan_json)

            months = triwulan_lista[0]
            year = triwulan_lista[1]
            satker = triwulan_lista[2]

            month_filters = Q()
            for month in months:
                month_filters |= Q(created_at__month=month, created_at__year=year)

            if satker == 0:
                data_survei_queryset = models.DataSurvei.objects.filter(month_filters, tipe = tipe_survei.id)
            else:
                data_survei_queryset = models.DataSurvei.objects.filter(month_filters, tipe = tipe_survei.id, satker=satker)

            serialized_data = self.serializer_class(data_survei_queryset, many=True).data

            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def life_skill(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="SKM Life Skill")
            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data

            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def test_urine(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="SKM Tes Urine")

            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data

            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def keberhasilan_kewirausahaan(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="Keberhasilan dan Kewirausahaan")

            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data

            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)


class DataRespondenSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataRespondenSurvei class"""

    queryset = models.DataRespondenSurvei.objects.all()
    serializer_class = serializers.DataRespondenSurveiSerializer
    filterset_fields = ('survei',)
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        survei_id = self.request.query_params.get('survei')
        if survei_id:
            return models.DataRespondenSurvei.objects.filter(survei=survei_id)
        return models.DataRespondenSurvei.objects.all()

    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def get_nama(self, request):
        try:
            nama = request.data.get('nama')

            responden = models.DataRespondenSurvei.objects.get(nama=nama)

            return Response({'data': True}, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'data': False}, status=status.HTTP_200_OK)

class DataPengisianSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataPengisianSurvei class"""

    queryset = models.DataPengisianSurvei.objects.all()
    serializer_class = serializers.DataPengisianSurveiSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('responden', 'survei',)

    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def triwulan(self, request):
        try:
            triwulan = request.data.get('triwulan')

            triwulan_json = json.dumps(triwulan)

            triwulan_lista = json.loads(triwulan_json)

            months = triwulan_lista[0]
            year = triwulan_lista[1]

            month_filters = Q()
            for month in months:
                month_filters |= Q(created_at__month=month, created_at__year=year)

            data_survei_queryset = models.DataPengisianSurvei.objects.filter(month_filters)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data

            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)


# --------------------------
# SURVEI INTELIJEN
# -----------------------------
class DataIntelijenSumberSurveiViewSet(viewsets.ModelViewSet):
    queryset = models.DataIntelijenSumberSurvei.objects.all()
    serializer_class = serializers.DataIntelijenSumberSurveiSerializer
    # filter_backends = [DjangoFilterBackend,]

class DataIntelijenSurveiViewSet(viewsets.ModelViewSet):
    queryset = models.DataIntelijenSurvei.objects.all()
    serializer_class = serializers.DataIntelijenSurveiSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = filters.DataIntelijenSurveiFilter

class DataIntelijenRespondenSurveiViewSet(viewsets.ModelViewSet):
    queryset = models.DataIntelijenRespondenSurvei.objects.all()
    serializer_class = serializers.DataIntelijenRespondenSurveiSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = filters.DataIntelijenRespondenSurveiFilter