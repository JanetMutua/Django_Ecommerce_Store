# Generated by Django 3.2.5 on 2022-06-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0030_rename_slug_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='slug',
        ),
    ]
