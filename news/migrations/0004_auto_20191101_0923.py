# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-01 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_neighborhood_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='name',
            new_name='neigborhood_name',
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='occupants',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
