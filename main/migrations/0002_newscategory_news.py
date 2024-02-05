# Generated by Django 5.0.1 on 2024-02-05 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsCategory",
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
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Категория новостей",
                "verbose_name_plural": "Категории новостей",
            },
        ),
        migrations.CreateModel(
            name="News",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="news")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.newscategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
