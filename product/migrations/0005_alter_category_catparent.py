# Generated by Django 5.1 on 2024-09-03 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_category_catsparent_category_catparent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent_isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
