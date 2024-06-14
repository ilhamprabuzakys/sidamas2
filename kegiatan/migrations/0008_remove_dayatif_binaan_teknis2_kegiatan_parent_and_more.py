# Generated by Django 4.1.7 on 2024-03-20 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0007_dayatif_binaan_teknis_status_psm_asistensi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayatif_binaan_teknis2_kegiatan',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='dayatif_binaan_teknis2_kegiatan',
            name='satker_target',
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='jumlah_hari_pelaksanaan',
            field=models.IntegerField(default=2, verbose_name='Jumlah Hari Pelaksanaan Kegiatan'),
        ),
        migrations.DeleteModel(
            name='DAYATIF_BINAAN_TEKNIS2',
        ),
        migrations.DeleteModel(
            name='DAYATIF_BINAAN_TEKNIS2_KEGIATAN',
        ),
    ]
