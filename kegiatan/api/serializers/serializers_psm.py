from rest_framework import serializers

from kegiatan import models
from users.models import Profile, Satker, Kegiatan_akun
from kegiatan.serializers import SatkerSerializer, UserSerializer

from django.utils import timezone

# ======= PSM RAKERNIS SERIALIZER =======
class PSM_RAKERNIS_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'satker_target',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'drive_url','dokumentasi', 'anggaran','penyerapan_anggaran','status'
        ]

class PSM_RAKERNIS_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKERNIS_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_RAKERNIS_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_RAKERNIS_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKERNIS_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_RAKERNIS_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    satker_target = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_RAKERNIS
        fields = '__all__'

# ======= PSM BINAAN TEKNIS SERIALIZER =======
class PSM_BINAAN_TEKNIS_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'satker_target',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'drive_url','dokumentasi', 'anggaran','penyerapan_anggaran', 'status'
        ]

class PSM_BINAAN_TEKNIS_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]
    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_BINAAN_TEKNIS_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    # satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_BINAAN_TEKNIS_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_BINAAN_TEKNIS_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_BINAAN_TEKNIS_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    satker_target = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        fields = '__all__'

# ======= PSM ASISTENSI SERIALIZER =======
class PSM_ASISTENSI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'jumlah_kegiatan', 'jumlah_peserta', 'stakeholder',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url' , 'dokumentasi', 'status'
        ]

class PSM_ASISTENSI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','satker','data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_ASISTENSI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_ASISTENSI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_ASISTENSI_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_ASISTENSI_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_ASISTENSI_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_ASISTENSI
        fields = '__all__'

# ======= PSM SINKRONISASI KEBIJAKAN SERIALIZER =======
class PSM_SINKRONISASI_KEBIJAKAN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_SINKRONISASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'jumlah_kegiatan', 'jumlah_peserta', 'stakeholder',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'status'
        ]

class PSM_SINKRONISASI_KEBIJAKAN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_SINKRONISASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','satker','data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_SINKRONISASI_KEBIJAKAN_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_SINKRONISASI_KEBIJAKAN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_SINKRONISASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_SINKRONISASI_KEBIJAKAN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_SINKRONISASI_KEBIJAKAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_SINKRONISASI_KEBIJAKAN_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_SINKRONISASI_KEBIJAKAN_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_SINKRONISASI_KEBIJAKAN
        fields = '__all__'

# ======= PSM WORKSHOP TEMATIK SERIALIZER =======
class PSM_WORKSHOP_TEMATIK_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_WORKSHOP_TEMATIK
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'jumlah_kegiatan', 'jumlah_peserta', 'stakeholder',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'status'
        ]

class PSM_WORKSHOP_TEMATIK_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_WORKSHOP_TEMATIK
        exclude = []
        fields = [
            'id','satker','data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_WORKSHOP_TEMATIK_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_WORKSHOP_TEMATIK_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_WORKSHOP_TEMATIK
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_WORKSHOP_TEMATIK_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_TEMATIK.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_WORKSHOP_TEMATIK_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_WORKSHOP_TEMATIK_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_WORKSHOP_TEMATIK
        fields = '__all__'

# ======= PSM TES URINE DETEKSI DINI SERIALIZER =======
class PSM_TES_URINE_DETEKSI_DINI_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI_PESERTA
        fields = ['id', 'parent', 'nama_peserta', 'jenis_kelamin', 'hasil_test', 'isi_parameter', 'alamat']

class PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    pegawai = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        datatables_always_serialize = ['id', 'satker', 'nama_satker', 'jumlah_kegiatan', 'tanggal', 'nama_lingkungan', 'hasil_tes_urine', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'pegawai']

    def get_pegawai(self, obj):
        parent_id = obj.id
        pegawai_objects = models.PSM_TES_URINE_DETEKSI_DINI_PESERTA.objects.filter(parent=parent_id)
        ret = PSM_TES_URINE_DETEKSI_DINI_PESERTA_Serializer(pegawai_objects, many=True).data
        return ret

class PSM_TES_URINE_DETEKSI_DINI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]
    def get_data(self, obj):

        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker)
        ret = PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(res, many=True).data
        return ret

