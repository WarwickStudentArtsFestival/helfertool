# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0003_auto_20160516_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpersgifts',
            name='got_shirt',
            field=models.BooleanField(default=False, verbose_name='Helper got her T-shirt'),
        ),
    ]