# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionsource', '0003_collectedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollecteRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default='', max_length=100)),
                ('appID', models.CharField(blank=True, default='', max_length=100)),
                ('appSecret', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='', max_length=100)),
                ('groupe', models.CharField(blank=True, default='', max_length=50)),
                ('type', models.CharField(blank=True, default='', max_length=50)),
                ('pays', models.CharField(blank=True, default='', max_length=50)),
                ('continent', models.CharField(blank=True, default='', max_length=50)),
                ('region', models.CharField(blank=True, default='', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SourceRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SourceSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.RenameModel(
            old_name='SourceData',
            new_name='CollecteSite',
        ),
        migrations.DeleteModel(
            name='CollecteData',
        ),
        migrations.RenameField(
            model_name='collectesite',
            old_name='link',
            new_name='xpath',
        ),
    ]