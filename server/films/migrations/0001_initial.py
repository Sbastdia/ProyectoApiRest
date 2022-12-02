# Generated by Django 4.1.3 on 2022-12-02 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FilmGenre",
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
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Nombre"),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "género",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Título")),
                ("year", models.PositiveIntegerField(default=2000, verbose_name="Año")),
                (
                    "review_short",
                    models.TextField(
                        blank=True, null=True, verbose_name="Argumento (corto)"
                    ),
                ),
                (
                    "review_large",
                    models.TextField(
                        blank=True, null=True, verbose_name="Historia (largo)"
                    ),
                ),
                (
                    "trailer_url",
                    models.URLField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="URL youtube",
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(
                        related_name="film_genres",
                        to="films.filmgenre",
                        verbose_name="Géneros",
                    ),
                ),
            ],
            options={
                "verbose_name": "Película",
                "ordering": ["title"],
            },
        ),
    ]
