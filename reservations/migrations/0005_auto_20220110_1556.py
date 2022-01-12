# Generated by Django 3.2 on 2022-01-10 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(),
        ),
        migrations.CreateModel(
            name='Gin_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
        ),
    ]
