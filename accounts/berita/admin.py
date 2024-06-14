from django.contrib import admin
from django import forms

from . import models


class TagAdminForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = "__all__"


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    list_display = [
        "created_at",
        "updated_at",
        "nama",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]

class KategoriAdminForm(forms.ModelForm):
    class Meta:
        model = models.Kategori
        fields = "__all__"


class KategoriAdmin(admin.ModelAdmin):
    form = KategoriAdminForm
    list_display = [
        "created_at",
        "updated_at",
        "nama",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


class BeritaAdminForm(forms.ModelForm):
    class Meta:
        model = models.Berita
        fields = "__all__"


class BeritaAdmin(admin.ModelAdmin):
    form = BeritaAdminForm
    list_display = [
        "created_at",
        "updated_at",
        "kategori",
        "judul",
        "isi_berita",
        "tanggal",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


admin.site.register(models.Berita, BeritaAdmin)
admin.site.register(models.Kategori, KategoriAdmin)
admin.site.register(models.Tag, TagAdmin)
