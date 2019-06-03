# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-03 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190603_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='pv',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='uv',
        ),
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]