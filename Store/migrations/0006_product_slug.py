# Generated by Django 4.0.5 on 2022-06-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=False, max_length=150),
        ),
    ]