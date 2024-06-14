from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Satker

import random
import string

class shortcode(models.Model):
    code = models.CharField(max_length=8)
    def __str__(self):
        return str(self.code)

class survey(models.Model):
    STATUS_CHOICES = (
        ('1', 'DRAFT'),
        ('2', 'PUBLISH'),
        ('3', 'ARCHIVE'),
    )

    PEMILIK_CHOICES = (
        ('1', 'PSM'),
        ('2', 'DAYATIF'),
    )

    judul = models.CharField(max_length=1000)
    jsontext = models.JSONField()
    pemilik = models.CharField(max_length=1, choices=PEMILIK_CHOICES, default="1")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    satker = models.ForeignKey(Satker, on_delete=models.CASCADE, null=True, blank=True,)
    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)
    batasan = models.IntegerField(blank=True, null=True)
    dibuat_oleh = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="survey_created_by")
    tanggal_awal = models.DateField(blank=True, null=True)
    tanggal_akhir = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.judul)

    def generate_unique_code(self):
        # Menghasilkan kode acak
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Mengecek apakah kode sudah digunakan
        while survey.objects.filter(kode=random_string).exists():
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        return random_string

    def get_jumlah_responden(self):
        survey_id_count = survey_result.objects.filter(survey_id=self.id).count()
        return survey_id_count

    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = self.generate_unique_code()
        super().save(*args, **kwargs)

        survey_short_instance = surveyshort.objects.create(
            satker=self.satker,
            shortcode=self.kode,  # Assuming you want to use the 'kode' field as 'shortcode'
            survey=self,  # Reference to the current survey instance
            status=self.status,
            dibuat_oleh=self.dibuat_oleh
        )
        survey_short_instance.save()

        shortcode_instance = shortcode.objects.create(
            code=self.kode
        )
        shortcode_instance.save()

    def delete(self, *args, **kwargs):
        surveyshort.objects.filter(shortcode=self.kode).delete()
        shortcode.objects.filter(code=self.kode).delete()

        super().delete(*args, **kwargs)

class surveyshort(models.Model):
    STATUS_CHOICES = (
        ('1', 'PUBLISH'),
        ('2', 'ARCHIVE'),
    )
    satker = models.ForeignKey(Satker, on_delete=models.CASCADE, blank=True, null=True, related_name="surveyshort_satker")
    shortcode = models.CharField(max_length=8)
    survey = models.ForeignKey(survey, on_delete=models.CASCADE, blank=True, null=True, related_name="surveyshort_survey")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    dibuat_oleh = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="shortcode_created_by")

class survey_result(models.Model):
    survey = models.ForeignKey(survey, on_delete=models.CASCADE, blank=True, null=True, related_name="surveyresult_survey")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    hasil = models.JSONField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    shortcode = models.ForeignKey(surveyshort, on_delete=models.CASCADE, blank=True, null=True, related_name="surveyresult_short")
