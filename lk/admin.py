from django.contrib import admin
from django import forms

from . import models


class tbl_eformAdminForm(forms.ModelForm):

    class Meta:
        model = models.tbl_eform
        fields = "__all__"


class tbl_eformAdmin(admin.ModelAdmin):
    form = tbl_eformAdminForm
    list_display = [
        "data_eform",
        "created",
        "last_updated",
        "nama_formulir",
        "role",
        "url",
        "tgl_akhir",
    ]
    readonly_fields = [
        "data_eform",
        "created",
        "last_updated",
        "nama_formulir",
        "role",
        "url",
        "tgl_akhir",
    ]


class tbl_responden_eformAdminForm(forms.ModelForm):

    class Meta:
        model = models.tbl_responden_eform
        fields = "__all__"


class tbl_responden_eformAdmin(admin.ModelAdmin):
    form = tbl_responden_eformAdminForm
    list_display = [
        "jawaban_eform",
        "last_updated",
        "id_eform",
        "id_user",
        "created",
    ]
    readonly_fields = [
        "jawaban_eform",
        "last_updated",
        "id_eform",
        "id_user",
        "created",
    ]


admin.site.register(models.tbl_eform, tbl_eformAdmin)
admin.site.register(models.tbl_responden_eform, tbl_responden_eformAdmin)