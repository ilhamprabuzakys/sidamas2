from django.db import models
from django.urls import reverse


class tbl_eform(models.Model):

    # Fields
    data_eform = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nama_formulir = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    url = models.TextField(max_length=100)
    tgl_akhir = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lk_tbl_eform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lk_tbl_eform_update", args=(self.pk,))



class tbl_responden_eform(models.Model):

    # Fields
    jawaban_eform = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id_eform = models.IntegerField()
    id_user = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lk_tbl_responden_eform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lk_tbl_responden_eform_update", args=(self.pk,))