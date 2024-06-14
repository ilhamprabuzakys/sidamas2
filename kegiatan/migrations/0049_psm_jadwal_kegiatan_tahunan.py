# Generated by Django 3.2.24 on 2024-04-16 07:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_observasi'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kegiatan', '0048_psm_tes_urine_deteksi_dini_peserta_keterangan_isi_parameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PSM_JADWAL_KEGIATAN_TAHUNAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('jenis_giat', models.TextField(blank=True, null=True)),
                ('tanggal_awal', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Tanggal Awal Kegiatan')),
                ('tanggal_akhir', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Tanggal Akhir Kegiatan')),
                ('lokasi', models.JSONField()),
                ('keterangan', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Keterangan')),
                ('dokumentasi', models.FileField(blank=True, upload_to='uploads/kegiatan/psm/jadwal_kegiatan_tahunan/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psm_jadwal_kegiatan_tahunan_created_by', to=settings.AUTH_USER_MODEL)),
                ('penyelenggara', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='psm_jadwal_kegiatan_tahunan_penyelenggara', to='users.satker', verbose_name='penyelenggara')),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='psm_jadwal_kegiatan_tahunan_target', to='users.satker', verbose_name='target')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psm_jadwal_kegiatan_tahunan_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PSM JADWAL KEGIATAN TAHUNAN',
                'verbose_name_plural': 'DAFTAR PSM JADWAL KEGIATAN TAHUNAN',
                'db_table': 'kegiatan_psm_jadwal_kegiatan_tahunan',
                'ordering': ['-updated_at'],
            },
        ),
    ]
