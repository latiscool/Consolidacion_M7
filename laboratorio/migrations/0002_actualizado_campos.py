# Generated by Django 5.1.4 on 2025-01-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("laboratorio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="directorgeneral",
            options={
                "verbose_name": "Director General",
                "verbose_name_plural": "Directores Generales",
            },
        ),
        migrations.AddField(
            model_name="directorgeneral",
            name="especialidad",
            field=models.CharField(default="PY", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="laboratorio",
            name="ciudad",
            field=models.CharField(default="SGTGO", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="laboratorio",
            name="pais",
            field=models.CharField(default="CHILE", max_length=100),
            preserve_default=False,
        ),
    ]
