# Generated by Django 3.2.24 on 2024-03-25 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0016_remove_dayatif_pemetaan_potensi_jumlah_hari_pelaksanaan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psm_tes_urine_deteksi_dini',
            name='dokumentasi',
            field=models.FileField(upload_to='uploads/kegiatan/psm/tes_urine_deteksi_dini/'),
        ),
    ]
