# Generated by Django 3.2.4 on 2021-07-10 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmos', '0002_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbum',
            name='date',
            field=models.DateField(default=datetime.date.today()),
            preserve_default=False,
        ),
    ]
