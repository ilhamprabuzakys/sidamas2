# Generated by Django 3.2.24 on 2024-04-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0060_auto_20240419_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='keterangan',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Keterangan'),
        ),
    ]