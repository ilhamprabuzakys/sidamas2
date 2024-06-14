# Generated by Django 3.2.24 on 2024-04-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0090_psm_tes_urine_deteksi_dini_drive_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_tes_urine_deteksi_dini',
            name='anggaran',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Perencanaan Anggaran'),
        ),
        migrations.AddField(
            model_name='psm_tes_urine_deteksi_dini',
            name='penyerapan_anggaran',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Penyerapan Anggaran'),
        ),
    ]
