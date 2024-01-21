# Generated by Django 5.0.1 on 2024-01-21 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pollutant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_level', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AirQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqi', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
            ],
        ),
        migrations.CreateModel(
            name='Ozone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('air_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.airquality')),
            ],
        ),
        migrations.CreateModel(
            name='PM25',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('air_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.airquality')),
            ],
        ),
        migrations.CreateModel(
            name='PollutantMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('air_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.airquality')),
                ('pollutant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.pollutant')),
            ],
        ),
    ]
