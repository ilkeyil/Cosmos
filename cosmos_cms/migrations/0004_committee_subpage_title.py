# Generated by Django 3.0.8 on 2020-08-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("cosmos_cms", "0003_contactpluginmodel"),
        ("cosmos", "0003_profile_terms_newsletter_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommitteeSubpageTitlePluginModel",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="cosmos_cms_committeesubpagetitlepluginmodel",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("committee", models.OneToOneField(on_delete=models.deletion.CASCADE, to="cosmos.Committee")),
                ("description", models.CharField(default="", max_length=400)),
                ("subtitle", models.CharField(default="", max_length=100)),
                ("image", models.ImageField(default="img/default.jpg", upload_to="committeeImg")),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        ),
    ]
