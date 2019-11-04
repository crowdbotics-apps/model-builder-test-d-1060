# Generated by Django 2.2.7 on 2019-11-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "street_name",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
            ],
        )
    ]
