# Generated by Django 4.2.1 on 2023-05-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Query",
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
                ("created_by", models.IntegerField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified at"),
                ),
                ("modified_by", models.IntegerField(blank=True, null=True)),
                ("query", models.TextField(default="")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
