# Generated by Django 3.2.24 on 2024-04-18 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20240418_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kegiatan_akun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_unit', models.IntegerField()),
                ('akun_kegiatan', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
