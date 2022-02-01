# Generated by Django 3.2.3 on 2021-06-06 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TourismBD', '0007_district_travel'),
    ]

    operations = [
        migrations.AddField(
            model_name='district_travel',
            name='map',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
