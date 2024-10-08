# Generated by Django 5.1 on 2024-09-07 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_product_prdprand_product_prdbrand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDescription',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDIs_BestSeller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDIs_New',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price'),
        ),
    ]
