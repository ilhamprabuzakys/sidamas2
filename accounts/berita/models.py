from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Kategori(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    nama = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Daftar Kategori'

    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.nama)
            super().save(*args, **kwargs)
            
    def __str__(self):
        return str(self.nama)


class Berita(models.Model):

    """
        DRAFT : Ketika user pegawai membuat berita berita baru, namun belum ia serahkan untuk direview
        ARCHIVED : Ketika user yang bersangkutan menyembunyikan berita
        PENDING : Ketika user pegawai membuat berita dan ia serahkan ke atasan untuk direview
        PUBLISHED : Ketika berita yang dibuat sudah diberikan izin tayang oleh atasan (admin, superadmin)
    """

    DRAFT = 'draft'
    PENDING = 'pending'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived'),
    ]

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.TextField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    isi_berita = RichTextField()
    tanggal = models.DateField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="draft")
    tags = models.TextField(max_length=1000)
    gambar_utama = models.ImageField(upload_to="upload/files/berita/")
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="berita_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="berita_updated_by")

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Berita'
        verbose_name_plural = 'Daftar Berita'

    def get_created_by_username(self):
        if self.created_by:
            return self.created_by.username
        return 'User?'

    def get_kategori(self):
        if self.kategori:
            return self.kategori.nama
        return 'Kategori?'

    def get_status_display(self):
        status_mapping = dict(self.STATUS_CHOICES)
        return status_mapping.get(self.status, 'Status?')

    def get_status_color(self):
        status_color_mapping = {
            'pending': 'bg-primary',
            'published': 'bg-success',
            'draft': 'bg-warning',
            'archived': 'bg-danger',
        }
        return status_color_mapping.get(self.status, 'bg-secondary')

    def get_status_icon(self):
        status_icon_mapping = {
            'pending': 'far fa-clock',
            'published': 'fas fa-check',
            'draft': 'fas fa-edit',
            'archived': 'fas fa-box-archive',
        }
        return status_icon_mapping.get(self.status, 'fa-question')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + "- " + self.judul + " " + str(self.kategori)

    def get_absolute_url(self):
        return f'/berita/{self.pk}/'


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    nama = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Tag'
        verbose_name_plural = 'Daftar Tag'

    def __str__(self):
        return str(self.nama)


class Images(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    berita = models.ForeignKey(
        Berita, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="upload/files/berita/")

    class Meta:
        pass
