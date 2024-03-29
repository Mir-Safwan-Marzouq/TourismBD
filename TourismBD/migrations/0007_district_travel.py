# Generated by Django 3.2.3 on 2021-06-06 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TourismBD', '0006_auto_20210604_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='District_travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('headline', models.TextField()),
                ('transportationCost', models.TextField()),
                ('FoodCost', models.TextField()),
                ('districtName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TourismBD.district_info')),
                ('divsion_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TourismBD.division')),
            ],
        ),
    ]
