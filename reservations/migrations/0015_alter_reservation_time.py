# Generated by Django 3.2 on 2022-01-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0014_auto_20220114_0929"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="time",
            field=models.TimeField(
                choices=[
                    ("13:00", "13:00"),
                    ("15:00", "15:00"),
                    ("17:00", "17:00"),
                    ("19:00", "19:00"),
                    ("21:00", "21:00"),
                ],
                max_length=10,
            ),
        ),
    ]
