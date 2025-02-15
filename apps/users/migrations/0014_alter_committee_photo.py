# Generated by Django 3.2.4 on 2021-09-06 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_alter_committee_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="committee",
            name="photo",
            field=models.FileField(
                default="committees/default.png",
                upload_to="committees",
                validators=[django.core.validators.FileExtensionValidator(["svg", "jpg", "jpeg", "png"])],
            ),
        ),
    ]
