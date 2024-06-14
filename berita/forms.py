from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget

class BeritaForm(forms.ModelForm):
    class Meta:
        model = models.Berita
        fields = [
            "kategori",
            "judul",
            "isi_berita",
            "status",
            "tags",
            "gambar_utama",
        ]

        widgets = {
            'isi_berita': CKEditorWidget(),
        }

class KategoriForm(forms.ModelForm):
    class Meta:
        model = models.Kategori
        fields = [
            "nama",
        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = [
            "nama",
        ]