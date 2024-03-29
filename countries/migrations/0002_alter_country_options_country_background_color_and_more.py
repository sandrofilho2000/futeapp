# Generated by Django 5.0.2 on 2024-03-14 02:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"ordering": ["name"], "verbose_name_plural": "Countries"},
        ),
        migrations.AddField(
            model_name="country",
            name="background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="Cor de fundo (vazio para automático)",
            ),
        ),
        migrations.AddField(
            model_name="country",
            name="text_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
                verbose_name="Cor do texto (vazio para automático)",
            ),
        ),
    ]
