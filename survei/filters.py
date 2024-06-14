from django.contrib.auth.models import User
import django_filters as filters
from django_filters.filters import Q

from . import models

class TipeSurveiFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    direktorat = filters.ChoiceFilter(field_name='direktorat', label='Direktorat', choices=models.TipeSurvei.DIREKTORAT_CHOICES)

    class Meta:
        model = models.TipeSurvei
        fields = ['s', 'direktorat']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(nama__icontains=value) |
            Q(kode__icontains=value) |
            Q(direktorat__icontains=value)
        )

# ======= Data Survei Intelijen =======
class DataIntelijenRespondenSurveiFilter(filters.FilterSet):
    parent = filters.ModelChoiceFilter(field_name='parent', label='Parent sumber', queryset=models.DataIntelijenSurvei.objects.all()) # Menggunakan queryset=models.DataIntelijenSurvei.objects.all() untuk mengambil semua objek dari model DataIntelijenSurvei

    class Meta:
        model = models.DataIntelijenRespondenSurvei
        fields = ['parent']

class DataIntelijenSurveiFilter(filters.FilterSet):
    parent = filters.ModelChoiceFilter(field_name='parent', label='Parent sumber', queryset=models.DataIntelijenSumberSurvei.objects.all()) # Menggunakan queryset=models.DataIntelijenSumberSurvei.objects.all() untuk mengambil semua objek dari model DataIntelijenSumberSurvei

    class Meta:
        model = models.DataIntelijenSurvei
        fields = ['parent']
