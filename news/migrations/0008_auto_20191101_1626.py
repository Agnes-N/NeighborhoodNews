# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-01 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20191101_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='neigborhood_name',
            new_name='neighborhood_name',
        ),
    ]