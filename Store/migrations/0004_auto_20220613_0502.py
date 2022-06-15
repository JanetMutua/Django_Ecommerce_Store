# Generated by Django 3.2.5 on 2022-06-13 05:02

import Store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='viewed_on_homepage',
            field=models.BooleanField(default=False, help_text='0=default, 1=Homepage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=Store.models.get_file_path),
        ),
    ]
