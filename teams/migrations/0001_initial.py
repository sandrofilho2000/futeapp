# Generated by Django 5.0.2 on 2024-03-02 01:17

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("stadiums", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                ("link", models.CharField(max_length=255)),
                ("small_img", models.CharField(max_length=255)),
                ("average_market_value", models.FloatField(blank=True, null=True)),
                ("total_market_value", models.FloatField(blank=True, null=True)),
                ("country_name", models.CharField(max_length=255)),
                ("country_img", models.CharField(max_length=255)),
                (
                    "background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Cor de fundo (vazio para automático)",
                    ),
                ),
                (
                    "text_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Cor do texto (vazio para automático)",
                    ),
                ),
                (
                    "id_stadium",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stadiums.stadium",
                        verbose_name="stadiums_stadium",
                    ),
                ),
            ],
        ),
    ]
