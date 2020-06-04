# Generated by Django 3.0.6 on 2020-06-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sightseeing.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sightseeing', '0008_auto_20200603_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=sightseeing.models.profile_directory_path)),
                ('bio', models.TextField(blank=True, null=True)),
                ('b_day', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
