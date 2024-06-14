from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from users.models import Satker, Observasi, Kegiatan_akun, Uraian_kegiatan

# ======= PSM RAKERNIS MODEL =======
class PSM_RAKERNIS(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker", verbose_name="SATUAN KERJA PELAKSANA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker_target", verbose_name="SATUAN KERJA TARGET")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/rakernis/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM RAKERNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_rakernis'

# ======= PSM BINAAN TEKNIS MODEL =======
class PSM_BINAAN_TEKNIS(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bintek_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bintek_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_bintek_satker", verbose_name="SATUAN KERJA PELAKSANA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_bintek_satker_target", verbose_name="SATUAN KERJA TARGET")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/bintek/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM BINAAN TEKNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_binaan_teknis'

# ======= PSM ASISTENSI MODEL =======
class PSM_ASISTENSI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_asistensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_asistensi_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_asistensi_satker", verbose_name="SATUAN KERJA")
    jumlah_kegiatan = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Kegiatan')

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    tanggal = models.DateField(verbose_name='Tanggal', blank=True, null=True, default=date.today)

    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta')
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder Yang Diasistensi Dalam Rangka Kotan')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/asistensi/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM ASISTENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_asistensi'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM ASISTENSI - {self.tanggal}'

# ======= PSM TES URINE DETEKSI DINI MODEL =======
class PSM_TES_URINE_DETEKSI_DINI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_satker", verbose_name="SATUAN KERJA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_tes_urine_satker_target", verbose_name="SATUAN KERJA TARGET")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')
    hasil_tes_urine = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hasil Tes Urine')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/tes_urine_deteksi_dini/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM TES URINE DETEKSI DINI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_test_urine_deteksi_dini'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM TES URINE DETEKSI DINI - {self.tanggal}'

class PSM_TES_URINE_DETEKSI_DINI_PESERTA(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    # HASIL_TEST_CHOICES = [
    #     ('P', 'Positif'),
    #     ('N', 'Negatif'),
    # ]

    parent = models.ForeignKey(PSM_TES_URINE_DETEKSI_DINI, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama_peserta = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)
    hasil_test = models.CharField(max_length=100, blank=True, null=True)
    isi_parameter = models.CharField(max_length=100, blank=True, null=True)
    keterangan_isi_parameter = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True,)

class PSM_TES_URINE_COUNT(models.Model):
    nama_satker = models.CharField(max_length=255)
    peserta_count_2021 = models.IntegerField(default=0)
    peserta_count_2022 = models.IntegerField(default=0)
    peserta_count_2023 = models.IntegerField(default=0)
    peserta_count_2024 = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'kegiatan_psm_kegiatan_p4gn_count_view'

# ======= PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN MODEL =======
class PSM_MONITORING_DAN_EVALUASI_SUPERVISI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_satker", verbose_name="SATUAN KERJA")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan Dan Satker')
    status_indeks = models.IntegerField(default=0, verbose_name='Status Indeks Kemandirian Partisipasi')
    nilai_ikp = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nilai IKP')
    status_ikp = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Status IKP')
    deskripsi_hasil = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    simpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/monev_supervisi_kegiatan_kotan/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_monev_supervisi_kegiatan_kotan'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN - {self.tanggal_awal}'

class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA(models.Model):

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    parent = models.ForeignKey(PSM_MONITORING_DAN_EVALUASI_SUPERVISI, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama_peserta = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)
    jabatan = models.CharField(max_length=100, blank=True, null=True,)

# ======= PSM PENGUMPULAN DATA IKOTAN =======
class PSM_PENGUMPULAN_DATA_IKOTAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_pengumpulan_data_ikotan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_pengumpulan_data_ikotan_updated_by")

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_pengumpulan_data_ikotan_satker", verbose_name="SATUAN KERJA")

    observasi = models.ForeignKey(Observasi, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_pengumpulan_data_ikotan_observasi", verbose_name="Unit Observasi")

    deskripsi_hasil = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    simpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/pengumpulan_data_ikotan/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM DUKUNGAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_pengumpulan_data_ikotan'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM DUKUNGAN STAKEHOLDER - {self.tanggal_awal}'

class PSM_PENGUMPULAN_DATA_IKOTAN_PESERTA(models.Model):
    parent = models.ForeignKey(PSM_PENGUMPULAN_DATA_IKOTAN, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama_peserta = models.CharField(max_length=100)

# ======= PSM DUKUNGAN STAKEHOLDER =======
class PSM_DUKUNGAN_STAKEHOLDER(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_dukungan_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_dukungan_stakeholder_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_dukungan_stakeholder_satker", verbose_name="SATUAN KERJA")

    alamat = models.JSONField()

    pemda = models.TextField(blank=True, null=True, max_length=2000)
    kegiatan = models.TextField(blank=True, null=True, max_length=2000)
    jumlah_sasaran = models.IntegerField(default=0)

    hasil_dampak = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/dukungan_stakeholder/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM DUKUNGAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_dukungan_stakeholder'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM DUKUNGAN STAKEHOLDER - {self.created_at}'

# ======= PSM RAKOR PEMETAAN MODEL =======
class PSM_RAKOR_PEMETAAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakor_pemetaan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakor_pemetaan_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakor_pemetaan_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/rakor_pemetaan/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM RAKOR PEMETAAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_rakor_pemetaan'

# ======= PSM KEGIATAN LAINNYA =======
class PSM_KEGIATAN_LAINNYA(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_kegiatan_lainnya_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_kegiatan_lainnya_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_kegiatan_lainnya_satker", verbose_name="SATUAN KERJA")

    kegiatan = models.TextField(blank=True, null=True)
    tempat = models.TextField(blank=True, null=True)
    waktu_awal = models.TimeField()
    waktu_akhir = models.TimeField()
    lingkungan = models.TextField(blank=True, null=True)
    jumlah_sasaran = models.IntegerField(default=0)

    hasil_dampak = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/kegiatan_lainnya/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    # kode = models.CharField(blank=True, null=True, max_length=255, verbose_name='Kode')
    # pendapatan = models.CharField(blank=True, null=True, max_length=255, verbose_name='Pendapatan')
    kegiatan_akun = models.ForeignKey(Kegiatan_akun, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Kode Kegiatan Akun')
    uraian_kegiatan = models.ForeignKey(Uraian_kegiatan, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Uraian Kegiatan')

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='URL GDrive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM KEGIATAN LAINNYA'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_kegiatan_lainnya'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM KEGIATAN LAINNYA - {self.created_at}'

# ======= PSM AUDIENSI MODEL =======
class PSM_AUDIENSI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_audiensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_audiensi_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_audiensi_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/audiensi/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM AUDIENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_audiensi'

# ======= PSM KONSOLIDASI_KEBIJAKAN MODEL =======
class PSM_KONSOLIDASI_KEBIJAKAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_konsolidasi_kebijakan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_konsolidasi_kebijakan_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_konsolidasi_kebijakan_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder')
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/konsolidasi_kebijakan/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM KONSOLIDASI KEBIJAKAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_konsolidasi_kebijakan'

# ======= PSM WORKSHOP_PENGGIAT MODEL =======
class PSM_WORKSHOP_PENGGIAT(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_workshop_penggiat_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_workshop_penggiat_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_workshop_penggiat_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder')
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/workshop_penggiat/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM WORKSHOP PENGGIAT'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_workshop_penggiat'

# ======= PSM SINKRONISASI KEBIJAKAN MODEL =======
class PSM_SINKRONISASI_KEBIJAKAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_sinkronisasi_kebijakan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_sinkronisasi_kebijakan_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_sinkronisasi_kebijakan_satker", verbose_name="SATUAN KERJA")
    jumlah_kegiatan = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Kegiatan')

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    tanggal = models.DateField(verbose_name='Tanggal', blank=True, null=True, default=date.today)

    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta')
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder Yang Diasistensi Dalam Rangka Kotan')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/sinkronisasi_kebijakan/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM SINKRONISASI KEBIJAKAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_sinkronisasi_kebijakan'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM SINKRONISASI KEBIJAKAN - {self.tanggal}'

# ======= PSM WORKSHOP TEMATIK MODEL =======
class PSM_WORKSHOP_TEMATIK(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_workshop_tematik_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_workshop_tematik_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_workshop_tematik_satker", verbose_name="SATUAN KERJA")
    jumlah_kegiatan = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Kegiatan')

    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    tanggal = models.DateField(verbose_name='Tanggal', blank=True, null=True, default=date.today)

    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta')
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder Yang Diasistensi Dalam Rangka Kotan')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/workshop_tematik/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")

    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')


    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM WORKSHOP TEMATIK'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_workshop_tematik'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM WORKSHOP TEMATIK - {self.tanggal}'

# ======= PSM BIMTEK P4GN MODEL =======
class PSM_BIMTEK_P4GN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bimtek_p4gn_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bimtek_p4gn_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_bimtek_p4gn_satker", verbose_name="SATUAN KERJA PELAKSANA")
    seri_pin_penggiat = models.CharField(blank=True, null=True, max_length=20, verbose_name="No. Seri Pin Penggiat")
    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    hasil_capaian = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hasil Capaian')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/bimtek_p4gn/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    drive_url = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tautan Drive')
    anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Perencanaan Anggaran')
    penyerapan_anggaran = models.DecimalField(max_digits=18, default=0.00, decimal_places=2, verbose_name='Penyerapan Anggaran')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM BIMBINGAN TEKNIS P4GN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_bimtek_p4gn'

class PSM_BIMTEK_P4GN_PESERTA(models.Model):
    parent = models.ForeignKey(PSM_BIMTEK_P4GN, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama = models.CharField(max_length=100, blank=True, null=True)
    jabatan = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.TextField(max_length=1000, blank=True, null=True)
    no_telepon = models.CharField(max_length=18, blank=True, null=True)

    JENIS_KELAMIN_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
	)

    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, default="L", verbose_name='Jenis Kelamin')

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM PESERTA BIMBINGAN TEKNIS PENGGIAT P4GN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_bimtek_p4gn_peserta'

# ======= PSM JADWAL KEGIATAN TAHUNAN =======
class PSM_JADWAL_KEGIATAN_TAHUNAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_jadwal_kegiatan_tahunan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_jadwal_kegiatan_tahunan_updated_by")

    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_jadwal_kegiatan_tahunan_satker", verbose_name="SATUAN KERJA")
    kode = models.ForeignKey(Kegiatan_akun, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_jadwal_kegiatan_tahunan_kegiatan_akun", verbose_name="KODE KEGIATAN AKUN")
    uraian = models.ForeignKey(Uraian_kegiatan, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_jadwal_kegiatan_tahunan_Uraian_kegiatan", verbose_name="URAIAN KEGIATAN")

    # ordering_asc = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Urutan')

    # tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    # tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    nama_kegiatan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='nama kegiatan')

    waktu_kegiatan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='waktu kegiatan')
    metode_kegiatan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='metode kegiatan')
    tempat_pelaksana = models.TextField(blank=True, null=True, max_length=2000, verbose_name='tempat kegiatan')
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta')
    # anggaran = models.TextField(blank=True, null=True, max_length=2000, verbose_name='anggaran')
    # pj = models.TextField(blank=True, null=True, max_length=2000, verbose_name='PJ')
    keterangan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Keterangan')

    # dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/jadwal_kegiatan_tahunan/", blank=True)

    status = models.IntegerField(default=0, blank=True, null=True, verbose_name="Status Pengiriman Kegiatan")

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM JADWAL KEGIATAN TAHUNAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_jadwal_kegiatan_tahunan'

    def __str__(self):
        return f'{self.satker.nama_satker} PSM JADWAL KEGIATAN TAHUNAN - {self.created_at}'
