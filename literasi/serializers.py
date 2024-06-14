from rest_framework import serializers

from . import models

class LiterasiSerializer(serializers.ModelSerializer):
    dokumen = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    
    class Meta:
        model = models.Literasi
        fields = '__all__'
        datatables_always_serialize = ['created_by', 'judul']
        depth = 1