class PSM_TES_URINE_DETEKSI_DINI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    # satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_provinsi = Satker.objects.values_list('provinsi_id', flat=True).get(id=satker)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker)
        ret = PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_provinsi = Satker.objects.values_list('provinsi_id', flat=True).get(id=satker)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_TES_URINE_DETEKSI_DINI_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker__parent = obj.satker).order_by('satker__id').distinct('satker__id')
        ret = PSM_TES_URINE_DETEKSI_DINI_CHILD_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_TES_URINE_DETEKSI_DINI_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        fields = ['id', 'satker', 'satker_target', 'tanggal_awal', 'tanggal_akhir', 'nama_lingkungan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi']

class PSM_TEST_URINE_DETEKSI_DINI_COUNT(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_TES_URINE_COUNT
        fields = ['id', 'nama_satker', 'peserta_count_2021', 'peserta_count_2022', 'peserta_count_2023', 'peserta_count_2024']

# ======= PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN SERIALIZER =======
class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA
        fields = ['id', 'parent', 'nama_peserta', 'jenis_kelamin', 'jabatan', 'parent_id']

    def __init__(self, *args, parent_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def to_internal_value(self, data):
        data['parent'] = self.parent_id
        return super().to_internal_value(data)

class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    pegawai = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI
        exclude = []
        datatables_always_serialize = ['id', 'satker', 'jumlah_kegiatan', 'tanggal_awal', 'tanggal_akhir', 'nama_lingkungan', 'status_indeks', 'nilai_ikp', 'status_ikp', 'deskripsi_hasil', 'simpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'pegawai']

    def get_pegawai(self, obj):
        parent_id = obj.id
        pegawai_objects = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA.objects.filter(parent=parent_id)
        ret = PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA_Serializer(pegawai_objects, many=True).data
        return ret

class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI
        exclude = []
        fields = [
            'id','satker', 'data'
        ]
    def get_data(self, obj):

        res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker = obj.satker)
        ret = PSM_MONITORING_DAN_EVALUASI_SUPERVISI_DATA_Serializer(res, many=True).data
        return ret

class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_MONITORING_DAN_EVALUASI_SUPERVISI_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

        res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker = obj.satker)
        ret = PSM_MONITORING_DAN_EVALUASI_SUPERVISI_DATA_Serializer(res, many=True).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_MONITORING_DAN_EVALUASI_SUPERVISI_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_MONITORING_DAN_EVALUASI_SUPERVISI
        fields = ['id', 'satker', 'tanggal_awal', 'tanggal_akhir', 'nama_lingkungan', 'status_indeks', 'nilai_ikp', 'status_ikp', 'deskripsi_hasil', 'simpulan', 'tindak_lanjut',  'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi']

# ======= PSM PENGUMPULAN DATA IKOTAN SERIALIZER =======
class PSM_PENGUMPULAN_DATA_IKOTAN_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN_PESERTA
        fields = ['id', 'parent', 'nama_peserta']

    def __init__(self, *args, parent_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def to_internal_value(self, data):
        data['parent'] = self.parent_id
        return super().to_internal_value(data)

class PSM_PENGUMPULAN_DATA_IKOTAN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    pegawai = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN
        exclude = []
        datatables_always_serialize = ['id', 'observasi', 'tanggal_awal', 'tanggal_akhir', 'satker', 'deskripsi_hasil', 'deskripsi_hasil', 'simpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'pegawai']

    def get_pegawai(self, obj):
        parent_id = obj.id
        pegawai_objects = models.PSM_PENGUMPULAN_DATA_IKOTAN_PESERTA.objects.filter(parent=parent_id)
        ret = PSM_PENGUMPULAN_DATA_IKOTAN_PESERTA_Serializer(pegawai_objects, many=True).data
        return ret

class PSM_PENGUMPULAN_DATA_IKOTAN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN
        exclude = []
        fields = [
            'id','satker','data'
        ]
    def get_data(self, obj):

        res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker = obj.satker)
        ret = PSM_PENGUMPULAN_DATA_IKOTAN_DATA_Serializer(res, many=True).data
        return ret

class PSM_PENGUMPULAN_DATA_IKOTAN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_PENGUMPULAN_DATA_IKOTAN_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_PENGUMPULAN_DATA_IKOTAN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_PENGUMPULAN_DATA_IKOTAN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

class PSM_PENGUMPULAN_DATA_IKOTAN_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_PENGUMPULAN_DATA_IKOTAN
        fields = ['id', 'observasi', 'tanggal_awal', 'tanggal_akhir','satker', 'deskripsi_hasil', 'deskripsi_hasil', 'simpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi']

# ======= PSM DUKUNGAN STAKEHOLDER SERIALIZER =======
class PSM_DUKUNGAN_STAKEHOLDER_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)

    class Meta:
        model = models.PSM_DUKUNGAN_STAKEHOLDER
        exclude = []
        datatables_always_serialize = ['id', 'satker', 'pemda', 'kegiatan', 'alamat', 'jumlah_sasaran', 'hasil_dampak', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi']

class PSM_DUKUNGAN_STAKEHOLDER_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_DUKUNGAN_STAKEHOLDER
        exclude = []
        fields = [
            'id','satker','data'
        ]
    def get_data(self, obj):

        res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker = obj.satker)
        ret = PSM_DUKUNGAN_STAKEHOLDER_DATA_Serializer(res, many=True).data
        return ret

class PSM_DUKUNGAN_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_DUKUNGAN_STAKEHOLDER
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_DUKUNGAN_STAKEHOLDER_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

        res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker = obj.satker)
        ret = PSM_DUKUNGAN_STAKEHOLDER_DATA_Serializer(res, many=True).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_DUKUNGAN_STAKEHOLDER.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_DUKUNGAN_STAKEHOLDER_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

