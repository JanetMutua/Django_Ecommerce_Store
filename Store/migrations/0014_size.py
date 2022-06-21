# Generated by Django 3.2.5 on 2022-06-21 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_rename_size_size_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_no', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('size_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Store.size_category')),
            ],
        ),
    ]
