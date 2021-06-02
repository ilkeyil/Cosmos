# Generated by Django 3.1.11 on 2021-06-01 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cosmos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmm',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='gmm',
            name='slides',
        ),
        migrations.CreateModel(
            name='FileObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_files', to='cosmos.gmm')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
