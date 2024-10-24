# Generated by Django 5.1.2 on 2024-10-20 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_create_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha de creacion'),
        ),
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha de actualizacion'),
        ),
    ]
