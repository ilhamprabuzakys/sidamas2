from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer
from users.models import Profile, Satker

from kegiatan.api.helpers.serializers_helpers import (
    get_list_data,
    get_list_data_dukungan,
    get_list_detail_dukungan,
    get_list_detail,
    get_serializer_update
)

# ======= KEGIATAN SATKER =======
class DAYATIF_KEGIATAN_SATKER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_KEGIATAN_SATKER
        exclude = []

# ======= BINAAN_TEKNIS =======
class DAYATIF_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    satker_target = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        # depth = 1
        exclude = []

    # def __init__(self, *args, **kwargs):
    #     super(DAYATIF_BINAAN_TEKNIS_Serializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method=='POST':
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 1
    def update(self, instance, validated_data):
        return super().update(get_serializer_update(self, instance, validated_data), validated_data)

# ======= BINAAN_TEKNIS LIST =======
class DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        exclude = []

class DAYATIF_BINAAN_TEKNIS_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        fields = ['id','satker', 'satker_target', 'data']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BINAAN_TEKNIS, DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer)

class DAYATIF_BINAAN_TEKNIS_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        fields = ['id','satker','data','detail']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BINAAN_TEKNIS, DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_BINAAN_TEKNIS, DAYATIF_BINAAN_TEKNIS_LIST_CHILD_Serializer)

# ======= PEMETAAN_POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_PEMETAAN_POTENSI_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return super().update(get_serializer_update(self, instance, validated_data), validated_data)

# ======= PEMETAAN_POTENSI LIST =======
class DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        exclude = []

class DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        fields = ['id', 'satker', 'data']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_PEMETAAN_POTENSI, DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer)

class DAYATIF_PEMETAAN_POTENSI_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_PEMETAAN_POTENSI, DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_PEMETAAN_POTENSI, DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer)


    def get_detail(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker, status__gt = 0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker, status= 2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

        serialized_data = DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(queryset, many=True, context=self.context).data
        print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
        return serialized_data

# ======= PEMETAAN_STAKEHOLDER =======
class DAYATIF_PEMETAAN_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_PEMETAAN_STAKEHOLDER_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return super().update(get_serializer_update(self, instance, validated_data), validated_data)

# ======= PEMETAAN_STAKEHOLDER LIST =======
class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        exclude = []

class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_PEMETAAN_STAKEHOLDER, DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer)

class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_PEMETAAN_STAKEHOLDER, DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_PEMETAAN_STAKEHOLDER, DAYATIF_PEMETAAN_STAKEHOLDER_LIST_CHILD_Serializer)

# ======= DAYATIF_RAPAT_SINERGI_STAKEHOLDER =======
class DAYATIF_RAPAT_SINERGI_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_RAPAT_SINERGI_STAKEHOLDER_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return super().update(get_serializer_update(self, instance, validated_data), validated_data)

# ======= DAYATIF_RAPAT_SINERGI_STAKEHOLDER LIST =======
class DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER
        exclude = []

class DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER, DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_DATA_Serializer)

class DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER, DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_RAPAT_SINERGI_STAKEHOLDER, DAYATIF_RAPAT_SINERGI_STAKEHOLDER_LIST_CHILD_Serializer)

# ======= DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER =======
class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return super().update(get_serializer_update(self, instance, validated_data), validated_data)

# ======= DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER LIST =======
class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER
        exclude = []

class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER, DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_DATA_Serializer)

class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER, DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER, DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_LIST_CHILD_Serializer)

# ======= DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL =======
class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_Serializer(serializers.ModelSerializer):
    gambar = serializers.ImageField(required=False)

    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method in ['POST', 'PATCH', 'PUT']:
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return get_serializer_update(self, instance, validated_data)


# ======= DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL LIST =======
class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL
        exclude = []

class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL, DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_DATA_Serializer)

class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL, DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL, DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_LIST_CHILD_Serializer)

# ======= DAYATIF_MONEV_DAYATIF =======
class DAYATIF_MONEV_DAYATIF_Serializer(serializers.ModelSerializer):
    gambar = serializers.ImageField(required=False)

    class Meta:
        model = models.DAYATIF_MONEV_DAYATIF
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_MONEV_DAYATIF_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method in ['POST', 'PATCH', 'PUT']:
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    def update(self, instance, validated_data):
        return get_serializer_update(self, instance, validated_data)

# ======= DAYATIF_MONEV_DAYATIF LIST =======
class DAYATIF_MONEV_DAYATIF_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_MONEV_DAYATIF
        exclude = []

class DAYATIF_MONEV_DAYATIF_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_MONEV_DAYATIF
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_MONEV_DAYATIF, DAYATIF_MONEV_DAYATIF_LIST_DATA_Serializer)

class DAYATIF_MONEV_DAYATIF_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_MONEV_DAYATIF
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data(self, obj, models.DAYATIF_MONEV_DAYATIF, DAYATIF_MONEV_DAYATIF_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail(self, obj, models.DAYATIF_MONEV_DAYATIF, DAYATIF_MONEV_DAYATIF_LIST_CHILD_Serializer)

# ======= DAYATIF_DUKUNGAN_STAKEHOLDER =======
class DAYATIF_DUKUNGAN_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_DUKUNGAN_STAKEHOLDER
        depth = 1
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DAYATIF_DUKUNGAN_STAKEHOLDER_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

# ======= DAYATIF_DUKUNGAN_STAKEHOLDER LIST =======
class DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_DUKUNGAN_STAKEHOLDER
        exclude = []

class DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_DUKUNGAN_STAKEHOLDER
        fields = ['id', 'satker', 'data']


    def get_data(self, obj):
        return get_list_data_dukungan(self, obj, models.DAYATIF_DUKUNGAN_STAKEHOLDER, DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_DATA_Serializer)

class DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_DUKUNGAN_STAKEHOLDER
        fields = ['id', 'satker', 'data', 'detail']

    def get_data(self, obj):
        return get_list_data_dukungan(self, obj, models.DAYATIF_DUKUNGAN_STAKEHOLDER, DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_DATA_Serializer)

    def get_detail(self, obj):
        return get_list_detail_dukungan(self, obj, models.DAYATIF_DUKUNGAN_STAKEHOLDER, DAYATIF_DUKUNGAN_STAKEHOLDER_LIST_CHILD_Serializer)