# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionsource', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Source',
            new_name='SourceData',
        ),
    ]
