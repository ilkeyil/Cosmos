# Generated by Django 3.2.6 on 2021-08-19 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_unique_slugs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="committee",
            name="photo",
            field=models.FileField(
                default="committees/default.png",
                upload_to="committees",
                validators=[django.core.validators.FileExtensionValidator("svg")],
            ),
        ),
    ]
