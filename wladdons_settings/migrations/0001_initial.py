# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-10 18:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddonNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Change this in wladdons_settings.settings', max_length=40, unique=True)),
                ('display', models.CharField(help_text='Change this in wladdons_settings.settings', max_length=50)),
                ('description', models.CharField(help_text='Change this in wladdons_settings.settings', max_length=100)),
                ('shouldsend', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Addon notice',
                'verbose_name_plural': 'Addon notices',
            },
        ),
    ]
