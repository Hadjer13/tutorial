# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionsource', '0006_remove_sourcesite_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectesite',
            name='type',
        ),
    ]