# Generated by Django 5.1 on 2024-09-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prand',
            name='PRDDescription',
            field=models.TextField(blank=True, null=True, verbose_name='Prand Description'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='VARDescription',
            field=models.TextField(blank=True, null=True, verbose_name='Variant Description'),
        ),
    ]
