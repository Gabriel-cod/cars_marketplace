# Generated by Django 4.2.16 on 2024-10-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]