from django import forms
from . import models


class tbl_eformForm(forms.ModelForm):
    class Meta:
        model = models.tbl_eform
        fields = [
            "data_eform",
            "nama_formulir",
            "role",
            "url",
            "tgl_akhir",
        ]


class tbl_responden_eformForm(forms.ModelForm):
    class Meta:
        model = models.tbl_responden_eform
        fields = [
            "jawaban_eform",
            "id_eform",
            "id_user",
        ]