# Generated by Django 3.2.24 on 2024-04-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0052_psm_jadwal_kegiatan_tahunan_jumlah_peserta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='dokumentasi',
        ),
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='keterangan',
        ),
    ]
