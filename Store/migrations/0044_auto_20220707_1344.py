# Generated by Django 3.2.5 on 2022-07-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0043_remove_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Clearance',
            field=models.BooleanField(default=False, help_text='0=default, 1=Clearance'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Petite',
            field=models.BooleanField(default=False, help_text='0=default, 1=Petite'),
        ),
        migrations.AlterField(
            model_name='category',
            name='PlusSize',
            field=models.BooleanField(default=False, help_text='0=default, 1=PlusSize'),
        ),
    ]