# Generated by Django 3.0.11 on 2020-11-30 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_institutionfontys_institutiontue"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="card_number",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="department",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="key_access",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="program",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="tue_id",
        ),
    ]
