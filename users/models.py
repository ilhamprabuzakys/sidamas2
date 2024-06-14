from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist


class UserLengkap(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    role = models.CharField(max_length=255)
    notelp = models.CharField(max_length=255)
    nama_satker = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'v_auth_users_lengkap'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Satker(models.Model):
    nama_satker = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(default=1)
    kabupaten = models.ForeignKey('reg_regencies', on_delete=models.SET_NULL, null=True, blank=True, related_name='satker')
    provinsi = models.ForeignKey('reg_provinces', on_delete=models.SET_NULL, null=True, blank=True, related_name='satker')
    order = models.IntegerField(null=True, blank=True)
    satker_order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['nama_satker', ]
        verbose_name = 'Satuan Kerja'
        verbose_name_plural = 'Daftar Satuan Kerja'

    def __str__(self):
        return str(self.nama_satker)

class Observasi(models.Model):
    nama_unit = models.CharField(null=True, blank=True, max_length=100)

class Kegiatan_akun(models.Model):
    no_unit = models.CharField(null=True, blank=True, max_length=100)
    akun_kegiatan = models.CharField(null=True, blank=True, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)

    def __str__(self):
        return str(self.no_unit + " - " + self.akun_kegiatan)

class Uraian_kegiatan(models.Model):
    kegiatan_akun = models.ForeignKey(Kegiatan_akun, on_delete=models.SET_NULL, null=True, blank=True, related_name='kode_kegiatan_akun')

    no = models.CharField(null=True, blank=True, max_length=100)
    uraian_kegiatan = models.TextField(null=True, blank=True, max_length=2000)
    pj = models.CharField(null=True, blank=True, max_length=100)
    keterangan = models.TextField(null=True, blank=True, max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)

    def __str__(self):
        return str(self.no + " - " + self.uraian_kegiatan)

class Profile(models.Model):

    DIREKTORAT_CHOICES = (
        ('psm', 'PSM'),
        ('dayatif', 'Dayatif'),
    )

    satker = models.ForeignKey(Satker, on_delete=models.CASCADE, null=True, blank=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    role = models.CharField(null=True, blank=True, max_length=12, choices=DIREKTORAT_CHOICES)
    notelp  = models.CharField(max_length=20, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(default='images/avatar.png', upload_to='profile_avatars')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Profile User'
        verbose_name_plural = 'Daftar Profile User'

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_role(self):
        role = 'PSM' if self.role == 'psm' else 'Dayatif'
        return role

    def get_data_user_profil(self):
        print(self.id)
        profile_instance = Profile.objects.get(id=self.id)  # Assuming there is only one user with this ID
        user_instance = User.objects.get(id=profile_instance.user_id)  # Assuming there is only one user with this ID
        user_data = {
            'id': user_instance.id,
            'username': user_instance.username,
        }
        return user_data

    def get_data_user_satker(self):
        try:
            satker_instance = Satker.objects.get(id=self.satker_id)
            satker_data = {
                'id': satker_instance.id,
                'satker': satker_instance.nama_satker,
            }
        except ObjectDoesNotExist:
            satker_data = {
                'message': "Satker Kosong",
            }

        return satker_data

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

class reg_provinces(models.Model):
    kode_provinsi = models.CharField(max_length=10)
    nama_provinsi = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)
    class Meta:
        ordering = ['nama_provinsi', ]
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Daftar Provinsi'

    def __str__(self):
        return str(self.nama_provinsi)

class reg_regencies(models.Model):
    kode_kabupaten = models.CharField(max_length=10)
    kode_provinsi = models.ForeignKey('reg_provinces', on_delete=models.CASCADE, null=True, blank=True)
    nama_kabupaten = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)
    class Meta:
        ordering = ['nama_kabupaten', ]
        verbose_name = 'Kabupaten'
        verbose_name_plural = 'Daftar Kabupaten'

    def __str__(self):
        return str(self.nama_kabupaten)

class reg_district(models.Model):
    kode_kecamatan = models.CharField(max_length=10)
    kode_kabupaten = models.ForeignKey('reg_regencies', on_delete=models.CASCADE, null=True, blank=True)
    nama_kecamatan = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)

    class Meta:
        ordering = ['nama_kecamatan', ]
        verbose_name = 'Kecamatan'
        verbose_name_plural = 'Daftar Kecamatan'

    def __str__(self):
        return str(self.nama_kecamatan)

class reg_villages(models.Model):
    kode_desa = models.CharField(max_length=10)
    kode_kecamatan = models.ForeignKey('reg_district', on_delete=models.CASCADE, null=True, blank=True)
    nama_desa = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geom = models.JSONField(null=True)

    class Meta:
        ordering = ['nama_desa', ]
        verbose_name = 'Desa'
        verbose_name_plural = 'Daftar Desa'

    def __str__(self):
        return str(self.nama_desa)


class SatkerBNNP(models.Model):
    id = models.IntegerField(primary_key=True)
    satker_id = models.BigIntegerField()
    nama_satker = models.CharField(max_length=12)
    provinsi_id = models.BigIntegerField()
    jumlah_profil = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'users_satker_bnnp'

    def __str__(self):
        return f'{self.id}_{self.satker_id} - {self.provinsi_id}: {self.nama_satker} Total : {self.jumlah_profil}'

class SatkerBNNK(models.Model):
    id = models.IntegerField(primary_key=True)
    satker_id = models.BigIntegerField()
    nama_satker = models.CharField(max_length=12)
    kabupaten_id = models.BigIntegerField()
    jumlah_profil = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'users_satker_bnnk'

    def __str__(self):
        return f'{self.id}_{self.satker_id} - {self.kabupaten_id}: {self.nama_satker} Total : {self.jumlah_profil}'

class SatkerPusat(models.Model):
    id = models.IntegerField(primary_key=True)
    satker_id = models.BigIntegerField()
    nama_satker = models.CharField(max_length=12)
    jumlah_profil = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'users_satker_pusat'

    def __str__(self):
        return f'{self.id}_{self.satker_id} -: {self.nama_satker} Total : {self.jumlah_profil}'
