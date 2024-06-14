from rest_framework import serializers

from . import models


class tbl_eformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_eform
        fields = [
            "data_eform",
            "created",
            "last_updated",
            "nama_formulir",
            "role",
            "url",
            "tgl_akhir",
        ]

class tbl_responden_eformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_responden_eform
        fields = [
            "jawaban_eform",
            "last_updated",
            "id_eform",
            "id_user",
            "created",
        ]