# Generated by Django 4.1.3 on 2022-12-05 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0003_alter_filmgenre_id_filmuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="average_note",
            field=models.FloatField(
                default=0.0,
                validators=[django.core.validators.MaxValueValidator(10.0)],
                verbose_name="nota media",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="favorites",
            field=models.IntegerField(default=0, verbose_name="favoritos"),
        ),
    ]