# Generated by Django 3.2.5 on 2022-07-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0037_rename_plus_size_plussize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
