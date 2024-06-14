# Generated by Django 3.2.24 on 2024-04-19 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20240419_1036'),
        ('kegiatan', '0059_auto_20240418_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='keterangan',
        ),
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='nama_kegiatan',
        ),
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='ordering_asc',
        ),
        migrations.RemoveField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='pj',
        ),
        migrations.AddField(
            model_name='psm_jadwal_kegiatan_tahunan',
            name='uraian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='psm_jadwal_kegiatan_tahunan_Uraian_kegiatan', to='users.uraian_kegiatan', verbose_name='URAIAN KEGIATAN'),
        ),
    ]