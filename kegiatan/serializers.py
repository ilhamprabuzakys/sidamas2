from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Satker, Profile

from . import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']

class SatkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satker
        exclude = []
        
        

# class Rakernis_psmSerializer(serializers.ModelSerializer):
#     dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
#     class Meta:
#         model = models.rakernis_psm
#         fields = [
#             "id",
#             "id_user",
#             "satker_pelaksana",
#             "satker_bnnp_bnnk_diundang",
#             "deskripsi_hasil",
#             "rekomendasi",
#             "hambatan_kendala",
#             "tanggal",
#             "kesimpulan",
#             "dokumentasi",
#             "created",
#             "last_updated",
#         ]
