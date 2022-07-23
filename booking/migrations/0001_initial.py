# Generated by Django 4.0.6 on 2022-07-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=50)),
                ('end_point', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=8)),
                ('bus_type', models.CharField(choices=[('PSV', 'PSV (14 seater)'), ('BUS', 'BUS (32 seater)')], max_length=3)),
                ('seats', models.JSONField()),
                ('departure', models.DateTimeField()),
                ('price', models.PositiveIntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buses', to='booking.route')),
            ],
        ),
    ]
