# Generated by Django 3.2.24 on 2024-04-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0062_psm_jadwal_kegiatan_tahunan_nama_kegiatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_bimtek_p4gn_peserta',
            name='jabatan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
