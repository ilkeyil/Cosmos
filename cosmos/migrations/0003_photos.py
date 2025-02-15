# Generated by Django 3.2.4 on 2021-07-12 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cosmos", "0002_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoAlbum",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("album_cover", models.ImageField(upload_to="photos")),
            ],
        ),
        migrations.CreateModel(
            name="PhotoObject",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("photo", models.ImageField(upload_to="photos")),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="has_photos", to="cosmos.photoalbum"
                    ),
                ),
            ],
        ),
    ]
