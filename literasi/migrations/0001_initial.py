# Generated by Django 4.1.7 on 2024-01-17 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='literasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('dokumen', models.FileField(upload_to='upload/files/literasi')),
                ('Judul', models.TextField(max_length=1000)),
                ('tags', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('1', 'DRAFT'), ('2', 'PUBLISH'), ('3', 'ARCHIVE')], default='1', max_length=1)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Literasi_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Literasi_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
