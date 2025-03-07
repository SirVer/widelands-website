# -*- coding: utf-8 -*-


from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("message", models.TextField(verbose_name="message")),
                (
                    "added",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="added"
                    ),
                ),
                ("unseen", models.BooleanField(default=True, verbose_name="unseen")),
                (
                    "archived",
                    models.BooleanField(default=False, verbose_name="archived"),
                ),
                ("on_site", models.BooleanField(verbose_name="on site")),
            ],
            options={
                "ordering": ["-added"],
                "verbose_name": "notice",
                "verbose_name_plural": "notices",
            },
        ),
        migrations.CreateModel(
            name="NoticeQueueBatch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("pickled_data", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="NoticeSetting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "medium",
                    models.CharField(
                        max_length=1, verbose_name="medium", choices=[(b"1", "Email")]
                    ),
                ),
                ("send", models.BooleanField(verbose_name="send")),
            ],
            options={
                "verbose_name": "notice setting",
                "verbose_name_plural": "notice settings",
            },
        ),
        migrations.CreateModel(
            name="NoticeType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("label", models.CharField(max_length=40, verbose_name="label")),
                ("display", models.CharField(max_length=50, verbose_name="display")),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="description"),
                ),
                ("default", models.IntegerField(verbose_name="default")),
            ],
            options={
                "verbose_name": "notice type",
                "verbose_name_plural": "notice types",
            },
        ),
        migrations.CreateModel(
            name="ObservedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                (
                    "added",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="added"
                    ),
                ),
                ("signal", models.TextField(verbose_name="signal")),
                (
                    "content_type",
                    models.ForeignKey(
                        to="contenttypes.ContentType", on_delete=models.CASCADE
                    ),
                ),
                (
                    "notice_type",
                    models.ForeignKey(
                        verbose_name="notice type",
                        to="notification.NoticeType",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        verbose_name="user",
                        to=settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "ordering": ["-added"],
                "verbose_name": "observed item",
                "verbose_name_plural": "observed items",
            },
        ),
        migrations.AddField(
            model_name="noticesetting",
            name="notice_type",
            field=models.ForeignKey(
                verbose_name="notice type",
                to="notification.NoticeType",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AddField(
            model_name="noticesetting",
            name="user",
            field=models.ForeignKey(
                verbose_name="user",
                to=settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AddField(
            model_name="notice",
            name="notice_type",
            field=models.ForeignKey(
                verbose_name="notice type",
                to="notification.NoticeType",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AddField(
            model_name="notice",
            name="user",
            field=models.ForeignKey(
                verbose_name="user",
                to=settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="noticesetting",
            unique_together=set([("user", "notice_type", "medium")]),
        ),
    ]
