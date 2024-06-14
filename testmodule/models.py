from django.db import models
from django.urls import reverse


class user(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nilai = models.CharField(max_length=30, verbose_name="nilainilai")
    nilai2 = models.CharField(max_length=30)
    hasil = models.CharField(max_length=30, null=True, blank=True)
    pengguna = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("testmodule_user_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("testmodule_user_update", args=(self.pk,))

class image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')  # 'images/' is the upload directory

    def __str__(self):
        return self.title
