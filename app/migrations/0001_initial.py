# Generated by Django 5.0.6 on 2024-05-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("zone_id", models.IntegerField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("status", models.CharField(max_length=100)),
                ("temp_out", models.FloatField()),
                ("high_temp", models.FloatField()),
                ("low_temp", models.FloatField()),
                ("out_humidity", models.FloatField()),
                ("dew_point", models.FloatField()),
                ("wind_speed", models.FloatField()),
                ("wind_dir", models.FloatField()),
                ("wind_run", models.FloatField()),
                ("hi_speed", models.FloatField()),
                ("hi_dir", models.FloatField()),
                ("wind_chill", models.FloatField()),
                ("heat_index", models.FloatField()),
                ("thw_index", models.FloatField()),
                ("bar", models.FloatField()),
                ("rain", models.FloatField()),
                ("rain_rate", models.FloatField()),
                ("head_dd", models.FloatField()),
                ("cool_dd", models.FloatField()),
                ("in_temp", models.FloatField()),
                ("in_humidity", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
