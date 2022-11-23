# Generated by Django 4.1.3 on 2022-11-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_name", models.CharField(max_length=20)),
                ("model", models.CharField(max_length=20)),
                ("model_year", models.IntegerField()),
                ("price", models.IntegerField(default=200000)),
            ],
        ),
        migrations.CreateModel(
            name="LogIn_Wrong",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("mobile_no", models.CharField(max_length=14)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="CarShowRoomInOut",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_in", models.DateTimeField()),
                ("car_out", models.DateTimeField()),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cars.cardetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchase_date", models.DateField()),
                (
                    "payment_mode",
                    models.CharField(
                        choices=[("Cash", "Cash"), ("Check", "Check")],
                        default="None",
                        max_length=6,
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        default="dh",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cars.cardetails",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.register"
                    ),
                ),
            ],
        ),
    ]
