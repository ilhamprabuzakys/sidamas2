import django_filters as filters
from django_filters.filters import Q

from kegiatan import models
from users.models import Profile, Satker

# ======= PSM RAKERNIS FILTER =======
class PSM_RAKERNIS_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
    satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')

    class Meta:
        model = models.PSM_RAKERNIS
        fields = ['s', 'satker', 'satker_target']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value) |
            Q(satker_target__nama_satker__icontains=value)
        )
    
# ======= PSM BINAAN TEKNIS FILTER =======
class PSM_BINAAN_TEKNIS_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
    satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        fields = ['s', 'satker', 'satker_target']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value) |
            Q(satker_target__nama_satker__icontains=value)
        )

# ======= PSM ASISTENSI FILTER =======
class PSM_ASISTENSI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_ASISTENSI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value)
        )

# ======= PSM SINKRONISASI KEBIJAKAN FILTER =======
class PSM_SINKRONISASI_KEBIJAKAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_SINKRONISASI_KEBIJAKAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value)
        )

# ======= PSM WORKSHOP TEMATIK FILTER =======
class PSM_WORKSHOP_TEMATIK_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_WORKSHOP_TEMATIK
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(satker__nama_satker__icontains=value)
        )
# ======= PSM TES URINE DETEKSI DINI FILTER =======
class PSM_TES_URINE_DETEKSI_DINI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
    satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_provinsi = Satker.objects.values_list('provinsi_id', flat=True).get(id=satker)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        return queryset.filter(satker=satker)

# ======= PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN FILTER =======
class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)

        return queryset.filter(satker=satker)

# ======= PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN FILTER =======
class PSM_PENGUMPULAN_DATA_IKOTAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)

        return queryset.filter(satker=satker)
    
# ======= PSM DUKUNGAN STAKEHOLDER FILTER =======
class PSM_DUKUNGAN_STAKEHOLDER_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_DUKUNGAN_STAKEHOLDER
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)

        return queryset.filter(satker=satker)

# ======= PSM KEGIATAN LAINNYA FILTER =======
class PSM_KEGIATAN_LAINNYA_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_KEGIATAN_LAINNYA
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)

        return queryset.filter(satker=satker)

# ======= PSM RAKOR PEMETAAN FILTER =======
class PSM_RAKOR_PEMETAAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM AUDIENSI FILTER =======
class PSM_AUDIENSI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_AUDIENSI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM KONSOLIDASI_KEBIJAKAN FILTER =======
class PSM_KONSOLIDASI_KEBIJAKAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM KONSOLIDASI_KEBIJAKAN FILTER =======
class PSM_KONSOLIDASI_KEBIJAKAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM BIMTEK_P4GN FILTER =======
class PSM_BIMTEK_P4GN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_BIMTEK_P4GN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM WORKSHOP_PENGGIAT FILTER =======
class PSM_WORKSHOP_PENGGIAT_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_WORKSHOP_PENGGIAT
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )
    
# ======= PSM JADWAL KEGIATAN TAHUNAN FILTER =======
class PSM_JADWAL_KEGIATAN_TAHUNAN_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value)
        )

    def filter_by_leveling(self, queryset, name, value):
        user_id = self.user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)

        return queryset.filter(satker=satker)