# Generated by Django 3.2.5 on 2022-07-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0041_rename_slug_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brief_description',
        ),
        migrations.RemoveField(
            model_name='size',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='Clearance',
            field=models.BooleanField(default=1, help_text='0=default, 1=Clearance'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Petite',
            field=models.BooleanField(default=1, help_text='0=default, 1=Petite'),
        ),
        migrations.AlterField(
            model_name='category',
            name='PlusSize',
            field=models.BooleanField(default=1, help_text='0=default, 1=PlusSize'),
        ),
    ]
