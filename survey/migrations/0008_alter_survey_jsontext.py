# Generated by Django 3.2.24 on 2024-03-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_alter_surveyshort_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='jsontext',
            field=models.JSONField(),
        ),
    ]
