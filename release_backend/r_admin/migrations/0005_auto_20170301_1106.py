# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r_admin', '0004_auto_20170301_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='project_env_id',
            field=models.IntegerField(),
        ),
    ]
