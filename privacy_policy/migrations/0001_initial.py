# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-08 18:23


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrivacyPolicy",
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
                (
                    "language",
                    models.CharField(
                        default="English",
                        help_text="Will be displayed as a level 1 header",
                        max_length=30,
                        unique=True,
                    ),
                ),
                (
                    "policy_text",
                    models.TextField(
                        help_text="Text will be rendered using markdown syntax"
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "ordering": ["language"],
            },
        ),
    ]
