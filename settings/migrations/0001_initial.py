# Generated by Django 5.1 on 2024-09-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=50, verbose_name='Prand Name')),
                ('PRDDescription', models.TextField(verbose_name='Prand Description')),
            ],
            options={
                'verbose_name': 'Prand',
                'verbose_name_plural': 'Prands',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=50, verbose_name='Variant Name')),
                ('VARDescription', models.TextField(verbose_name='Variant Description')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
    ]
