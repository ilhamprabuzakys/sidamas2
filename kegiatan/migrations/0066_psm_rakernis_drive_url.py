# Generated by Django 3.2.24 on 2024-04-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0065_delete_dayatif_bimbingan_teknis_lifeskill_peserta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_rakernis',
            name='drive_url',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='URL GDrive'),
        ),
    ]