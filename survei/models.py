from datetime import datetime, time
from email.policy import default
import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Satker


from django.core.serializers import serialize

"""
    DataSurvei memiliki satu TipeSurvei
    TipeSurvei memiliki banyak DataSurvei
    DataSurvei memiliki banyak DataRespondenSurvei
    DataRespondenSurvei memiliki satu DataPengisianSurvei
    DataPengisianSurvei memiliki satu DataSurvei dan satu DataRespondenSurvei
"""

# Percobaan
class TipeSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="tipe_survei_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="tipe_survei_updated_by")

    nama = models.CharField(max_length=255)
    daftar_pertanyaan = models.JSONField()

    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)

    DIREKTORAT_CHOICES = (
        ('psm', 'PSM'),
        ('dayatif', 'Dayatif'),
    )

    direktorat = models.CharField(max_length=12, choices=DIREKTORAT_CHOICES, default='psm')

    class Meta:
        ordering = ['nama', ]
        verbose_name = 'Tipe Survei'
        verbose_name_plural = 'Daftar Tipe Survei'

    def generate_unique_code(self):
        # Menghasilkan kode acak
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Mengecek apakah kode sudah digunakan
        while DataSurvei.objects.filter(kode=random_string).exists():
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        return random_string

    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = self.generate_unique_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tipe Survei - {self.nama}'

class DataSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_survei_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_survei_updated_by")

    dikirimkan_kepada = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="daftar_data_survei")

    judul = models.CharField(max_length=255, blank=True, null=True)

    tanggal_awal = models.DateField(blank=True, null=True)
    tanggal_akhir = models.DateField(blank=True, null=True)

    jam_awal = models.TimeField(blank=True, null=True)
    jam_akhir = models.TimeField(blank=True, null=True)

    batas_responden = models.IntegerField(blank=True, null=True)

    status_pengiriman = models.BooleanField(blank=True, null=True, default=False)
    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)

    keterangan = models.TextField(blank=True, null=True)

    # Relasi
    tipe = models.ForeignKey(TipeSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name='survei')
    satker = models.ForeignKey(Satker, on_delete=models.CASCADE, blank=True, null=True, related_name='survei')

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Data Survei'
        verbose_name_plural = 'Daftar Data Survei'

    def generate_unique_code(self):
        # Menghasilkan kode acak
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Mengecek apakah kode sudah digunakan
        while DataSurvei.objects.filter(kode=random_string).exists():
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        return random_string

    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = self.generate_unique_code()
        super().save(*args, **kwargs)

    def get_jumlah_responden(self):
        print(self.responden.count())
        return self.responden.count()

    def get_status_responden(self):
        if self.get_jumlah_responden() >= self.batas_responden:
            return 'Sudah penuh'
        else:
            return 'Belum penuh'

    def get_status_keberlangsungan(self):
        current_datetime = datetime.now().replace(microsecond=0)
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        expected_start_datetime = datetime.combine(self.tanggal_awal, self.jam_awal)

        try:
            if self.tanggal_akhir is not None:
                expected_end_datetime = datetime.combine(self.tanggal_akhir, self.jam_akhir)
            else:
                # Jika tanggal_akhir None, anggap batas akhirnya adalah tanggal_awal
                expected_end_datetime = datetime.combine(self.tanggal_awal, self.jam_akhir)

            if current_datetime < expected_start_datetime:
                return 'Belum dibuka'
            elif current_datetime >= expected_start_datetime and current_datetime <= expected_end_datetime:
                text = 'Berlangsung'
                if self.get_jumlah_responden() and self.get_jumlah_responden() >= self.batas_responden:
                    text = 'Berakhir'
                return text
            else:
                return 'Berakhir'
        except Exception as e:
            print(f"Error: {e}")
            return '?'

    def get_data_isian(self):
        data_isian_queryset = DataPengisianSurvei.objects.filter(survei=self.id)
        data_isian_list = list(data_isian_queryset.values('responden__nama', 'array_nilai_jawaban', 'data_mentahan', 'sigma_nilai'))
        return data_isian_list

    def get_data_tipe(self):
        data_tipe_queryset = TipeSurvei.objects.filter(survei=self.id)
        data_tipe_list = list(data_tipe_queryset.values())
        return data_tipe_list

    def get_satker_name(self):
        if self.satker:
            return self.satker.nama_satker
        return None

    @property
    def responden(self):
        return DataRespondenSurvei.objects.filter(survei=self)

    def __str__(self):
        return f'Survei {self.tanggal_awal} - {self.tanggal_akhir}'

    class Meta:
        ordering = ['-updated_at', ]

class DataRespondenSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_responden_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_responden_updated_by")

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)

    RENTANG_USIA_CHOICES = [
        ('12-25', '12 - 25 tahun'),
        ('26-45', '26 - 45 tahun'),
        ('46-65', '46 - 65 tahun'),
    ]

    rentang_usia = models.CharField(max_length=30, choices=RENTANG_USIA_CHOICES)

    PENDIDIKAN_CHOICES = [
        ('Doktor (S3)', 'Doktor (S3)'),
        ('Magister (S2)', 'Magister (S2)'),
        ('Sarjana (S1)', 'Sarjana (S1)'),
        ('Diploma (D1-D4)', 'Diploma (D1-D4)'),
        ('SMA/SMK/MA', 'SMA/SMK/MA'),
        ('SMP/MTs', 'SMP/MTs'),
    ]

    pendidikan = models.CharField(max_length=50, choices=PENDIDIKAN_CHOICES)

    # Bisi nanti diperlukan
    nama = models.CharField(blank=True, null=True, max_length=100)
    alamat = models.TextField(blank=True, null=True, max_length=100)
    pekerjaan = models.CharField(blank=True, null=True, max_length=100)
    handphone = models.CharField(blank=True, null=True, max_length=13)
    email = models.CharField(blank=True, null=True, max_length=100)

    # Relasi
    survei = models.ForeignKey(DataSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="responden")

    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Responden Survei'
        verbose_name_plural = 'Daftar Data Responden Survei'

    def __str__(self):
        return str(self.pk)

class DataPengisianSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian_updated_by")

    array_nilai_jawaban = models.TextField()
    data_mentahan = models.JSONField()
    sigma_nilai = models.FloatField()

    # Relasi
    survei = models.ForeignKey(DataSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")

    # responden = models.ForeignKey(DataRespondenSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")
    responden = models.ForeignKey(DataRespondenSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")

    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Pengisian Survei'
        verbose_name_plural = 'Daftar Data Pengisian Survei'

    def get_data_responden(self):
        if self.responden:
            data_responden_queryset = DataRespondenSurvei.objects.filter(id=self.responden.id)
            data_responden_list = list(data_responden_queryset.values())
            return data_responden_list
        else:
            return []

    # def get_data_isian(self):
    #     data_isian_queryset = DataPengisianSurvei.objects.filter(survei=self.id)
    #     data_isian_list = list(data_isian_queryset.values())
    #     return data_isian_list

    def __str__(self):
        return str(self.pk)


# ----------------------
# Survei Data Intelijen
# ----------------------
class DataIntelijenSumberSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen_sumber_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen_sumber_updated_by")

    nama = models.CharField(max_length=255, unique=True)
    json = models.JSONField()
    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        ordering = ['nama', ]
        verbose_name = 'Data Intelijen Sumber Survei'
        verbose_name_plural = 'Daftar Data Intelijen Sumber Survei'

    def generate_unique_code(self):
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        while DataIntelijenSumberSurvei.objects.filter(kode=random_string).exists() and DataIntelijenSurvei.objects.filter(kode=random_string).exists():
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return random_string

    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = self.generate_unique_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Data Intelijen Sumber Survei - {self.nama}'

class DataIntelijenSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen_updated_by")

    # Relasi
    parent = models.ForeignKey(DataIntelijenSumberSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen")

    # Wilayah
    desa = models.CharField(max_length=10, null=True, blank=True)
    kecamatan = models.CharField(max_length=10, null=True, blank=True)
    kabupaten = models.CharField(max_length=10, null=True, blank=True)
    provinsi = models.CharField(max_length=10, null=True, blank=True)
    nama_desa = models.CharField(max_length=100, null=True, blank=True)
    nama_kecamatan = models.CharField(max_length=100, null=True, blank=True)
    nama_kabupaten = models.CharField(max_length=100, null=True, blank=True)
    nama_provinsi = models.CharField(max_length=100, null=True, blank=True)

    wilayah = models.TextField(max_length=255, null=True, blank=True)

    # Petugas
    nama_petugas = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nama Petugas')
    nik_petugas = models.CharField(max_length=255, null=True, blank=True, verbose_name='ID Petugas')

    # Waktu
    tanggal_wawancara = models.DateField(null=True, blank=True, verbose_name='Tanggal Dilaksanakan Wawancara')
    waktu_mulai = models.TimeField(null=True, blank=True)
    waktu_akhir = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Intelijen Survei'

class DataIntelijenRespondenSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Biodata
    nik = models.CharField(blank=True, null=True, max_length=100)
    nama = models.CharField(blank=True, null=True, max_length=100)
    alamat = models.TextField(blank=True, null=True, max_length=100)

    json = models.JSONField()

    # Relasi
    parent = models.ForeignKey(DataIntelijenSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_intelijen_responden")

    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Intelijen Responden Survei'