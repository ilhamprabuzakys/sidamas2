# Generated by Django 4.1.7 on 2024-03-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0003_auto_20240318_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='nama_desa',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='nama_kabupaten',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='nama_kecamatan',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='nama_provinsi',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='psm_rakernis',
            name='kendala',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Kendala'),
        ),
        migrations.AlterField(
            model_name='psm_rakernis',
            name='kesimpulan',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Kesimpulan'),
        ),
        migrations.AlterField(
            model_name='psm_rakernis',
            name='tindak_lanjut',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Tindak Lanjut'),
        ),
    ]
