# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160926_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=30),
        ),
    ]