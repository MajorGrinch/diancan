# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20160928_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=11),
        ),
    ]
