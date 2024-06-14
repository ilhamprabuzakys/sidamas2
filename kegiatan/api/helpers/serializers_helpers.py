def get_serializer_update(self, instance, validated_data):
    request = self.context.get('request')
    request_data = request.data

    delete_gambar = request_data.get('delete_gambar')
    gambar = validated_data.get('gambar')

    print({ 'delete_gambar': delete_gambar, 'gambar': gambar })

    if delete_gambar:
        # Hapus gambar yang ada
        instance.gambar.delete()
        # Atur nilai field gambar menjadi null
        instance.gambar = None

    if gambar:
        instance.gambar.save(gambar.name, gambar, save=True)

    # Update remaining fields
    for attr, value in validated_data.items():
        setattr(instance, attr, value)

    instance.save()  # Save instance with updated fields

    return instance

def get_list_data(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level

    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

    serialized_data = serializer_class(queryset, many=True).data
    print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
    return serialized_data

def get_list_detail(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level

    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker__parent=obj.satker).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker__parent=obj.satker, status__gt=0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker__parent=obj.satker, status=2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

    serialized_data = serializer_class(queryset, many=True, context=self.context).data
    print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
    return serialized_data

def get_list_data_dukungan(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level

    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker=obj.satker)
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker=obj.satker, status__gt=0)
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker=obj.satker, status=2)

    serialized_data = serializer_class(queryset, many=True).data
    print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
    return serialized_data

def get_list_detail_dukungan(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level

    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker__parent=obj.satker).order_by('satker__order').distinct('satker__order')
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker__parent=obj.satker, status__gt=0).order_by('satker__order').distinct('satker__order')
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker__parent=obj.satker, status=2).order_by('satker__order').distinct('satker__order')

    serialized_data = serializer_class(queryset, many=True, context=self.context).data
    print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
    return serialized_data