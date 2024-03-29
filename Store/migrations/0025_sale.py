# Generated by Django 3.2.5 on 2022-06-22 10:07

import Store.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0024_remove_product_viewed_on_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(upload_to=Store.models.get_file_path)),
                ('brief_description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=500)),
                ('buying_price', models.FloatField()),
                ('original_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.category')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Store.size')),
            ],
        ),
    ]
