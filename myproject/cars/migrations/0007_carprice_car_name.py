# Generated by Django 4.1.3 on 2022-11-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0006_rename_car_name_carprice_car_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="carprice",
            name="car_name",
            field=models.CharField(default="None", max_length=20),
        ),
    ]
