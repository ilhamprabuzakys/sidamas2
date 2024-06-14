# Generated by Django 3.2.24 on 2024-04-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0076_psm_audiensi_drive_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_audiensi',
            name='anggaran',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Perencanaan Anggaran'),
        ),
        migrations.AddField(
            model_name='psm_audiensi',
            name='penyerapan_anggaran',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Penyerapan Anggaran'),
        ),
    ]
