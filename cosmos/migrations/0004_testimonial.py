# Generated by Django 3.2.4 on 2021-08-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cosmos", "0003_photos"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                ("author", models.CharField(max_length=100)),
            ],
        ),
    ]
