# Generated by Django 3.2 on 2022-01-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0011_alter_reservation_for_how_many"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="for_how_many",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="time",
            field=models.TimeField(),
        ),
    ]
