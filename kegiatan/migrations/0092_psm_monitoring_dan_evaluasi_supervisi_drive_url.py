# Generated by Django 3.2.24 on 2024-04-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0091_auto_20240424_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_monitoring_dan_evaluasi_supervisi',
            name='drive_url',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Tautan Drive'),
        ),
    ]
