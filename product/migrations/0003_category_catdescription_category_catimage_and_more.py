# Generated by Django 5.1 on 2024-09-03 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_alter_product_prdcost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CATDescription',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATImage',
            field=models.ImageField(default='', upload_to='category/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATSParent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.category'),
            preserve_default=False,
        ),
    ]
