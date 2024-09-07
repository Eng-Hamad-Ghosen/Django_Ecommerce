# Generated by Django 5.1 on 2024-09-07 14:37

import accounts.models
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='citty',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=15, verbose_name='Mobile'),
        ),
    ]
