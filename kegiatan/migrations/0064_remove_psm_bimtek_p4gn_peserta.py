# Generated by Django 3.2.24 on 2024-04-22 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0063_psm_bimtek_p4gn_peserta_jabatan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psm_bimtek_p4gn',
            name='peserta',
        ),
    ]