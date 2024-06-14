import django_filters as filters
from django_filters.filters import Q

from . import models

class BeritaFilter(filters.FilterSet):
    status = filters.ChoiceFilter(field_name='status', choices=models.Berita.STATUS_CHOICES, label='Status')
    s = filters.CharFilter(method='filter_global_search', label='Global search')

    class Meta:
        model = models.Berita
        fields = ['status', 's']
        order_by = ['judul', 'created_at', 'updated_at']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(judul__icontains=value) |
            Q(status__icontains=value) |
            Q(created_by__first_name__icontains=value)
        )