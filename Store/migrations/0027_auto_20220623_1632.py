# Generated by Django 3.2.5 on 2022-06-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0026_rename_original_price_product_buying_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Petite',
            field=models.BooleanField(default=False, help_text='0=default, 1=Petite'),
        ),
        migrations.AddField(
            model_name='category',
            name='PlusSize',
            field=models.BooleanField(default=False, help_text='0=default, 1=PlusSize'),
        ),
    ]