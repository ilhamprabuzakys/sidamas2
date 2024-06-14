from django.contrib.auth.models import User
import django_filters as filters
from django_filters.filters import Q

from . import models

class UserFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    profile = filters.NumberFilter(field_name='profile__id', label='ID Profile')
    satker = filters.NumberFilter(field_name='profile__satker_id', label='ID Satuan Kerja')

    direktorat = filters.ChoiceFilter(field_name='profile__role', label='Direktorat', choices=models.Profile.DIREKTORAT_CHOICES)

    LEVEL_CHOICES = (
        (0, 'Provinsi'),
        (1, 'Kabupaten'),
        (2, 'Pusat')
    )

    satker_level = filters.ChoiceFilter(field_name='profile__satker__level', label='Level Satuan Kerja', choices=LEVEL_CHOICES)
    satker_parent = filters.NumberFilter(field_name='profile__satker__parent', label='Parent Satuan Kerja')

    class Meta:
        model = User
        fields = ['s', 'profile', 'satker', 'satker_level', 'satker_parent']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(username__icontains=value) |
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
        )

class SatkerFilter(filters.FilterSet):
    TYPE_CHOICES = (
        ("BNNP", "BNNP"),
        ("BNNK", "BNNK"),
        ("SEMUA", "SEMUA"),
    )

    id = filters.NumberFilter(field_name='id', label='ID')
    id_provinsi = filters.NumberFilter(field_name='provinsi', label='ID Provinsi')
    id_kabupaten = filters.CharFilter(field_name='kabupaten', label='ID Kabupaten')
    parent = filters.CharFilter(field_name='parent', label='ID Parent')
    is_type = filters.ChoiceFilter(method='filter_is_type', label='Is TYPE', choices=TYPE_CHOICES)
    s = filters.CharFilter(method='filter_global_search', label='Global search')

    class Meta:
        model = models.Satker
        fields = ['s', 'id', 'id_kabupaten', 'id_provinsi', 'nama_satker']


    def filter_is_type(self, queryset, name, value):
        if value == 'BNNP':
            return queryset.filter(Q(nama_satker__icontains='BNNP'))
        elif value == 'BNNK':
            return queryset.filter(Q(nama_satker__icontains='BNN Kabupaten') | Q(nama_satker__icontains='BNN Kota'))
        else:
            return queryset.all()

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(nama_satker__icontains=value)
        )

class UraianKegiatanFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    no = filters.NumberFilter(field_name='no', label='Nomor')
    pj = filters.CharFilter(field_name='pj', label='PJ')

    kegiatan_akun = filters.ModelChoiceFilter(field_name='kegiatan_akun', label='Kegiatan Akun', queryset=models.Kegiatan_akun.objects.all())

    class Meta:
        model = models.Uraian_kegiatan
        fields = ['s', 'no', 'uraian_kegiatan', 'keterangan', 'pj', 'kegiatan_akun']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(no__icontains=value) |
            Q(uraian_kegiatan__icontains=value) |
            Q(keterangan__icontains=value) |
            Q(pj__icontains=value)
        )