# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 13:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0011_auto_20161228_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='RUB',
            field=models.FloatField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='Date',
            field=models.CharField(default=datetime.datetime(2016, 12, 28, 17, 43, 34, 361451), max_length=255),
        ),
    ]