class PSM_DUKUNGAN_STAKEHOLDER_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_DUKUNGAN_STAKEHOLDER
        fields = ['id', 'satker', 'pemda', 'kegiatan', 'alamat', 'jumlah_sasaran', 'hasil_dampak', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi']

# ======= PSM KEGIATAN LAINNYA SERIALIZER =======
class PSM_KEGIATAN_LAINNYA_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)

    class Meta:
        model = models.PSM_KEGIATAN_LAINNYA
        exclude = []
        depth = 1
        datatables_always_serialize = ['id', 'satker', 'kegiatan', 'tempat', 'waktu_awal', 'waktu_akhir', 'lingkungan', 'jumlah_sasaran', 'hasil_dampak', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'kegiatan_akun', 'uraian_kegiatan', 'drive_url', 'anggaran', 'penyerapan_anggaran']

class PSM_KEGIATAN_LAINNYA_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_KEGIATAN_LAINNYA
        exclude = []
        fields = [
            'id','satker','data'
        ]
    def get_data(self, obj):

        res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker = obj.satker)
        ret = PSM_KEGIATAN_LAINNYA_DATA_Serializer(res, many=True).data
        return ret

class PSM_KEGIATAN_LAINNYA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_KEGIATAN_LAINNYA
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_KEGIATAN_LAINNYA_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

        res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker = obj.satker)
        ret = PSM_KEGIATAN_LAINNYA_DATA_Serializer(res, many=True).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_KEGIATAN_LAINNYA.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_KEGIATAN_LAINNYA_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

class PSM_KEGIATAN_LAINNYA_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_KEGIATAN_LAINNYA
        fields = ['id', 'satker', 'kegiatan', 'tempat', 'waktu_awal', 'waktu_akhir', 'lingkungan', 'jumlah_sasaran', 'hasil_dampak', 'kesimpulan', 'tindak_lanjut', 'anggaran', 'penyerapan_anggaran', 'drive_url', 'dokumentasi', 'kegiatan_akun', 'uraian_kegiatan', 'drive_url', 'anggaran', 'penyerapan_anggaran']

