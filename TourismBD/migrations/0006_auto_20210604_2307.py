# Generated by Django 3.2.3 on 2021-06-04 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourismBD', '0005_alter_district_info_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district_info',
            name='census1991',
        ),
        migrations.RemoveField(
            model_name='district_info',
            name='census2001',
        ),
    ]
