# Generated by Django 3.0.6 on 2020-06-02 14:55

from django.db import migrations, models
import sightseeing.models


class Migration(migrations.Migration):

    dependencies = [
        ('sightseeing', '0002_auto_20200601_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='photo',
            field=models.ImageField(upload_to=sightseeing.models.location_directory_path),
        ),
    ]