# ======= PSM RAKOR PEMETAAN SERIALIZER =======
class PSM_RAKOR_PEMETAAN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker__parent = obj.satker).order_by('satker__id').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id').distinct('satker__id')

        ret = PSM_RAKOR_PEMETAAN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKOR_PEMETAAN_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_RAKOR_PEMETAAN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        exclude = []
        fields = [
            'id','satker', 'data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKOR_PEMETAAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKOR_PEMETAAN_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_RAKOR_PEMETAAN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'nama_lingkungan', 'peserta',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'status'
        ]

class PSM_RAKOR_PEMETAAN_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        fields = '__all__'

# ======= PSM AUDIENSI SERIALIZER =======
class PSM_AUDIENSI_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_AUDIENSI
        fields = '__all__'

class PSM_AUDIENSI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_AUDIENSI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_AUDIENSI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_AUDIENSI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_AUDIENSI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_AUDIENSI_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_AUDIENSI_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_AUDIENSI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_AUDIENSI
        exclude = []
        fields = [
            'id','satker', 'data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_AUDIENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_AUDIENSI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_AUDIENSI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_AUDIENSI
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'nama_lingkungan', 'peserta',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut','anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'status'
        ]

# ======= PSM KONSOLIDASI KEBIJAKAN SERIALIZER =======
class PSM_KONSOLIDASI_KEBIJAKAN_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        fields = '__all__'

class PSM_KONSOLIDASI_KEBIJAKAN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_KONSOLIDASI_KEBIJAKAN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_KONSOLIDASI_KEBIJAKAN_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_KONSOLIDASI_KEBIJAKAN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','satker', 'data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_KONSOLIDASI_KEBIJAKAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_KONSOLIDASI_KEBIJAKAN_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_KONSOLIDASI_KEBIJAKAN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_KONSOLIDASI_KEBIJAKAN
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'stakeholder', 'peserta',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut','anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'status'
        ]

# ======= PSM WORKSHOP PENGGIAT SERIALIZER =======
class PSM_WORKSHOP_PENGGIAT_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_WORKSHOP_PENGGIAT
        fields = '__all__'

class PSM_WORKSHOP_PENGGIAT_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_WORKSHOP_PENGGIAT
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_WORKSHOP_PENGGIAT_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_WORKSHOP_PENGGIAT_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_WORKSHOP_PENGGIAT_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_WORKSHOP_PENGGIAT
        exclude = []
        fields = [
            'id','satker', 'data'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_WORKSHOP_PENGGIAT.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_WORKSHOP_PENGGIAT_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_WORKSHOP_PENGGIAT_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_WORKSHOP_PENGGIAT
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'stakeholder', 'peserta',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'status'
        ]

# ======= PSM BIMBINGAN TEKNIS PENGGIAT P4GN SERIALIZER =======
class PSM_BIMTEK_P4GN_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_BIMTEK_P4GN
        fields = '__all__'

