import django_filters as filters
from django_filters.filters import Q

from kegiatan import models

# ======= BINAAN TEKNIS =======
class DAYATIF_BINAAN_TEKNIS_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    nama_satker = filters.CharFilter(method='nama_satker', label='Nama Satker')

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        fields = ['s']
        order_by = ['-nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(nama_satker__icontains=value)
        )

# ======= PEMETAAN POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        fields = ['satker', 's']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value)
        )

# ======= PEMETAAN STAKEHOLDER =======
class DAYATIF_PEMETAAN_STAKEHOLDER_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        fields = ['satker', 's']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value)
        )
