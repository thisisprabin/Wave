# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20170217_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
    ]