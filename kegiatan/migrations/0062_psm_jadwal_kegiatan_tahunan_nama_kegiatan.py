# Generated by Django 3.2.24 on 2024-04-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0061_psm_jadwal_kegiatan_tahunan_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='nama_kegiatan',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='nama kegiatan'),
        ),
    ]