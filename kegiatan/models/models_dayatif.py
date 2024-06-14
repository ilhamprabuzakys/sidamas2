from random import choices
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from users.models import Satker

# =============================================
# DAYATIF : 8
# =============================================

"""
    Setiap Kegiatan memiliki kolom status yang memiliki arti yakni Status Pengiriman, yang masing-masing nilai memiliki arti :
    0: Kegiatan belum dikirim ke manapun
    1: Kegiatan sudah dikirim ke BNNP
    2: Kegiatan sudah dikirim ke Pusat
"""

class DAYATIF_BINAAN_TEKNIS(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_binaan_teknis_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_binaan_teknis_updated_by")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    jumlah_hari_pelaksanaan = models.IntegerField(default=2, verbose_name='Jumlah Hari Pelaksanaan Kegiatan')

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_binaan_teknis_satker", verbose_name="SATUAN KERJA PELAKSANA")

    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, related_name="dayatif_binaan_teknis_satker_target", verbose_name="SATUAN KERJA TARGET")

    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Kegiatan')

    tujuan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tujuan')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/binaan_teknis/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/binaan_teknis/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF KEGIATAN BINAAN TEKNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_binaan_teknis'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BINAAN TEKNIS - {self.tanggal_awal} s/d {self.tanggal_akhir} - Target : {self.satker_target.nama_satker}'

