# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-04 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]
