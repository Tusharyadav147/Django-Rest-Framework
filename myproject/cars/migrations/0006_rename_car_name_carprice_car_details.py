# Generated by Django 4.1.3 on 2022-11-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0005_carprice"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carprice", old_name="car_name", new_name="car_details",
        ),
    ]