class DAYATIF_PEMETAAN_POTENSI(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_pemetaan_potensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_pemetaan_potensi_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_pemetaan_potensi_satker", verbose_name="SATUAN KERJA PELAKSANA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    desa = models.CharField(max_length=258, blank=True, null=True)
    kecamatan = models.CharField(max_length=258, blank=True, null=True)
    kabupaten = models.CharField(max_length=258, blank=True, null=True)
    provinsi = models.CharField(max_length=258, blank=True, null=True)

    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)

    # Potensi
    """
    {
        sda: {
            isi: "",
            swot: {},
            kesimpulan: ""
        },
        sdm: {
            isi: "",
            swot: {},
            kesimpulan: ""
        },
    }
    """
    potensi = models.JSONField(blank=True, null=True, verbose_name='Potensi SDA & SDM')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil') # -> Not used, use potensi
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_potensi/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_potensi/gambar/', null=True, verbose_name='Dokumentasi Gambar')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF PEMETAAN POTENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_pemetaan_potensi'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF PEMETAAN POTENSI - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_PEMETAAN_STAKEHOLDER(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    desa = models.CharField(max_length=250, blank=True, null=True)
    kecamatan = models.CharField(max_length=250, blank=True, null=True)
    kabupaten = models.CharField(max_length=250, blank=True, null=True)
    provinsi = models.CharField(max_length=250, blank=True, null=True)

    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)

    stakeholders = models.JSONField(blank=True, null=True, verbose_name='Daftar Stakeholder')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_stakeholder/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_stakeholder/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF PEMETAAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_pemetaan_stakeholder'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF PEMETAAN STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_RAPAT_SINERGI_STAKEHOLDER(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Kegiatan')

    stakeholders = models.JSONField(blank=True, null=True, verbose_name='Daftar Stakeholder')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    rekomendasi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Rekomendasi')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/rapat_sinergi_stakeholder/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/rapat_sinergi_stakeholder/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF RAPAT SINERGI STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_rapat_sinergi_stakeholder'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF RAPAT SINERGI STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    JENIS_BIMBINGAN_CHOICES = (
        ('bimbingan_teknis_stakeholder', 'Bimbingan Teknis Stakeholder'),
        ('bimbingan_teknis_pendamping', 'Bimbingan Teknis Pendamping')
	)

    jenis_bimbingan = models.CharField(max_length=max(len(key) for key, _ in JENIS_BIMBINGAN_CHOICES), choices=JENIS_BIMBINGAN_CHOICES, default="bimbingan_teknis_stakeholder", verbose_name='Jenis Bimbingan')

    tempat = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tempat')
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Yang Hadir')

    stakeholders = models.JSONField(blank=True, null=True, verbose_name='Daftar Stakeholder')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    rekomendasi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Rekomendasi')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_stakeholder/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_stakeholder/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF BIMBINGAN TEKNIS STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_bimbingan_teknis_stakeholder'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BIMBINGAN TEKNIS STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_satker", verbose_name="SATUAN KERJA PELAKSANA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    tempat = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tempat')

    # Kawasan yang diintervensi
    desa = models.CharField(max_length=250, blank=True, null=True)
    kecamatan = models.CharField(max_length=250, blank=True, null=True)
    kabupaten = models.CharField(max_length=250, blank=True, null=True)
    provinsi = models.CharField(max_length=250, blank=True, null=True)

    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)

    keterampilan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='keterampilan')

    peserta = models.JSONField(blank=True, null=True, verbose_name='Daftar Peserta')
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Yang Hadir')

    sinergi_desa = models.BooleanField(default=False, verbose_name='Sinergi Desa')
    sinergi_ibm = models.BooleanField(default=False, verbose_name='Sinergi IBM')

    hasil_skm_nilai = models.FloatField(blank=True, null=True, verbose_name='Hasil SKM Nilai')

    HASIL_SKM_KATEGORI_CHOICES = (
        ('buruk', 'Buruk'),
        ('cukup', 'Cukup'),
        ('baik', 'Baik'),
        ('sangat_baik', 'Sangat Baik')
	)

    hasil_skm_kategori = models.CharField(max_length=max(len(key) for key, _ in HASIL_SKM_KATEGORI_CHOICES), choices=HASIL_SKM_KATEGORI_CHOICES, default="cukup", verbose_name='Hasil SKM Kategori')

    anggaran = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Anggaran')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_lifeskill/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_lifeskill/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF BIMBINGAN TEKNIS LIFESKILL'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_bimbingan_teknis_lifeskill'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BIMBINGAN TEKNIS LIFESKILL - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_MONEV_DAYATIF(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_monev_dayatif_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="dayatif_monev_dayatif_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_monev_dayatif_satker", verbose_name="SATUAN KERJA PELAKSANA")

    JENIS_CHOICES = (
        ('Monitoring dan Evaluasi Kinerja', 'Monitoring dan Evaluasi Kinerja'),
        ('Monitoring dan Evaluasi dalam rangka Pendampingan', 'Monitoring dan Evaluasi dalam rangka Pendampingan'),
	)

    jenis = models.CharField(max_length=max(len(key) for key, _ in JENIS_CHOICES), choices=JENIS_CHOICES, blank=True, null=True, verbose_name='Jenis')

    PERIODE_CHOICES = (
        ('Triwulan', 'Triwulan'),
        ('Semester', 'Semester'),
        ('Tahunan', 'Tahunan'),
	)

    periode = models.CharField(max_length=max(len(key) for key, _ in PERIODE_CHOICES), choices=PERIODE_CHOICES, blank=True, null=True, verbose_name='Periode')

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)

    tempat = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tempat')

    # Kawasan yang diintervensi
    desa = models.CharField(max_length=250, blank=True, null=True)
    kecamatan = models.CharField(max_length=250, blank=True, null=True)
    kabupaten = models.CharField(max_length=250, blank=True, null=True)
    provinsi = models.CharField(max_length=250, blank=True, null=True)

    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)

    keterampilan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='keterampilan')

    peserta = models.JSONField(blank=True, null=True, verbose_name='Daftar Peserta')
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Yang Hadir')

    # Sinergi
    sinergi_desa = models.BooleanField(default=False, verbose_name='Sinergi Desa')
    sinergi_ibm = models.BooleanField(default=False, verbose_name='Sinergi IBM')

    # Hasil SKM
    KRITERIA_KATEGORI_CHOICES = (
        ('buruk', 'Buruk'),
        ('cukup', 'Cukup'),
        ('baik', 'Baik'),
        ('sangat_baik', 'Sangat Baik')
	)

    hasil_skm_nilai = models.FloatField(blank=True, null=True, verbose_name='Hasil SKM Nilai')

    hasil_skm_kategori = models.CharField(max_length=max(len(key) for key, _ in KRITERIA_KATEGORI_CHOICES), choices=KRITERIA_KATEGORI_CHOICES, default="cukup", verbose_name='Hasil SKM Kategori')

    # Hasil Indeks Kewirausahaan
    hasil_indeks_kewirausahaan_nilai = models.FloatField(blank=True, null=True, verbose_name='Hasil Indeks Kewirausahaan')
    hasil_indeks_kewirausahaan_kategori = models.CharField(max_length=max(len(key) for key, _ in KRITERIA_KATEGORI_CHOICES), choices=KRITERIA_KATEGORI_CHOICES, default="cukup", verbose_name='Hasil SKM Kategori')

    # Status Kerawanan Kawasan
    status_kerawanan_kawasan_awal_kategori = models.CharField(max_length=250, blank=True, null=True, verbose_name='Status Kerawanan Awal Kategori')
    status_kerawanan_kawasan_akhir_nilai = models.FloatField(blank=True, null=True, verbose_name='Status Kerawanan Akhir Nilai IKKR')
    status_kerawanan_kawasan_akhir_kategori = models.CharField(max_length=250, blank=True, null=True, verbose_name='Status Kerawanan Akhir Kategori')
    status_kerawanan_kawasan_kepulihan = models.CharField(max_length=250, blank=True, null=True, verbose_name='Status Kerawanan Kepulihan')

    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/monev_dayatif/', verbose_name='Dokumentasi File')
    gambar = models.FileField(upload_to='uploads/kegiatan/dayatif/monev_dayatif/gambar/', null=True, verbose_name='Dokumentasi Gambar')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF MONEV DAYATIF'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_monev_dayatif'

    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF MONEV DAYATIF - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_DUKUNGAN_STAKEHOLDER(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")
    stakeholder = models.CharField(max_length=250, blank=True, null=True, verbose_name='Nama Stakeholder')

    JENIS_CHOICES = (
        ('Dukungan Sarana Produksi', 'Dukungan Sarana Produksi'),
        ('Dukungan SDM', 'Dukungan SDM'),
        ('Dukungan Lainnya', 'Dukungan Lainnya')
	)

    jenis = models.CharField(max_length=50, choices=JENIS_CHOICES, default="DSP")
    bentuk = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Bentuk')
    jumlah = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Jumlah')

    # Kawasan yang diintervensi
    desa = models.CharField(max_length=250, blank=True, null=True)
    kecamatan = models.CharField(max_length=250, blank=True, null=True)
    kabupaten = models.CharField(max_length=250, blank=True, null=True)
    provinsi = models.CharField(max_length=250, blank=True, null=True)

    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)

    jumlah_sasaran = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Jumlah Sasaran')
    pengaruh = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Pengaruh/Manfaat')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')

    dokumentasi = models.FileField(blank=True, null=True, upload_to="uploads/kegiatan/dayatif/dukungan_stakeholder/")

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF DUKUNGAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_dukungan_stakeholder'

    def __str__(self):
        return f'DAYATIF DUKUNGAN STAKEHOLDER - {self.satker.nama_satker}'


class DAYATIF_KEGIATAN_SATKER(models.Model):
    id = models.IntegerField(primary_key=True)
    nama_satker = models.CharField(max_length=255)
    hasil = models.JSONField(null=True)

    class Meta:
        managed = False
        db_table = 'v_kegiatan_dayatif_satker2'