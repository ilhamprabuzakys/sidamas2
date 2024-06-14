from django.contrib import admin
from django import forms

from . import models
from . import forms as survei_forms

# Percobaan
class TipeSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'daftar_pertanyaan']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.TipeSurveiForm

class DataRespondenSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'jenis_kelamin', 'rentang_usia', 'pendidikan', 'pekerjaan']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataRespondenSurveiForm

class DataSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'tanggal_awal', 'tanggal_akhir', 'jam_awal', 'jam_akhir', 'batas_responden', 'kode']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataSurveiForm
    
class DataPengisianSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'array_nilai_jawaban', 'data_mentahan', 'sigma_nilai']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataPengisianSurveiForm
    
admin.site.register(models.TipeSurvei, TipeSurveiAdmin)
admin.site.register(models.DataRespondenSurvei, DataRespondenSurveiAdmin)
admin.site.register(models.DataSurvei, DataSurveiAdmin)
admin.site.register(models.DataPengisianSurvei, DataPengisianSurveiAdmin)