# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 17:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170921_1324'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('lagos', django.db.models.manager.Manager()),
            ],
        ),
    ]
