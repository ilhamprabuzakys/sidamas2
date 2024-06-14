from django import forms
from . import models

# Percobaan
class TipeSurveiForm(forms.ModelForm):
    class Meta:
        model = models.TipeSurvei
        fields = "__all__"
        # fields = [
        #     "nama",
        #     "daftar_pertanyaan",
        # ]
        
class DataRespondenSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataRespondenSurvei
        fields = "__all__"
        # fields = [
        #     "jenis_kelamin",
        #     "rentang_usia",
        #     "pendidikan",
        #     "nama",
        #     "pekerjaan",
        # ]
        
class DataSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataSurvei
        fields = "__all__"
        # fields = [
        #     "judul",
        #     "tanggal",
        #     "jam_awal",
        #     "jam_akhir",
        #     "jumlah_responden",
        #     "kode",
        # ]

class DataPengisianSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataSurvei
        fields = "__all__"
        # fields = [
        #     "array_nilai_jawaban",
        #     "data_mentahan",
        #     "sigma_nilai",
        # ]