class PSM_BIMTEK_P4GN_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_BIMTEK_P4GN_PESERTA
        fields = ['id', 'parent', 'nama', 'jabatan', 'jenis_kelamin', 'alamat', 'no_telepon']

    def __init__(self, *args, parent_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def to_internal_value(self, data):
        data['parent'] = self.parent_id
        return super().to_internal_value(data)

class PSM_BIMTEK_P4GN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    peserta_bimtek = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BIMTEK_P4GN
        exclude = []
        datatables_always_serialize = [
            'id', 'satker', 'seri_pin_penggiat', 'tanggal_awal', 'tanggal_akhir', 'nama_lingkungan',
            'kendala', 'hasil_capaian', 'kesimpulan', 'tindak_lanjut', 'anggaran','penyerapan_anggaran','drive_url', 'dokumentasi', 'peserta_bimtek', 'peserta'
        ]

    def get_peserta_bimtek(self, obj):
        parent_id = obj.id
        peserta_bimtek_objects = models.PSM_BIMTEK_P4GN_PESERTA.objects.filter(parent=parent_id)
        ret = PSM_BIMTEK_P4GN_PESERTA_Serializer(peserta_bimtek_objects, many=True).data
        return ret

class PSM_BIMTEK_P4GN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BIMTEK_P4GN
        exclude = []
        fields = [
            'id','satker', 'data'
        ]
    def get_data(self, obj):

        res = models.PSM_BIMTEK_P4GN.objects.filter(satker = obj.satker)
        ret = PSM_BIMTEK_P4GN_DATA_Serializer(res, many=True).data
        return ret

class PSM_BIMTEK_P4GN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BIMTEK_P4GN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        res = models.PSM_BIMTEK_P4GN.objects.filter(satker = obj.satker)
        ret = PSM_BIMTEK_P4GN_DATA_Serializer(res, many=True).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_BIMTEK_P4GN.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BIMTEK_P4GN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_BIMTEK_P4GN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_BIMTEK_P4GN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

# ======= PSM KEGIATAN LAINNYA SERIALIZER =======
class PSM_JADWAL_KEGIATAN_TAHUNAN_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    kode_no_unit = serializers.CharField(source='kode.no_unit', read_only=True)
    uraian_no = serializers.CharField(source='uraian.no', read_only=True)

    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        exclude = []
        datatables_always_serialize = ['id', 'satker', 'kode_no_unit', 'uraian_no', 'nama_kegiatan', 'waktu_kegiatan', 'metode_kegiatan', 'tempat_pelaksana', 'jumlah_peserta', 'keterangan', 'created_at']

class PSM_JADWAL_KEGIATAN_TAHUNAN_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        exclude = []
        fields = [
            'id','satker','data'
        ]
    def get_data(self, obj):

        res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker = obj.satker)
        ret = PSM_JADWAL_KEGIATAN_TAHUNAN_DATA_Serializer(res, many=True).data
        return ret

class PSM_JADWAL_KEGIATAN_TAHUNAN_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_JADWAL_KEGIATAN_TAHUNAN_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        if satker_level == 1:
            # bnnk
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_JADWAL_KEGIATAN_TAHUNAN_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        return ret

class PSM_JADWAL_KEGIATAN_TAHUNAN_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        fields = ['id', 'satker', 'kode', 'uraian', 'nama_kegiatan', 'waktu_kegiatan', 'metode_kegiatan', 'tempat_pelaksana', 'jumlah_peserta', 'keterangan', 'created_at']

class PSM_JADWAL_SERIALIZERS(serializers.ModelSerializer):
    kegiatan = serializers.SerializerMethodField()

    class Meta:
        model = Kegiatan_akun
        fields = ['id', 'no_unit', 'akun_kegiatan', 'kegiatan', 'created_at', 'updated_at']

    def get_kegiatan(self, obj):
        parent_id = obj.id
        current_year = timezone.now().year

        kegiatan_objects = models.PSM_JADWAL_KEGIATAN_TAHUNAN.objects.filter(kode_id=parent_id, created_at__year=current_year).order_by('created_at')
        ret = PSM_JADWAL_CHILD_SERIALIZERS(kegiatan_objects, many=True).data
        return ret

class PSM_JADWAL_CHILD_SERIALIZERS(serializers.ModelSerializer):
    kode_no_unit = serializers.CharField(source='kode.no_unit', read_only=True)
    uraian_no = serializers.CharField(source='uraian.no', read_only=True)
    uraian_name = serializers.CharField(source='uraian.uraian_kegiatan', read_only=True)

    class Meta:
        model = models.PSM_JADWAL_KEGIATAN_TAHUNAN
        fields = ['id', 'satker', 'kode_no_unit', 'uraian_no', 'uraian_name', 'waktu_kegiatan', 'metode_kegiatan', 'tempat_pelaksana', 'jumlah_peserta', 'keterangan', 'created_at']


# ======= PSM KEGIATAN LAINNYA SERIALIZER =======
